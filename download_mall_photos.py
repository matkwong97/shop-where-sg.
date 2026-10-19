"""Run via GitHub Actions; downloads only explicitly curated, openly licensed images."""
import io,json,pathlib,time,urllib.parse,urllib.request
from PIL import Image,ImageOps
root=pathlib.Path(__file__).resolve().parent
sources=json.loads((root/'photo-sources.json').read_text())
out=root/'public'/'mall-photos';out.mkdir(parents=True,exist_ok=True)
manifest=json.loads((root/'mall-photos.json').read_text()) if (root/'mall-photos.json').exists() else {}
for mall,entry in sources.items():
 try:
  params=urllib.parse.urlencode({'action':'query','titles':'File:'+entry['file'],'prop':'imageinfo','iiprop':'url|extmetadata','format':'json'})
  req=urllib.request.Request('https://commons.wikimedia.org/w/api.php?'+params,headers={'User-Agent':'ShopWhereSG/1.0 (educational website; Wikimedia Commons image attribution)'})
  with urllib.request.urlopen(req,timeout=30) as r: data=json.load(r)
  info=next(iter(data['query']['pages'].values()))['imageinfo'][0]
  license_name=info.get('extmetadata',{}).get('LicenseShortName',{}).get('value','')
  if license_name.strip().lower()!=entry['license'].strip().lower():
   print('SKIP unapproved licence:',mall,license_name);continue
  req=urllib.request.Request(info['url'],headers={'User-Agent':'ShopWhereSG/1.0 (image cache)'})
  with urllib.request.urlopen(req,timeout=45) as r: raw=r.read(14_000_001)
  if len(raw)>14_000_000:raise ValueError('Image too large')
  with Image.open(io.BytesIO(raw)) as im:
   im=ImageOps.exif_transpose(im).convert('RGB'); im=ImageOps.fit(im,(1200,675),method=Image.Resampling.LANCZOS,centering=(0.5,0.5)); im.save(out/(urllib.parse.quote(mall,safe='').replace('%20','-')+'.webp'),'WEBP',quality=78,method=5)
  filename=urllib.parse.quote(mall,safe='').replace('%20','-')+'.webp'
  manifest[mall]={'src':'/mall-photos/'+filename,'credit':entry['credit'],'license':entry['license'],'licenseUrl':entry['licenseUrl'],'page':entry['page'],'modified':True}
  print('Saved:',mall,filename)
 except Exception as e: print('SKIP:',mall,str(e))
 time.sleep(.5)
(root/'mall-photos.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Images downloaded:',len(manifest),'/',len(sources))

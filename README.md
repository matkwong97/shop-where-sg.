# Shop Where SG

A responsive React + Vite mall-finder demo, ready for GitHub and Cloudflare Pages.

## Deploy
1. Upload **the contents** of this folder to the root of a new GitHub repository, keeping `public/` as a folder.
2. Cloudflare dashboard → Workers & Pages → Create → Pages → Connect to Git → select repository.
3. Framework preset: **Vite**. Build command: `npm run build`. Build output directory: `dist`. Root directory: `/`.
4. Deploy and use the `*.pages.dev` link.

## Important data limitations
The bundled 25-mall tenant dataset is **illustrative and not verified**. It is not a complete list of Singapore malls, and stores may have moved or closed. Store unit numbers, opening hours, Google ratings, travel durations, taxi fares, and transit fares are deliberately **not invented**. OneMap public search may be unavailable due to CORS, authentication, or policy changes; postal lookup gracefully falls back to unsorted results. Leaflet uses OpenStreetMap tiles and Google Maps links provide routing externally. Do not represent the sample data as live. To make this production-ready, add a licensed regularly refreshed tenant database, a compliant geocoding/routing service, and a licensed places/hours/reviews provider. Confirm API terms, rate limits, and attribution before use.

## Local development
`npm install` then `npm run dev`.

Payment QR crops come from user-supplied screenshots. Test scanning and verify recipient before publishing.

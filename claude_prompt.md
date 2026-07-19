# Context & Objective
We are currently updating the "Hall of Fame" section on the Praktikum Komputasi Numerik 2026 website (`Web-KN-26`). 
The previous podium layout has been successfully redesigned into a "Golden Ticket" card layout (3 cards side-by-side) with a nice golden gradient background. 

## Current Status & Issues
1. **White Background Issue**: The winner photos (`.JPG`) have solid white backgrounds. We tried using CSS `mix-blend-mode: multiply` in `style.css` (class `.golden-photo`) to make the white transparent against the golden gradient, but it's not looking right or not working as expected. We need a proper solution to remove the white background from these images so the golden gradient shows through cleanly behind the subjects.
2. **Timer State**: For local debugging purposes, the countdown timer in `js/script.js` (`targetDate`) is currently set to `10:00 WIB` so the cards are instantly revealed. 

## Required Tasks for Claude
1. **Fix the Image Backgrounds**: Find the best way to remove the white backgrounds from the 3 photos. You might need to download the images from the URLs, run a python background removal script (like `rembg`), save them as transparent PNGs locally, update the `index.html` `src` tags to point to the local PNGs, and remove the `mix-blend-mode` hack from `style.css`.
2. **Revert Timer**: In `js/script.js`, change the `targetDate` back to its original time: `15:00 WIB` on `July 19, 2026`.
3. **Review & Push**: Ensure the layout looks perfect locally, then commit and push the final changes to the `main` branch.

## Key Files
- `index.html` (Golden Ticket markup starts around line 691)
- `css/style.css` (Golden Ticket CSS starts around line 1640)
- `js/script.js` (Timer logic is in `initHallTimer` at the bottom of the file)

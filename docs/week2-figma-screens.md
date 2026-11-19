# Verda — Figma Screens and Prototype

Frame size: **393 × 852** (iPhone 15). Style: [week2-design-system.md](week2-design-system.md).

## What we already have (Figma, Page 1)

| Frame | Module | Status |
|---|---|---|
| `beginning`: onboarding "Your greenhouse, beautifully in balance." | — | ✅ |
| `login`: email + greenhouse code | M1 | ✅ (needs error state, see below) |
| `Verda Home`: health ring 92 %, 24 °C, priority alert "Zone B", quick stats | M2 | ✅ |
| `greenhouse`: My Greenhouse, Overview / Head House / Zone A chips, "Tap an area to explore" | Extra feature (map) | 🟡 Centre of the frame is empty: the zone map needs to be drawn |
| `cloud`: zone sheet "Selected zone: Zone B", temperature 24°, humidity 68 %, Watering / Ventilation / Lighting | Extra feature + M3 | ✅ |
| `analysis`: Week / Month / Year, plant growth, water usage, harvest | M6 | 🟡 Needs temperature and soil-moisture charts |
| `harvest`: harvest this month, ready now, upcoming | Track (agro-intelligence) | ✅ |
| `profile`: user, my greenhouse, settings, notifications, preferences, log out | M7 entry | ✅ |
| `Weather selector` component | — | ✅ |
| Prototype "Flow 1" + tab bar links | — | ✅ partly |

## Missing for the Week 2 rubric (2.1: "all screens for M1–M8 and the extra feature")

| # | New frame | Module | Must show |
|---|---|---|---|
| 1 | **Greenhouse map** (fill the `greenhouse` frame) | ★ Extra | Top-down plan, zones A–F; layer chips **Temperature / Moisture / Plants**; zones tinted sage / amber / red by crop limits; legend |
| 2 | **Alerts** | M5 | List: "Zone B — soil moisture 18 %, below 40 %" · "Zone D — 45 °C, above 28 °C" · time · unread dot. Tapping opens the zone. Opened from the bell on Home. |
| 3 | **Alert banner** (overlay on Home) | M5 | "Overheating in Zone D — 45 °C · Open vents" |
| 4 | **Devices** (full control) | M3 + M4 | Mode switch **Auto / Manual**; 4 rows: Watering, Ventilation, Grow lights, **Frost heater**; states Off → Sending… → On ✓ |
| 5 | **Greenhouse settings** (from Profile) | M7 | Crop thresholds (tomato 18–28 °C, moisture 40–70 %), units °C/°F, watering schedule |
| 6 | **Automation rule** | M4 + M7 | "If soil moisture < 30 % → water for 2 min" with an input; **error state** "Must be between 0 and 100 %" |
| 7 | **Analysis: climate** (or a new section in `analysis`) | M6 | Temperature (°C) and soil moisture (%) line charts, **Day / Week**, allowed-range band, red dot at the low point |
| 8 | **No connection** state (variant of Home) | M8 | Grey bar "No connection to greenhouse — showing data from 14:32", disabled toggles |
| 9 | **Login error** (variant of `login`) | M1 | Red text "Wrong email or greenhouse code" |
| 10 | **Cold-night card** (on Home) | ★ Extra | "Frost tonight · −2 °C at 04:00"; checklist **Vents closed** (live) and **Seedlings covered** (tap to confirm); "Close vents" button |

**Small fixes:** remove the tab bar from `login` (the user isn't logged in yet); delete the empty `Verda Login` frame and the stray `Group`.

## Prototype: the 4 key scenarios

1. **"Is everything OK?"** `beginning` → Log In → `login` → `Verda Home` (health ring answers in 5 s).
2. **Overheating → open the vents.** `Verda Home` + *alert banner* → tap → `greenhouse` map (Zone D red) → tap zone → `cloud` sheet → Ventilation **On** → `Verda Home` (24 °C, Healthy).
3. **Auto-watering for the weekend.** `Verda Home` → `Devices` → toggle **Auto** → rule → *Save* → "Active ✓".
4. **When did plants lack water?** Tab Analysis → **Week** → soil-moisture chart → red dot "Thu · Zone B · 18 %".
5. **Cold night (extra feature).** Instructor sets `outdoorLow` to −2 °C → cold-night card on `Verda Home` → **Close vents** → ✓ → **Seedlings covered** → ✓ "Ready for tonight".

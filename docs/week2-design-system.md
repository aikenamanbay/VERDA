# Verda — Design System

**Direction:** warm, calm SaaS in the spirit of Linear, Notion or Stripe, but organic. Cream paper, sage green, soft rounded cards, generous white space. Colour is used for **status**, not decoration. Aigerim checks the app in a bright greenhouse or on the road, so **readability and an instant status** matter more than ornament.

## Logo

The Verda mark is a **sage tile with a sprouting leaf pair** next to the wordmark **Verda** (Inter Bold). It is shown on Login and Onboarding.

- **Tile** = the greenhouse seen from above (the same rounded rectangle as the cards and the map).
- **Two leaves** = growth, and the two views of the app: map and dashboard.
- **Tagline:** "A little care. A lot of growth."

Source: Figma file, frame `login` (export the mark to `design/logo.svg`).

## Colours (taken from the Figma file)

| Token | Hex | Use | Why it suits our user |
|---|---|---|---|
| `forest` | `#26352C` | Headings, dark pill buttons ("Overview"), primary text | Deep plant green, nearly black: serious and readable in sunlight. |
| `sage` | `#4B8864` | Primary button ("Log in", "Get Started"), health ring, active tab, links | Calm, natural green; reads as "healthy" without being neon. |
| `cream` | `#F7F3EC` | App background | Warm paper tone, easier on the eyes than pure white and connected to soil and nature. |
| `paper` | `#FEFFFA` | Cards, sheets, inputs on cream | Cards float on cream with almost no shadow (flat SaaS look). |
| `stone` | `#EEECE4` | Input fields, chips, dividers | Soft neutral that separates without lines. |
| `muted` | `#63756B` | Secondary text, captions, inactive tabs | Green-grey keeps even the grey text "on brand". |

**Status colours** (used only when something is wrong):

| Token | Hex | Meaning |
|---|---|---|
| `ok` | `#4B8864` (sage) | Normal, "All good" |
| `warning` | `#E3A33B` | Close to the limit, "look soon" (matches the sun icon) |
| `critical` | `#802E2F` | Out of range, "act now" (priority alert icon) |
| `water` | `#6E9BC4` | Humidity, moisture and irrigation icons; too wet on the map |

**Map heat scale (temperature layer):** `water` (too cold) → `sage` (OK) → `warning` → `critical`, always relative to the zone's crop profile.

## Typography

**Inter**, the single typeface (free, built into Figma, covers Cyrillic for a future Russian/Kazakh version, and has tabular numbers, so 24.3 °C doesn't jump as it updates).

| Style | Size / line | Weight | Example in the file |
|---|---|---|---|
| Display | 32 / 38 | Bold | "Welcome", "My Greenhouse", "1,280 kg" |
| H1 | 24 / 30 | Bold | "Zone B", "Tomatoes" |
| H2 | 18 / 24 | Semibold | "Priority alert", "Quick Stats" |
| Body | 15 / 22 | Regular | Descriptions, list rows |
| Label | 13 / 18 | Medium | Field labels, chips, units |
| Caption | 11 / 14 | Regular, `muted` | "Updated now", "Next harvest", tab labels |

## Components and spacing

- **Spacing:** 4-pt grid (4, 8, 12, 16, 20, 24, 32). Screen side padding is 20.
- **Radius:** cards 20, inputs 14, buttons 999 (pill). Soft and friendly, never sharp.
- **Cards:** `paper` on `cream`, no or very soft shadow. An icon in a tinted 32 px circle (amber for sun, pink for alert, blue for water).
- **Buttons:** primary = sage pill with white text; secondary = outline pill; dark chip = forest pill.
- **Status:** always icon + word ("Healthy · All good", "Moisture below target"), never colour alone.
- **Touch targets:** at least 48 pt. Device rows are full-width cards.
- **Tab bar (5):** Home · Greenhouse (map) · Analysis · Harvest · Profile. Alerts open from the bell on Home.
- **Icons:** outline, rounded caps, 1.5 px stroke (Lucide-style).

## Design principles

1. **5-second answer.** The health ring on Home ("92 % · Healthy · All good") tells you at once whether everything is OK.
2. **Show where, not just what.** The priority alert names the zone ("Zone B — moisture below target") and opens it on the map.
3. **Calm by default.** Colour appears only when something needs attention.
4. **Honest data.** Every screen shows when the data is from ("Updated now"). When offline, the app says so.

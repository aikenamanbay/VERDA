# Verda — Project Charter

**Team Supernova** · Aiken, Aruzhan, Asylay, Asel · Week 1 · November 2026

**Repository:** _add GitHub link_

## 1. Name and one-liner

**Verda helps greenhouse operators to spot the exact zone that is in trouble and fix it from their phone in under a minute.**

*Verda* comes from *verde* ("green"). The name is short, easy to say in English, Russian and Kazakh, and doesn't sound like a generic "smart greenhouse".

## 2. Target user

**Marat Seitkali, 46, agronomist-manager of a family greenhouse farm near Talgar, Almaty region.** One 0.4 ha film greenhouse, split into 8 growing zones: tomatoes, cucumbers and strawberries, each with different needs. Marat walks every zone twice a day with a handheld thermometer, and two seasonal workers handle the watering.

His problems:

- **Averages lie.** The thermometer by the door reads 22 °C, but the south-east corner (Area 4) reaches 31 °C by noon. Last June he lost the tomato flowers in that zone before anyone noticed.
- **He can't be everywhere.** When he drives to the Almaty bazaar to sell produce, nobody can tell him whether the windows are open or the drip line is running.
- **Watering is guesswork.** Workers water on a fixed schedule. Strawberries in Area 5 get overwatered while cucumbers in Area 2 dry out.

## 3. Our own extra feature: Live Zone Map

> **Our app can show, on a live colour map of the greenhouse, which exact zone is too hot, too dry or too wet, *because our user* runs 8 zones with different crops, and a greenhouse-wide average hides the one zone that is failing.**

- A top-down plan of the greenhouse split into zones (Area 1–8).
- Three layers: **Temperature / Soil moisture / Plants** (crop, plant count, days to harvest).
- Each zone is coloured green, amber or red against **its own crop's** limits.
- Tapping a zone opens its readings and the devices that serve it.
- The dashboard shows averages; a badge such as "2 zones need attention" links to the map.

**Why it fits in 6 weeks:** the map is a grid of tappable shapes coloured from the same Firestore zone documents that the dashboard already reads. It needs no extra backend, only a different view of the same data.

## 4. Direction (track)

**Agro-intelligence** — the app helps make decisions, not just show numbers:

- **Crop profiles** (tomato, cucumber, strawberry) with preset thresholds. Each zone uses its crop's thresholds for colours, alerts and automation.
- **Trend hint**: "Area 4 will pass 30 °C in ~2 h if nothing changes", estimated from the last hour of history.

## 5. Required modules M1–M8 in Verda

| # | Module | How it works in Verda |
|---|---|---|
| M1 | Login | Email and password via Firebase Auth. Each greenhouse document has an `ownerId`, and Firestore security rules let a user read only their own greenhouse. A wrong password shows an inline error. |
| M2 | Dashboard | One big status ("All good" / "2 zones need attention") plus cards for average air temperature, air humidity, soil moisture and light, and the time of the last update. Values update live through Firestore listeners. |
| M3 | Remote control | Toggle cards for Irrigation, Ventilation (roof windows), Lighting and Heating. A tap writes `isOn` to Firestore; the card shows "Sending…", then a ✓ confirmation within 5 seconds. |
| M4 | Modes | A Manual / Auto switch for the whole greenhouse. In Auto, rules such as "soil moisture < 30% → irrigation on for 2 min" and "temperature > 30 °C → open windows" run without the user. |
| M5 | Alerts | An in-app banner, a push notification and an Alerts list when any zone leaves its crop's range. Tapping an alert opens that zone on the map. |
| M6 | History | Line charts for temperature and soil moisture, switchable between Day and Week, with a zone filter. The scenario it supports: find when the plants lacked water. |
| M7 | Settings | Thresholds per crop profile, a watering schedule, and units (°C / °F). Values are checked (for example, moisture must be 0–100%), and the automation uses them immediately. |
| M8 | No connection | A grey "No connection to greenhouse — showing data from 14:32" bar; controls are disabled. The app reconnects by itself and never crashes. |

## 6. Team and roles

| Member | Role | Builds |
|---|---|---|
| Aiken | Lead mobile developer | Navigation, M1, M2, Zone Map, M3 |
| Aruzhan | Product designer | Logo, design system, Figma prototype, UI kit, M7 screen |
| Asylay | Backend and data | Firebase, schema, security rules, test data, M4, M8 |
| Asel | PM and QA | Charter, README, M5, M6, testing, demo video, slides |

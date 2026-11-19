# VERDA — Project Charter

**Team Supernova** · Aiken Amanbay, Arujan Tulegenova, Assylai Zhumakulova, Assel Balgabay · Week 1 · November 2026

**Repository:** https://github.com/aikenamanbay/VERDA

## 1. Name and one-liner

**VERDA helps home gardeners to see which bed of their greenhouse needs attention, and what to do before a cold night, without being there.**

*Verda* comes from *verde* ("green"). The name is short, easy to say in English, Russian and Kazakh, and doesn't sound like a generic "smart greenhouse".

## 2. Target user

**Aigerim, 37, grows tomato seedlings, cucumbers and lettuce in an unheated polycarbonate greenhouse at her dacha near Almaty.** The greenhouse has 6 beds (Zone A–F). She works weekdays in the city and gets to the dacha in the evenings and at weekends.

Her problems:

- **She can't ventilate at midday.** On sunny days the greenhouse overheats by noon, and the bed under the roof ridge gets much hotter than the one by the door. One thermometer by the door doesn't show it.
- **Watering is guesswork.** A fixed schedule leaves the cucumber bed dry and the lettuce bed soaked.
- **Cold nights catch her out.** In spring and autumn the outdoor low can drop below 0 °C. Before she leaves in the evening she has to remember to close the vents and cover the seedlings, and sometimes she forgets one of them.
- **Morning condensation.** When she finds water dripping on the leaves, she wants to know how long the humidity stayed high.

## 3. Our own extra feature: Zone Map with Cold-Night Readiness

> **Our app can show, on a live map of the greenhouse, which bed is too hot, too dry or at risk of frost tonight, and what still needs doing before she leaves, *because our user* grows different crops in 6 beds of an unheated greenhouse that she can't check in person every day.**

**Zone map** (the idea from our Supernova deck):

- A top-down plan of the greenhouse with beds Zone A–F.
- Three layers: **Temperature / Moisture / Plants** (crop, number of plants, days to harvest).
- Each bed is coloured green, amber or red against **its own crop's** limits. An average of 22 °C can hide one bed at 31 °C.
- Tapping a bed opens its readings and the devices that serve it.

**Cold-night card** (on Home, when the forecast low is below 3 °C):

- "Frost tonight · −2 °C at 04:00" and a checklist: **Vents closed** (taken from the real vent state) and **Seedlings covered** (Aigerim confirms it with a tap).
- She can close the vents from the card. Each item turns green on its own.
- Beds with seedlings are marked on the map as "frost risk".

**Demo:** in the database console, change the overnight low from 6 °C to −2 °C while the vent is open. The card appears with two pending checks. Close the vent from the app and confirm the covers, and both checks turn green.

**Why it fits in 6 weeks:** the map and the card read the same Firestore documents as the dashboard (zones, devices, a `forecast` document). No extra backend is needed.

## 4. Direction (track)

**Agro-intelligence:** the app helps make decisions, not just show numbers.

- **Crop profiles** (tomato, cucumber, lettuce) with preset thresholds. Each bed uses its own crop's limits for colours, alerts and automation.
- The **cold-night readiness** card turns the forecast and the vent state into a to-do list.

## 5. Required modules M1–M8 in VERDA

| # | Module | How it works in VERDA |
|---|---|---|
| M1 | Login | Email and greenhouse code via Firebase Auth. Security rules let each user read only their own greenhouse. A wrong code shows a clear inline error. Logout from Profile. |
| M2 | Dashboard | A health ring ("92 % · Healthy · All good"), cards for average air temperature, air humidity, soil moisture and light, and the last-update time. Values update live through Firestore listeners. |
| M3 | Remote control | Toggles for Watering, Ventilation (roof vents) and Grow lights, plus a Frost heater. Each toggle shows Sending… and then On ✓, confirmed by the database within 5 seconds. |
| M4 | Modes | A Manual / Auto switch. In Auto, watering turns on when soil moisture falls below the bed's threshold and off once it reaches the threshold again; the vents open above 28 °C. |
| M5 | Alerts | An in-app banner, a push notification and an Alerts list when any bed leaves its range. Tapping an alert opens that bed on the map. |
| M6 | History | Charts of temperature, humidity and soil moisture with a Day / Week switch and a zone filter. High-humidity periods (condensation risk) are highlighted. |
| M7 | Settings | Thresholds per crop, the grow-light and watering schedule, and units. Values are checked: −50 % is rejected with a message. The automation uses the new values immediately. |
| M8 | No connection | "No connection to greenhouse — showing data from 14:32", cached values labelled with their time, controls disabled. The app reconnects on its own and never crashes. |

## 6. Team and roles

| Member | Role | Builds |
|---|---|---|
| Aiken Amanbay | Lead mobile developer | Project setup, navigation, M1 Login, M2 Dashboard, Zone Map, M3 Control |
| Arujan Tulegenova | Product designer | Logo, design system, Figma prototype, shared UI kit, M7 Settings screen |
| Assylai Zhumakulova | Backend and data | Firebase, Firestore schema, security rules, test data, M4 Automation, M8 Offline, cold-night logic |
| Assel Balgabay | PM and QA | Charter, README, M5 Alerts, M6 History charts, testing, demo video, slides |

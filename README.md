<h1 align="center">🌿 VERDA</h1>

<p align="center"><b>See which bed needs you, and what to do before a cold night, from your phone.</b></p>

---

**VERDA** helps home gardeners manage an unheated greenhouse remotely. A live **zone map** shows which bed is too hot, too dry or at risk of frost. A **dashboard** shows the overall picture. A **cold-night card** lists what still needs doing before the gardener leaves. The planned app lets the owner control watering, roof vents, grow lights and the frost heater from their phone.

Built by **Team Supernova** for the *Smart Greenhouse* course project (6 weeks, November–December 2026).

## Target user

Aigerim, 37, grows tomato seedlings, cucumbers and lettuce in an unheated 6-bed greenhouse at her dacha. She works weekdays in the city, can't ventilate at midday, waters by guesswork, and sometimes forgets to close the vents or cover the seedlings before a frosty night. Full persona: [project charter](docs/VERDA-Week1-Project-Charter.pdf).

## Team and roles

| Member | Role | Owns in the app (code + design) |
|---|---|---|
| **Aiken Amanbay** | Lead mobile developer | Project setup, navigation, M1 Login, M2 Dashboard, Zone Map, M3 Device control |
| **Arujan Tulegenova** | Product designer | Logo, design system, Figma mockups and clickable prototype; codes the shared UI kit and the M7 Settings screen |
| **Assylai Zhumakulova** | Backend and data engineer | Firebase project, Firestore schema, security rules, test-data seed, data layer, M4 Automation, M8 Offline, cold-night logic |
| **Assel Balgabay** | Product manager and QA | Charter, README, task board, M5 Alerts, M6 History charts, testing, demo video, final presentation |

Team responsibilities are listed above. Application development starts in Week 3.

## Project status

| Week | Deliverable | Status |
|---|---|---|
| 1 | Idea and team ([project charter PDF](docs/VERDA-Week1-Project-Charter.pdf)) | Complete |
| 2 | Design ([documentation](docs/week2-review/README.md), [PDF](docs/week2-review/VERDA-Week2-Design-Supplement.pdf), [app diagram](design/week2-review/architecture.svg)) | Prototype and documents available |
| 3 | App skeleton and test data | Not started |
| 4 | Login, dashboard and device control (M1–M3) | Planned |
| 5 | Automation, alerts, history, settings and offline handling (M4–M8) | Planned |
| 6 | Signature feature and final defense | Planned |

## Current Figma prototype

[Open Verda Copy in Figma](https://www.figma.com/design/Cpu2TuHMSD0BYgCJ9bxeu6/Verda--Copy-?node-id=2029-1402)

- Welcome, sign-in and sign-in error
- Home dashboard, greenhouse status and no-connection state
- Greenhouse map with heat, soil moisture, plants and frost risk, plus details for zones A–F
- Device control, Manual and Auto modes, and automatic watering
- Alerts, Day and Week history, Profile and Settings
- Cold Night forecast and checklist

The Week 2 documentation lists the remaining prototype fixes before the defense.

## Tech stack

**React Native (Expo, TypeScript) + Firebase (Auth, Cloud Firestore).** We plan to preview the app on iPhones with Expo Go and build the Android APK with EAS. See the [stack rationale](docs/week2-review/README.md#stack).

## Repository layout

- [brief/](brief/) contains the team’s idea presentation.
- [docs/](docs/) contains the Week 1 charter and Week 2 documents.
- [design/week2-review/](design/week2-review/) contains the current architecture diagram.
- Application setup and run instructions will be added in Week 3.

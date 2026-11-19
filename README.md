<h1 align="center">🌿 Verda</h1>

<p align="center"><b>Find the zone that's in trouble — and fix it from your phone.</b></p>

---

**Verda** is a mobile app for greenhouse operators. It shows a live **zone map** of the greenhouse next to a **dashboard of averages**, so the user sees both the big picture and the exact spot where something is wrong, and can turn on watering, ventilation, lighting or heating remotely.

Built by **Team Supernova** for the *Smart Greenhouse* course project (6 weeks, Nov–Dec 2026).

## Team and roles

| Member | Role | Owns in the app (code + design) |
|---|---|---|
| **Aiken** | Lead mobile developer | Project setup, navigation, M1 Login, M2 Dashboard, Zone Map (signature feature), M3 Device control |
| **Aruzhan** | Product designer | Logo, design system, Figma mockups + clickable prototype; codes the shared UI kit (theme, cards, buttons) and M7 Settings screen |
| **Asylay** | Backend and data engineer | Firebase project, Firestore schema, security rules, test-data seed script, data layer, M4 Automation, M8 Offline handling |
| **Asel** | Product manager and QA | Charter, README, task board, M5 Alerts, M6 History charts, testing, demo video, final presentation |

Every member commits code every week (the brief asks for 20+ meaningful commits per member).

## Project status

| Week | Deliverable | Status |
|---|---|---|
| 1 | Idea and team — [Project charter](docs/week1-project-charter.md) | ✅ Ready |
| 2 | Design — [Design system](docs/week2-design-system.md), [Data model](docs/week2-data-model.md), [Architecture and stack](docs/week2-architecture.md), [Figma screens and prototype](docs/week2-figma-screens.md) | 🟡 Figma refinement in progress |
| 3 | App skeleton and data | ⏳ |
| 4 | Login, dashboard, control (M1–M3) | ⏳ |
| 5 | Automation, alerts, history (M4–M8) | ⏳ |
| 6 | Extra feature and final defense | ⏳ |

**Figma:** _add the prototype link here_

## Tech stack

**React Native (Expo, TypeScript) + Firebase (Auth, Cloud Firestore).** Full reasoning: [docs/week2-architecture.md](docs/week2-architecture.md#stack).

## How to run (from week 3)

```bash
git clone <repo-url> && cd verda/app
npm install
cp .env.example .env      # add your Firebase web config (never commit .env)
npx expo start            # scan the QR code with the Expo Go app on iPhone
```

Android APK: `npx eas build -p android --profile preview`.

## Repository layout

```
verda/
├── README.md
├── design/   logo, app diagram
├── docs/     weekly deliverables (charter, design system, data model, architecture)
├── brief/    course brief, rubrics, idea deck
└── app/      Expo app (from week 3)
```

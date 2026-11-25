# VERDA Week 2 Design Supplement

Team Supernova · [Current Figma prototype](https://www.figma.com/design/Cpu2TuHMSD0BYgCJ9bxeu6/Verda--Copy-?node-id=2029-1402) · [Architecture diagram](../../design/week2-review/architecture.svg)

## Prototype and style

VERDA helps Aigerim check six beds at her dacha and prepare for frost. The prototype uses the Verda wordmark and Onest. The main palette is forest #13231A for text, mist #EFF3EE for the background, white #FFFFFF for surfaces, lime #C9F25B for primary actions, and muted green-grey #5F6D65 for secondary text. Warning colours appear alongside text labels so Aigerim can spot a problem quickly.

The prototype includes sign-in, Home, the zone map and bed details, Control, Alerts, Day and Week history, Settings, Profile and Cold Night. Home includes a no-connection state.

## Four defense scenarios

| Scenario | Walkthrough |
| --- | --- |
| Check greenhouse status | Open Home. Show the update time and identify overheating in A and dry soil in B. |
| Respond to overheating | Open Alerts → Zone A → open vents. Show confirmation and temperature falling from 31°C to 27°C. |
| Prepare automatic watering | Open Control → Auto → Automatic watering. Show the threshold, duration and selected zones, then save. |
| Find a dry period | Open History → Week for B. Show Monday to Tuesday and the low of 22%. Switch to Day. |

Before defense, update the Figma return states so cooling A leaves B marked dry and watering B leaves A marked hot. Make one watering setting editable and show its new value after saving. Keep Auto active when reopening Control. Route offline users to disabled controls, preserve Cold Night steps on return from the map, and connect a third device such as Grow lights. These are prototype fixes still to make in Figma.

## Firestore data structure

Paths beginning with an ellipsis are under `greenhouses/{id}`.

| Path | Main fields and purpose |
| --- | --- |
| `users/{uid}` | name, email, greenhouseId |
| `greenhouses/{id}` | name, ownerId, mode, lastUpdate |
| `…/zones/{zoneId}` | name, crop, plantCount, airTemp, airHumidity, soilMoisture, light, updatedAt |
| `…/devices/{deviceId}` | type, zoneIds, isOn, updatedAt, updatedBy. Example: irrigation-B serves Zone B. |
| `…/settings/main` | cropProfiles, rules, schedule, units. The cucumber rule targets B and E below 30% and runs for two minutes. |
| `…/history/{readingId}` | ts, zoneId and the four readings. Seed hourly readings per zone for at least seven days. |
| `…/alerts/{alertId}` | ts, zoneId, param, value, limit, read |
| `…/activity/{eventId}` | ts, deviceId, isOn, actorId, source (manual or auto) |
| `…/forecast/tonight` | outdoorLow, lowAt, forecastDate |
| `…/checklist/tonight` | forecastDate, seedlingsCovered, coveredAt. Read vent status from devices. |

Use Firebase Auth email and password. Firestore rules should check the authenticated UID against the parent greenhouse owner for greenhouse documents and their subcollections. Give users access to their own account document.

## From screen to database and back

1. When Aigerim taps Water in Zone B, the screen shows Sending and calls the data layer with the `irrigation-B` device ID.
2. The data layer sends one Firestore batch for the device state and the activity log. Firestore checks ownership.
3. After Firestore confirms the batch, the app shows On. A device subscription keeps the displayed state in sync.
4. For the course demo, update Zone B's test moisture separately in Firebase Console. The zones listener updates Home and the map.
5. If the connection drops, show the last reading and its time. Disable device controls until reconnection.

The planned in-app automation listens for reading changes while the app is running and checks the active mode, crop rules and schedule before writing device changes. On the defense demo, keep the app open and change test readings in Firestore Console. Operation when the app is closed would require an always-running service and is outside this plan.

Cold Night reads the test forecast and current vent state, then writes the cover confirmation to the checklist. The completed state combines the vent state and the cover confirmation for the current forecast date.

## Stack

React Native with Expo and TypeScript lets the team preview screens on iPhones and build the Android APK with EAS. Firebase Auth handles sign-in, and Cloud Firestore listeners update readings and device states as data changes. NetInfo detects connection changes, and the app retains the latest readings in memory during a connection loss. The Firebase JavaScript SDK in React Native does not provide persistent Firestore caching. Use in-app alerts for the course demo and react-native-gifted-charts for history.

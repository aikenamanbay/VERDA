# VERDA

VERDA helps home gardeners to manage an unheated greenhouse from their phone by showing when to ventilate, water, or prepare for a cold night.

## Target user

Aigerim is 37 and grows tomato seedlings in an unheated greenhouse at her dacha. She works weekdays and cannot ventilate in person if it overheats at midday. A fixed watering schedule sometimes leaves the soil too dry or too wet. When she finds condensation in the morning, she wants to know how long humidity stayed high. Before leaving in the evening, she needs to know whether to protect the seedlings from cold.

## Extra feature

Our app can show when a cold night is expected and track whether the vents are closed and the seedlings are covered because our user needs to know what still needs doing before she leaves. The card uses the reported vent state and lets Aigerim confirm that she covered the seedlings.

For the demo, change the stored overnight outdoor low from 6°C to −2°C with the vent open. The card shows the forecast time and two pending checks. Close the vent from the app, then confirm the seedlings are covered. The card updates each check separately.

## Dashboard design

An animated greenhouse scene reflects outdoor conditions. Indoor cards flag readings that need attention and show when the data was updated. [Animated farm weather reference](https://www.instagram.com/p/DeHgsCZpfgS/)

## A day with VERDA

1. **Midday heat.** Indoor temperature crosses the configured limit. The gardener opens the alert, checks the latest reading, and turns on ventilation in manual mode.
2. **Dry soil.** In automatic mode, irrigation starts below the configured soil moisture threshold and stops once the reading reaches it.
3. **Cold evening.** The cold-night card shows when the outdoor low is expected and what still needs checking before Aigerim leaves.
4. **Morning condensation.** The gardener opens the humidity chart to see when and for how long the air was unusually humid.

## Direction

**Agro-intelligence.** VERDA uses the forecast and vent state to show what Aigerim still needs to check before a cold night.

## Required modules

| Module | VERDA behavior |
| --- | --- |
| M1 · Login | Sign in or out, show a clear error for a wrong password, and restrict access to the greenhouse assigned to that account. |
| M2 · Dashboard | Show live air temperature, air humidity, soil moisture, and light, with the last reading time. |
| M3 · Device control | In manual mode, switch irrigation, ventilation, and seedling grow lights on or off and confirm the new cloud state within five seconds. |
| M4 · Modes | Switch between manual and automatic modes. In automatic mode, turn irrigation on below the soil moisture threshold and off once moisture reaches it. |
| M5 · Alerts | Warn when a reading leaves its configured range. Open the relevant reading when the gardener taps the alert. |
| M6 · History | Chart air temperature, air humidity, and soil moisture by day or week. Highlight high-humidity periods so the gardener can spot when condensation is more likely. |
| M7 · Settings | Save valid thresholds, a grow-light schedule, and display units. Automation uses the saved rules immediately. |
| M8 · Offline | Show a connection message, label any cached readings with their timestamps, and resume live updates automatically after reconnecting. |

The mobile app uses simulated sensor readings, device states, and outdoor forecast data from a cloud database.

## Team roles

Proposed assignments for the four team members.

| Member | Responsibility |
| --- | --- |
| Aiken Amanbay | Product and UI design. Own the charter, user flows, and Figma prototype. |
| Assel Balgabay | Core app and cloud data. Implement login, live dashboard, and device controls (M1–M3). |
| Arujan Tulegenova | Automation and alerts. Implement modes, rules, notifications, and settings (M4, M5, M7). |
| Assylai Zhumakulova | History, offline behavior, and cold-night readiness. Implement M6, M8, and the extra feature. Coordinate demo testing. |

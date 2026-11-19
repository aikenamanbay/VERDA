# Verda — Data Structure (Cloud Firestore)

All data for one greenhouse sits under one document, so a single security rule (`ownerId == request.auth.uid`) protects everything (M1).

```
users/{uid}
greenhouses/{greenhouseId}
 ├── zones/{zoneId}          current readings per zone   (M2, map)
 ├── devices/{deviceId}      on/off state                 (M3, M4)
 ├── settings/main           thresholds, rules, units      (M4, M7)
 ├── history/{readingId}     hourly snapshots, 7+ days     (M6)
 ├── alerts/{alertId}        out-of-range events           (M5)
 └── activity/{eventId}      who switched what and when    (M3 log)
```

## 1. `users/{uid}`

| Field | Type | Example |
|---|---|---|
| `name` | string | "Marat Seitkali" |
| `email` | string | "marat@verda.app" |
| `greenhouseId` | string | "gh_talgar_01" |
| `createdAt` | timestamp | |

## 2. `greenhouses/{greenhouseId}`

| Field | Type | Example | Notes |
|---|---|---|---|
| `name` | string | "Talgar Greenhouse" | |
| `ownerId` | string | uid | Used by the security rules |
| `areaM2` | number | 4000 | |
| `mode` | string | `"auto"` \| `"manual"` | M4 switch |
| `lastUpdate` | timestamp | | Shown on Home ("Updated 12 s ago") |

## 3. Current readings — `zones/{zoneId}`

| Field | Type | Example |
|---|---|---|
| `name` | string | "Area 4" |
| `crop` | string | `"tomato"` (key into crop profiles) |
| `plantCount` | number | 180 |
| `plantedAt` | timestamp | 2026-09-01 |
| `daysToHarvest` | number | 34 |
| `layout` | map | `{ x: 2, y: 0, w: 1, h: 1 }` — position on the map grid |
| `airTemp` | number (°C) | 31.5 |
| `airHumidity` | number (%) | 62 |
| `soilMoisture` | number (%) | 28 |
| `light` | number (lux) | 14500 |
| `updatedAt` | timestamp | |

The dashboard **averages are computed in the app** from all zone documents, for example (10 + 15 + 19 + 17) / 4 = 15.3 °C. The map colours each zone against its crop's limits. Map and dashboard read the same data.

## 4. Devices — `devices/{deviceId}`

| Field | Type | Example |
|---|---|---|
| `type` | string | `"irrigation"` \| `"ventilation"` \| `"lighting"` \| `"heating"` |
| `name` | string | "Drip irrigation" |
| `zoneIds` | array | `["area_2","area_4"]` (empty = whole greenhouse) |
| `isOn` | boolean | true |
| `autoOffAt` | timestamp \| null | Irrigation stops automatically after N minutes |
| `updatedAt` | timestamp | |
| `updatedBy` | string | uid or `"automation"` |

## 5. Settings — `settings/main`

```json
{
  "units": { "temperature": "C" },
  "cropProfiles": {
    "tomato":     { "airTemp": [18, 28], "soilMoisture": [40, 70], "airHumidity": [50, 75] },
    "cucumber":   { "airTemp": [20, 30], "soilMoisture": [50, 80], "airHumidity": [60, 85] },
    "strawberry": { "airTemp": [15, 26], "soilMoisture": [35, 65], "airHumidity": [50, 70] }
  },
  "rules": [
    { "id": "r1", "param": "soilMoisture", "op": "<", "value": 30, "device": "irrigation",  "action": "on", "durationMin": 2 },
    { "id": "r2", "param": "airTemp",      "op": ">", "value": 30, "device": "ventilation", "action": "on" }
  ],
  "schedule": [
    { "device": "irrigation", "time": "06:00", "durationMin": 10, "days": ["mon","wed","fri"] }
  ]
}
```

Validation in the app (M7): a percentage must be 0–100, min < max, temperature −20…60 °C. Wrong values (for example −50 %) are rejected with a message.

## 6. History — `history/{readingId}`

One document **per zone per hour**: 8 zones × 24 h × 7 days = **1,344 docs** of test data.

| Field | Type | Example |
|---|---|---|
| `ts` | timestamp | 2026-11-18 14:00 |
| `zoneId` | string | "area_4" |
| `airTemp` | number | 29.8 |
| `airHumidity` | number | 58 |
| `soilMoisture` | number | 22 ← intentionally low (week 3 test data) |
| `light` | number | 16000 |

Query for the charts: `where("zoneId","==",z).where("ts",">=",from).orderBy("ts")`.

## 7. Alerts — `alerts/{alertId}`

| Field | Type | Example |
|---|---|---|
| `ts` | timestamp | |
| `zoneId` | string | "area_4" |
| `param` | string | "airTemp" |
| `value` / `limit` | number | 45 / 28 |
| `severity` | string | `"warning"` \| `"critical"` |
| `read` | boolean | false |

## 8. Activity log — `activity/{eventId}`

`{ ts, deviceId, action: "on"|"off", source: "user"|"automation"|"schedule", uid }`. This answers "who turned the heating on at 3 AM?".

## What is written when a device is turned on?

1. `devices/irrigation` ← `{ isOn: true, updatedAt: serverTimestamp(), updatedBy: uid, autoOffAt: now + 2 min }`
2. `activity/{new}` ← `{ ts, deviceId: "irrigation", action: "on", source: "user", uid }`

Both are written in one **batch**, so either both succeed or neither does.

## Security rules (sketch)

```
match /greenhouses/{gh} {
  allow read, write: if request.auth.uid == resource.data.ownerId;
  match /{sub=**}/{doc} {
    allow read, write: if request.auth.uid ==
      get(/databases/$(database)/documents/greenhouses/$(gh)).data.ownerId;
  }
}
```

Firebase keys live in `.env` (git-ignored) and are read through `app.config.ts`. They are never committed.

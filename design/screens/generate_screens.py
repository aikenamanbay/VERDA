"""Generates the Week 2 Verda screens as SVG (393x852, iPhone 15) in the Verda design system.
Run: python3 design/screens/generate_screens.py  -> writes design/screens/*.svg
The SVGs paste into Figma as editable vectors and Inter text layers."""
from pathlib import Path
from xml.sax.saxutils import escape

W, H = 393, 852
C = dict(forest="#26352C", sage="#4B8864", cream="#F7F3EC", paper="#FEFFFA", stone="#EEECE4",
         muted="#63756B", faint="#92988D", warn="#E3A33B", crit="#802E2F", water="#6E9BC4",
         sageT="#E3ECE2", warnT="#FBF0DC", critT="#F6E3E1", waterT="#E3EDF6", line="#E6E2D8")

ICONS = {
    "home": "M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z",
    "sprout": "M12 21v-9 M12 12c0-4 3-6 7-6 0 4-3 6-7 6z M12 14c0-3-2-5-6-5 0 3 2 5 6 5z",
    "chart": "M4 20h16 M6 16l4-5 3 3 6-8",
    "basket": "M3 10h18l-2 10H5z M8 10l4-6 4 6",
    "user": "M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8z M4 21c1-4 4-6 8-6s7 2 8 6",
    "bell": "M6 16v-5a6 6 0 0 1 12 0v5l2 2H4z M10 21h4",
    "drop": "M12 3s6 7 6 11a6 6 0 0 1-12 0c0-4 6-11 6-11z",
    "wind": "M3 8h11a3 3 0 1 0-3-3 M3 12h16a3 3 0 1 1-3 3 M3 16h8",
    "sun": "M12 16a4 4 0 1 0 0-8 4 4 0 0 0 0 8z M12 2v2 M12 20v2 M4.9 4.9l1.4 1.4 M17.7 17.7l1.4 1.4 M2 12h2 M20 12h2 M4.9 19.1l1.4-1.4 M17.7 6.3l1.4-1.4",
    "bulb": "M9 18h6 M10 21h4 M12 3a6 6 0 0 0-4 10.5c1 1 1 2 1 3h6c0-1 0-2 1-3A6 6 0 0 0 12 3z",
    "flame": "M12 3c1 4 6 6 6 11a6 6 0 0 1-12 0c0-3 2-4 3-6 1 2 2 3 3 3 0-3-1-5 0-8z",
    "right": "M9 6l6 6-6 6", "back": "M15 6l-6 6 6 6", "down": "M6 9l6 6 6-6",
    "wifioff": "M3 3l18 18 M8.5 16.5a5 5 0 0 1 7 0 M5 12.5a10 10 0 0 1 5-2.7 M19 12.5a10 10 0 0 0-2.5-1.8 M2 8.8a15 15 0 0 1 4.5-2.7 M22 8.8A15 15 0 0 0 11 5 M12 20h.01",
    "thermo": "M14 14.8V4a2 2 0 0 0-4 0v10.8a4 4 0 1 0 4 0z",
    "alert": "M12 3 2 20h20z M12 10v4 M12 17h.01",
    "check": "M5 12l5 5 9-10", "pin": "M12 21s-7-6-7-11a7 7 0 0 1 14 0c0 5-7 11-7 11z M12 12a2 2 0 1 0 0-4 2 2 0 0 0 0 4z",
    "mail": "M3 6h18v12H3z M3 6l9 7 9-7", "lock": "M5 11h14v10H5z M8 11V7a4 4 0 0 1 8 0v4",
    "eyeoff": "M3 3l18 18 M10.6 10.6a2 2 0 0 0 2.8 2.8 M9.9 5.1A10 10 0 0 1 22 12a17 17 0 0 1-2.2 3.2 M6.6 6.6A17 17 0 0 0 2 12s3.6 7 10 7a9 9 0 0 0 4.4-1.1",
    "plus": "M12 5v14 M5 12h14", "clock": "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18z M12 7v5l3 2",
    "refresh": "M20 11a8 8 0 1 0-2.3 5.7 M20 4v7h-7",
}


class S:
    def __init__(self, name, bg=C["cream"]):
        self.name, self.parts = name, [f'<rect x="0" y="0" width="{W}" height="{H}" fill="{bg}"/>']

    def add(self, s):
        self.parts.append(s)

    def rect(self, x, y, w, h, r=0, fill=C["paper"], stroke=None, sw=1, op=None, dash=None):
        a = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        a += f' opacity="{op}"' if op is not None else ""
        a += f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"{a}/>')

    def text(self, x, y, s, size=15, weight=400, fill=C["forest"], anchor="start", op=None, ls=None):
        a = f' text-anchor="{anchor}"' if anchor != "start" else ""
        a += f' opacity="{op}"' if op is not None else ""
        a += f' letter-spacing="{ls}"' if ls is not None else ""
        self.add(f'<text x="{x}" y="{y}" font-family="Inter" font-size="{size}" font-weight="{weight}" fill="{fill}"{a}>{escape(s)}</text>')

    def icon(self, name, cx, cy, size=20, color=C["forest"], sw=1.8):
        k = size / 24
        self.add(f'<path transform="translate({cx - size / 2} {cy - size / 2}) scale({k})" d="{ICONS[name]}" '
                 f'fill="none" stroke="{color}" stroke-width="{sw / k:.2f}" stroke-linecap="round" stroke-linejoin="round"/>')

    def badge(self, name, cx, cy, tint, color, r=18, size=18):
        self.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{tint}"/>')
        self.icon(name, cx, cy, size, color)

    def statusbar(self, dark=False):
        col = C["forest"]
        self.text(32, 34, "9:41", 15, 600, col)
        self.rect(330, 23, 25, 12, 3.5, "none", col, 1.2)
        self.rect(332, 25, 18, 8, 2, col)
        for i, h in enumerate([4, 6, 8, 10]):
            self.rect(296 + i * 5, 34 - h, 3, h, 1, col)

    def header(self, title, sub=None, back=False, right=None):
        x = 20
        if back:
            self.rect(20, 56, 40, 40, 20, C["paper"], C["line"])
            self.icon("back", 40, 76, 18)
            x = 20
            self.text(x, 128, title, 30, 700, ls=-0.6)
            if sub:
                self.text(x, 152, sub, 13, 400, C["muted"])
        else:
            self.text(x, 100, title, 30, 700, ls=-0.6)
            if sub:
                self.icon("pin", 27, 119, 13, C["muted"])
                self.text(38, 124, sub, 13, 400, C["muted"])
        if right:
            self.rect(333, 70 if not back else 56, 40, 40, 20, C["paper"], C["line"])
            self.icon(right, 353, 90 if not back else 76, 18)

    def chips(self, y, labels, active, x=20, h=34):
        for i, l in enumerate(labels):
            w = 22 + len(l) * 7.4
            on = i == active
            self.rect(x, y, w, h, h / 2, C["forest"] if on else C["paper"], None if on else C["line"])
            self.text(x + w / 2, y + h / 2 + 5, l, 13, 600 if on else 500, C["paper"] if on else C["forest"], "middle")
            x += w + 8
        return x

    def toggle(self, x, y, on, disabled=False, pending=False):
        fill = C["sage"] if on else (C["stone"] if not pending else C["sageT"])
        op = 0.45 if disabled else None
        self.rect(x, y, 50, 30, 15, fill, None, op=op)
        kx = x + 35 if on else (x + 25 if pending else x + 15)
        self.add(f'<circle cx="{kx}" cy="{y + 15}" r="12" fill="#FFFFFF"{f' opacity="{op}"' if op else ""}/>')
        if pending:
            self.add(f'<path d="M{kx - 6} {y + 15} a6 6 0 0 1 6 -6" fill="none" stroke="{C["sage"]}" stroke-width="2" stroke-linecap="round"/>')

    def tabbar(self, active):
        self.rect(0, 772, W, 80, 0, C["paper"])
        self.add(f'<line x1="0" y1="772" x2="{W}" y2="772" stroke="{C["line"]}"/>')
        tabs = [("home", "Home"), ("sprout", "Greenhouse"), ("chart", "Analysis"), ("basket", "Harvest"), ("user", "Profile")]
        for i, (ic, label) in enumerate(tabs):
            cx = 39 + i * 78.75
            col = C["sage"] if i == active else C["faint"]
            self.icon(ic, cx, 796, 22, col)
            self.text(cx, 822, label, 10.5, 600 if i == active else 500, col, "middle")
        self.rect(130, 838, 134, 5, 2.5, C["forest"])

    def homebar(self):
        self.rect(130, 838, 134, 5, 2.5, C["forest"])

    def save(self, out):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
               f'<title>{escape(self.name)}</title>\n' + "\n".join(self.parts) + "\n</svg>\n")
        (out / f"{self.name}.svg").write_text(svg)


# ---------------------------------------------------------------- screens
def map_screen():
    s = S("10 Greenhouse map"); s.statusbar()
    s.header("My Greenhouse", "Verda Greenhouse · 6 zones", right="bell")
    s.add(f'<circle cx="365" cy="76" r="5" fill="{C["crit"]}"/>')
    s.chips(146, ["Temperature", "Moisture", "Plants"], 0)
    # map card
    s.rect(20, 196, 353, 372, 24)
    s.text(36, 224, "Live zone map", 13, 600, C["muted"])
    s.text(357, 224, "Updated 12 s ago", 11, 400, C["faint"], "end")
    s.rect(36, 238, 321, 34, 10, C["stone"])
    s.text(196.5, 260, "Head House · entrance", 12, 500, C["muted"], "middle")
    zones = [("Zone A", "Tomatoes", "19°", C["sageT"], C["sage"]), ("Zone B", "Cucumbers", "22°", C["sageT"], C["sage"]),
             ("Zone C", "Tomatoes", "24°", C["sageT"], C["sage"]), ("Zone D", "Tomatoes", "31°", C["critT"], C["crit"]),
             ("Zone E", "Lettuce", "27°", C["warnT"], C["warn"]), ("Zone F", "Seedlings", "14°", C["waterT"], C["water"])]
    for i, (n, crop, v, tint, col) in enumerate(zones):
        x = 36 + (i % 2) * 164; y = 282 + (i // 2) * 92
        s.rect(x, y, 157, 84, 14, tint, col, 2 if col == C["crit"] else 1)
        s.text(x + 12, y + 24, n, 13, 600, C["forest"])
        s.text(x + 12, y + 40, crop, 11, 400, C["muted"])
        s.text(x + 145, y + 70, v, 26, 700, col, "end", ls=-0.5)
        if col == C["crit"]:
            s.badge("alert", x + 133, y + 22, "#FFFFFF", C["crit"], 11, 13)
    # aisle
    s.rect(193, 282, 7, 268, 3.5, C["stone"])
    # legend
    lx = 36
    for label, col in [("Cold", C["water"]), ("OK", C["sage"]), ("Warm", C["warn"]), ("Hot", C["crit"])]:
        s.add(f'<circle cx="{lx + 5}" cy="{586 + 0}" r="5" fill="{col}"/>')
        s.text(lx + 15, 590, label, 11.5, 500, C["muted"]); lx += 62
    s.text(357, 590, "vs. crop limits", 11, 400, C["faint"], "end")
    # insight + zone peek
    s.rect(20, 606, 353, 54, 16, C["warnT"])
    s.icon("alert", 44, 633, 18, C["warn"])
    s.text(64, 628, "Average 22.8 °C looks fine —", 13, 600)
    s.text(64, 646, "but Zone D is 3 °C above the tomato limit.", 12, 400, C["muted"])
    s.rect(20, 670, 353, 88, 20)
    s.badge("thermo", 54, 714, C["critT"], C["crit"])
    s.text(84, 704, "Zone D · Tomatoes", 16, 700)
    s.text(84, 724, "31 °C · limit 28 °C · 180 plants", 12, 400, C["muted"])
    s.text(84, 742, "Tap to open zone controls", 11.5, 600, C["sage"])
    s.icon("right", 350, 714, 18, C["muted"])
    s.tabbar(1); return s


def alerts_screen():
    s = S("11 Alerts"); s.statusbar()
    s.header("Alerts", "3 new · Verda Greenhouse", back=True)
    s.chips(172, ["All", "Unread 3", "Critical"], 0)
    items = [
        ("thermo", C["critT"], C["crit"], "Zone D is overheating", "45 °C · limit 28 °C · Tomatoes", "2 min ago", True, "CRITICAL"),
        ("drop", C["warnT"], C["warn"], "Zone B is too dry", "Soil moisture 18 % · min 40 %", "25 min ago", True, "WARNING"),
        ("check", C["sageT"], C["sage"], "Watering turned on automatically", "Rule: moisture < 30 % → 2 min", "26 min ago", True, "AUTO"),
    ]
    earlier = [
        ("thermo", C["waterT"], C["water"], "Zone F is too cold", "14 °C · min 15 °C · Seedlings", "Yesterday, 05:40", False, "RESOLVED"),
        ("refresh", C["stone"], C["muted"], "Connection restored", "Greenhouse back online after 4 min", "Yesterday, 02:12", False, "SYSTEM"),
    ]
    s.text(20, 238, "Today", 13, 600, C["muted"])
    y = 250
    def row(it, y):
        ic, tint, col, t, sub, when, unread, tag = it
        s.rect(20, y, 353, 84, 18)
        s.badge(ic, 54, y + 42, tint, col)
        s.text(84, y + 30, t, 15, 600)
        s.text(84, y + 50, sub, 12.5, 400, C["muted"])
        s.text(84, y + 69, when, 11, 400, C["faint"])
        tw = 12 + len(tag) * 6.4
        s.rect(357 - tw, y + 58, tw, 18, 9, tint)
        s.text(357 - tw / 2, y + 71, tag, 9.5, 700, col, "middle", ls=0.4)
        if unread:
            s.add(f'<circle cx="359" cy="{y + 24}" r="5" fill="{C["crit"] if col == C["crit"] else C["sage"]}"/>')
    for it in items:
        row(it, y); y += 94
    s.text(20, y + 22, "Earlier", 13, 600, C["muted"]); y += 34
    for it in earlier:
        row(it, y); y += 94
    s.tabbar(0); return s


def banner_overlay():
    s = S("12 Alert banner (overlay)", bg="none")
    s.parts = []
    s.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="none"/>')
    s.rect(12, 54, 369, 96, 22, C["forest"])
    s.badge("thermo", 48, 92, "#3A4A40", "#F6B4AE", 20, 20)
    s.text(80, 84, "Overheating in Zone D", 15, 700, "#FFFFFF")
    s.text(80, 104, "45 °C · limit 28 °C · tomatoes at risk", 12.5, 400, "#C9D3CC")
    s.rect(80, 116, 118, 26, 13, C["sage"])
    s.text(139, 133, "Open vents", 12, 600, "#FFFFFF", "middle")
    s.rect(206, 116, 76, 26, 13, "#3A4A40")
    s.text(244, 133, "View zone", 12, 600, "#FFFFFF", "middle")
    s.text(365, 80, "now", 11, 400, "#9FB0A6", "end")
    return s


def devices_screen():
    s = S("13 Devices"); s.statusbar()
    s.header("Devices", "Verda Greenhouse · 4 systems", back=True)
    # mode card
    s.rect(20, 172, 353, 112, 22)
    s.text(36, 202, "Mode", 13, 600, C["muted"])
    s.rect(36, 214, 321, 40, 20, C["stone"])
    s.rect(40, 218, 157, 32, 16, C["sage"])
    s.text(118.5, 239, "Auto", 14, 700, "#FFFFFF", "middle")
    s.text(275.5, 239, "Manual", 14, 500, C["muted"], "middle")
    s.text(36, 272, "2 rules active · edit in Profile › Greenhouse settings", 11.5, 400, C["muted"])
    rows = [
        ("drop", C["waterT"], C["water"], "Watering", "On · auto-off in 1:42", "on", "Zones B, D"),
        ("wind", C["sageT"], C["sage"], "Ventilation", "Sending… opening roof vents", "pending", "Whole greenhouse"),
        ("bulb", C["warnT"], C["warn"], "Grow lights", "Off · schedule 18:00–22:00", "off", "Zones A, C"),
        ("flame", C["critT"], C["crit"], "Frost heater", "Off · auto-on below 2 °C", "off", "Zone F seedlings"),
    ]
    y = 296
    for ic, tint, col, name, st, state, zone in rows:
        s.rect(20, y, 353, 82, 20, C["paper"], C["sage"] if state == "on" else None, 1.5 if state == "on" else 1)
        s.badge(ic, 56, y + 41, tint, col, 20, 20)
        s.text(88, y + 34, name, 16, 600)
        stc = C["sage"] if state == "on" else (C["warn"] if state == "pending" else C["muted"])
        if state == "on":
            s.icon("check", 94, y + 51, 13, C["sage"], 2.2)
            s.text(104, y + 55, st, 12.5, 600, stc)
        else:
            s.text(88, y + 55, st, 12.5, 500 if state == "pending" else 400, stc)
        s.text(88, y + 71, zone, 10.5, 400, C["faint"])
        s.toggle(307, y + 26, state == "on", pending=state == "pending")
        y += 92
    s.text(20, y + 18, "Recent activity", 13, 600, C["muted"])
    s.text(20, y + 40, "14:02  Watering on — automation (Zone B < 30 %)", 12, 400, C["forest"])
    s.text(20, y + 58, "13:40  Ventilation off — Aiken", 12, 400, C["forest"])
    s.tabbar(0); return s


def settings_screen():
    s = S("14 Greenhouse settings"); s.statusbar()
    s.header("Greenhouse settings", "Thresholds, units and schedule", back=True)
    s.text(20, 196, "Crop profiles", 13, 600, C["muted"])
    s.rect(20, 206, 353, 214, 20)
    s.badge("sprout", 52, 238, C["critT"], C["crit"], 16, 16)
    s.text(78, 236, "Tomato", 16, 700); s.text(78, 252, "Zones A, C, D", 11.5, 400, C["muted"])
    s.icon("down", 350, 240, 18, C["muted"])
    for i, (lab, rng, lo, hi, col) in enumerate([("Air temperature", "18 – 28 °C", 0.32, 0.72, C["sage"]),
                                                  ("Soil moisture", "40 – 70 %", 0.40, 0.70, C["water"]),
                                                  ("Air humidity", "50 – 75 %", 0.50, 0.75, C["sage"])]):
        y = 284 + i * 46
        s.text(36, y, lab, 13, 500); s.text(357, y, rng, 13, 700, C["forest"], "end")
        s.rect(36, y + 12, 321, 6, 3, C["stone"])
        s.rect(36 + 321 * lo, y + 12, 321 * (hi - lo), 6, 3, col)
        for p in (lo, hi):
            s.add(f'<circle cx="{36 + 321 * p}" cy="{y + 15}" r="8" fill="#FFFFFF" stroke="{col}" stroke-width="2"/>')
    for i, (crop, zones, tint, col) in enumerate([("Cucumber", "Zone B · 20 – 30 °C · 50 – 80 %", C["sageT"], C["sage"]),
                                                    ("Lettuce", "Zone E · 12 – 24 °C · 45 – 75 %", C["warnT"], C["warn"])]):
        y = 430 + i * 62
        s.rect(20, y, 353, 54, 16)
        s.badge("sprout", 50, y + 27, tint, col, 15, 15)
        s.text(76, y + 24, crop, 14.5, 600); s.text(76, y + 41, zones, 11.5, 400, C["muted"])
        s.icon("right", 350, y + 27, 16, C["muted"])
    s.text(20, 576, "Units", 13, 600, C["muted"])
    s.rect(20, 586, 353, 48, 16)
    s.text(36, 615, "Temperature", 14, 500)
    s.rect(253, 595, 104, 30, 15, C["stone"])
    s.rect(256, 598, 50, 24, 12, C["forest"]); s.text(281, 615, "°C", 12.5, 700, "#FFFFFF", "middle")
    s.text(331, 615, "°F", 12.5, 500, C["muted"], "middle")
    s.text(20, 660, "Watering schedule & rules", 13, 600, C["muted"])
    s.rect(20, 670, 353, 92, 16)
    s.icon("clock", 40, 694, 18, C["water"])
    s.text(60, 699, "06:00 · 10 min · Mon Wed Fri", 13.5, 500); s.toggle(315, 682, True)
    s.add(f'<line x1="36" y1="716" x2="357" y2="716" stroke="{C["line"]}"/>')
    s.icon("sprout", 40, 739, 18, C["sage"])
    s.text(60, 744, "Automation rules", 13.5, 500); s.text(330, 744, "2 active", 12.5, 600, C["sage"], "end")
    s.icon("right", 350, 739, 16, C["muted"])
    s.tabbar(4); return s


def rule_screen():
    s = S("15 Edit rule (validation)"); s.statusbar()
    s.header("Edit rule", "Automatic watering · Zone B", back=True)
    s.rect(20, 172, 353, 224, 22)
    s.rect(36, 188, 36, 22, 11, C["sageT"]); s.text(54, 203, "IF", 11, 700, C["sage"], "middle", ls=0.6)
    s.text(36, 236, "Parameter", 12, 500, C["muted"])
    s.rect(36, 244, 321, 44, 14, C["stone"])
    s.icon("drop", 56, 266, 16, C["water"]); s.text(72, 271, "Soil moisture · Zone B", 14, 500)
    s.icon("down", 338, 266, 16, C["muted"])
    s.text(36, 312, "Is below", 12, 500, C["muted"])
    s.rect(36, 320, 321, 44, 14, "#FFF7F6", C["crit"], 1.5)
    s.text(52, 348, "−50", 16, 600, C["forest"]); s.text(340, 348, "%", 14, 500, C["muted"], "end")
    s.icon("alert", 44, 381, 13, C["crit"])
    s.text(56, 385, "Must be between 0 and 100 %", 12, 600, C["crit"])
    s.rect(20, 406, 353, 150, 22)
    s.rect(36, 422, 52, 22, 11, C["waterT"]); s.text(62, 437, "THEN", 11, 700, C["water"], "middle", ls=0.6)
    s.text(36, 470, "Device", 12, 500, C["muted"])
    s.rect(36, 478, 200, 44, 14, C["stone"]); s.icon("drop", 56, 500, 16, C["water"])
    s.text(72, 505, "Watering on", 14, 500); s.icon("down", 218, 500, 16, C["muted"])
    s.text(248, 470, "For", 12, 500, C["muted"])
    s.rect(248, 478, 109, 44, 14, C["stone"]); s.text(264, 505, "2", 14, 600); s.text(341, 505, "min", 13, 500, C["muted"], "end")
    s.text(36, 544, "Then pause 30 min before checking again", 11.5, 400, C["faint"])
    s.rect(20, 568, 353, 64, 18, C["stone"])
    s.text(36, 594, "Preview", 11.5, 600, C["muted"])
    s.text(36, 614, "Fix the threshold to see what this rule will do.", 12.5, 400, C["muted"])
    s.rect(20, 650, 353, 52, 26, C["sage"], op=0.4)
    s.text(196.5, 681, "Save rule", 15, 600, "#FFFFFF", "middle")
    s.text(196.5, 732, "Delete rule", 14, 600, C["crit"], "middle")
    s.homebar(); return s


def analysis_screen():
    s = S("16 Analysis — climate (week)"); s.statusbar()
    s.header("Analysis", "Verda Greenhouse", right="clock")
    x = s.chips(146, ["Day", "Week"], 1)
    s.rect(x + 4, 146, 112, 34, 17, C["paper"], C["line"])
    s.text(x + 18, 168, "Zone B", 13, 600); s.icon("down", x + 100, 163, 14, C["muted"])
    s.text(357, 168, "12 – 18 Nov", 12, 400, C["muted"], "end")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def chart(y0, title, avg, unit, lo, hi, vmin, vmax, vals, col, low_idx=None, tip=None):
        s.rect(20, y0, 353, 268, 22)
        s.text(36, y0 + 28, title, 13, 600, C["muted"])
        s.text(36, y0 + 60, avg, 28, 700, ls=-0.6); s.text(36 + len(avg) * 15.5, y0 + 60, unit, 13, 500, C["muted"])
        px0, px1, py0, py1 = 60, 355, y0 + 90, y0 + 228

        def P(i, v):
            return px0 + (px1 - px0) * i / (len(vals) - 1), py1 - (py1 - py0) * (v - vmin) / (vmax - vmin)
        _, yh = P(0, hi); _, yl = P(0, lo)
        s.rect(px0, yh, px1 - px0, yl - yh, 6, C["sageT"])
        s.text(px1, yh - 4, f"allowed {lo}–{hi} {unit.split()[0]}", 10, 500, C["sage"], "end")
        for gv in (vmin, (vmin + vmax) / 2, vmax):
            _, gy = P(0, gv)
            s.add(f'<line x1="{px0}" y1="{gy}" x2="{px1}" y2="{gy}" stroke="{C["line"]}" stroke-dasharray="3 4"/>')
            s.text(px0 - 8, gy + 4, f"{gv:g}", 10, 400, C["faint"], "end")
        pts = " ".join(f"{P(i, v)[0]:.1f},{P(i, v)[1]:.1f}" for i, v in enumerate(vals))
        s.add(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>')
        for d, lab in enumerate(days):
            i = d * (len(vals) - 1) / 6
            s.text(px0 + (px1 - px0) * i / (len(vals) - 1), py1 + 22, lab, 10.5, 600 if lab == "Thu" else 400,
                   C["forest"] if lab == "Thu" else C["faint"], "middle")
        if low_idx is not None:
            cx, cy = P(low_idx, vals[low_idx])
            s.add(f'<circle cx="{cx}" cy="{cy}" r="9" fill="{C["crit"]}" opacity="0.18"/>')
            s.add(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{C["crit"]}" stroke="#FFFFFF" stroke-width="2"/>')
            tx = min(max(cx, px0 + 90), px1 - 90)
            s.rect(tx - 90, cy - 48, 180, 32, 10, C["forest"])
            s.text(tx, cy - 27, tip, 11.5, 600, "#FFFFFF", "middle")

    temp = [21, 23, 26, 24, 22, 25, 27, 24, 21, 23, 26, 25, 22, 24, 27, 25, 23, 22, 24, 26, 24, 22, 23, 25]
    moist = [62, 58, 55, 51, 47, 44, 41, 37, 33, 27, 22, 18, 26, 48, 63, 60, 57, 54, 52, 61, 58, 55, 53, 51]
    chart(196, "Air temperature", "23.9", " °C avg", 20, 30, 15, 35, temp, C["sage"])
    chart(474, "Soil moisture", "47", " % avg", 50, 80, 0, 100, moist, C["water"], 11, "Thu 14:00 · 18 % — too dry")
    s.tabbar(2); return s


def offline_screen():
    s = S("17 Home — no connection"); s.statusbar()
    s.text(20, 86, "Good evening!", 13, 400, C["muted"])
    s.text(20, 110, "Verda Greenhouse", 22, 700, ls=-0.4)
    s.rect(333, 72, 40, 40, 20, C["paper"], C["line"]); s.icon("bell", 353, 92, 18)
    s.rect(20, 132, 353, 70, 18, C["forest"])
    s.badge("wifioff", 52, 167, "#3A4A40", "#FFFFFF", 18, 18)
    s.text(82, 160, "No connection to greenhouse", 14.5, 700, "#FFFFFF")
    s.text(82, 180, "Showing data from 14:32 · retrying…", 12, 400, "#C9D3CC")
    s.icon("refresh", 352, 167, 18, "#C9D3CC")
    # last known cards (dimmed)
    s.text(20, 232, "Last known values", 13, 600, C["muted"])
    s.rect(20, 244, 172, 112, 22, op=0.75)
    s.add(f'<circle cx="62" cy="300" r="24" fill="none" stroke="{C["stone"]}" stroke-width="6"/>')
    s.add(f'<path d="M62 276 a24 24 0 1 1 -14.1 4.6" fill="none" stroke="{C["faint"]}" stroke-width="6" stroke-linecap="round"/>')
    s.text(62, 305, "92%", 13, 700, C["muted"], "middle")
    s.text(98, 288, "Health", 11, 400, C["faint"]); s.text(98, 306, "Healthy", 15, 600, C["muted"])
    s.text(98, 323, "at 14:32", 11, 400, C["faint"])
    s.rect(201, 244, 172, 112, 22, op=0.75)
    s.icon("sun", 236, 300, 34, C["faint"], 1.6)
    s.text(266, 306, "24°C", 22, 700, C["muted"]); s.text(266, 324, "at 14:32", 11, 400, C["faint"])
    s.text(20, 388, "Controls", 13, 600, C["muted"])
    s.rect(20, 400, 353, 168, 22)
    for i, (ic, name, col) in enumerate([("drop", "Watering", C["water"]), ("wind", "Ventilation", C["sage"]), ("bulb", "Lighting", C["warn"])]):
        y = 416 + i * 44
        s.icon(ic, 44, y + 14, 18, C["faint"]); s.text(66, y + 19, name, 14, 500, C["faint"])
        s.toggle(307, y, False, disabled=True)
    s.rect(36, 548 - 6, 321, 0.1, 0, C["paper"])
    s.text(196.5, 556, "Controls are paused until the connection is back", 11.5, 500, C["muted"], "middle")
    s.rect(20, 584, 353, 64, 18, C["stone"])
    s.icon("alert", 44, 616, 18, C["muted"])
    s.text(64, 611, "Nothing is sent while offline", 13, 600, C["forest"])
    s.text(64, 629, "New readings and alerts load when you're back.", 11.5, 400, C["muted"])
    s.tabbar(0); return s


def login_error_screen():
    s = S("18 Login — error", bg=C["paper"]); s.statusbar()
    s.rect(20, 78, 40, 40, 12, C["sageT"])
    s.icon("sprout", 40, 98, 22, C["sage"])
    s.text(70, 107, "Verda", 26, 700, ls=-0.6)
    s.text(20, 170, "Welcome", 30, 700, ls=-0.6)
    s.text(20, 198, "Log in to care for your plants and keep your", 14.5, 400, C["muted"])
    s.text(20, 218, "greenhouse growing.", 14.5, 400, C["muted"])
    s.rect(20, 246, 353, 300, 24, "#FFFFFF", C["line"])
    s.text(40, 284, "Email", 13, 600)
    s.rect(40, 296, 313, 48, 14, C["stone"]); s.icon("mail", 62, 320, 17, C["muted"])
    s.text(82, 325, "maya@verda.app", 14.5, 400)
    s.text(40, 374, "Greenhouse code", 13, 600)
    s.rect(40, 386, 313, 48, 14, "#FFF7F6", C["crit"], 1.5); s.icon("lock", 62, 410, 17, C["crit"])
    s.text(82, 415, "••••••••••", 15, 600, C["forest"], ls=1); s.icon("eyeoff", 330, 410, 17, C["muted"])
    s.icon("alert", 46, 452, 13, C["crit"])
    s.text(58, 456, "Wrong email or greenhouse code. Try again.", 12, 600, C["crit"])
    s.rect(40, 474, 313, 50, 25, C["sage"])
    s.text(196.5, 504, "Log In", 15.5, 600, "#FFFFFF", "middle")
    s.text(196.5, 580, "Forgot your code?", 13, 600, C["sage"], "middle")
    s.text(160, 606, "New to Verda?", 13, 400, C["muted"], "middle")
    s.text(248, 606, "Get started", 13, 600, C["sage"], "middle")
    s.homebar(); return s


def cold_night_card():
    s = S("19 Cold-night card (Home)", bg="none")
    s.parts = [f'<rect x="0" y="0" width="{W}" height="{H}" fill="none"/>']
    s.rect(16, 40, 361, 250, 24, "#1F2D3D")
    s.add('<circle cx="330" cy="82" r="22" fill="#E8EEF6" opacity="0.9"/><circle cx="341" cy="74" r="20" fill="#1F2D3D"/>')
    for x, y in [(290, 60), (270, 92), (312, 112)]:
        s.add(f'<circle cx="{x}" cy="{y}" r="1.6" fill="#E8EEF6"/>')
    s.text(36, 72, "COLD NIGHT", 11, 700, "#9DB4CF", ls=1)
    s.text(36, 102, "Frost tonight · −2 °C", 22, 700, "#FFFFFF", ls=-0.4)
    s.text(36, 124, "Lowest at 04:00 · Zone F seedlings at risk", 12.5, 400, "#B8C6D6")
    s.rect(32, 142, 329, 52, 14, "#2B3B4E")
    s.add(f'<circle cx="58" cy="168" r="11" fill="{C["sage"]}"/>'); s.icon("check", 58, 168, 13, "#FFFFFF", 2.4)
    s.text(80, 165, "Vents closed", 14, 600, "#FFFFFF"); s.text(80, 182, "Closed from the app · 19:42", 11, 400, "#9DB4CF")
    s.text(345, 173, "Done", 12, 600, "#8FD3A8", "end")
    s.rect(32, 202, 329, 52, 14, "#2B3B4E")
    s.add('<circle cx="58" cy="228" r="10" fill="none" stroke="#9DB4CF" stroke-width="2"/>')
    s.text(80, 225, "Seedlings covered", 14, 600, "#FFFFFF"); s.text(80, 242, "Tap when you've covered Zone F", 11, 400, "#9DB4CF")
    s.rect(263, 214, 86, 28, 14, "#E8EEF6"); s.text(306, 233, "Covered", 12.5, 700, "#1F2D3D", "middle")
    s.text(36, 276, "1 of 2 done · we'll remind you at 21:00", 11.5, 500, "#B8C6D6")
    return s


if __name__ == "__main__":
    out = Path(__file__).parent
    for f in (map_screen, alerts_screen, banner_overlay, devices_screen, settings_screen, rule_screen,
              analysis_screen, offline_screen, login_error_screen, cold_night_card):
        f().save(out)
        print("wrote", f.__name__)

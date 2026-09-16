# -*- coding: utf-8 -*-
"""Interaktive Kiwi für den Hero: großes Signet + Kernpositionen (in %) für n Pakete."""
import math

def kiwi_svg(n):
    cx, cy, R, r = 50.0, 56.0, 46.0, 28.0
    seeds = []
    for i in range(n):
        th = math.radians(200 + (140.0 / (n - 1)) * i) if n > 1 else math.radians(270)
        x, y = cx + r * math.cos(th), cy + r * math.sin(th)
        side = "l" if i < n / 2 - 1 else ("r" if i > n / 2 else "t")
        seeds.append({"x": round(x, 2), "y": round(y / 58 * 100, 2), "rot": round(math.degrees(th) + 90, 1),
                      "side": side, "sx": round(x, 2), "sy": round(y, 2)})
    rays = "".join('<line x1="%s" y1="%s" x2="%.2f" y2="%.2f"/>' % (cx, cy, cx + (sd["sx"] - cx) * 0.78, cy + (sd["sy"] - cy) * 0.78) for sd in seeds)
    svg = (
        '<svg class="kiwi-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 58" aria-hidden="true" focusable="false">'
        '<path d="M%(l)s %(cy)sA%(R)s %(R)s 0 0 1 %(rr)s %(cy)sZ" fill="#8FA748"/>'
        '<path d="M%(l2)s %(cy)sA%(R2)s %(R2)s 0 0 1 %(rr2)s %(cy)sZ" fill="#9DB255" opacity=".55"/>'
        '<path d="M%(l3)s %(cy)sA15 15 0 0 1 %(rr3)s %(cy)sZ" fill="#E4EAD0"/>'
        '<g stroke="#33261D" stroke-width=".7" opacity=".55">%(rays)s</g>'
        '<path d="M%(l)s %(cy)sA%(R)s %(R)s 0 0 1 %(rr)s %(cy)sZ" fill="none" stroke="#33261D" stroke-width="3" stroke-linejoin="miter"/>'
        '<path d="M%(l4)s %(cy)sA5 5 0 0 1 %(rr4)s %(cy)sZ" fill="#33261D"/>'
        '</svg>'
    ) % {"cy": cy, "R": R, "l": cx - R, "rr": cx + R, "R2": R - 12, "l2": cx - R + 12, "rr2": cx + R - 12,
         "l3": cx - 15, "rr3": cx + 15, "l4": cx - 5, "rr4": cx + 5, "rays": rays}
    return {"svg": svg, "seeds": seeds}

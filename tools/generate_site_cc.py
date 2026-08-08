#!/usr/bin/env python3
"""ClearCrest location page generator + deploy folder assembler.
Base components taken verbatim from clearcrest-home.html.
Every replacement asserted; outputs GitHub Pages-ready /site tree."""

import json, os, shutil, datetime

BASE = open("clearcrest-home.html", encoding="utf-8").read()
SITE = "site"
DOMAIN = "https://clearcresthome.com"

CITIES = [
  dict(slug="park-city", city="Park City", st="UT", lat=40.6461, lng=-111.4980,
       gpg="12\\u201325+ gpg", gpg_text="12 to 25+ grains per gallon",
       eyebrow="Park City's Whole-Home Water & Air Specialists",
       hero="Park City and the Snyderville Basin run 12 to 25+ grains hard depending on source, and mountain wells can run harder still. Scale shortens the life of radiant heat systems, tankless heaters, and steam showers. Add wildfire smoke drifting over the Wasatch Back, and the air in your mountain home needs help too. ClearCrest fixes both in one visit.",
       communities=["Promontory", "Glenwild", "Tuhaye", "Red Ledges", "Jeremy Ranch", "Park Meadows"],
       area=["Park City UT", "Snyderville Basin UT", "Promontory UT", "Tuhaye UT", "Jeremy Ranch UT", "Kamas Valley UT", "Heber Valley UT"],
       faq_q="How hard is the water in Park City, and do I really need a softener?",
       faq_local="Most homes in Park City, the Snyderville Basin, and the surrounding golf communities test between 12 and 25+ grains per gallon, with some mountain wells running even harder",
       extraction_local="ClearCrest Water & Air installs and maintains whole-home water and air quality systems for homeowners in Park City's golf course and master-planned communities, including Promontory, Glenwild, Tuhaye, Red Ledges, Jeremy Ranch, and Park Meadows, plus the greater Snyderville Basin and Kamas Valley"),

  dict(slug="heber-city", city="Heber City", st="UT", lat=40.5070, lng=-111.4133,
       gpg="15\\u201328+ gpg", gpg_text="15 to 28+ grains per gallon",
       eyebrow="Heber Valley's Whole-Home Water & Air Specialists",
       hero="The Heber Valley runs 15 to 28+ grains hard, and homes on wells or secondary water often test harder. Scale attacks radiant systems, tankless heaters, and fixtures in the valley's newest luxury builds. Add wildfire smoke funneling through the valley, and the air inside needs help too. ClearCrest fixes both in one visit.",
       communities=["Red Ledges", "Midway", "Charleston", "Daniel", "Timberlakes", "Soldier Hollow area"],
       area=["Heber City UT", "Midway UT", "Red Ledges UT", "Charleston UT", "Daniel UT", "Timberlakes UT"],
       faq_q="How hard is the water in Heber City, and do I really need a softener?",
       faq_local="Most homes in Heber City, Midway, and the Heber Valley's golf communities test between 15 and 28+ grains per gallon, with wells and secondary sources often running harder",
       extraction_local="ClearCrest Water & Air installs and maintains whole-home water and air quality systems for homeowners in the Heber Valley's golf course and master-planned communities, including Red Ledges, Midway, Charleston, Daniel, and Timberlakes"),

  dict(slug="eagle-mountain", city="Eagle Mountain", st="UT", lat=40.3141, lng=-112.0069,
       gpg="18\\u201330+ gpg", gpg_text="18 to 30+ grains per gallon",
       eyebrow="Eagle Mountain's Whole-Home Water & Air Specialists",
       hero="Eagle Mountain and the Cedar Valley run 18 to 30+ grains hard, some of the hardest municipal water in Utah. New builds here lose tankless heaters and fixtures years early to scale. Add valley dust, inversions, and wildfire smoke, and the air in your new home needs help too. ClearCrest fixes both in one visit.",
       communities=["The Ranches", "SilverLake", "Brandon Park", "Pony Express communities", "Saratoga Springs", "Cedar Valley"],
       area=["Eagle Mountain UT", "Saratoga Springs UT", "The Ranches UT", "SilverLake UT", "Cedar Fort UT", "Lehi UT"],
       faq_q="How hard is the water in Eagle Mountain, and do I really need a softener?",
       faq_local="Most homes in Eagle Mountain, The Ranches, SilverLake, and neighboring Saratoga Springs test between 18 and 30+ grains per gallon, among the hardest municipal water in Utah",
       extraction_local="ClearCrest Water & Air installs and maintains whole-home water and air quality systems for homeowners in Eagle Mountain and Cedar Valley's master-planned communities, including The Ranches, SilverLake, Brandon Park, and neighboring Saratoga Springs"),

  dict(slug="south-jordan-daybreak", city="South Jordan", st="UT", lat=40.5622, lng=-111.9297,
       gpg="14\\u201326+ gpg", gpg_text="14 to 26+ grains per gallon",
       eyebrow="Daybreak & South Jordan's Whole-Home Water & Air Specialists",
       hero="South Jordan and Daybreak run 14 to 26+ grains hard. Scale coats tankless heaters, glass, and fixtures across the valley's fastest-growing master-planned community. Add some of the worst winter inversion air on the Wasatch Front, and the air inside your home needs help too. ClearCrest fixes both in one visit.",
       communities=["Daybreak", "Glenmoor golf area", "River Park", "Highland Park", "Riverton", "Herriman"],
       area=["South Jordan UT", "Daybreak UT", "Riverton UT", "Herriman UT", "West Jordan UT", "Bluffdale UT"],
       faq_q="How hard is the water in South Jordan and Daybreak, and do I really need a softener?",
       faq_local="Most homes in South Jordan, Daybreak, Riverton, and Herriman test between 14 and 26+ grains per gallon, far into the very hard range",
       extraction_local="ClearCrest Water & Air installs and maintains whole-home water and air quality systems for homeowners in South Jordan's master-planned communities, including Daybreak, the Glenmoor golf area, Riverton, Herriman, and Bluffdale"),

  dict(slug="lehi", city="Lehi", st="UT", lat=40.3916, lng=-111.8508,
       gpg="15\\u201328+ gpg", gpg_text="15 to 28+ grains per gallon",
       eyebrow="Lehi & North Utah County's Whole-Home Water & Air Specialists",
       hero="Lehi and north Utah County run 15 to 28+ grains hard. Silicon Slopes' newest homes lose tankless heaters and appliances early to scale. Add lake dust off Utah Lake, inversions, and wildfire smoke, and the air inside your home needs help too. ClearCrest fixes both in one visit.",
       communities=["Traverse Mountain", "Thanksgiving Point area", "Holbrook Farms", "Highland", "Alpine", "Saratoga Springs"],
       area=["Lehi UT", "Highland UT", "Alpine UT", "American Fork UT", "Saratoga Springs UT", "Draper UT"],
       faq_q="How hard is the water in Lehi, and do I really need a softener?",
       faq_local="Most homes in Lehi, Traverse Mountain, Highland, and Alpine test between 15 and 28+ grains per gallon, well into the very hard range",
       extraction_local="ClearCrest Water & Air installs and maintains whole-home water and air quality systems for homeowners in Lehi and north Utah County's communities, including Traverse Mountain, Holbrook Farms, Highland, Alpine, and the Thanksgiving Point area"),

  dict(slug="st-george", city="St. George", st="UT", lat=37.0965, lng=-113.5684,
       gpg="15\\u201326+ gpg", gpg_text="15 to 26+ grains per gallon",
       eyebrow="St. George's Whole-Home Water & Air Specialists",
       hero="St. George and Washington County run 15 to 26+ grains hard on Virgin River basin water. Scale is brutal on the pools, misters, tankless heaters, and fixtures of Utah's golf capital. Add desert dust and summer wildfire smoke, and the air inside your home needs help too. ClearCrest fixes both in one visit.",
       communities=["Entrada", "SunRiver", "Coral Canyon", "Green Spring", "Sun City area", "Washington Fields"],
       area=["St. George UT", "Washington UT", "Santa Clara UT", "Ivins UT", "Hurricane UT", "SunRiver UT"],
       faq_q="How hard is the water in St. George, and do I really need a softener?",
       faq_local="Most homes in St. George, Washington, Santa Clara, and Ivins test between 15 and 26+ grains per gallon on Virgin River basin sources",
       extraction_local="ClearCrest Water & Air installs and maintains whole-home water and air quality systems for homeowners in Washington County's golf course communities, including Entrada, SunRiver, Coral Canyon, Green Spring, and Washington Fields"),

  dict(slug="scottsdale-az", city="Scottsdale", st="AZ", lat=33.4942, lng=-111.9261,
       gpg="12\\u201322+ gpg", gpg_text="12 to 22+ grains per gallon",
       eyebrow="Scottsdale's Whole-Home Water & Air Specialists",
       hero="Scottsdale and the Valley run 12 to 22+ grains hard on Colorado River and Salt River water. Scale attacks pool equipment, misters, tankless heaters, and glass across the most golf-dense metro in America. Add dust storms and wildfire smoke, and the air inside your home needs help too. ClearCrest fixes both in one visit.",
       communities=["DC Ranch", "Silverleaf", "Grayhawk", "Troon", "Desert Mountain", "McCormick Ranch"],
       area=["Scottsdale AZ", "Paradise Valley AZ", "Fountain Hills AZ", "Cave Creek AZ", "North Phoenix AZ", "Carefree AZ"],
       faq_q="How hard is the water in Scottsdale, and do I really need a softener?",
       faq_local="Most homes in Scottsdale, Paradise Valley, and the North Valley test between 12 and 22+ grains per gallon on Colorado River and Salt River supplies",
       extraction_local="ClearCrest Water & Air installs and maintains whole-home water and air quality systems for homeowners in Scottsdale's golf course communities, including DC Ranch, Silverleaf, Grayhawk, Troon, Desert Mountain, and McCormick Ranch",
       extra_swaps=[("Utah's winter inversions and summer wildfire smoke", "Arizona's dust storms and wildfire smoke"),
                    ("hardest Utah neighborhoods", "hardest Valley neighborhoods"),
                    ("Utah owned and operated", "Locally operated"),
                    ("Licensed & Insured in Utah", "Licensed & Insured in Arizona"),
                    ("Licensed & Insured \\u00B7 Utah", "Licensed & Insured \\u00B7 Arizona")]),
]

def swap(html, old, new, label, expect_min=1):
    n = html.count(old)
    assert n >= expect_min, f"MISS [{label}]: '{old[:60]}...' found {n}x"
    return html.replace(old, new)

def add_canonical(html, url):
    anchor = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    return swap(html, anchor, anchor + '\n<link rel="canonical" href="' + url + '">', "canonical")

# ---- Assemble site tree ----
os.makedirs(SITE, exist_ok=True)  # non-destructive: aux files (robots, llms, agents, legal) live alongside

# Homepage
home = add_canonical(BASE, DOMAIN + "/")
open(os.path.join(SITE, "index.html"), "w", encoding="utf-8").write(home)
print("BUILT site/index.html")

# CNAME for GitHub Pages custom domain
open(os.path.join(SITE, "CNAME"), "w").write("clearcresthome.com\n")

urls = [DOMAIN + "/"]

for c in CITIES:
    html = BASE
    loc = f"{c['city']}, {c['st']}"
    url = f"{DOMAIN}/locations/{c['slug']}/"

    html = swap(html, "<title>Water Softening &amp; Air Filtration Utah | ClearCrest</title>",
        f"<title>Water Softening &amp; Air Filtration {c['city']} {c['st']} | ClearCrest</title>", "title")
    html = swap(html,
        'content="ClearCrest installs whole-home water softening, PFAS drinking water filtration, and air purification for Utah homes. Book a free in-home test at clearcresthome.com."',
        f'content="ClearCrest installs whole-home water softening, PFAS filtration, and air purification in {loc}. Book a free in-home test at clearcresthome.com."', "meta")
    html = add_canonical(html, url)

    html = swap(html,
        '"areaServed": ["Park City UT", "Eagle Mountain UT", "Salt Lake Valley UT", "Utah County UT", "Davis County UT", "Weber County UT", "Heber Valley UT", "South Jordan UT"],',
        '"areaServed": ' + json.dumps(c["area"]) + ",", "areaServed")
    html = swap(html,
        '"address": {"@type": "PostalAddress", "addressRegion": "UT", "addressCountry": "US"},',
        '"address": {"@type": "PostalAddress", "addressLocality": "' + c["city"] + '", "addressRegion": "' + c["st"] + '", "addressCountry": "US"},\n'
        '  "geo": {"@type": "GeoCoordinates", "latitude": ' + str(c["lat"]) + ', "longitude": ' + str(c["lng"]) + '},', "geo")

    html = swap(html, "How hard is the water in Utah, and do I really need a softener?", c["faq_q"], "faq_q", expect_min=2)
    html = swap(html,
        "Most homes along the Wasatch Front, in Park City, and in Eagle Mountain test between 15 and 30+ grains per gallon",
        c["faq_local"], "faq_a", expect_min=2)

    html = swap(html, "Utah's Whole-Home Water & Air Specialists", c["eyebrow"], "eyebrow")
    html = swap(html,
        "Utah's water runs 15 to 30+ grains hard, some of the hardest in America. It scales your plumbing, shortens the life of every appliance, and dries out skin and hair. Add winter inversions and wildfire smoke, and the air inside your home needs help too. ClearCrest fixes both in one visit.",
        c["hero"], "hero_para")
    html = swap(html, '"15\\u201330+ gpg"', '"' + c["gpg"] + '"', "gpg")

    html = swap(html,
        "ClearCrest Water & Air installs and maintains whole-home water and air quality systems for Utah homeowners, including Park City, Eagle Mountain, the Salt Lake Valley, Utah County, Davis and Weber counties, the Heber Valley, and South Jordan",
        c["extraction_local"], "extraction")
    html = swap(html, "for Utah's 15 to 30+ grain hard water", f"for {c['city']}'s {c['gpg_text']} hard water", "extraction_gpg")
    html = swap(html,
        "for Utah homeowners. Email schedule@clearcresthome.com",
        f"for homeowners in {loc} and surrounding communities. Email schedule@clearcresthome.com", "agent_sentence")
    html = swap(html,
        '["Service Area", ["Park City", "Eagle Mountain", "Salt Lake Valley", "Utah County", "Davis & Weber", "Heber Valley"]]',
        '["Service Area", ' + json.dumps(c["communities"]) + ']', "footer_area")

    for old, new in c.get("extra_swaps", []):
        html = swap(html, old, new, "extra")

    d = os.path.join(SITE, "locations", c["slug"])
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)
    urls.append(url)
    print("BUILT site/locations/" + c["slug"] + "/index.html")

urls += [DOMAIN + "/privacy-policy/", DOMAIN + "/for-agents/"]

# sitemap.xml
today = datetime.date.today().isoformat()
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    sm.append(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>")
sm.append("</urlset>")
open(os.path.join(SITE, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
print("BUILT site/sitemap.xml (" + str(len(urls)) + " URLs)")
print("DONE")

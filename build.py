"""Generates the Gold Hospital multi-page site. Run: python build.py
Edit the content below, then re-run to regenerate every page."""
from pathlib import Path

ROOT = Path(__file__).parent
PHONE1, PHONE1_T = "+91 93922 75000", "+919392275000"
PHONE2, PHONE2_T = "+91 85208 42485", "+918520842485"
EMAIL = "goldhospitalguntur@gmail.com"
WA = "https://wa.me/919392275000"

ICON = {
    "drop": '<path d="M12 3c3 4 6 7 6 11a6 6 0 0 1-12 0c0-4 3-7 6-11z"/>',
    "pulse": '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
    "thyroid": '<path d="M8 4c-3 3-3 7 0 9s2 6 0 7M16 4c3 3 3 7 0 9s-2 6 0 7M8 12h8"/>',
    "spiral": '<path d="M12 3a9 9 0 1 0 9 9M12 7a5 5 0 1 0 5 5M12 11a1 1 0 1 0 1 1"/>',
    "nerve": '<path d="M12 2v6M12 8l-5 5M12 8l5 5M7 13l-3 5M7 13l2 6M17 13l3 5M17 13l-2 6"/>',
    "moon": '<path d="M20 14A8 8 0 1 1 10 4a6 6 0 0 0 10 10z"/>',
    "leaf": '<path d="M12 21c-5 0-8-3-8-7 3 0 6 1 8 4 2-3 5-4 8-4 0 4-3 7-8 7zM12 18V9M12 9c-2-2-2-5 0-7 2 2 2 5 0 7z"/>',
    "heart": '<path d="M12 20s-7-4.4-9-9a4.5 4.5 0 0 1 9-3 4.5 4.5 0 0 1 9 3c-2 4.6-9 9-9 9z"/>',
    "pin": '<path d="M12 22s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/>',
    "cal": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "user": '<circle cx="12" cy="7" r="4"/><path d="M5 21v-2a7 7 0 0 1 14 0v2"/>',
    "check": '<circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/>',
    "alert": '<circle cx="12" cy="12" r="10"/><path d="M12 7v6M12 17h.01"/>',
    "star": '<path d="M12 2l3 6.5 7 .8-5.2 4.8 1.4 7L12 17.6 5.8 21l1.4-7L2 9.3l7-.8z"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
}
def svg(name, extra=""):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke-width="2" {extra}>{ICON[name]}</svg>'

T = [  # slug, name, icon, image, short, intro, symptoms title, symptoms, benefits
 ("diabetes","Diabetes","drop","Endocrinology-Diabetes.png",
  "Blood-sugar control through medication, diet and regular monitoring.",
  "Our approach goes beyond simply managing blood sugar levels. We educate patients about healthy eating, physical activity, weight management and preventive care to reduce the risk of diabetes-related complications, with regular follow-ups for long-term control.",
  "Common signs and symptoms",
  ["Frequent urination","Increased thirst","Unexplained weight changes","Constant fatigue","Increased hunger","Slow-healing wounds","Blurred vision","Frequent infections"],
  ["Better blood sugar control","Reduced risk of heart disease","Improved energy and daily functioning","Protection of kidney and nerve health","Better weight management","Lower risk of vision-related complications"]),
 ("blood-pressure","Blood Pressure","pulse","Hypertension-High-BP-Wellness-Profile.jpg",
  "Early detection and management of hypertension to protect the heart.",
  "Effective blood pressure treatment combines accurate diagnosis, medication when required, lifestyle guidance and regular follow-up. Our goal is to help you maintain healthy blood pressure and reduce the risk of long-term complications.",
  "Symptoms that should not be ignored",
  ["Frequent headaches","Dizziness or light-headedness","Shortness of breath","Fatigue","Chest discomfort","Blurred vision"],
  ["Reduced risk of heart disease and stroke","Better heart and blood vessel health","Improved kidney function","More energy and well-being","Lower risk of hypertension complications","Early detection of associated concerns"]),
 ("thyroid","Thyroid","thyroid","thyroid-image.jpg",
  "Diagnosis and treatment of hypo- and hyperthyroidism.",
  "Whether you have recently been diagnosed with a thyroid disorder or need ongoing management, we provide comprehensive care aimed at the root cause of your symptoms and your overall quality of life.",
  "Common signs and symptoms",
  ["Unexplained weight gain or loss","Persistent tiredness","Hair thinning or hair loss","Changes in appetite","Mood swings or irritability","Difficulty concentrating","Sleep disturbances","Sensitivity to heat or cold"],
  ["Improved energy and less fatigue","Better metabolism and weight control","Better mood and emotional balance","Improved concentration","Better sleep quality","Healthy hormonal balance"]),
 ("vertigo","Vertigo","spiral","Vertigo.jpg",
  "Evaluation and treatment of dizziness and balance problems.",
  "Our vertigo care begins with a detailed evaluation of your symptoms, health history and lifestyle to understand what is causing dizziness or imbalance, followed by a personalised treatment plan.",
  "Common symptoms",
  ["A spinning sensation","Feeling unsteady or off balance","Dizziness when moving the head","Nausea or vomiting","Difficulty walking or standing steadily","Feeling the surroundings are moving"],
  ["Identify causes of recurring dizziness","Fewer and milder episodes","Better balance and confidence","Reduced risk of falls and injuries","Better management of related conditions","Improved daily comfort"]),
 ("neuropathy","Neuropathy","nerve","Neuropathy-Treatment-23.jpg",
  "Care for nerve pain, tingling and numbness, including diabetic neuropathy.",
  "We focus on understanding the possible causes of nerve-related symptoms and building a suitable care plan that considers your overall health, history, lifestyle and conditions such as diabetes or hypertension.",
  "Common symptoms",
  ["Tingling or pins and needles","Numbness in hands or feet","Burning or sharp pain","Increased sensitivity to touch","Muscle weakness","Difficulty with balance or walking","Discomfort that worsens at night"],
  ["Identify underlying causes","Manage nerve pain and discomfort","Improve mobility and daily function","Support better blood sugar control","Reduce the risk of worsening symptoms","Improve comfort and quality of life"]),
 ("sleep-deprivation","Sleep Problems","moon","Sleep-Disorders.png",
  "Treatment for insomnia and poor sleep by addressing the root cause.",
  "We help restore healthy sleep through lifestyle changes, sleep hygiene education, stress management and medical support when necessary, because quality sleep is one of the foundations of good health.",
  "Signs of sleep deprivation",
  ["Persistent daytime tiredness","Difficulty concentrating","Mood changes or irritability","Trouble falling or staying asleep","Memory problems","Increased stress and anxiety"],
  ["Improved energy and alertness","Better concentration and memory","Better mood","Stronger immune function","Less daytime fatigue","Improved quality of life"]),
 ("stress-management","Stress Management","leaf","Stress-image.jpg",
  "Medical support for stress and its effects on BP, sugar and sleep.",
  "Long-term stress affects blood pressure, blood sugar and sleep. We help patients build practical, sustainable strategies to manage stress and protect both mental and physical health.",
  "Signs stress may be affecting your health",
  ["Persistent fatigue","Difficulty sleeping","Frequent headaches","Irritability or mood changes","Difficulty concentrating","Muscle tension","Feeling overwhelmed or anxious"],
  ["Improved emotional well-being","Better sleep quality","More energy and productivity","Better focus","Better work-life balance","A greater sense of calm"]),
 ("sexual-problems","Sexual Health","heart","Sexual-Problems-image.jpg",
  "Confidential, respectful consultation and treatment.",
  "We understand the sensitive nature of these concerns and ensure complete privacy, respect and compassionate care throughout consultation and treatment. Seeking help can also uncover other health conditions early.",
  "Signs that should not be ignored",
  ["Reduced sexual desire","Difficulty with sexual performance","Reduced satisfaction","Relationship-related stress","Anxiety about sexual health","Loss of confidence"],
  ["Improved confidence","Healthier relationships","Better emotional well-being","Early detection of related conditions","Improved quality of life","Greater overall wellness"]),
]

LOCS = [
 ("Main Hospital","Guntur","12-12-13/2, Opposite Amravati Hospital, Old Club Road, GV Thota, Guntur, Andhra Pradesh 522001","https://maps.app.goo.gl/8vp49yUhH4xesyKYA",PHONE1_T),
 ("Hyderabad","Gachibowli","3rd Floor, Maharaja Abode, Lumbini Avenue, Gachibowli, Hyderabad, Telangana 500032","https://maps.app.goo.gl/BS2TNJMsL8JmcVRh8",PHONE2_T),
 ("Hyderabad","Kukatpally","2nd Floor, Likhita Diagnostics, Opposite JK Hospital, KPHB Colony, Hyderabad, Telangana 500072","https://maps.app.goo.gl/L6GABzcSboY91FHW7",PHONE2_T),
]

REVIEWS = [
 ("My vertigo improved by about 70% after three visits. The doctor was patient and thorough.","Vertigo patient"),
 ("The doctor explained everything clearly and helped reduce my fear of illness.","Retired government employee"),
 ("Good treatment for my neuropathy with clear follow-up advice.","Neuropathy patient"),
 ("Dr. Lenin Reddy treated my urinary tract infection with great care.","Patient"),
]

NAV = [("index.html","Home"),("about.html","About Us"),("treatments.html","Treatments"),
       ("gallery.html","Gallery"),("testimonials.html","Testimonials"),("contact.html","Contact")]


def layout(fname, title, desc, body, current):
    links = []
    for href, label in NAV:
        cls = ' class="current"' if href == current else ""
        if href == "treatments.html":
            sub = "".join(f'<a href="{s}.html">{n}</a>' for s, n, *_ in T)
            links.append(f'<div class="dd"><a href="{href}"{cls}>{label}</a><button class="dd-btn" aria-label="Show treatments" aria-expanded="false"></button><div class="dd-menu">{sub}</div></div>')
        else:
            links.append(f'<a href="{href}"{cls}>{label}</a>')
    tlinks = "".join(f'<a href="{s}.html">{n}</a>' for s, n, *_ in T[:5])
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="images/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="topbar"><div class="wrap">
  <div style="display:flex;gap:20px;flex-wrap:wrap">
    <a href="tel:{PHONE1_T}">{svg("phone")}{PHONE1}</a>
    <a href="mailto:{EMAIL}" class="hide-sm">{svg("mail")}{EMAIL}</a>
  </div>
  <span class="hide-sm">Guntur · Gachibowli · Kukatpally</span>
</div></div>
<header id="hdr"><div class="wrap">
  <a href="index.html" class="brand"><img src="images/logo.png" alt="Gold Hospital logo"><div><b>GOLD HOSPITAL</b><small>GENUINE HEALTH</small></div></a>
  <nav class="menu" id="menu">{"".join(links)}</nav>
  <a href="contact.html" class="btn btn-primary">Book Appointment</a>
  <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
  <div class="fgrid">
    <div><a href="index.html" class="brand" style="margin-bottom:14px"><img src="images/logo.png" alt=""><div><b>GOLD HOSPITAL</b><small>GENUINE HEALTH</small></div></a><p>Preventive, lifestyle and chronic-disease care led by Dr. T. Lenin Reddy, MD, FICN.</p>
      <div class="soc">
        <a href="https://www.facebook.com/goldhospitalguntur/" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24"><path d="M15 3h-2a4 4 0 0 0-4 4v3H7v4h2v7h4v-7h3l1-4h-4V7a1 1 0 0 1 1-1h2z"/></svg></a>
        <a href="https://www.instagram.com/goldhospital_guntur" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/></svg></a>
        <a href="https://www.youtube.com/channel/UC_iLjMo9iGosExm4Rg5Y2Zw/videos" target="_blank" rel="noopener" aria-label="YouTube"><svg viewBox="0 0 24 24"><rect x="2" y="5" width="20" height="14" rx="4"/><path d="M10 9l5 3-5 3z"/></svg></a>
      </div></div>
    <div><h4>Quick Links</h4>{"".join(f'<a href="{h}">{l}</a>' for h, l in NAV)}</div>
    <div><h4>Treatments</h4>{tlinks}<a href="treatments.html">View all →</a></div>
    <div><h4>Contact</h4><a href="tel:{PHONE1_T}">{PHONE1}</a><a href="tel:{PHONE2_T}">{PHONE2}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
  </div>
  <div class="legal"><span>© 2026 Gold Hospital. All rights reserved.</span><span>Information on this website is for general awareness and is not a substitute for a medical consultation.</span></div>
</div></footer>
<div class="mcall"><a href="tel:{PHONE1_T}" class="btn btn-primary">Call Now</a><a href="{WA}" class="btn btn-gold" target="_blank" rel="noopener">WhatsApp</a></div>
<script src="assets/main.js"></script>
</body>
</html>
"""
    (ROOT / fname).write_text(html, encoding="utf-8")


def page_hero(title, crumb, sub=""):
    return f"""<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> / {crumb}</div>
  <h1>{title}</h1>{f'<p>{sub}</p>' if sub else ''}
</div></section>"""


def svc_cards(items):
    return "".join(f"""<a class="svc fade" href="{s}.html"><div class="svc-img"><img src="images/{img}" alt="{n} treatment" loading="lazy"></div><div class="ic over"><svg viewBox="0 0 24 24">{ICON[ic]}</svg></div><h3>{n}</h3><p>{short}</p><span class="more">Learn more →</span></a>""" for s, n, ic, img, short, *_ in items)


def reviews(items):
    return "".join(f'<div class="rev fade"><div class="stars">★★★★★</div><p>{q}</p><span>{who}</span></div>' for q, who in items)


def locs():
    return "".join(f"""<div class="loc fade"><div class="ic"><svg viewBox="0 0 24 24">{ICON["pin"]}</svg></div><small>{k}</small><h3>{c}</h3><p>{a}</p><div class="links"><a href="{m}" target="_blank" rel="noopener">Get directions →</a><a href="tel:{p}">Call</a></div></div>""" for k, c, a, m, p in LOCS)


CTA = f"""<div class="wrap" style="margin-top:88px"><div class="cta fade">
  <div><h2>Book your appointment today</h2><p>Call us or send a WhatsApp message and our team will help you choose a time.</p></div>
  <div class="actions"><a href="tel:{PHONE1_T}" class="btn btn-white">Call {PHONE1}</a><a href="{WA}" target="_blank" rel="noopener" class="btn btn-gold">WhatsApp Us</a></div>
</div></div>"""

GOLD_CHECK = svg("check", 'stroke="#d9a43a"')
CHECKS = "".join(f'<div>{GOLD_CHECK}{t}</div>' for t in
                 ["Diabetes &amp; hypertension","Vertigo &amp; neuropathy","Preventive &amp; lifestyle medicine","Weight &amp; metabolic health"])

# ---------------- Home ----------------
home = f"""<section class="hero"><div class="wrap">
  <div>
    <span class="tag fade" style="--d:.05s">Multispeciality Care in Guntur &amp; Hyderabad</span>
    <h1 class="fade" style="--d:.15s">Expert care for <span>diabetes, BP, thyroid</span> and everyday health.</h1>
    <p class="fade" style="--d:.25s">Led by Dr. T. Lenin Reddy (MD General Medicine, FICN), Gold Hospital focuses on accurate diagnosis, personalised treatment and long-term lifestyle care.</p>
    <div class="actions fade" style="--d:.35s">
      <a href="contact.html" class="btn btn-primary"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{ICON["cal"]}</svg>Book Appointment</a>
      <a href="treatments.html" class="btn btn-outline">View Treatments</a>
    </div>
    <div class="trust fade" style="--d:.45s">
      <div>{svg("user")}16+ years experience</div>
      <div>{svg("pin")}3 clinic locations</div>
      <div>{svg("star")}Rated on Google</div>
    </div>
  </div>
  <div class="fade" style="--d:.3s"><img class="hero-img" src="images/Gold-Hospital-Building.jpeg" alt="Gold Hospital building"></div>
</div></section>

<div class="quick"><div class="wrap">
  <a href="contact.html"><div class="ic">{svg("cal")}</div><div><b>Book a Visit</b><span>Call or WhatsApp</span></div></a>
  <a href="treatments.html"><div class="ic">{svg("pulse")}</div><div><b>Treatments</b><span>8 care programs</span></div></a>
  <a href="about.html"><div class="ic">{svg("user")}</div><div><b>Our Doctor</b><span>Profile &amp; expertise</span></div></a>
  <a href="contact.html#locations"><div class="ic">{svg("pin")}</div><div><b>Find a Clinic</b><span>Directions &amp; address</span></div></a>
</div></div>

<section><div class="wrap">
  <div class="head fade"><span class="tag">Treatments</span><h2>Conditions we treat</h2><p>Focused, evidence-based care for long-term and lifestyle conditions.</p></div>
  <div class="services">{svc_cards(T)}</div>
</div></section>

<section class="alt"><div class="wrap doc">
  <div class="doc-photo real fade"><img src="images/dr.lenin1_.jpg" alt="Dr. T. Lenin Reddy"><div class="badge"><b>Dr. T. Lenin Reddy</b><span>MD General Medicine, FICN</span></div></div>
  <div class="fade">
    <span class="tag">Our Doctor</span>
    <h2>Dr. T. Lenin Reddy</h2>
    <p>Dr. T. Lenin Reddy is a Consultant Physician with more than 16 years of experience in general medicine. He takes time to understand each patient's history and lifestyle, and combines early diagnosis with practical, long-term treatment plans.</p>
    <div class="checks">{CHECKS}</div>
    <a href="about.html" class="btn btn-primary">Learn more about us</a>
  </div>
</div></section>

<section><div class="wrap">
  <div class="head fade"><span class="tag">Your Visit</span><h2>What to expect</h2></div>
  <div class="process">
    <div class="step fade"><h4>Book</h4><p>Call or WhatsApp to choose a clinic and time.</p></div>
    <div class="step fade"><h4>Consult</h4><p>A detailed discussion of your symptoms and history.</p></div>
    <div class="step fade"><h4>Diagnose</h4><p>Tests where needed to find the underlying cause.</p></div>
    <div class="step fade"><h4>Follow up</h4><p>A personal plan with regular reviews of progress.</p></div>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="head fade"><span class="tag">Patient Reviews</span><h2>What our patients say</h2></div>
  <div class="reviews">{reviews(REVIEWS[:3])}</div>
  <div class="center fade"><a class="btn btn-outline" href="testimonials.html">Read all reviews</a></div>
</div></section>

<section><div class="wrap">
  <div class="head fade"><span class="tag">Locations</span><h2>Visit a clinic near you</h2></div>
  <div class="locs">{locs()}</div>
</div></section>
{CTA}"""
layout("index.html", "Gold Hospital | Guntur &amp; Hyderabad",
       "Gold Hospital: diabetes, BP, thyroid, vertigo, neuropathy and lifestyle care by Dr. T. Lenin Reddy in Guntur and Hyderabad.",
       home, "index.html")

# ---------------- About ----------------
about = page_hero("About Gold Hospital", "About Us", "Preventive, lifestyle and chronic-disease care with a personal touch.") + f"""
<section><div class="wrap split">
  <div class="fade"><img class="hero-img" src="images/Gold-Hospital-Building.jpeg" alt="Gold Hospital building"></div>
  <div class="prose fade">
    <span class="tag">Who we are</span>
    <h2 style="margin-top:12px">Healthcare built around the patient</h2>
    <p>Gold Hospital provides comprehensive care for diabetes, hypertension, thyroid disorders, stress, sleep and other lifestyle-related conditions. We serve patients in Guntur and Hyderabad.</p>
    <p>Our approach is holistic: prevention, early diagnosis, compassionate care and lasting lifestyle change. We take time to understand each person so that treatment fits their life.</p>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="services three">
    <div class="svc fade"><div class="ic"><svg viewBox="0 0 24 24">{ICON["star"]}</svg></div><h3>Our Vision</h3><p>To promote healthier lives through preventive care, chronic disease management and personalised guidance.</p></div>
    <div class="svc fade"><div class="ic"><svg viewBox="0 0 24 24">{ICON["heart"]}</svg></div><h3>Our Mission</h3><p>To deliver comprehensive, affordable care for diabetes, BP, thyroid, stress, sleep and lifestyle concerns.</p></div>
    <div class="svc fade"><div class="ic"><svg viewBox="0 0 24 24">{ICON["leaf"]}</svg></div><h3>Our Philosophy</h3><p>Treat the whole person through prevention, early diagnosis and lasting lifestyle change.</p></div>
  </div>
</div></section>

<section><div class="wrap doc">
  <div class="doc-photo real fade"><img src="images/dr.lenin1_.jpg" alt="Dr. T. Lenin Reddy"><div class="badge"><b>Dr. T. Lenin Reddy</b><span>MD General Medicine, FICN</span></div></div>
  <div class="fade">
    <span class="tag">Meet the Doctor</span>
    <h2>Dr. T. Lenin Reddy</h2>
    <p><b>MD General Medicine, FICN · Consultant Physician</b></p>
    <p style="margin-top:12px">With more than 16 years of clinical experience, Dr. Reddy focuses on preventive and lifestyle medicine. He is known among patients for listening carefully, explaining clearly and following up closely.</p>
    <div class="checks">{CHECKS}</div>
    <a href="contact.html" class="btn btn-primary">Book a Consultation</a>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="head fade"><span class="tag">Our Locations</span><h2>Three clinics, one standard of care</h2></div>
  <div class="locs">{locs()}</div>
</div></section>
{CTA}"""
layout("about.html", "About Us | Gold Hospital", "About Gold Hospital and Dr. T. Lenin Reddy, MD, FICN.", about, "about.html")

# ---------------- Treatments ----------------
tr = page_hero("Our Treatments", "Treatments", "Personalised care for chronic and lifestyle-related conditions.") + f"""
<section><div class="wrap"><div class="services">{svc_cards(T)}</div></div></section>
<section class="alt"><div class="wrap">
  <div class="head fade"><span class="tag">Our Focus</span><h2>Three areas of care</h2></div>
  <div class="services three">
    <div class="svc fade"><div class="svc-img"><img src="images/chronic-image.jpg" alt="Chronic disease management" loading="lazy"></div><h3>Chronic Disease Management</h3><p>Diabetes, hypertension, thyroid, vertigo and neuropathy, managed with regular follow-up.</p></div>
    <div class="svc fade"><div class="svc-img"><img src="images/checkup-image.jpg" alt="General medicine" loading="lazy"></div><h3>General Medicine</h3><p>Diagnosis and treatment of acute and chronic illnesses for adults.</p></div>
    <div class="svc fade"><div class="svc-img"><img src="images/lifestyle-image.jpg" alt="Preventive and lifestyle care" loading="lazy"></div><h3>Preventive &amp; Lifestyle Care</h3><p>Health check-ups, lifestyle changes and patient education.</p></div>
  </div>
</div></section>
{CTA}"""
layout("treatments.html", "Treatments | Gold Hospital", "Treatments offered at Gold Hospital, Guntur and Hyderabad.", tr, "treatments.html")

# ---------------- Treatment detail pages ----------------
for slug, name, ic, img, short, intro, stitle, symptoms, benefits in T:
    cur = ' class="current"'
    others = "".join(f'<a href="{s}.html"{cur if s == slug else ""}>{n}</a>' for s, n, *_ in T)
    body = page_hero(f"{name} Treatment", f'<a href="treatments.html">Treatments</a> / {name}', short) + f"""
<section><div class="wrap layout">
  <div>
    <img class="hero-img fade" src="images/{img}" alt="{name} treatment at Gold Hospital" style="aspect-ratio:16/9">
    <div class="prose fade" style="margin:36px 0">
      <h2>Personalised {name.lower()} care</h2>
      <p>{intro}</p>
      <p>Care is led by Dr. T. Lenin Reddy, who brings more than 16 years of experience in General Medicine and considers your overall health and lifestyle in every plan.</p>
    </div>
    <div class="two-lists">
      <div class="box fade"><h3>{svg("alert")}{stitle}</h3><ul>{"".join(f"<li>{s}</li>" for s in symptoms)}</ul></div>
      <div class="box fade"><h3>{svg("check")}Benefits of treatment</h3><ul>{"".join(f"<li>{b}</li>" for b in benefits)}</ul></div>
    </div>
    <p class="fade" style="margin-top:24px">If these symptoms affect your daily life, a medical evaluation can help find the cause and the right treatment.</p>
  </div>
  <aside class="side">
    <div class="box book fade"><h3>Book a consultation</h3><p>Speak to our team to book a visit with Dr. Reddy.</p><a href="tel:{PHONE1_T}" class="btn btn-white">Call {PHONE1}</a><a href="{WA}" target="_blank" rel="noopener" class="btn btn-gold">WhatsApp</a></div>
    <div class="box fade"><h3>All treatments</h3>{others}</div>
  </aside>
</div></section>
{CTA}"""
    layout(f"{slug}.html", f"{name} Treatment in Guntur | Gold Hospital",
           f"{name} treatment at Gold Hospital by Dr. T. Lenin Reddy. {short}", body, "treatments.html")

# ---------------- Gallery ----------------
gal = "".join(f'<button class="fade"><img src="images/Gold-Hospital-Gallery-{i}.jpeg" alt="Gold Hospital photo {i}" loading="lazy"></button>' for i in range(1, 10))
gallery = page_hero("Gallery", "Gallery", "A look inside Gold Hospital.") + f"""
<section><div class="wrap"><div class="gallery">{gal}</div></div></section>
<div class="lb" id="lb" role="dialog" aria-label="Image viewer"><button class="x" aria-label="Close">✕</button><button class="p" aria-label="Previous">‹</button><img alt=""><button class="n" aria-label="Next">›</button></div>
{CTA}"""
layout("gallery.html", "Gallery | Gold Hospital", "Photos of Gold Hospital.", gallery, "gallery.html")

# ---------------- Testimonials ----------------
testi = page_hero("Patient Testimonials", "Testimonials", "Experiences shared by our patients on Google.") + f"""
<section><div class="wrap">
  <div class="reviews">{reviews(REVIEWS)}</div>
  <div class="center fade"><a class="btn btn-outline" href="https://www.youtube.com/channel/UC_iLjMo9iGosExm4Rg5Y2Zw/videos" target="_blank" rel="noopener">Watch video testimonials on YouTube</a></div>
</div></section>
{CTA}"""
layout("testimonials.html", "Testimonials | Gold Hospital", "Patient reviews of Gold Hospital.", testi, "testimonials.html")

# ---------------- Contact ----------------
contact = page_hero("Contact Us", "Contact", "Book an appointment or find your nearest clinic.") + f"""
<section><div class="wrap contact-grid">
  <div class="fade">
    <span class="tag">Get in touch</span>
    <h2 style="margin:12px 0 8px">Book an appointment</h2>
    <p>Call or WhatsApp us to book a visit at any of our clinics.</p>
    <div class="info-row"><div class="ic">{svg("phone")}</div><div><b>Phone</b><a class="tap" href="tel:{PHONE1_T}">{PHONE1}</a><a class="tap" href="tel:{PHONE2_T}">{PHONE2}</a></div></div>
    <div class="info-row"><div class="ic">{svg("mail")}</div><div><b>Email</b><a class="tap" href="mailto:{EMAIL}">{EMAIL}</a></div></div>
    <div class="info-row"><div class="ic">{svg("clock")}</div><div><b>Appointments</b>Please call ahead to confirm timings at each clinic.</div></div>
    <div style="display:flex;gap:12px;margin-top:24px;flex-wrap:wrap"><a href="tel:{PHONE1_T}" class="btn btn-primary">Call Now</a><a href="{WA}" target="_blank" rel="noopener" class="btn btn-gold">WhatsApp Us</a></div>
  </div>
  <div class="fade"><iframe class="map" title="Gold Hospital Guntur map" loading="lazy" src="https://maps.google.com/maps?q=Gold%20Hospital%20Old%20Club%20Road%20Guntur&output=embed"></iframe></div>
</div></section>
<section class="alt" id="locations"><div class="wrap">
  <div class="head fade"><span class="tag">Locations</span><h2>Our clinics</h2></div>
  <div class="locs">{locs()}</div>
</div></section>"""
layout("contact.html", "Contact Us | Gold Hospital", "Contact Gold Hospital in Guntur, Gachibowli and Kukatpally.", contact, "contact.html")

print("Built", len(list(ROOT.glob("*.html"))), "pages")


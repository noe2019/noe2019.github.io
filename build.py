"""Builds the bilingual (FR/EN) static site for noe2019.github.io."""
import json, pathlib

OUT = pathlib.Path(__file__).parent
SITE = "https://noe2019.github.io"
REPO = "https://github.com/noe2019/ML4EO_Bootcamp"
COLAB = "https://colab.research.google.com/github/noe2019/ML4EO_Bootcamp/blob/main/notebooks/"
EMAIL = "noecaremee@gmail.com"
LINKS = {"LinkedIn": "https://www.linkedin.com/in/noefouotsa/", "GitHub": "https://github.com/noe2019",
         "Google Scholar": "https://scholar.google.com/citations?user=acKVfowAAAAJ",
         "Portfolio": "https://noe2019.github.io/DA-Portfolio-Website/"}


def T(fr, en):
    return f'<span class="fr">{fr}</span><span class="en">{en}</span>'


def B(fr, en, tag="div"):
    return f'<{tag} class="fr">{fr}</{tag}><{tag} class="en">{en}</{tag}>'


NAV = [("index.html", "Accueil", "Home"), ("teaching.html", "Enseignement", "Teaching"),
       ("cours-ml4eo.html", "Cours ML4EO", "ML4EO course"), ("cours-fraude360.html", "Cours Fraude", "Fraud course"),
       ("publications.html", "Recherche", "Research"),
       ("portfolio.html", "Projets", "Projects"), ("resume.html", "CV", "CV"), ("contact.html", "Contact", "Contact")]


def page(slug, title, desc, body):
    nav = "".join(f'<a href="{h}"{" class=active" if h == slug else ""}>{T(fr, en)}</a>' for h, fr, en in NAV)
    person = {"@context": "https://schema.org", "@type": "Person", "name": "Noé Carème Fouotsa Manfouo",
              "jobTitle": "Lecturer in data science, statistics and remote sensing", "url": SITE,
              "email": f"mailto:{EMAIL}", "alumniOf": ["Stellenbosch University", "African Institute for Mathematical Sciences"],
              "address": {"@type": "PostalAddress", "addressLocality": "Sherbrooke", "addressRegion": "QC", "addressCountry": "CA"},
              "sameAs": list(LINKS.values())}
    html = f"""<!doctype html>
<html lang="fr" data-lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Noé Carème Fouotsa Manfouo</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title} · Noé Carème Fouotsa Manfouo">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/images/portrait.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="images/portrait-sm.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
<script src="assets/site.js"></script>
<script type="application/ld+json">{json.dumps(person, ensure_ascii=False)}</script>
</head>
<body>
<header class="top"><div class="wrap">
  <a class="logo" href="index.html">Noé C. Fouotsa Manfouo<small>Ph. D. · {T("Science des données", "Data science")}</small></a>
  <button class="burger" id="burger" aria-label="Menu">☰</button>
  <nav class="nav" id="nav">{nav}<button class="lang" id="lang" aria-label="Langue / Language">EN</button></nav>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
  <div>© 2026 Noé Carème Fouotsa Manfouo · Sherbrooke (Québec)</div>
  <div class="icons"><a href="mailto:{EMAIL}">{EMAIL}</a>{"".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in LINKS.items())}</div>
</div></footer>
</body>
</html>
"""
    (OUT / slug).write_text(html, encoding="utf-8")


SESSIONS = [
    (1, "python_bases", "Observation de la Terre et bases de Python", "Earth observation and Python basics"),
    (2, "controle_fonctions", "Structures de contrôle et fonctions", "Control flow and functions"),
    (3, "pandas_meteo", "Analyse de données avec pandas", "Data analysis with pandas"),
    (4, "teledetection_indices", "Fondements de la télédétection et indices spectraux", "Remote sensing foundations and spectral indices"),
    (5, "geopandas_vectoriel", "Données vectorielles (GeoPandas)", "Vector data (GeoPandas)"),
    (6, "raster_xarray", "Données matricielles (rasterio, xarray)", "Raster data (rasterio, xarray)"),
    (7, "gee_chirps", "Google Earth Engine I : pluie CHIRPS", "Google Earth Engine I: CHIRPS rainfall"),
    (8, "gee_hrsl_population", "Google Earth Engine II : population HRSL · examen", "Google Earth Engine II: HRSL population · exam"),
    (9, "ml_fondements", "Fondements de l'apprentissage automatique", "Machine learning foundations"),
    (10, "classification_occupation_sol", "Classification de l'occupation du sol", "Land-cover classification"),
    (11, "validation_cartes", "Validation des cartes et superficies", "Map validation and area estimation"),
    (12, "changements_series_temporelles", "Changements, séries temporelles, sécheresse", "Change, time series and drought"),
    (13, "apprentissage_profond_eurosat", "Apprentissage profond (EuroSAT)", "Deep learning (EuroSAT)"),
    (14, "diffusion_streamlit", "Reproductibilité, éthique et diffusion", "Reproducibility, ethics and communication"),
]

PUBS = [
    ("Race/Ethnicity and Other Predictors of Early-Onset Type 2 Diabetes Mellitus in the US Population",
     "Fouotsa Manfouo, N. C., Ndjaboue, R., Ngueta, G.", "Journal of Racial and Ethnic Health Disparities, 2024",
     [("Article", "https://www.researchgate.net/publication/379147208_Journal_of_Racial_and_Ethnic_Health_Disparities")], "Santé · Health"),
    ("Monitoring commercial and smallholder production inequalities during South Africa's lockdown using remotely sensed data",
     "Fouotsa Manfouo, N. C.", "Agrosystems, Geosciences & Environment, 7(1), 2024",
     [("Article", "https://acsess.onlinelibrary.wiley.com/doi/epdf/10.1002/agg2.20460")], "Télédétection · Remote sensing"),
    ("A Comparison of the Statistical Downscaling and Long-Short-Term-Memory Artificial Neural Network Models for Long-Term Temperature and Precipitations Forecasting",
     "Fouotsa Manfouo, N. C., Potgieter, L., Watson, A., Nel, J. H.", "Atmosphere, 14(4), 708, 2023",
     [("Article", "https://www.mdpi.com/2073-4433/14/4/708")], "Climat · Climate"),
    ("Investigating the effects of drought and lockdowns on smallholder and commercial agricultural production in KwaZulu-Natal using remotely sensed data",
     "Fouotsa Manfouo, N. C., Von Fintel, D.", "Heliyon, 8(11), 2022",
     [("Article", "https://www.researchgate.net/publication/365322669_Investigating_the_effects_of_drought_and_lockdowns_on_smallholder_and_commercial_farming_agricultural_production_in_KwaZulu-Natal_using_remotely_sensed_data_Investigating_the_effects_of_drought_and_lo")], "Télédétection · Remote sensing"),
    ("Temporal trajectories of type 2 diabetes complications from inpatient data collected from 2006 to 2021 at the CHUS",
     "Fouotsa Manfouo, N. C., Ndjaboue, R., Ngueta, G.", "Affiche · Poster, 2024",
     [("PDF", "docs/poster-t2dm-trajectories-2024.pdf"), ("Démo · Demo", "https://noe-t2dm-trajectories-094c80ceabf2.herokuapp.com/")], "Santé · Health"),
    ("Application of classification models on Sentinel-2 images and tree stands shapefiles for invasive alien trees mapping in the Overberg region, South Africa",
     "Fouotsa Manfouo, N. C., et al.", "Manuscrit · Manuscript",
     [("PDF", "https://drive.google.com/file/d/1pqSl5teMe3puq1RqqU6gwzns7rLO9H9f/view?usp=drive_link"), ("Démo · Demo", "https://noe-invasive-species-814a7fc4c770.herokuapp.com/")], "Télédétection · Remote sensing"),
    ("Comparison of time series methods for Lake Chad Basin storage forecasting",
     "Fouotsa Manfouo, N. C., et al.", "Manuscrit · Manuscript",
     [("PDF", "https://drive.google.com/file/d/1IUm6gZS1sqg7qPlrQwD0KnH2vtpy5e_-/view?usp=sharing"), ("Démo · Demo", "https://noe-water-storage-34fdf1488682.herokuapp.com/")], "Climat · Climate"),
]

APPS = [
    ("Reservoir Water Storage Forecasting", "Prévision du stockage d'eau des réservoirs (séries temporelles, ML).", "Reservoir storage forecasting (time series, ML).", "https://noe-water-storage-34fdf1488682.herokuapp.com/", "Télédétection"),
    ("Invasive Alien Tree Mapping", "Classification Sentinel-2 des arbres envahissants (Overberg).", "Sentinel-2 classification of invasive trees (Overberg).", "https://noe-invasive-species-814a7fc4c770.herokuapp.com/", "Télédétection"),
    ("Food Security Monitoring", "Effets de la sécheresse et des confinements sur l'agriculture (NDVI).", "Drought and lockdown effects on farming (NDVI).", "https://noe-food-security-c984fe0b9737.herokuapp.com/", "Télédétection"),
    ("T2DM Complication Trajectories", "Analyse de graphes des complications du diabète de type 2.", "Graph analysis of type 2 diabetes complications.", "https://noe-t2dm-trajectories-094c80ceabf2.herokuapp.com/", "Santé"),
    ("Multiple Disease Prediction", "Risque de diabète, maladies cardiaques et Parkinson.", "Diabetes, heart disease and Parkinson's risk.", "https://noe-multi-disease-5ba608b87c4d.herokuapp.com/", "Santé"),
    ("AutoML Task Generalizer", "Profilage, sélection de modèle et export automatiques.", "Automatic profiling, model selection and export.", "https://noe-automl-55f69a9f06c9.herokuapp.com/", "Outils"),
]


def build_index():
    can_teach = [
        ("Programmation et science des données", "Programming and data science",
         "Python, pandas, visualisation, bases de données SQL, introduction à la science des données",
         "Python, pandas, visualization, SQL databases, introduction to data science", ["Informatique", "Cégep TI", "Bishop's CS"]),
        ("Statistique et probabilités", "Statistics and probability",
         "Statistique descriptive et inférentielle, régression, séries chronologiques et prévision",
         "Descriptive and inferential statistics, regression, time series and forecasting", ["Mathématiques", "Cégep", "SIMQG"]),
        ("Apprentissage automatique", "Machine learning",
         "Apprentissage supervisé et non supervisé, validation, apprentissage profond, MLOps",
         "Supervised and unsupervised learning, validation, deep learning, MLOps", ["Informatique", "Bishop's CS"]),
        ("Télédétection et géomatique", "Remote sensing and GIS",
         "Images satellites, Google Earth Engine, classification de l'occupation du sol, SIG avec Python",
         "Satellite imagery, Google Earth Engine, land-cover classification, GIS with Python", ["Géomatique appliquée", "Bishop's Geography"]),
        ("Recherche opérationnelle et méthodes quantitatives", "Operations research and quantitative methods",
         "Programmation linéaire, optimisation, gestion des stocks, aide à la décision",
         "Linear programming, optimization, inventory control, decision support", ["SIMQG", "Mathématiques"]),
        ("Analytique d'affaires", "Business analytics",
         "Intelligence d'affaires, tableaux de bord Power BI et Tableau, analytique prédictive",
         "Business intelligence, Power BI and Tableau dashboards, predictive analytics", ["École de gestion", "Williams School"]),
    ]
    cards = "".join(f'<div class="card"><h3>{T(fr, en)}</h3><p>{T(dfr, den)}</p>{"".join(f"<span class=tag>{t}</span>" for t in tags)}</div>'
                    for fr, en, dfr, den, tags in can_teach)
    body = f"""
<section class="hero"><div class="wrap grid">
  <div>
    <div class="kicker">{T("Chargé de cours · Science des données · Télédétection", "Lecturer · Data science · Remote sensing")}</div>
    <h1>Noé Carème Fouotsa Manfouo, Ph. D.</h1>
    <p class="lead">{T("J'enseigne la statistique, l'apprentissage automatique et l'analyse d'images satellites avec une approche concrète : chaque notion est mise en pratique sur des données réelles, dans des notebooks prêts à l'emploi.",
                      "I teach statistics, machine learning and satellite-image analysis with a hands-on approach: every concept is practised on real data, in ready-to-use notebooks.")}</p>
    <div class="chips"><span class="chip">{T("Enseignement universitaire depuis 2015", "University teaching since 2015")}</span><span class="chip">{T("Ph. D. recherche opérationnelle (Stellenbosch)", "PhD Operations Research (Stellenbosch)")}</span><span class="chip">{T("Bilingue français · anglais", "Bilingual French · English")}</span><span class="chip">Sherbrooke (QC)</span></div>
    <div class="btns">
      <a class="btn primary" href="cours-ml4eo.html">{T("Découvrir mon cours de 45 h", "See my 45-hour course")}</a>
      <a class="btn light" href="teaching.html">{T("Dossier d'enseignement", "Teaching portfolio")}</a>
      <a class="btn ghost" href="resume.html">CV</a>
    </div>
  </div>
  <img class="portrait" src="images/portrait.jpg" alt="Noé Carème Fouotsa Manfouo">
</div></section>

<section><div class="wrap">
  <div class="stats">
    <div class="stat"><b>2015</b><span>{T("première charge de cours universitaire", "first university course taught")}</span></div>
    <div class="stat"><b>3</b><span>{T("pays : Cameroun, Afrique du Sud, Canada", "countries: Cameroon, South Africa, Canada")}</span></div>
    <div class="stat"><b>28</b><span>{T("notebooks de cours ouverts et testés (2 cours)", "open, tested course notebooks (2 courses)")}</span></div>
    <div class="stat"><b>16</b><span>{T("applications de ML déployées", "deployed ML applications")}</span></div>
  </div>
</div></section>

<section class="soft"><div class="wrap">
  <div class="section-head"><div class="eyebrow">{T("Cours vedette", "Featured course")}</div>
  <h2>{T("Apprentissage automatique pour l'observation de la Terre", "Machine Learning for Earth Observation")}</h2>
  <p>{T("Un cours complet de 3 crédits (15 séances de 3 h), prêt à être offert : plan de cours, 14 laboratoires Colab avec rétroaction automatique, évaluations et grille de correction.",
        "A complete 3-credit course (15 × 3-hour sessions), ready to offer: course outline, 14 Colab labs with automatic feedback, assessments and rubric.")}</p></div>
  <div class="feature">
    <div>
      <ul class="list-check">
        <li>{T("De la première ligne de Python aux cartes d'occupation du sol validées", "From the first line of Python to validated land-cover maps")}</li>
        <li>{T("Google Earth Engine, scikit-learn, PyTorch, données ouvertes (Sentinel-2, CHIRPS, WorldCover)", "Google Earth Engine, scikit-learn, PyTorch, open data (Sentinel-2, CHIRPS, WorldCover)")}</li>
        <li>{T("Bonnes pratiques de validation (Olofsson et al., 2014) et validation croisée spatiale", "Validation good practice (Olofsson et al., 2014) and spatial cross-validation")}</li>
        <li>{T("Projet de session reproductible publié sur GitHub et diffusé en application web", "Reproducible term project published on GitHub and shared as a web app")}</li>
      </ul>
      <div class="btns" style="margin-top:18px"><a class="btn outline" href="cours-ml4eo.html">{T("Voir le plan et le calendrier", "See outline and schedule")}</a><a class="btn outline" href="{REPO}" target="_blank" rel="noopener">GitHub</a></div>
    </div>
    <div class="blocks">
      <div class="block b1"><b>S1–S3</b><span>{T("Python et analyse de données", "Python and data analysis")}</span></div>
      <div class="block b2"><b>S4–S8</b><span>{T("Données géospatiales et Earth Engine", "Geospatial data and Earth Engine")}</span></div>
      <div class="block b3"><b>S9–S13</b><span>{T("Apprentissage automatique et profond", "Machine and deep learning")}</span></div>
      <div class="block b4"><b>S14–S15</b><span>{T("Reproductibilité, éthique, projets", "Reproducibility, ethics, projects")}</span></div>
    </div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div class="eyebrow">{T("Deuxième cours prêt à offrir", "Second ready-to-offer course")}</div>
  <h2>{T("Science des données appliquée : détection de la fraude", "Applied Data Science: Fraud Detection")}</h2>
  <p>{T("Du pipeline à la production, sur un prototype industriel ouvert (PySpark, MLflow, FastAPI, Power BI). Trois parcours avec séances associées : gestion (SIMQG, Williams School), informatique, cégep/formation continue.",
        "From pipeline to production on an open industrial prototype (PySpark, MLflow, FastAPI, Power BI). Three tracks with mapped sessions: business (SIMQG, Williams School), computer science, college/continuing education.")}</p></div>
  <div class="feature">
    <div>
      <ul class="list-check">
        <li>{T("Seuil de décision choisi en dollars, sous contrainte de capacité d'enquête", "Decision threshold chosen in dollars, under investigation capacity")}</li>
        <li>{T("Test A/B, API de scoring, surveillance de la dérive et réentraînement conditionnel", "A/B testing, scoring API, drift monitoring and conditional retraining")}</li>
        <li>{T("Gouvernance (BSIF E-23), équité, risque de crédit IFRS 9 et IA générative encadrée", "Governance (OSFI E-23), fairness, IFRS 9 credit risk and governed generative AI")}</li>
      </ul>
      <div class="btns" style="margin-top:18px"><a class="btn outline" href="cours-fraude360.html">{T("Voir les séances par cursus", "See sessions by program")}</a><a class="btn outline" href="{REPO_F}" target="_blank" rel="noopener">GitHub</a></div>
    </div>
    <div class="blocks">
      <div class="block b1"><b>S1–S5</b><span>{T("Données : Bronze, Silver, Gold", "Data: Bronze, Silver, Gold")}</span></div>
      <div class="block b2"><b>S6–S8</b><span>{T("Modèles, seuil, registre", "Models, threshold, registry")}</span></div>
      <div class="block b3"><b>S9–S12</b><span>{T("Production et surveillance", "Production and monitoring")}</span></div>
      <div class="block b4"><b>S13–S15</b><span>{T("Gouvernance, BI, projets", "Governance, BI, projects")}</span></div>
    </div>
  </div>
</div></section>

<section class="soft"><div class="wrap">
  <div class="section-head"><div class="eyebrow">{T("Domaines d'enseignement", "Teaching areas")}</div>
  <h2>{T("Cours que je peux donner", "Courses I can teach")}</h2>
  <p>{T("En français ou en anglais, au cégep, au 1er cycle ou aux cycles supérieurs. Les étiquettes indiquent les unités où ces cours sont habituellement offerts.",
        "In French or English, at college, undergraduate or graduate level. Tags show the units where these courses are usually offered.")}</p></div>
  <div class="cards">{cards}</div>
</div></section>

<section><div class="wrap two">
  <div><div class="section-head"><div class="eyebrow">{T("Recherche", "Research")}</div><h2>{T("Des données au service des décisions", "Data for better decisions")}</h2>
  <p>{T("Mes travaux appliquent la statistique et l'apprentissage automatique à la sécurité alimentaire, à l'eau, aux espèces envahissantes et à la santé (diabète de type 2). Ils nourrissent directement les études de cas de mes cours.",
        "My work applies statistics and machine learning to food security, water, invasive species and health (type 2 diabetes). It feeds directly into the case studies of my courses.")}</p>
  <a class="btn outline" href="publications.html">{T("Publications", "Publications")}</a></div></div>
  <div class="cards">
    <a class="card" href="publications.html" style="color:inherit"><div class="meta">Heliyon · 2022</div><h3>{T("Sécheresse, confinements et agriculture au KwaZulu-Natal", "Drought, lockdowns and farming in KwaZulu-Natal")}</h3></a>
    <a class="card" href="publications.html" style="color:inherit"><div class="meta">J. Racial Ethn. Health Disparities · 2024</div><h3>{T("Prédicteurs du diabète de type 2 précoce", "Predictors of early-onset type 2 diabetes")}</h3></a>
  </div>
</div></section>

<section><div class="wrap"><div class="cta">
  <div><h2>{T("Un cours à pourvoir ?", "A course to staff?")}</h2><p>{T("Je réponds en 48 h. CV, plan de cours et références disponibles sur demande.", "I reply within 48 hours. CV, course outline and references available on request.")}</p></div>
  <div class="btns"><a class="btn primary" href="mailto:{EMAIL}">{T("Me contacter", "Contact me")}</a><a class="btn ghost" href="resume.html">CV</a></div>
</div></div></section>"""
    page("index.html", "Accueil · Home",
         "Chargé de cours en science des données, statistique, apprentissage automatique et télédétection (Sherbrooke). Lecturer in data science and remote sensing.",
         body)


def build_teaching():
    exp = [
        ("2018 – 2023", "Université de Stellenbosch, Afrique du Sud", "Stellenbosch University, South Africa",
         "Chargé d'enseignement (Assistant Lecturer)", "Assistant Lecturer",
         ["Cours de statistique et de techniques de prévision en 3e année du baccalauréat en recherche opérationnelle",
          "Cours de science des données aux cycles supérieurs",
          "Conception des plans de cours, travaux, examens ; encadrement et conseils aux étudiants"],
         ["Lectures in statistics and forecasting techniques for third-year Operations Research undergraduates",
          "Data science lectures for postgraduate students",
          "Designed course outlines, assignments and exams; supervised and advised students"]),
        ("2022", "Atelier intensif ML4EO (5 jours) — Département d'économie, Université de Stellenbosch", "ML4EO intensive workshop (5 days) — Department of Economics, Stellenbosch University",
         "Concepteur et formateur", "Designer and instructor",
         ["Python et apprentissage automatique pour l'observation de la Terre : Earth Engine, GeoPandas, classification",
          "Matériel ouvert, devenu le cours de 45 h présenté sur ce site"],
         ["Python and machine learning for Earth observation: Earth Engine, GeoPandas, classification",
          "Open material, now the 45-hour course presented on this site"]),
        ("2019 – 2020", "Teach Me2, Le Cap, Afrique du Sud", "Teach Me2, Cape Town, South Africa",
         "Tuteur en statistique et en économétrie", "Statistics and econometrics tutor",
         ["Tutorat individuel d'étudiants au 1er cycle et aux cycles supérieurs ; préparation aux examens"],
         ["One-on-one tutoring of undergraduate and graduate students; exam preparation"]),
        ("2015 – 2016", "Institut Universitaire de la Côte, Douala, Cameroun", "Institut Universitaire de la Côte, Douala, Cameroon",
         "Chargé de cours en statistique et recherche opérationnelle", "Lecturer in statistics and operations research",
         ["Programmation linéaire, gestion des stocks et mathématiques financières au 1er cycle",
          "Coordination de programme : horaires, réunions d'enseignants, développement des programmes"],
         ["Linear programming, inventory control and financial mathematics (undergraduate)",
          "Program coordination: schedules, faculty meetings, curriculum development"]),
    ]
    tl = "".join(f"""<div class="tl"><div class="when">{w}</div><h3>{T(rfr, ren)}</h3><div class="where">{T(pfr, pen)}</div>
<ul class="fr">{"".join(f"<li>{x}</li>" for x in lfr)}</ul><ul class="en">{"".join(f"<li>{x}</li>" for x in len_)}</ul></div>"""
                 for w, pfr, pen, rfr, ren, lfr, len_ in exp)
    body = f"""
<section class="page-hero"><div class="wrap"><h1>{T("Dossier d'enseignement", "Teaching portfolio")}</h1>
<p>{T("Philosophie, expérience et matériel pédagogique. Tout le matériel de cours est ouvert et peut être consulté avant une entrevue.",
      "Philosophy, experience and teaching material. All course material is open and can be reviewed before an interview.")}</p></div></section>

<section><div class="wrap two">
  <div>
    <div class="section-head"><div class="eyebrow">{T("Philosophie", "Philosophy")}</div><h2>{T("Apprendre en faisant, avec rigueur", "Learning by doing, with rigour")}</h2></div>
    <p class="quote">{T("« Un concept n'est compris que lorsqu'il a été appliqué à de vraies données, vérifié, puis expliqué à quelqu'un d'autre. »",
                       "“A concept is understood only once it has been applied to real data, checked, and explained to someone else.”")}</p>
    {B("<p>Je conçois mes cours pour que les étudiantes et étudiants passent rapidement de la théorie à la pratique, reçoivent une rétroaction fréquente et terminent avec un travail dont ils sont fiers.</p>",
       "<p>I design my courses so that students move quickly from theory to practice, receive frequent feedback and finish with work they are proud of.</p>")}
  </div>
  <div class="cards" style="grid-template-columns:1fr">
    <div class="card"><h3>1 · {T("Pratique sur données réelles", "Practice on real data")}</h3><p>{T("Chaque séance alterne exposé et laboratoire Colab ; les cas viennent de projets de recherche concrets (sécheresse, eau, santé).", "Each session alternates lecture and Colab lab; cases come from real research projects (drought, water, health).")}</p></div>
    <div class="card"><h3>2 · {T("Rétroaction tôt et souvent", "Early and frequent feedback")}</h3><p>{T("Vérifications automatiques dans les notebooks, quiz courts et projet en jalons évalués avant la note finale.", "Automatic checks in notebooks, short quizzes and a milestone-based project assessed before the final grade.")}</p></div>
    <div class="card"><h3>3 · {T("Rigueur et responsabilité", "Rigour and responsibility")}</h3><p>{T("Validation honnête des modèles, reproductibilité (Git, environnements) et réflexion éthique sur l'usage des données.", "Honest model validation, reproducibility (Git, environments) and ethical reflection on data use.")}</p></div>
    <div class="card"><h3>4 · {T("Inclusion", "Inclusion")}</h3><p>{T("Aucune installation requise, consignes en français et en anglais, accommodements appliqués dès la première semaine.", "Nothing to install, instructions in French and English, accommodations applied from week one.")}</p></div>
  </div>
</div></section>

<section class="soft"><div class="wrap">
  <div class="section-head"><div class="eyebrow">{T("Expérience", "Experience")}</div><h2>{T("Expérience d'enseignement", "Teaching experience")}</h2></div>
  <div class="timeline">{tl}</div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div class="eyebrow">{T("Matériel", "Material")}</div><h2>{T("Matériel pédagogique ouvert", "Open teaching material")}</h2></div>
  <div class="cards">
    <div class="card"><span class="tag green">{T("45 h · 3 crédits", "45 h · 3 credits")}</span><h3>{T("Apprentissage automatique pour l'observation de la Terre", "Machine Learning for Earth Observation")}</h3>
      <p>{T("Plan de cours bilingue, 14 notebooks Colab avec rétroaction automatique, examen pratique, projet et grille.", "Bilingual outline, 14 Colab notebooks with automatic feedback, practical exam, project and rubric.")}</p>
      <a href="cours-ml4eo.html">{T("Voir le cours →", "See the course →")}</a></div>
    <div class="card"><span class="tag green">{T("45 h · 3 parcours", "45 h · 3 tracks")}</span><h3>{T("Science des données appliquée : détection de la fraude", "Applied Data Science: Fraud Detection")}</h3>
      <p>{T("Plan de cours avec séances par cursus (gestion, informatique, cégep), 14 notebooks Colab testés, projet devant un « comité de risque ».", "Outline with sessions per program (business, CS, college), 14 tested Colab notebooks, project before a “risk committee”.")}</p>
      <a href="cours-fraude360.html">{T("Voir le cours →", "See the course →")}</a></div>
    <div class="card"><span class="tag">{T("Exemples", "Examples")}</span><h3>{T("16 applications de démonstration", "16 demonstration apps")}</h3>
      <p>{T("Applications web déployées utilisées en classe pour illustrer la mise en production de modèles.", "Deployed web apps used in class to show how models reach production.")}</p>
      <a href="portfolio.html">{T("Voir les projets →", "See the projects →")}</a></div>
    <div class="card"><span class="tag">{T("Communication scientifique", "Science communication")}</span><h3>{T("Articles de vulgarisation", "Popular-science articles")}</h3>
      <p>{T("Articles Medium sur l'AutoML, la télédétection agricole et la prédiction du diabète.", "Medium articles on AutoML, agricultural remote sensing and diabetes prediction.")}</p>
      <a href="https://medium.com/@noe.fouotsa" target="_blank" rel="noopener">Medium →</a></div>
  </div>
</div></section>"""
    page("teaching.html", "Enseignement · Teaching",
         "Dossier d'enseignement : philosophie, expérience depuis 2015, matériel ouvert. Teaching portfolio of Noé Carème Fouotsa Manfouo.", body)


def build_course():
    G = {i: "●" for i in range(1, 16)}; G[13] = "○"
    I = {i: "●" for i in range(1, 16)}; I.update({1: "○", 2: "○"})
    C = {i: "●" for i in (1, 2, 3, 4, 5, 7, 9, 10, 14, 15)}; C.update({6: "○", 11: "○", 8: "—", 12: "—", 13: "—"})

    def cell(v):
        return f'<td class="trk"><span class="{ {"●": "dot full", "○": "dot demo", "—": "dot off"}[v] }">{v}</span></td>'
    rows = "".join(f'<tr><td class="n">{n}</td><td>{T(fr, en)}</td><td><a class="colab" href="{COLAB}{n:02d}_{slug}.ipynb" target="_blank" rel="noopener">Colab ↗</a></td>{cell(G[n])}{cell(I[n])}{cell(C[n])}</tr>'
                   for n, slug, fr, en in SESSIONS)
    rows += f'<tr><td class="n">15</td><td>{T("Présentations des projets et synthèse", "Project presentations and wrap-up")}</td><td>—</td>{cell("●")}{cell("●")}{cell("●")}</tr>'
    tracks_ml = [
        ("Géomatique / environnement", "Geomatics / environment", "45 h",
         "UdeS Département de géomatique appliquée (bac et maîtrise) ; Bishop's Environmental Studies and Geography",
         "UdeS Applied Geomatics (bachelor's, master's); Bishop's Environmental Studies and Geography",
         "S1–S12, S14, S15", "S13",
         "Earth Engine, validation des cartes, estimation des superficies", "Earth Engine, map validation, area estimation"),
        ("Informatique", "Computer science", "45 h",
         "UdeS Département d'informatique (maîtrise IA et science des données, bac) ; Bishop's Computer Science",
         "UdeS Computer Science (AI and data science master's, bachelor's); Bishop's Computer Science",
         "S3–S15", "S1, S2",
         "Révision rapide de Python ; plus de temps pour l'apprentissage profond et un projet technique", "Fast Python review; more time for deep learning and a technical project"),
        ("Cégep / FC", "College / CE", "30 h (→ 45 h)",
         "Cégep de Sherbrooke, formation continue (AEC) ; UdeS formation continue",
         "Cégep de Sherbrooke continuing education (AEC); UdeS continuing education",
         "S1–S5, S7, S9, S10, S14, S15", "S6, S11",
         "Sans examen ni apprentissage profond ; projet guidé", "No exam or deep learning; guided project"),
    ]
    tracks_html = "".join(f"""<div class="card"><span class="tag green">{d}</span><h3>{T(fr, en)}</h3><p class="meta">{T(pfr, pen)}</p>
<p><b>{T("Séances complètes", "Full sessions")} :</b> {full}<br><b>{T("Démonstrations", "Demonstrations")} :</b> {demo}</p><p>{T(nfr, nen)}</p></div>"""
                          for fr, en, d, pfr, pen, full, demo, nfr, nen in tracks_ml)
    outcomes_fr = ["Écrire des programmes Python structurés pour les données environnementales.",
                   "Expliquer la physique de la télédétection et calculer des indices spectraux (NDVI, NDWI, NDBI).",
                   "Manipuler des données vectorielles et matricielles avec les bons systèmes de coordonnées.",
                   "Extraire des séries et des statistiques zonales à grande échelle avec Google Earth Engine.",
                   "Entraîner et comparer des classifieurs pour cartographier l'occupation du sol.",
                   "Évaluer une carte selon les bonnes pratiques (précisions, superficies et intervalles de confiance).",
                   "Appliquer un modèle d'apprentissage profond préentraîné et en critiquer les limites.",
                   "Communiquer une analyse reproductible et en discuter les enjeux éthiques."]
    outcomes_en = ["Write structured Python programs for environmental data.",
                   "Explain remote-sensing physics and compute spectral indices (NDVI, NDWI, NDBI).",
                   "Handle vector and raster data with correct coordinate systems.",
                   "Extract time series and zonal statistics at scale with Google Earth Engine.",
                   "Train and compare classifiers to map land cover.",
                   "Assess maps with good practice (accuracies, areas and confidence intervals).",
                   "Apply a pretrained deep-learning model and critique its limits.",
                   "Communicate a reproducible analysis and discuss its ethical implications."]
    assess = [("Carnets de laboratoire (4)", "Lab notebooks (4)", "20 %"), ("Quiz en ligne (3)", "Online quizzes (3)", "15 %"),
              ("Examen pratique de mi-session", "Midterm practical exam", "20 %"),
              ("Projet : proposition, rapport d'étape, présentation, rapport final + GitHub", "Project: proposal, progress report, talk, final report + GitHub", "45 %")]
    body = f"""
<section class="page-hero"><div class="wrap">
  <h1>{T("Apprentissage automatique pour l'observation de la Terre", "Machine Learning for Earth Observation")}</h1>
  <p>{T("Cours de 3 crédits (45 h) · 1er cycle avancé ou 2e cycle · français ou anglais · prêt à être offert dès l'automne 2027.",
        "3-credit course (45 h) · upper-year undergraduate or graduate · French or English · ready to offer from Fall 2027.")}</p>
  <div class="btns" style="margin-top:22px"><a class="btn primary" href="{REPO}" target="_blank" rel="noopener">{T("Dépôt GitHub du cours", "Course GitHub repository")}</a>
  <a class="btn ghost" href="{COLAB}01_python_bases.ipynb" target="_blank" rel="noopener">{T("Essayer la séance 1 dans Colab", "Try session 1 in Colab")}</a></div>
</div></section>

<section><div class="wrap two">
  <div><div class="section-head"><div class="eyebrow">{T("Description", "Description")}</div><h2>{T("De l'image satellite à la carte validée", "From satellite image to validated map")}</h2></div>
  {B("<p>Sentinel-2 et Landsat livrent gratuitement des images de toute la planète tous les 5 à 16 jours. Les transformer en information fiable — occupation du sol, sécheresse, urbanisation — exige à la fois des bases en télédétection et en apprentissage automatique. Le cours couvre toute la chaîne, de Python à l'apprentissage profond, avec un accent sur la validation et la reproductibilité.</p><p>Il s'adresse aux étudiantes et étudiants en géomatique, environnement, géographie, informatique et science des données. Aucune expérience de Python n'est exigée.</p>",
     "<p>Sentinel-2 and Landsat provide free imagery of the whole planet every 5 to 16 days. Turning it into reliable information — land cover, drought, urban growth — requires both remote sensing and machine learning. The course covers the full pipeline, from Python to deep learning, with an emphasis on validation and reproducibility.</p><p>It is designed for students in geomatics, environmental science, geography, computer science and data science. No prior Python is required.</p>")}
  <p><span class="tag">Python</span><span class="tag">Google Earth Engine</span><span class="tag">GeoPandas</span><span class="tag">rasterio · xarray</span><span class="tag">scikit-learn</span><span class="tag">PyTorch</span><span class="tag">Streamlit</span></p></div>
  <div class="card"><h3>{T("Objectifs d'apprentissage", "Learning outcomes")}</h3>
    <ol class="fr">{"".join(f"<li>{o}</li>" for o in outcomes_fr)}</ol><ol class="en">{"".join(f"<li>{o}</li>" for o in outcomes_en)}</ol></div>
</div></section>

<section class="soft"><div class="wrap">
  <div class="section-head"><div class="eyebrow">{T("Parcours de formation", "Training tracks")}</div><h2>{T("Un cours, trois cursus", "One course, three programs")}</h2>
  <p>{T("Les séances associées à chaque cursus sont indiquées ci-dessous et dans le calendrier.", "The sessions associated with each program are listed below and in the schedule.")}</p></div>
  <div class="cards">{tracks_html}</div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div class="eyebrow">{T("Calendrier", "Schedule")}</div><h2>{T("15 séances de 3 h et séances par cursus", "15 three-hour sessions, by program")}</h2>
  <p>{T("Chaque séance : 1 h 30 d'exposé interactif + 1 h 30 de laboratoire. ● séance complète · ○ démonstration (laboratoire facultatif) · — hors parcours.", "Each session: 1.5 h interactive lecture + 1.5 h lab. ● full session · ○ demonstration (optional lab) · — not in track.")}</p></div>
  <div class="table-wrap"><table><thead><tr><th>#</th><th>{T("Séance", "Session")}</th><th>{T("Laboratoire", "Lab")}</th><th>{T("Géomatique", "Geomatics")}</th><th>{T("Informatique", "CS")}</th><th>{T("Cégep / FC", "College / CE")}</th></tr></thead><tbody>{rows}</tbody></table></div>
</div></section>

<section class="soft"><div class="wrap two">
  <div><div class="section-head"><div class="eyebrow">{T("Évaluation", "Assessment")}</div><h2>{T("Évaluer pour faire apprendre", "Assessment for learning")}</h2>
  <p>{T("Le projet de session est évalué en quatre jalons pour que la rétroaction arrive avant la note finale. Une grille critériée (question, données, modélisation, validation, reproductibilité) est fournie dès la première semaine.",
        "The term project is assessed in four milestones so feedback comes before the final grade. A criterion-based rubric (question, data, modelling, validation, reproducibility) is shared in week one.")}</p></div></div>
  <div class="table-wrap"><table><thead><tr><th>{T("Élément", "Component")}</th><th>{T("Poids", "Weight")}</th></tr></thead><tbody>
  {"".join(f"<tr><td>{T(fr, en)}</td><td><b>{w}</b></td></tr>" for fr, en, w in assess)}</tbody></table></div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div class="eyebrow">{T("Pourquoi ce cours", "Why this course")}</div><h2>{T("Ce que les étudiants en retirent", "What students take away")}</h2></div>
  <div class="cards">
    <div class="card"><h3>{T("Un portfolio concret", "A concrete portfolio")}</h3><p>{T("Un projet complet sur GitHub et une application web à montrer à un employeur.", "A complete GitHub project and a web app to show employers.")}</p></div>
    <div class="card"><h3>{T("Des outils actuels", "Current tools")}</h3><p>{T("Earth Engine avec projets Cloud, Cloud Score+, ESA WorldCover, TorchGeo et Source Cooperative.", "Earth Engine with Cloud projects, Cloud Score+, ESA WorldCover, TorchGeo and Source Cooperative.")}</p></div>
    <div class="card"><h3>{T("Des cartes crédibles", "Credible maps")}</h3><p>{T("Validation croisée spatiale et estimation des superficies avec intervalles de confiance.", "Spatial cross-validation and area estimation with confidence intervals.")}</p></div>
  </div>
</div></section>

<section><div class="wrap"><div class="cta">
  <div><h2>{T("Plan de cours complet", "Full course outline")}</h2><p>{T("Version détaillée en français et en anglais (politiques, grille, bibliographie) envoyée sur demande.", "Detailed French and English version (policies, rubric, readings) sent on request.")}</p></div>
  <div class="btns"><a class="btn primary" href="mailto:{EMAIL}?subject=Plan%20de%20cours%20ML4EO">{T("Demander le plan de cours", "Request the outline")}</a></div>
</div></div></section>"""
    page("cours-ml4eo.html", "Cours ML4EO · Course",
         "Cours de 45 h « Apprentissage automatique pour l'observation de la Terre » : plan, 15 séances, laboratoires Colab, évaluation. 45-hour Machine Learning for Earth Observation course.", body)


REPO_F = "https://github.com/noe2019/fraude-360"
COLAB_F = "https://colab.research.google.com/github/noe2019/fraude-360/blob/main/cours/laboratoires/"
# (séance, notebook, thème FR, thème EN, Gestion, Informatique, Cégep/FC) — ● complète · ○ démonstration · — hors parcours
SESSIONS_F = [
    (1, "contexte_simulation", "La fraude transactionnelle et ses coûts ; données simulées", "Transaction fraud and its costs; simulated data", "●", "●", "●"),
    (2, "ingestion_bronze", "Ingestion incrémentale (Bronze), PySpark", "Incremental ingestion (Bronze), PySpark", "○", "●", "—"),
    (3, "qualite_silver", "Qualité des données et quarantaine (Silver)", "Data quality and quarantine (Silver)", "●", "●", "●"),
    (4, "variables_gold", "Variables comportementales sans fuite temporelle (Gold)", "Behavioural features without leakage (Gold)", "○", "●", "○"),
    (5, "exploration", "Analyse exploratoire orientée décision", "Decision-oriented exploratory analysis", "●", "●", "●"),
    (6, "modelisation_calibration", "Découpage temporel, déséquilibre, calibration", "Temporal split, imbalance, calibration", "●", "●", "●"),
    (7, "seuil_economique", "Seuil choisi en dollars, capacité d'enquête", "Dollar-based threshold, investigation capacity", "●", "●", "●"),
    (8, "mlflow_registre", "Registre MLflow, champion/challenger · examen", "MLflow registry, champion/challenger · exam", "●", "●", "—"),
    (9, "test_ab", "Test A/B : randomisation par carte, bootstrap", "A/B testing: card-level randomisation, bootstrap", "●", "●", "○"),
    (10, "deploiement_api", "Déploiement : API de scoring en temps réel", "Deployment: real-time scoring API", "○", "●", "●"),
    (11, "surveillance_derive", "Surveillance : PSI, KS, dérive de performance", "Monitoring: PSI, KS, performance drift", "●", "●", "○"),
    (12, "nouvelle_fraude_reentrainement", "Nouvelle typologie et réentraînement conditionnel", "New fraud pattern and conditional retraining", "○", "●", "—"),
    (13, "gouvernance_credit", "Gouvernance, équité et risque de crédit (IFRS 9)", "Governance, fairness and credit risk (IFRS 9)", "●", "○", "—"),
    (14, "bi_ia_generative", "Power BI et triage des alertes par IA générative", "Power BI and generative-AI alert triage", "●", "●", "●"),
]
TRACKS_F = [
    ("Gestion", "Business",
     "UdeS École de gestion (SIMQG) : microprogramme en intelligence d'affaires et analytique, maîtrise/DESS ; Bishop's Williams School of Business",
     "UdeS School of Management (SIMQG): business intelligence and analytics programs; Bishop's Williams School of Business",
     "45 h", "Coûts, expérimentation, gouvernance, tableau de bord ; code PySpark fourni et commenté",
     "Costs, experimentation, governance, dashboard; PySpark code provided and explained"),
    ("Informatique", "Computer science",
     "UdeS Département d'informatique : maîtrise (cheminement IA et science des données), baccalauréat",
     "UdeS Computer Science: master's (AI and data science stream), bachelor's",
     "45 h", "PySpark, MLflow, API, surveillance ; projet déployable sur Azure Databricks",
     "PySpark, MLflow, API, monitoring; project deployable on Azure Databricks"),
    ("Cégep / FC", "College / CE",
     "Cégep de Sherbrooke (formation continue, AEC), Techniques de l'informatique ; UdeS formation continue",
     "Cégep de Sherbrooke (continuing education, AEC), Computer Techniques; UdeS continuing education",
     "30 h (→ 45 h)", "Version pandas, API prête à l'emploi, projet guidé",
     "pandas version, ready-made API, guided project"),
]


def build_course_fraude():
    def cell(v):
        cls = {"●": "dot full", "○": "dot demo", "—": "dot off"}[v]
        return f'<td class="trk"><span class="{cls}" title="{v}">{v}</span></td>'
    rows = "".join(f'<tr><td class="n">{n}</td><td>{T(fr, en)}</td><td><a class="colab" href="{COLAB_F}{n:02d}_{slug}.ipynb" target="_blank" rel="noopener">Colab ↗</a></td>{cell(g)}{cell(i)}{cell(c)}</tr>'
                   for n, slug, fr, en, g, i, c in SESSIONS_F)
    rows += f'<tr><td class="n">15</td><td>{T("Présentations des projets devant un « comité de risque »", "Project presentations to a “risk committee”")}</td><td>—</td>{cell("●")}{cell("●")}{cell("●")}</tr>'

    def seances(idx, sym):
        nums = [s[0] for s in SESSIONS_F if s[idx] == sym] + ([15] if sym == "●" else [])
        out, start = [], None
        for k, x in enumerate(nums):
            if start is None:
                start = x
            if k == len(nums) - 1 or nums[k + 1] != x + 1:
                out.append(f"S{start}" if start == x else f"S{start}–S{x}")
                start = None
        return ", ".join(out) or "—"
    tracks = "".join(f"""<div class="card"><span class="tag green">{dur}</span><h3>{T(fr, en)}</h3><p class="meta">{T(pfr, pen)}</p>
<p><b>{T("Séances complètes", "Full sessions")} :</b> {seances(4 + k, "●")}<br><b>{T("Démonstrations", "Demonstrations")} :</b> {seances(4 + k, "○")}</p>
<p>{T(nfr, nen)}</p></div>""" for k, (fr, en, pfr, pen, dur, nfr, nen) in enumerate(TRACKS_F))
    outcomes = [("Construire un pipeline de données en couches avec contrôles de qualité et quarantaine traçable.", "Build a layered data pipeline with quality checks and traceable quarantine."),
                ("Créer des variables comportementales en fenêtres glissantes, sans fuite d'information du futur.", "Engineer rolling-window behavioural features without leakage from the future."),
                ("Entraîner, calibrer et comparer des modèles sur données très déséquilibrées (découpage temporel).", "Train, calibrate and compare models on highly imbalanced data (temporal split)."),
                ("Choisir un seuil qui minimise le coût en dollars sous contrainte de capacité d'enquête.", "Choose a threshold that minimises dollar cost under investigation capacity."),
                ("Planifier et analyser un test A/B valide (randomisation par grappe, A/A, bootstrap).", "Design and analyse a valid A/B test (cluster randomisation, A/A, bootstrap)."),
                ("Déployer un modèle (API temps réel, lots) avec MLflow et un moteur de règles hybride.", "Deploy a model (real-time API, batch) with MLflow and a hybrid rules engine."),
                ("Surveiller la dérive (PSI, KS, performance) et décider d'un réentraînement.", "Monitor drift (PSI, KS, performance) and decide on retraining."),
                ("Documenter et gouverner un modèle (fiche, équité, IA générative encadrée) et communiquer dans Power BI.", "Document and govern a model (model card, fairness, governed GenAI) and report in Power BI.")]
    assess = [("Carnets de laboratoire (4 remises)", "Lab notebooks (4 submissions)", "20 %"), ("Quiz en ligne (3)", "Online quizzes (3)", "15 %"),
              ("Examen pratique de mi-session", "Midterm practical exam", "20 %"),
              ("Projet d'équipe : proposition, rapport d'étape, présentation, rapport final + GitHub + fiche de modèle",
               "Team project: proposal, progress report, presentation, final report + GitHub + model card", "45 %")]
    body = f"""
<section class="page-hero"><div class="wrap">
  <h1>{T("Science des données appliquée : détection de la fraude", "Applied Data Science: Fraud Detection")}</h1>
  <p>{T("Du pipeline à la production · cours de 3 crédits (45 h) · trois parcours : gestion, informatique, cégep/formation continue · français (laboratoires) et anglais (plan).",
        "From pipeline to production · 3-credit course (45 h) · three tracks: business, computer science, college/continuing education · French labs, bilingual outline.")}</p>
  <div class="btns" style="margin-top:22px"><a class="btn primary" href="{REPO_F}" target="_blank" rel="noopener">{T("Dépôt GitHub du cours", "Course GitHub repository")}</a>
  <a class="btn ghost" href="{COLAB_F}01_contexte_simulation.ipynb" target="_blank" rel="noopener">{T("Essayer la séance 1 dans Colab", "Try session 1 in Colab")}</a></div>
</div></section>

<section><div class="wrap two">
  <div><div class="section-head"><div class="eyebrow">{T("Description", "Description")}</div><h2>{T("Tout le cycle de vie d'un modèle, pas seulement l'entraînement", "The whole model life cycle, not just training")}</h2></div>
  {B("<p>En entreprise, entraîner le modèle représente à peine 20 % du travail. Ce cours fait construire, séance après séance, le système de détection de la fraude d'une coopérative financière fictive : ingestion, qualité, variables, modèle calibré, seuil choisi en dollars, registre, test A/B, API, surveillance, réentraînement, gouvernance, Power BI et triage des alertes par IA générative.</p><p>Le fil conducteur est <b>Fraude-360</b>, un prototype ouvert construit par le chargé de cours (PySpark, MLflow, FastAPI, Power BI ; données 100 % synthétiques). Chaque laboratoire exécute une étape, puis fait réécrire sa fonction clé et la compare à l'implémentation de référence.</p>",
     "<p>In industry, training the model is barely 20% of the work. Session by session, students build the fraud-detection system of a fictional credit union: ingestion, data quality, features, calibrated model, dollar-based threshold, registry, A/B test, API, monitoring, retraining, governance, Power BI and generative-AI alert triage.</p><p>The common thread is <b>Fraude-360</b>, an open prototype built by the instructor (PySpark, MLflow, FastAPI, Power BI; 100% synthetic data). Each lab runs one pipeline step, then has students rewrite its key function and compare it with the reference implementation.</p>")}
  <p><span class="tag">PySpark</span><span class="tag">scikit-learn</span><span class="tag">MLflow</span><span class="tag">FastAPI</span><span class="tag">Power BI</span><span class="tag">SAS</span><span class="tag">{T("IA générative (RAG)", "Generative AI (RAG)")}</span><span class="tag">Azure Databricks</span></p></div>
  <div class="card"><h3>{T("Objectifs d'apprentissage", "Learning outcomes")}</h3>
    <ol class="fr">{"".join(f"<li>{fr}</li>" for fr, _ in outcomes)}</ol><ol class="en">{"".join(f"<li>{en}</li>" for _, en in outcomes)}</ol></div>
</div></section>

<section class="soft"><div class="wrap">
  <div class="section-head"><div class="eyebrow">{T("Parcours de formation", "Training tracks")}</div><h2>{T("Un cours, trois cursus", "One course, three programs")}</h2>
  <p>{T("Les séances associées à chaque cursus sont indiquées ci-dessous et dans le calendrier. Dans chaque notebook, les exercices sont aussi étiquetés : 🟢 tous · 🟣 gestion + informatique · 🔷 informatique · 🔶 gestion.",
        "The sessions associated with each program are listed below and in the schedule. Inside every notebook, exercises are also tagged: 🟢 all · 🟣 business + CS · 🔷 CS · 🔶 business.")}</p></div>
  <div class="cards">{tracks}</div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div class="eyebrow">{T("Calendrier", "Schedule")}</div><h2>{T("15 séances de 3 h et séances par cursus", "15 three-hour sessions, by program")}</h2>
  <p>{T("● séance complète · ○ démonstration en classe (laboratoire facultatif) · — hors parcours. Chaque laboratoire s'ouvre dans Google Colab en un clic, sans installation.",
        "● full session · ○ in-class demonstration (optional lab) · — not in track. Each lab opens in Google Colab in one click, nothing to install.")}</p></div>
  <div class="table-wrap"><table><thead><tr><th>#</th><th>{T("Séance", "Session")}</th><th>{T("Laboratoire", "Lab")}</th><th>{T("Gestion", "Business")}</th><th>{T("Informatique", "CS")}</th><th>{T("Cégep / FC", "College / CE")}</th></tr></thead><tbody>{rows}</tbody></table></div>
</div></section>

<section class="soft"><div class="wrap two">
  <div><div class="section-head"><div class="eyebrow">{T("Évaluation", "Assessment")}</div><h2>{T("Des décisions défendues devant un comité", "Decisions defended before a committee")}</h2>
  <p>{T("Le projet d'équipe adapte le pipeline à un nouveau contexte (autre institution, autre fraude) et se termine par une présentation à un « comité de risque ». La grille porte sur le problème d'affaires, les données, le seuil, la production et la gouvernance.",
        "The team project adapts the pipeline to a new context (another institution, another fraud) and ends with a presentation to a “risk committee”. The rubric covers the business problem, data, threshold, production and governance.")}</p></div></div>
  <div class="table-wrap"><table><thead><tr><th>{T("Élément", "Component")}</th><th>{T("Poids", "Weight")}</th></tr></thead><tbody>
  {"".join(f"<tr><td>{T(fr, en)}</td><td><b>{w}</b></td></tr>" for fr, en, w in assess)}</tbody></table></div>
</div></section>

<section><div class="wrap"><div class="cta">
  <div><h2>{T("Plan de cours complet", "Full course outline")}</h2><p>{T("Version détaillée (calendrier par cursus, grille, politiques, bibliographie) envoyée sur demande.", "Detailed version (schedule by program, rubric, policies, readings) sent on request.")}</p></div>
  <div class="btns"><a class="btn primary" href="mailto:{EMAIL}?subject=Plan%20de%20cours%20Fraude-360">{T("Demander le plan de cours", "Request the outline")}</a></div>
</div></div></section>"""
    page("cours-fraude360.html", "Cours Fraude-360 · Course",
         "Cours de 45 h « Science des données appliquée : détection de la fraude » : séances par cursus (gestion, informatique, cégep), laboratoires Colab. 45-hour applied fraud-detection data science course.", body)


def build_publications():
    pubs = "".join(f"""<div class="pub"><span class="tag">{area}</span><div class="title">{t}</div><div class="venue">{a} — <i>{v}</i></div>
<div class="links">{"".join(f'<a href="{u}" target="_blank" rel="noopener">{n} ↗</a>' for n, u in links)}</div></div>""" for t, a, v, links, area in PUBS)
    body = f"""
<section class="page-hero"><div class="wrap"><h1>{T("Recherche et publications", "Research and publications")}</h1>
<p>{T("Statistique, apprentissage automatique et télédétection appliqués à la sécurité alimentaire, à l'eau, à l'environnement et à la santé.",
      "Statistics, machine learning and remote sensing applied to food security, water, the environment and health.")}</p></div></section>
<section><div class="wrap two">
  <div class="card">{pubs}</div>
  <div>
    <div class="card"><h3>{T("Axes de recherche", "Research themes")}</h3>
      <ul class="fr"><li>Suivi de l'agriculture et de la sécheresse par satellite</li><li>Cartographie des espèces envahissantes (Sentinel-2)</li><li>Prévision des ressources en eau (bassin du lac Tchad)</li><li>Trajectoires et prédicteurs du diabète de type 2</li></ul>
      <ul class="en"><li>Satellite monitoring of agriculture and drought</li><li>Invasive species mapping (Sentinel-2)</li><li>Water resource forecasting (Lake Chad Basin)</li><li>Type 2 diabetes trajectories and predictors</li></ul></div>
    <div class="card" style="margin-top:20px"><h3>{T("Postes de recherche", "Research positions")}</h3>
      <p>{T("Stagiaire postdoctoral, Faculté de médecine et des sciences de la santé, Université de Sherbrooke (2023–2024) ; stagiaire postdoctoral, Faculté des sciences naturelles, Université de Stellenbosch (2020–2023).",
            "Postdoctoral fellow, Faculty of Medicine and Health Sciences, Université de Sherbrooke (2023–2024); postdoctoral fellow, Faculty of Natural Sciences, Stellenbosch University (2020–2023).")}</p>
      <a href="{LINKS['Google Scholar']}" target="_blank" rel="noopener">Google Scholar ↗</a></div>
  </div>
</div></section>"""
    page("publications.html", "Recherche · Research", "Publications de Noé Carème Fouotsa Manfouo en télédétection, climat et santé. Research publications.", body)


def build_portfolio():
    cards = "".join(f'<div class="card"><span class="tag green">{tag}</span><h3>{name}</h3><p>{T(fr, en)}</p><a href="{url}" target="_blank" rel="noopener">{T("Ouvrir l'application ↗", "Open the app ↗")}</a></div>'
                    for name, fr, en, url, tag in APPS)
    body = f"""
<section class="page-hero"><div class="wrap"><h1>{T("Projets et applications", "Projects and applications")}</h1>
<p>{T("Des modèles déployés en applications web, utilisés aussi comme exemples en classe. Données simulées lorsque les données originales sont confidentielles.",
      "Models deployed as web apps, also used as classroom examples. Simulated data where the original data are confidential.")}</p></div></section>
<section><div class="wrap">
  <div class="cards">{cards}</div>
  <p style="margin-top:24px">{T("Les applications s'éveillent en 10 à 20 secondes au premier accès.", "Apps wake up in 10–20 seconds on first visit.")}</p>
  <div class="btns"><a class="btn outline" href="{LINKS['Portfolio']}" target="_blank" rel="noopener">{T("Les 16 projets du portfolio", "All 16 portfolio projects")}</a><a class="btn outline" href="{LINKS['GitHub']}" target="_blank" rel="noopener">GitHub</a></div>
</div></section>"""
    page("portfolio.html", "Projets · Projects", "Applications d'apprentissage automatique déployées : télédétection, santé, outils. Deployed machine learning applications.", body)


def build_resume():
    jobs = [
        ("2024 –", "Consultant en science des données", "Data science consultant", "BeamData (Toronto) et mandats indépendants", "BeamData (Toronto) and freelance",
         "Modèles prédictifs, pipelines ETL, tableaux de bord Power BI, systèmes RAG en français.", "Predictive models, ETL pipelines, Power BI dashboards, French-language RAG systems."),
        ("2023 – 2024", "Stagiaire postdoctoral", "Postdoctoral fellow", "Université de Sherbrooke, FMSS", "Université de Sherbrooke, Faculty of Medicine and Health Sciences",
         "Prédicteurs du diabète précoce (NHANES) ; trajectoires de complications à partir des données du CHUS.", "Early-onset diabetes predictors (NHANES); complication trajectories from CHUS data."),
        ("2020 – 2023", "Stagiaire postdoctoral", "Postdoctoral fellow", "Université de Stellenbosch, Faculté des sciences naturelles", "Stellenbosch University, Faculty of Natural Sciences",
         "Cartographie des arbres envahissants (Sentinel-2), prévision de l'eau au bassin du lac Tchad, suivi agricole au KwaZulu-Natal.", "Invasive tree mapping (Sentinel-2), Lake Chad Basin water forecasting, agricultural monitoring in KwaZulu-Natal."),
        ("2018 – 2023", "Chargé d'enseignement", "Assistant Lecturer", "Université de Stellenbosch", "Stellenbosch University",
         "Statistique et prévision (1er cycle), science des données (cycles supérieurs).", "Statistics and forecasting (undergraduate), data science (graduate)."),
        ("2015 – 2016", "Chargé de cours", "Lecturer", "Institut Universitaire de la Côte, Douala", "Institut Universitaire de la Côte, Douala",
         "Programmation linéaire, gestion des stocks, mathématiques financières ; coordination de programme.", "Linear programming, inventory control, financial mathematics; program coordination."),
    ]
    tl = "".join(f'<div class="tl"><div class="when">{w}</div><h3>{T(rfr, ren)}</h3><div class="where">{T(pfr, pen)}</div><p>{T(dfr, den)}</p></div>'
                 for w, rfr, ren, pfr, pen, dfr, den in jobs)
    edu = [("2020", "Ph. D. en recherche opérationnelle", "PhD in Operations Research", "Université de Stellenbosch, Afrique du Sud", "Stellenbosch University, South Africa"),
           ("2015", "M. Sc. en sciences mathématiques", "MSc in Mathematical Sciences", "African Institute for Mathematical Sciences (AIMS), Cameroun", "African Institute for Mathematical Sciences (AIMS), Cameroon"),
           ("2013", "M. Sc. en économie mathématique", "MSc in Mathematical Economics", "Université de Dschang, Cameroun", "University of Dschang, Cameroon")]
    edu_html = "".join(f'<div class="tl"><div class="when">{y}</div><h3>{T(a, b)}</h3><div class="where">{T(c, d)}</div></div>' for y, a, b, c, d in edu)
    awards = [("Bourse de voyage, Réseau CMDO (2023–2024)", "Travel grant, CMDO network (2023–2024)"),
              ("Bourse départementale, Université de Stellenbosch (2019)", "Departmental scholarship, Stellenbosch University (2019)"),
              ("Subvention d'échange et de collaboration, NRF (2018)", "Knowledge Interchange and Collaboration grant, NRF (2018)"),
              ("Prix d'affiche, Deep Learning Indaba (2018)", "Poster award, Deep Learning Indaba (2018)"),
              ("Bourse de maîtrise, Next Einstein Initiative (2014–2015)", "Master's scholarship, Next Einstein Initiative (2014–2015)"),
              ("Prix d'excellence du Chef de l'État pour l'enseignement supérieur (2011–2013)", "Head of State Higher Education Excellence Award (2011–2013)")]
    body = f"""
<section class="page-hero"><div class="wrap"><h1>Curriculum vitae</h1>
<p>{T("Version abrégée. CV complet et références disponibles sur demande.", "Short version. Full CV and references available on request.")}</p>
<div class="btns" style="margin-top:20px"><a class="btn primary" href="mailto:{EMAIL}?subject=CV">{T("Demander le CV complet", "Request the full CV")}</a><a class="btn ghost" href="{LINKS['LinkedIn']}" target="_blank" rel="noopener">LinkedIn</a></div></div></section>
<section><div class="wrap two">
  <div><h2>{T("Expérience", "Experience")}</h2><div class="timeline">{tl}</div></div>
  <div><h2>{T("Formation", "Education")}</h2><div class="timeline">{edu_html}</div>
    <div class="card" style="margin-top:10px"><h3>{T("Prix et bourses", "Awards and scholarships")}</h3>
      <ul class="fr">{"".join(f"<li>{a}</li>" for a, _ in awards)}</ul><ul class="en">{"".join(f"<li>{b}</li>" for _, b in awards)}</ul></div>
    <div class="card" style="margin-top:20px"><h3>{T("Compétences", "Skills")}</h3>
      <p><span class="tag">Python</span><span class="tag">R</span><span class="tag">SQL</span><span class="tag">scikit-learn</span><span class="tag">PyTorch</span><span class="tag">Google Earth Engine</span><span class="tag">QGIS</span><span class="tag">Power BI</span><span class="tag">Tableau</span><span class="tag">Git · Docker</span><span class="tag">LaTeX</span></p>
      <p>{T("<b>Langues :</b> français (langue maternelle), anglais (IELTS C1).", "<b>Languages:</b> French (native), English (IELTS C1).")}</p></div>
  </div>
</div></section>"""
    page("resume.html", "CV", "Curriculum vitae de Noé Carème Fouotsa Manfouo, Ph. D. CV.", body)


def build_contact():
    body = f"""
<section class="page-hero"><div class="wrap"><h1>Contact</h1>
<p>{T("Départements, directions de programme et collègues : écrivez-moi pour une charge de cours, une collaboration ou une conférence invitée.",
      "Departments, program directors and colleagues: write to me about a course, a collaboration or a guest lecture.")}</p></div></section>
<section><div class="wrap"><div class="cards">
  <div class="card"><h3>{T("Courriel", "Email")}</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p><p class="meta">{T("Réponse en 48 h ouvrables", "Reply within 2 business days")}</p></div>
  <div class="card"><h3>{T("Lieu", "Location")}</h3><p>Sherbrooke (Québec), Canada</p><p class="meta">{T("Disponible en présentiel à Sherbrooke et à Lennoxville", "Available in person in Sherbrooke and Lennoxville")}</p></div>
  <div class="card"><h3>{T("En ligne", "Online")}</h3><p>{"<br>".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in LINKS.items())}</p></div>
</div></div></section>"""
    page("contact.html", "Contact", "Contacter Noé Carème Fouotsa Manfouo. Contact.", body)


def redirects():
    for old, new in {"about.html": "index.html", "services.html": "index.html", "students.html": "teaching.html", "awards.html": "resume.html"}.items():
        (OUT / old).write_text(f'<!doctype html><html><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url={new}">'
                               f'<link rel="canonical" href="{SITE}/{new}"><title>Redirection</title></head>'
                               f'<body><a href="{new}">{new}</a></body></html>\n', encoding="utf-8")
    pages = ["index.html", "teaching.html", "cours-ml4eo.html", "cours-fraude360.html", "publications.html", "portfolio.html", "resume.html", "contact.html"]
    (OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                     + "".join(f"  <url><loc>{SITE}/{p}</loc></url>\n" for p in pages) + "</urlset>\n")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    (OUT / "404.html").write_text('<!doctype html><html><head><meta charset="utf-8"><meta http-equiv="refresh" content="3; url=index.html"><title>404</title></head>'
                                  '<body style="font-family:sans-serif;padding:40px">Page introuvable · Page not found — <a href="index.html">Accueil · Home</a></body></html>\n')
    (OUT / "README.md").write_text("# noe2019.github.io\n\nBilingual (FR/EN) academic and teaching website of Noé Carème Fouotsa Manfouo, PhD.\n"
                                   "Static HTML/CSS (no build step needed to serve). Pages are generated by `build.py` (`python build.py`).\n"
                                   "Append `?lang=en` to any URL to open the English version.\n")


if __name__ == "__main__":
    build_index(); build_teaching(); build_course(); build_course_fraude(); build_publications(); build_portfolio(); build_resume(); build_contact(); redirects()
    print("built")

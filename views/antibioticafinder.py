import streamlit as st
import pandas as pd
from datetime import datetime

# =========================================================
# SEITENKONFIGURATION
# =========================================================

# 🎨 MODERNES DESIGN
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f8fbff 0%, #eaf4f8 100%);
        color: #1f2937;
    }

    h1, h2, h3 {
        color: #12343b;
        font-weight: 700;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #12343b 0%, #1f4e5f 100%);
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    .stButton > button {
        background-color: #1f7a8c;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #155e6b;
        color: white;
    }

    div[data-testid="stMetric"],
    div[data-testid="stExpander"],
    div[data-testid="stAlert"] {
        border-radius: 16px;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    div[data-testid="stForm"] {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 24px;
        border-radius: 20px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.6);
    }
    </style>
    """,
    unsafe_allow_html=True
)
# =========================================================
# DATENBANK (ERWEITERT)
# =========================================================

antibiotika_df = pd.DataFrame([

    # HARNWEGE
    {
        "Name": "Nitrofurantoin",
        "Bakterium": "E. coli",
        "Infektion": "Harnwege",
        "Wirkstoff": "Nitrofurantoin",
        "Dosierung": "100 mg 2x täglich",
        "Interaktionen": "Nierenfunktion beachten",
        "Warum": "Standard bei HWI",
        "Resistenz": "Niedrig"
    },
    {
        "Name": "Fosfomycin",
        "Bakterium": "E. coli",
        "Infektion": "Harnwege",
        "Wirkstoff": "Fosfomycin",
        "Dosierung": "3 g Einmalgabe",
        "Interaktionen": "Wenig Interaktionen",
        "Warum": "Einmaltherapie HWI",
        "Resistenz": "Niedrig"
    },

    # ATEMWEGE
    {
        "Name": "Amoxicillin",
        "Bakterium": "Streptococcus pneumoniae",
        "Infektion": "Atemwege",
        "Wirkstoff": "Aminopenicillin",
        "Dosierung": "750 mg 3x täglich",
        "Interaktionen": "Allergie möglich",
        "Warum": "Pneumonie Standard",
        "Resistenz": "Mittel"
    },
    {
        "Name": "Penicillin",
        "Bakterium": "Streptococcus pyogenes",
        "Infektion": "Atemwege",
        "Wirkstoff": "Penicillin G",
        "Dosierung": "1 Mio IE 3x täglich",
        "Interaktionen": "Allergie möglich",
        "Warum": "Sehr effektiv",
        "Resistenz": "Niedrig"
    },
    {
        "Name": "Azithromycin",
        "Bakterium": "Mycoplasma pneumoniae",
        "Infektion": "Atemwege",
        "Wirkstoff": "Makrolid",
        "Dosierung": "500 mg 1x täglich",
        "Interaktionen": "QT-Zeit beachten",
        "Warum": "Atypische Pneumonie",
        "Resistenz": "Mittel"
    },

    # HAUT
    {
        "Name": "Flucloxacillin",
        "Bakterium": "Staphylococcus aureus",
        "Infektion": "Haut",
        "Wirkstoff": "Penicillinase-stabil",
        "Dosierung": "500 mg 4x täglich",
        "Interaktionen": "Leberwerte",
        "Warum": "Staphylokokken",
        "Resistenz": "Mittel"
    },
    {
        "Name": "Vancomycin",
        "Bakterium": "MRSA",
        "Infektion": "Haut",
        "Wirkstoff": "Glykopeptid",
        "Dosierung": "1 g 2x täglich",
        "Interaktionen": "Niere beachten",
        "Warum": "MRSA",
        "Resistenz": "Niedrig"
    },

    # Magen-Darm
    {
        "Name": "Metronidazol",
        "Bakterium": "Clostridium difficile",
        "Infektion": "Magen-Darm",
        "Wirkstoff": "Nitroimidazol",
        "Dosierung": "500 mg 3x täglich",
        "Interaktionen": "Kein Alkohol",
        "Warum": "Anaerobier",
        "Resistenz": "Mittel"
    },

    # Geschlechtsorgane
    {
        "Name": "Doxycyclin",
        "Bakterium": "Chlamydia trachomatis",
        "Infektion": "Geschlechtsorgane",
        "Wirkstoff": "Tetrazyklin",
        "Dosierung": "100 mg 2x täglich",
        "Interaktionen": "Milch vermeiden",
        "Warum": "Chlamydien",
        "Resistenz": "Niedrig"
    },

    # Krankenhaus
    {
        "Name": "Meropenem",
        "Bakterium": "ESBL Enterobacteriaceae",
        "Infektion": "Krankenhausinfektion",
        "Wirkstoff": "Carbapenem",
        "Dosierung": "1 g 3x täglich",
        "Interaktionen": "Krampfschwelle",
        "Warum": "Reserveantibiotikum",
        "Resistenz": "Niedrig"
    },

    # Breitband
    {
        "Name": "Breitbandantibiotikum",
        "Bakterium": "Unbekannt",
        "Infektion": "Alle",
        "Wirkstoff": "Variabel",
        "Dosierung": "Individuell",
        "Interaktionen": "Arzt nötig",
        "Warum": "Unklarer Erreger",
        "Resistenz": "Hoch"
    }
])

# =========================================================
# SESSION STATE
# =========================================================

if "verlauf_df" not in st.session_state:
    st.session_state["verlauf_df"] = pd.DataFrame()

# =========================================================
# MEDIKAMENTENKLASSE
# =========================================================

def medikamentenklasse(wirkstoff):

    mapping = {
        "Aminopenicillin": "Penicilline",
        "Penicillin G": "Penicilline",
        "Penicillinase-stabil": "Penicilline",
        "Glykopeptid": "Glykopeptide",
        "Makrolid": "Makrolide",
        "Tetrazyklin": "Tetrazykline",
        "Nitroimidazol": "Nitroimidazole",
        "Nitrofurantoin": "Nitrofurane"
    }

    return mapping.get(wirkstoff, "Unbekannt")

# =========================================================
# FUNKTIONEN
# =========================================================

def antibiotika_empfehlung(bakterium, infekt, allergie):

    daten = antibiotika_df[
        (antibiotika_df["Bakterium"] == bakterium) &
        (antibiotika_df["Infektion"] == infekt)
    ]

    if daten.empty:
        return "Breitbandantibiotikum"

    antibiotikum = daten.iloc[0]["Name"]

    if allergie == "Penicillin":
        if antibiotikum in ["Penicillin", "Amoxicillin", "Flucloxacillin"]:
            antibiotikum = "Makrolid (Alternative)"

    return antibiotikum


def hole_details(name):

    daten = antibiotika_df[antibiotika_df["Name"] == name]

    if not daten.empty:
        return daten.iloc[0]

    return None


def berechne_risiko(alter, nier, schwanger, immu, allergie, multi, resistenz):

    punkte = 0

    if alter >= 65:
        punkte += 3
    elif alter >= 40:
        punkte += 1

    if nier:
        punkte += 3
    if schwanger:
        punkte += 2
    if immu:
        punkte += 3
    if allergie != "Keine":
        punkte += 1
    if multi:
        punkte += 2

    if resistenz == "Hoch":
        punkte += 3
    elif resistenz == "Mittel":
        punkte += 1

    if punkte >= 8:
        return "Hoch", punkte
    elif punkte >= 4:
        return "Mittel", punkte

    return "Niedrig", punkte


def speichern(entry):
    st.session_state["verlauf_df"] = pd.concat(
        [st.session_state["verlauf_df"], pd.DataFrame([entry])],
        ignore_index=True
    )

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("Navigation")

seite = st.sidebar.radio(
    "Bereich",
    ["Empfehlungssystem", "Statistik", "Lernbereich", "Verlauf"]
)

# =========================================================
# EMPFEHLUNGSSYSTEM
# =========================================================

if seite == "Empfehlungssystem":

    st.title("🦠 Antibiotika System")

    tab1, tab2 = st.tabs(["Empfehlung", "Suche"])

    with tab1:

        with st.form("f"):

            infektion = st.selectbox("Infektion", antibiotika_df["Infektion"].unique())
            bakterium = st.selectbox("Bakterium", antibiotika_df["Bakterium"].unique())
            alter = st.number_input("Alter", 0, 120, 30)

            allergie = st.selectbox("Allergie", ["Keine", "Penicillin", "Andere"])
            nier = st.checkbox("Niere")
            schw = st.checkbox("Schwangerschaft")
            immu = st.checkbox("Immunschwäche")
            multi = st.checkbox("Mehrere Medikamente")

            lern = st.toggle("Lernmodus")

            ok = st.form_submit_button("Start")

        if ok:

            if antibiotika_df[
                (antibiotika_df["Bakterium"] == bakterium) &
                (antibiotika_df["Infektion"] == infektion)
            ].empty:
                st.error("❌ Bakterium passt NICHT zur Infektion")
                st.stop()

            ab = antibiotika_empfehlung(bakterium, infektion, allergie)
            d = hole_details(ab)

            risiko, p = berechne_risiko(alter, nier, schw, immu, allergie, multi, d["Resistenz"])
            klasse = medikamentenklasse(d["Wirkstoff"])

            speichern({
                "Zeit": datetime.now(),
                "Bakterium": bakterium,
                "Infektion": infektion,
                "Empfehlung": ab,
                "Risiko": risiko
            })

            st.success(f"💊 {ab}")

            st.write("Wirkstoff:", d["Wirkstoff"])
            st.write("Klasse:", klasse)
            st.write("Resistenz:", d["Resistenz"])

            if risiko != "Niedrig":
                st.warning("⚠ Arzt/Apotheker abklären!")

            # ===== LERNMODUS =====
            st.markdown("---")
            st.header("📚 Erweiterter Lernmodus")

            st.info(
                """
                Antibiotika-Auswahl basiert auf:
                - Bakterium
                - Infektionsort
                - Resistenzlage
                - Allergien
                - Patientenrisiko
                """
            )# =========================================================
# STATISTIK
# =========================================================

elif seite == "Statistik":

    st.title("📊 Statistik")

    df = st.session_state["verlauf_df"]

    col1, col2, col3 = st.columns(3)

    col1.metric("Gespeicherte Empfehlungen", len(df))
    col2.metric("Antibiotika in Datenbank", len(antibiotika_df))
    col3.metric("Infektionsarten", antibiotika_df["Infektion"].nunique())

    st.markdown("---")

    if not df.empty:
        st.subheader("Häufig empfohlene Antibiotika")
        st.bar_chart(df["Empfehlung"].value_counts())

        st.subheader("Risikoverteilung")
        st.bar_chart(df["Risiko"].value_counts())
    else:
        st.info("Noch keine Statistik vorhanden. Starte zuerst eine Empfehlung.")


# =========================================================
# LERNBEREICH
# =========================================================

elif seite == "Lernbereich":

    st.title("📚 Lernbereich")

    st.subheader("Grundbegriffe")

    with st.expander("Was ist ein Wirkstoff?"):
        st.write("Ein Wirkstoff ist der aktive Bestandteil eines Medikaments.")

    with st.expander("Was bedeutet Resistenz?"):
        st.write("Resistenz bedeutet, dass Bakterien unempfindlich gegen ein Antibiotikum werden.")

    with st.expander("Was ist eine Medikamentenklasse?"):
        st.write("Eine Medikamentenklasse beschreibt, zu welcher Gruppe ein Medikament gehört.")

    st.markdown("---")

    st.subheader("Mini-Quiz")

    antwort = st.radio(
        "Was bedeutet Antibiotikaresistenz?",
        [
            "Bakterien werden unempfindlich gegen Antibiotika",
            "Antibiotika werden stärker",
            "Der Körper produziert Antibiotika"
        ]
    )

    if antwort == "Bakterien werden unempfindlich gegen Antibiotika":
        st.success("✅ Richtig")
    else:
        st.error("❌ Nicht ganz richtig")


# =========================================================
# VERLAUF
# =========================================================

elif seite == "Verlauf":

    st.title("📋 Verlauf")

    df = st.session_state["verlauf_df"]

    if not df.empty:
        st.dataframe(df, use_container_width=True)

        if st.button("Verlauf löschen"):
            st.session_state["verlauf_df"] = pd.DataFrame()
            st.success("Verlauf wurde gelöscht.")
            st.rerun()
    else:
        st.info("Noch keine Empfehlungen gespeichert.")

        # ================= ANALYSE =================
        st.subheader("🦠 Analyse")

        col1, col2 = st.columns(2)

        # Falls d nicht existiert
        if "d" not in locals():
            d = {}
        klasse = d.get("Medikamentenklasse", "Keine Angabe")
        bakterium = locals().get("bakterium", "Keine Angabe")
        infektion = locals().get("infektion", "Keine Angabe")
        klasse = d.get("Medikamentenklasse", klasse)

        with col1:
            st.write(f"**Bakterium:** {bakterium}")
            st.write(f"**Infektion:** {infektion}")
            st.write(
                f"**Empfehlung:** {d.get('Empfehlung', 'Keine Empfehlung verfügbar')}"
            )

        with col2:
            st.write(f"**Wirkstoff:** {d.get('Wirkstoff', 'Keine Angabe')}")
            st.write(f"**Dosierung:** {d.get('Dosierung', 'Keine Angabe')}")
            st.write(f"**Resistenz:** {d.get('Resistenz', 'Keine Angabe')}")
            st.write(f"**Medikamentenklasse:** {klasse}")

        st.markdown("---")
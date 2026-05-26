import streamlit as st
import pandas as pd
from datetime import datetime

# =========================================================
# SEITENKONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Antibiotika Empfehlungssystem",
    layout="wide"
)

# 🎨 DESIGN
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f8d7da;
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
    )

    # ================= ANALYSE =================
    st.subheader("🦠 Analyse")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Bakterium:** {bakterium}")
        st.write(f"**Infektion:** {infektion}")
        st.write(f"**Empfehlung:** {ab}")

    with col2:
        st.write(f"**Wirkstoff:** {d['Wirkstoff']}")
        st.write(f"**Dosierung:** {d['Dosierung']}")
        st.write(f"**Resistenz:** {d['Resistenz']}")
        st.write(f"**Medikamentenklasse:** {klasse}")

    st.markdown("---")

    # ================= WARUM =================
    st.subheader("💡 Warum diese Therapie?")

    st.success(d["Warum"])

    st.markdown("---")

    # ================= RISIKOFAKTOREN =================
    st.subheader("⚠ Risikofaktoren")

    if alter >= 65:
        st.warning("Alter erhöht Risiko")
    if nier:
        st.warning("Nierenerkrankung")
    if schw:
        st.warning("Schwangerschaft")
    if immu:
        st.warning("Immunschwäche")
    if multi:
        st.warning("Mehrere Medikamente")
    if allergie != "Keine":
        st.warning("Allergie vorhanden")

    st.markdown("---")

    # ================= INTERAKTIONEN =================
    st.subheader("💊 Interaktionen")

    st.info(d["Interaktionen"])

    st.markdown("---")

    # ================= LERNKARTEN =================
    st.subheader("🧠 Lernkarten")

    with st.expander("Was ist ein Wirkstoff?"):
        st.write("""
        Ein Wirkstoff ist der aktive Bestandteil eines Medikaments,
        der für die Heilung, Linderung oder Vorbeugung verantwortlich ist.
        """)

    with st.expander("Was ist Resistenz?"):
        st.write("""
        Eine Antibiotikaresistenz bedeutet, dass Bakterien unempfindlich
        gegenüber einem Antibiotikum werden.
        """)

    with st.expander("Warum ist die Medikamentenklasse wichtig?"):
        st.write("""
        Sie zeigt den Wirkmechanismus (z.B. Zellwandhemmung oder Proteinsynthesehemmung).
        """)

    with st.expander("Warum sind Allergien kritisch?"):
        st.write("""
        Allergien können schwere Reaktionen auslösen und müssen bei der Auswahl berücksichtigt werden.
        """)

    st.markdown("---")

    # ================= MINI QUIZ =================
    st.subheader("📝 Mini Quiz")

    quiz = st.radio(
        "Was bedeutet Resistenz?",
        [
            "Bakterien werden unempfindlich gegen Antibiotika",
            "Antibiotika werden stärker",
            "Der Körper produziert mehr Medikamente"
        ]
    )

    if quiz == "Bakterien werden unempfindlich gegen Antibiotika":
        st.success("✅ Richtig")
    else:
        st.error("❌ Falsch")

# =========================================================
# STATISTIK
# =========================================================

elif seite == "Statistik":

    st.title("Statistik")

    df = st.session_state["verlauf_df"]

    if not df.empty:
        st.bar_chart(df["Empfehlung"].value_counts())
    else:
        st.info("Keine Daten")

# =========================================================
# LERNBEREICH
# =========================================================

elif seite == "Lernbereich":

    st.title("Lernbereich")

    st.write("Wirkstoff = aktiver Bestandteil eines Medikaments")
    st.write("Resistenz = Bakterien werden unempfindlich gegen Antibiotika")

# =========================================================
# VERLAUF
# =========================================================

elif seite == "Verlauf":

    st.title("Verlauf")

    df = st.session_state["verlauf_df"]

    if not df.empty:
        st.dataframe(df)
    else:
        st.info("Keine Daten")
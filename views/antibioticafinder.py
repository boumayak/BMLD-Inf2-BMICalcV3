import streamlit as st
import pandas as pd
from datetime import datetime


# =========================================================
# KONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Antibiotika Empfehlungssystem",
    page_icon="🧪",
    layout="wide"
)


# =========================================================
# DATENBANK
# =========================================================

antibiotika_df = pd.DataFrame([

    {
        "Name": "Nitrofurantoin",
        "Bakterium": "E. coli",
        "Infektion": "Harnwege",
        "Wirkstoff": "Nitrofurantoin",
        "Dosierung": "100 mg 2x täglich",
        "Interaktionen": "Nicht bei Niereninsuffizienz",
        "Warum": "Standard bei unkomplizierten Harnwegsinfekten",
        "Resistenz": "Niedrig"
    },

    {
        "Name": "Fosfomycin",
        "Bakterium": "E. coli",
        "Infektion": "Harnwege",
        "Wirkstoff": "Fosfomycin",
        "Dosierung": "3 g Einmaldosis",
        "Interaktionen": "Wenig Interaktionen",
        "Warum": "Alternative bei Harnwegsinfekten",
        "Resistenz": "Niedrig"
    },

    {
        "Name": "Flucloxacillin",
        "Bakterium": "Staphylococcus aureus",
        "Infektion": "Haut",
        "Wirkstoff": "Penicillinase-festes Penicillin",
        "Dosierung": "500 mg 4x täglich",
        "Interaktionen": "Leberwerte überwachen",
        "Warum": "Gut wirksam gegen Staphylokokken",
        "Resistenz": "Mittel"
    },

    {
        "Name": "Vancomycin",
        "Bakterium": "MRSA",
        "Infektion": "Haut",
        "Wirkstoff": "Glykopeptid",
        "Dosierung": "1 g 2x täglich",
        "Interaktionen": "Nierenfunktion kontrollieren",
        "Warum": "Standardtherapie gegen MRSA",
        "Resistenz": "Niedrig"
    },

    {
        "Name": "Penicillin",
        "Bakterium": "Streptococcus",
        "Infektion": "Atemwege",
        "Wirkstoff": "Beta-Lactam",
        "Dosierung": "1 Mio IE 3x täglich",
        "Interaktionen": "Allergische Reaktionen möglich",
        "Warum": "Sehr effektiv gegen Streptokokken",
        "Resistenz": "Niedrig"
    },

    {
        "Name": "Makrolid (Alternative wegen Allergie)",
        "Bakterium": "Streptococcus",
        "Infektion": "Atemwege",
        "Wirkstoff": "Azithromycin",
        "Dosierung": "500 mg 1x täglich",
        "Interaktionen": "QT-Zeit Verlängerung möglich",
        "Warum": "Alternative bei Penicillinallergie",
        "Resistenz": "Mittel"
    },

    {
        "Name": "Ceftriaxon",
        "Bakterium": "Neisseria meningitidis",
        "Infektion": "Meningitis",
        "Wirkstoff": "Cephalosporin der 3. Generation",
        "Dosierung": "2 g täglich",
        "Interaktionen": "Calciumhaltige Lösungen vermeiden",
        "Warum": "Standard bei Meningokokken",
        "Resistenz": "Niedrig"
    },

    {
        "Name": "Doxycyclin",
        "Bakterium": "Chlamydia trachomatis",
        "Infektion": "Geschlechtsorgane",
        "Wirkstoff": "Tetrazyklin",
        "Dosierung": "100 mg 2x täglich",
        "Interaktionen": "Nicht mit Milchprodukten einnehmen",
        "Warum": "Standardtherapie bei Chlamydien",
        "Resistenz": "Niedrig"
    },

    {
        "Name": "Azithromycin",
        "Bakterium": "Mycoplasma pneumoniae",
        "Infektion": "Atemwege",
        "Wirkstoff": "Makrolid",
        "Dosierung": "500 mg täglich",
        "Interaktionen": "QT-Zeit überwachen",
        "Warum": "Gut bei atypischen Pneumonien",
        "Resistenz": "Mittel"
    },

    {
        "Name": "Piperacillin/Tazobactam",
        "Bakterium": "Pseudomonas aeruginosa",
        "Infektion": "Krankenhausinfektion",
        "Wirkstoff": "Breitbandpenicillin",
        "Dosierung": "4,5 g 3x täglich",
        "Interaktionen": "Nierenfunktion beachten",
        "Warum": "Breit wirksam gegen Pseudomonas",
        "Resistenz": "Hoch"
    },

    {
        "Name": "Metronidazol",
        "Bakterium": "Clostridium difficile",
        "Infektion": "Magen-Darm",
        "Wirkstoff": "Nitroimidazol",
        "Dosierung": "500 mg 3x täglich",
        "Interaktionen": "Kein Alkohol",
        "Warum": "Wirksam gegen anaerobe Bakterien",
        "Resistenz": "Mittel"
    },

    {
        "Name": "Ciprofloxacin",
        "Bakterium": "Salmonella",
        "Infektion": "Magen-Darm",
        "Wirkstoff": "Fluorchinolon",
        "Dosierung": "500 mg 2x täglich",
        "Interaktionen": "Sehnenprobleme möglich",
        "Warum": "Gut wirksam gegen Salmonellen",
        "Resistenz": "Mittel"
    },

    {
        "Name": "Amoxicillin",
        "Bakterium": "Haemophilus influenzae",
        "Infektion": "Atemwege",
        "Wirkstoff": "Aminopenicillin",
        "Dosierung": "750 mg 3x täglich",
        "Interaktionen": "Allergische Reaktionen möglich",
        "Warum": "Häufig bei Atemwegsinfekten",
        "Resistenz": "Mittel"
    },

    {
        "Name": "Levofloxacin",
        "Bakterium": "Legionella pneumophila",
        "Infektion": "Atemwege",
        "Wirkstoff": "Fluorchinolon",
        "Dosierung": "500 mg täglich",
        "Interaktionen": "QT-Zeit Verlängerung",
        "Warum": "Sehr wirksam gegen Legionellen",
        "Resistenz": "Niedrig"
    },

    {
        "Name": "Meropenem",
        "Bakterium": "ESBL-bildende Enterobakterien",
        "Infektion": "Krankenhausinfektion",
        "Wirkstoff": "Carbapenem",
        "Dosierung": "1 g 3x täglich",
        "Interaktionen": "Krampfschwelle beachten",
        "Warum": "Reserveantibiotikum bei ESBL",
        "Resistenz": "Niedrig"
    },

    {
        "Name": "Breitbandantibiotikum",
        "Bakterium": "Unbekannt",
        "Infektion": "Alle",
        "Wirkstoff": "Variabel",
        "Dosierung": "Abhängig vom Präparat",
        "Interaktionen": "Individuell prüfen",
        "Warum": "Wenn Erreger unbekannt ist",
        "Resistenz": "Hoch"
    }

])


# =========================================================
# SESSION STATE
# =========================================================

if "data_df" not in st.session_state:
    st.session_state["data_df"] = pd.DataFrame()


# =========================================================
# FUNKTIONEN
# =========================================================

def antibiotika_empfehlung(bakterium, allergie):

    daten = antibiotika_df[
        antibiotika_df["Bakterium"] == bakterium
    ]

    if daten.empty:
        antibiotikum = "Breitbandantibiotikum"

    else:
        antibiotikum = daten.iloc[0]["Name"]

    # Allergie prüfen
    if allergie == "Penicillin":

        if antibiotikum in [
            "Penicillin",
            "Amoxicillin",
            "Flucloxacillin"
        ]:
            antibiotikum = (
                "Makrolid (Alternative wegen Allergie)"
            )

    return antibiotikum


def hole_details(name):

    daten = antibiotika_df[
        antibiotika_df["Name"] == name
    ]

    if not daten.empty:
        return daten.iloc[0]

    return None


def berechne_risiko(alter):

    if alter >= 65:
        return "Hoch"

    elif alter >= 40:
        return "Mittel"

    return "Niedrig"


def zeige_resistenz(resistenz):

    if resistenz == "Niedrig":
        st.success("🟢 Niedrige Resistenz")

    elif resistenz == "Mittel":
        st.warning("🟡 Mittlere Resistenz")

    else:
        st.error("🔴 Hohe Resistenz")


def speichere_abfrage(result):

    st.session_state["data_df"] = pd.concat(
        [
            st.session_state["data_df"],
            pd.DataFrame([result])
        ],
        ignore_index=True
    )


def statistik_dashboard():

    st.subheader("Statistik Dashboard")

    df = st.session_state["data_df"]

    if df.empty:
        st.info("Noch keine Daten vorhanden")
        return

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Abfragen", len(df))

    with col2:
        durchschnitt = round(
            df["Alter"].mean(),
            1
        )
        st.metric(
            "Durchschnittsalter",
            durchschnitt
        )

    with col3:
        top = (
            df["Bakterium"]
            .value_counts()
            .idxmax()
        )

        st.metric(
            "Häufigstes Bakterium",
            top
        )

    st.markdown("---")

    st.markdown("### Empfehlungen")

    empfehlungen = (
        df["Empfehlung"]
        .value_counts()
    )

    st.bar_chart(empfehlungen)

    st.markdown("### Bakterien")

    bakterien = (
        df["Bakterium"]
        .value_counts()
    )

    st.bar_chart(bakterien)

    st.markdown("### Risikoanalyse")

    risiko = (
        df["Risiko"]
        .value_counts()
    )

    st.bar_chart(risiko)


def lernbereich():

    st.subheader("Medizinischer Lernbereich")

    with st.expander("Wirkstoff"):
        st.write(
            "Aktiver Bestandteil eines Medikaments."
        )

    with st.expander("Dosierung"):
        st.write(
            "Menge und Häufigkeit der Einnahme."
        )

    with st.expander("Resistenz"):
        st.write(
            "Bakterien können unempfindlich "
            "gegen Antibiotika werden."
        )

    with st.expander("MRSA"):
        st.write(
            "Multiresistenter Staphylococcus aureus."
        )

    with st.expander("ESBL"):
        st.write(
            "Bakterien mit erweiterten "
            "Beta-Lactamasen."
        )


def verlauf_anzeigen():

    st.subheader("Verlauf")

    df = st.session_state["data_df"]

    if df.empty:
        st.info("Noch keine Daten gespeichert")
        return

    st.dataframe(df)

    csv = df.to_csv(index=False)

    st.download_button(
        label="⬇ CSV herunterladen",
        data=csv,
        file_name="abfragen.csv",
        mime="text/csv"
    )


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("Navigation")

seite = st.sidebar.radio(
    "Bereich auswählen",
    [
        "Empfehlungssystem",
        "Statistik",
        "Lernbereich",
        "Verlauf"
    ]
)


# =========================================================
# EMPFEHLUNGSSYSTEM
# =========================================================

if seite == "Empfehlungssystem":

    st.title(" Antibiotika Empfehlungssystem")

    tab1, tab2 = st.tabs([
        "Empfehlung",
        "Bakteriensuche"
    ])

    # =====================================================
    # TAB 1
    # =====================================================

    with tab1:

        with st.form("formular"):

            col1, col2 = st.columns(2)

            with col1:

                infektion = st.selectbox(
                    "Infektionsart",
                    antibiotika_df["Infektion"]
                    .unique()
                )

                bakterium = st.selectbox(
                    "Bakterium",
                    antibiotika_df["Bakterium"]
                    .unique()
                )

            with col2:

                alter = st.number_input(
                    "Alter",
                    min_value=0,
                    max_value=120,
                    value=30
                )

                allergie = st.selectbox(
                    "Allergie",
                    [
                        "Keine",
                        "Penicillin",
                        "Andere"
                    ]
                )

            lernmodus = st.toggle(
                "Lernmodus"
            )

            submitted = st.form_submit_button(
                "Empfehlung anzeigen"
            )

        # =================================================
        # ERGEBNIS
        # =================================================

        if submitted:

            antibiotikum = antibiotika_empfehlung(
                bakterium,
                allergie
            )

            details = hole_details(
                antibiotikum
            )

            risiko = berechne_risiko(
                alter
            )

            result = {

                "Zeitpunkt":
                    datetime.now(),

                "Infektion":
                    infektion,

                "Bakterium":
                    bakterium,

                "Alter":
                    alter,

                "Allergie":
                    allergie,

                "Risiko":
                    risiko,

                "Empfehlung":
                    antibiotikum
            }

            speichere_abfrage(result)

            st.markdown("---")

            st.success(
                f"Empfehlung: {antibiotikum}"
            )

            # Risiko
            st.markdown(
                "### ⚠ Risikoanalyse"
            )

            if risiko == "Hoch":
                st.error("Hohes Risiko")

            elif risiko == "Mittel":
                st.warning(
                    "Mittleres Risiko"
                )

            else:
                st.success(
                    "Niedriges Risiko"
                )

            # Allergie
            if allergie == "Penicillin":

                st.warning(
                    "⚠ Penicillinallergie beachten"
                )

            # Details
            if details is not None:

                st.markdown(
                    "### Medikamentendetails"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.write(
                        f"**Wirkstoff:** "
                        f"{details['Wirkstoff']}"
                    )

                    st.write(
                        f"**Dosierung:** "
                        f"{details['Dosierung']}"
                    )

                    st.write(
                        f"**Resistenz:** "
                        f"{details['Resistenz']}"
                    )

                with col2:

                    st.write(
                        f"**Interaktionen:** "
                        f"{details['Interaktionen']}"
                    )

                    st.write(
                        f"**Warum?:** "
                        f"{details['Warum']}"
                    )

                st.markdown(
                    "### Resistenzbewertung"
                )

                zeige_resistenz(
                    details["Resistenz"]
                )

            # Lernmodus
            if lernmodus:

                st.markdown(
                    "### Lernmodus"
                )

                st.info(
                    "Die Antibiotikawahl "
                    "hängt von Bakterium, "
                    "Infektionsort, "
                    "Allergien und "
                    "Resistenzen ab."
                )

    # =====================================================
    # TAB 2
    # =====================================================

    with tab2:

        st.subheader(
            "Bakteriensuche"
        )

        search = st.text_input(
            "Bakterium suchen"
        )

        if search:

            resultate = antibiotika_df[
                antibiotika_df["Bakterium"]
                .str.contains(
                    search,
                    case=False
                )
            ]

            if not resultate.empty:

                st.success(
                    "Treffer gefunden"
                )

                st.dataframe(
                    resultate[
                        [
                            "Bakterium",
                            "Name",
                            "Infektion",
                            "Resistenz"
                        ]
                    ]
                )

            else:
                st.warning(
                    "Kein Treffer gefunden"
                )


# =========================================================
# STATISTIK
# =========================================================

elif seite == "Statistik":

    st.title("Statistik")

    statistik_dashboard()


# =========================================================
# LERNBEREICH
# =========================================================

elif seite == "Lernbereich":

    st.title("Lernbereich")

    lernbereich()


# =========================================================
# VERLAUF
# =========================================================

elif seite == "Verlauf":

    st.title("Verlauf")

    verlauf_anzeigen()
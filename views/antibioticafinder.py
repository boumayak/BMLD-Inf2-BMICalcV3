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
    }

])

# =========================================================
# SESSION STATE
# =========================================================

if "verlauf_df" not in st.session_state:
    st.session_state["verlauf_df"] = pd.DataFrame()

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


# =========================================================
# ERWEITERTE RISIKOANALYSE
# =========================================================

def berechne_risiko(
    alter,
    nierenerkrankung,
    schwangerschaft,
    immunschwäche,
    allergie,
    mehrere_medikamente,
    resistenz
):

    punkte = 0

    if alter >= 65:
        punkte += 3

    elif alter >= 40:
        punkte += 1

    if nierenerkrankung:
        punkte += 3

    if schwangerschaft:
        punkte += 2

    if immunschwäche:
        punkte += 3

    if allergie != "Keine":
        punkte += 1

    if mehrere_medikamente:
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


def zeige_resistenz(resistenz):

    if resistenz == "Niedrig":
        st.success("🟢 Niedrige Resistenz")

    elif resistenz == "Mittel":
        st.warning("🟡 Mittlere Resistenz")

    else:
        st.error("🔴 Hohe Resistenz")


def speichere_verlauf(resultat):

    st.session_state["verlauf_df"] = pd.concat(
        [
            st.session_state["verlauf_df"],
            pd.DataFrame([resultat])
        ],
        ignore_index=True
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

    st.title("🦠 Antibiotika Empfehlungssystem")

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
                    antibiotika_df["Infektion"].unique()
                )

                bakterium = st.selectbox(
                    "Bakterium",
                    antibiotika_df["Bakterium"].unique()
                )

                alter = st.number_input(
                    "Alter",
                    min_value=0,
                    max_value=120,
                    value=30
                )

            with col2:

                allergie = st.selectbox(
                    "Allergie",
                    [
                        "Keine",
                        "Penicillin",
                        "Andere"
                    ]
                )

                nierenerkrankung = st.checkbox(
                    "Nierenerkrankung"
                )

                schwangerschaft = st.checkbox(
                    "Schwangerschaft"
                )

                immunschwäche = st.checkbox(
                    "Immunschwäche"
                )

                mehrere_medikamente = st.checkbox(
                    "Mehrere Medikamente"
                )

            lernmodus = st.toggle(
                "📚 Lernmodus aktivieren"
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

            risiko, punkte = berechne_risiko(
                alter,
                nierenerkrankung,
                schwangerschaft,
                immunschwäche,
                allergie,
                mehrere_medikamente,
                details["Resistenz"]
            )

            resultat = {

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

                "Punkte":
                    punkte,

                "Empfehlung":
                    antibiotikum
            }

            speichere_verlauf(resultat)

            st.markdown("---")

            st.success(
                f"💊 Empfehlung: {antibiotikum}"
            )

            st.markdown("## Medikamentendetails")

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"**Wirkstoff:** {details['Wirkstoff']}"
                )

                st.write(
                    f"**Dosierung:** {details['Dosierung']}"
                )

                st.write(
                    f"**Resistenz:** {details['Resistenz']}"
                )

            with col2:

                st.write(
                    f"**Interaktionen:** {details['Interaktionen']}"
                )

                st.write(
                    f"**Warum empfohlen?:** {details['Warum']}"
                )

            st.markdown("---")

            st.markdown("## ⚠ Risikoanalyse")

            st.write(
                f"**Risiko-Score:** {punkte} Punkte"
            )

            if risiko == "Hoch":

                st.error(
                    """
                    🔴 Hohes Risiko erkannt
                    """
                )

            elif risiko == "Mittel":

                st.warning(
                    """
                    🟡 Mittleres Risiko erkannt
                    """
                )

            else:

                st.success(
                    """
                    🟢 Niedriges Risiko erkannt
                    """
                )

            st.markdown("---")

            st.markdown("## 🧪 Resistenzbewertung")

            zeige_resistenz(
                details["Resistenz"]
            )

            # =================================================
            # LERNMODUS
            # =================================================

            if lernmodus:

                st.markdown("---")

                st.header("📚 Erweiterter Lernmodus")

                st.info(
                    """
                    Die Auswahl eines Antibiotikums basiert auf:
                    - Bakterium
                    - Infektionsort
                    - Resistenzlage
                    - Allergien
                    - Patientenrisiko
                    """
                )

                # =============================================
                # ANALYSE
                # =============================================

                st.subheader("🦠 Analyse")

                col1, col2 = st.columns(2)

                with col1:

                    st.write(
                        f"**Bakterium:** {bakterium}"
                    )

                    st.write(
                        f"**Infektion:** {infektion}"
                    )

                    st.write(
                        f"**Empfohlenes Medikament:** {antibiotikum}"
                    )

                with col2:

                    st.write(
                        f"**Wirkstoff:** {details['Wirkstoff']}"
                    )

                    st.write(
                        f"**Dosierung:** {details['Dosierung']}"
                    )

                    st.write(
                        f"**Resistenz:** {details['Resistenz']}"
                    )

                st.markdown("---")

                # =============================================
                # WARUM
                # =============================================

                st.subheader("💡 Warum diese Empfehlung?")

                st.success(
                    details["Warum"]
                )

                st.markdown("---")

                # =============================================
                # RISIKOFAKTOREN
                # =============================================

                st.subheader("⚠ Erkannte Risikofaktoren")

                if alter >= 65:
                    st.warning("Hohes Alter")

                if nierenerkrankung:
                    st.warning("Nierenerkrankung")

                if schwangerschaft:
                    st.warning("Schwangerschaft")

                if immunschwäche:
                    st.warning("Immunschwäche")

                if mehrere_medikamente:
                    st.warning("Viele Medikamente")

                if allergie != "Keine":
                    st.warning("Allergie vorhanden")

                if punkte == 0:
                    st.success(
                        "Keine Risikofaktoren erkannt"
                    )

                st.markdown("---")

                # =============================================
                # INTERAKTIONEN
                # =============================================

                st.subheader("💊 Interaktionen")

                st.info(
                    details["Interaktionen"]
                )

                st.markdown("---")

                # =============================================
                # LERNKARTEN
                # =============================================

                st.subheader("🧠 Medizinische Lernkarten")

                with st.expander(
                    "Was bedeutet Resistenz?"
                ):

                    st.write(
                        """
                        Bakterien können gegen Antibiotika
                        unempfindlich werden.
                        """
                    )

                with st.expander(
                    "Warum sind Allergien wichtig?"
                ):

                    st.write(
                        """
                        Allergien können gefährliche
                        Reaktionen auslösen.
                        """
                    )

                with st.expander(
                    "Warum ist Dosierung wichtig?"
                ):

                    st.write(
                        """
                        Falsche Dosierungen fördern
                        Resistenzen.
                        """
                    )

                with st.expander(
                    "Was bedeutet MRSA?"
                ):

                    st.write(
                        """
                        MRSA bedeutet:
                        Multiresistenter
                        Staphylococcus aureus.
                        """
                    )

                st.markdown("---")

                # =============================================
                # QUIZ
                # =============================================

                st.subheader("📝 Mini Quiz")

                quiz = st.radio(
                    "Wofür steht MRSA?",
                    [
                        "Multiresistenter Staphylococcus aureus",
                        "Medizinische Resistenz Analyse",
                        "Mikrobiologische Standard Analyse"
                    ]
                )

                if (
                    quiz ==
                    "Multiresistenter Staphylococcus aureus"
                ):

                    st.success(
                        "✅ Richtig beantwortet"
                    )

                else:

                    st.error(
                        "❌ Leider falsch"
                    )

    # =====================================================
    # TAB 2 - BAKTERIENSUCHE
    # =====================================================

    with tab2:

        st.subheader("🔎 Bakteriensuche")

        suche = st.text_input(
            "Bakterium suchen"
        )

        infektion_filter = st.selectbox(
            "Infektion filtern",
            ["Alle"] +
            list(
                antibiotika_df["Infektion"]
                .unique()
            )
        )

        resistenz_filter = st.selectbox(
            "Resistenz filtern",
            [
                "Alle",
                "Niedrig",
                "Mittel",
                "Hoch"
            ]
        )

        gefiltert = antibiotika_df.copy()

        if suche:

            gefiltert = gefiltert[
                gefiltert["Bakterium"]
                .str.contains(
                    suche,
                    case=False
                )
            ]

        if infektion_filter != "Alle":

            gefiltert = gefiltert[
                gefiltert["Infektion"]
                == infektion_filter
            ]

        if resistenz_filter != "Alle":

            gefiltert = gefiltert[
                gefiltert["Resistenz"]
                == resistenz_filter
            ]

        st.dataframe(
            gefiltert,
            use_container_width=True
        )

        st.metric(
            "Gefundene Einträge",
            len(gefiltert)
        )

# =========================================================
# STATISTIK
# =========================================================

elif seite == "Statistik":

    st.title("📊 Statistik")

    df = st.session_state["verlauf_df"]

    if df.empty:

        st.info(
            "Noch keine Daten vorhanden"
        )

    else:

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Abfragen",
                len(df)
            )

        with col2:

            st.metric(
                "Durchschnittsalter",
                round(df["Alter"].mean(), 1)
            )

        with col3:

            st.metric(
                "Häufigstes Bakterium",
                df["Bakterium"]
                .value_counts()
                .idxmax()
            )

        st.markdown("---")

        st.subheader("Empfehlungen")

        st.bar_chart(
            df["Empfehlung"]
            .value_counts()
        )

        st.subheader("Risikoanalyse")

        st.bar_chart(
            df["Risiko"]
            .value_counts()
        )

# =========================================================
# LERNBEREICH
# =========================================================

elif seite == "Lernbereich":

    st.title("📚 Lernbereich")

    with st.expander("Wirkstoff"):
        st.write(
            "Aktiver Bestandteil eines Medikaments."
        )

    with st.expander("Resistenz"):
        st.write(
            """
            Bakterien können gegen Antibiotika
            resistent werden.
            """
        )

    with st.expander("MRSA"):
        st.write(
            """
            Multiresistenter
            Staphylococcus aureus.
            """
        )

    with st.expander("Breitbandantibiotikum"):
        st.write(
            """
            Wirkt gegen viele verschiedene
            Bakterienarten.
            """
        )

# =========================================================
# VERLAUF
# =========================================================

elif seite == "Verlauf":

    st.title("🕒 Verlauf")

    df = st.session_state["verlauf_df"]

    if df.empty:

        st.info(
            "Noch keine Daten gespeichert"
        )

    else:

        st.dataframe(
            df,
            use_container_width=True
        )

        csv = df.to_csv(index=False)

        st.download_button(
            label="⬇ CSV herunterladen",
            data=csv,
            file_name="verlauf.csv",
            mime="text/csv"
        )
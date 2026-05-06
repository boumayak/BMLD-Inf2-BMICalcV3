import pandas as pd
import streamlit as st



 page_title="Antibiotika Empfehlung",
 page_icon="🧪"


st.title('🧪 Antibiotika Empfehlung')

# -----------------------------
#  Detail-Datenbank 
# -----------------------------
details_db = {
    "Nitrofurantoin": {
        "Wirkstoff": "Nitrofurantoin",
        "Dosierung": "100 mg 2x täglich",
        "Interaktionen": "Nicht bei Niereninsuffizienz",
        "Warum": "Standard bei Harnwegsinfekten durch E. coli"
    },
    "Flucloxacillin": {
        "Wirkstoff": "Penicillinase-festes Penicillin",
        "Dosierung": "500 mg 4x täglich",
        "Interaktionen": "Leberwerte überwachen",
        "Warum": "Wirksam gegen Staphylokokken"
    },
    "Penicillin": {
        "Wirkstoff": "Beta-Lactam",
        "Dosierung": "1 Mio IE 3x täglich",
        "Interaktionen": "Allergische Reaktionen möglich",
        "Warum": "Sehr effektiv gegen Streptokokken"
    },
    "Makrolid (Alternative wegen Allergie)": {
        "Wirkstoff": "Makrolid",
        "Dosierung": "500 mg 1x täglich",
        "Interaktionen": "QT-Zeit Verlängerung möglich",
        "Warum": "Alternative bei Penicillinallergie"
    },
    "Breitbandantibiotikum": {
        "Wirkstoff": "Variabel",
        "Dosierung": "Abhängig vom Präparat",
        "Interaktionen": "Individuell prüfen",
        "Warum": "Wenn Erreger unbekannt ist"
    }
}

# -----------------------------
#  Eingabeformular 
# -----------------------------
with st.form("Eingabeformular"):

    infektion = st.selectbox(
        'Wählen Sie eine Infektionsart',
        ['Atemwege', 'Harnwege', 'Haut', 'Magen-Darm']
    )

    bakterium = st.selectbox(
        'Wählen Sie ein Bakterium',
        ['Unbekannt', 'E. coli', 'Staphylococcus aureus', 'Streptococcus']
    )

    alter = st.number_input('Alter', min_value=0, max_value=120, value=30)

    allergie = st.selectbox(
        'Allergien vorhanden?',
        ['Keine', 'Penicillin', 'Andere']
    )

    #  Lernmodus
    lernmodus = st.toggle(" Lernmodus aktivieren")

    submitted = st.form_submit_button("Empfehlung anzeigen")


# -----------------------------
#  Logik + Anzeige 
# -----------------------------
if submitted:

    # V4 – Basislogik
    if bakterium == 'E. coli':
        antibiotikum = 'Nitrofurantoin'
    elif bakterium == 'Staphylococcus aureus':
        antibiotikum = 'Flucloxacillin'
    elif bakterium == 'Streptococcus':
        antibiotikum = 'Penicillin'
    else:
        antibiotikum = 'Breitbandantibiotikum'

    # Allergie berücksichtigen
    if allergie == 'Penicillin' and antibiotikum == 'Penicillin':
        antibiotikum = 'Makrolid (Alternative wegen Allergie)'

    result = {
        "Infektion": infektion,
        "Bakterium": bakterium,
        "Alter": alter,
        "Allergie": allergie,
        "Empfehlung": antibiotikum
    }

    st.write("### Ergebnis")

    #  Hervorhebung
    st.success(f' Beste Empfehlung: {result["Empfehlung"]}')

    #  Details
    if antibiotikum in details_db:
        daten = details_db[antibiotikum]

        st.markdown("###  Details")
        st.write(f"**Wirkstoff:** {daten['Wirkstoff']}")
        st.write(f"**Dosierung:** {daten['Dosierung']}")
        st.write(f"**Interaktionen:** {daten['Interaktionen']}")

        # Warum dieses Antibiotikum?
        st.markdown("###  Warum dieses Antibiotikum?")
        st.info(daten["Warum"])

    # Lernmodus
    if lernmodus:
        st.markdown("###  Lerninfo")
        st.write(
            "Die Auswahl eines Antibiotikums basiert auf Erreger, "
            "Infektionsort und individuellen Faktoren wie Allergien."
        )

    # Speicherung
    if 'data_df' not in st.session_state:
        st.session_state['data_df'] = pd.DataFrame()

    st.session_state['data_df'] = pd.concat(
        [st.session_state['data_df'], pd.DataFrame([result])],
        ignore_index=True
    )


# -----------------------------
# Suchfunktion
# -----------------------------
st.markdown("---")
st.subheader("🔍 Bakterium suchen")

search = st.text_input("Name eingeben")

bakterien_liste = ['E. coli', 'Staphylococcus aureus', 'Streptococcus']

if search:
    matches = [b for b in bakterien_liste if search.lower() in b.lower()]

    if matches:
        st.write("Gefunden:", matches)
    else:
        st.warning("Kein Bakterium gefunden")


# -----------------------------
#  Tooltips
# -----------------------------
st.markdown("---")
st.subheader("Fachbegriffe")

with st.expander("Wirkstoff"):
    st.write("Aktiver Bestandteil eines Medikaments")

with st.expander("Dosierung"):
    st.write("Wie oft und wie viel ein Medikament eingenommen wird")

with st.expander("Interaktionen"):
    st.write("Wechselwirkungen mit anderen Medikamenten")


# -----------------------------
#  Tabelle anzeigen
# -----------------------------
if 'data_df' in st.session_state:
    st.markdown("---")
    st.subheader("Bisherige Abfragen")
    st.dataframe(st.session_state['data_df'])


import pandas as pd
import streamlit as st

st.title('Antibiotika Empfehlung')

with st.form("Eingabeformular"):

    ### V1.0 – Eingabe: Infektionsart auswählen
    infektion = st.selectbox(
        'Wählen Sie eine Infektionsart',
        ['Atemwege', 'Harnwege', 'Haut', 'Magen-Darm']
    )

    ### V2.0 – Eingabe: Bakterium auswählen
    bakterium = st.selectbox(
        'Wählen Sie ein Bakterium',
        ['Unbekannt', 'E. coli', 'Staphylococcus aureus', 'Streptococcus']
    )

    ### V3.0 – Eingabe: Patientendaten
    alter = st.number_input('Alter', min_value=0, max_value=120, value=30)
    allergie = st.selectbox(
        'Allergien vorhanden?',
        ['Keine', 'Penicillin', 'Andere']
    )

    submitted = st.form_submit_button("Empfehlung anzeigen")


if submitted:

    ### V4.0 – Anzeige von Antibiotika-Vorschlägen

    # einfache Logik (Demo)
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
    st.write(f'Empfohlenes Antibiotikum: {result["Empfehlung"]}')

    # Daten speichern
    if 'data_df' not in st.session_state:
        st.session_state['data_df'] = pd.DataFrame()

    st.session_state['data_df'] = pd.concat(
        [st.session_state['data_df'], pd.DataFrame([result])]
    )

# Tabelle anzeigen
st.dataframe(st.session_state['data_df'])


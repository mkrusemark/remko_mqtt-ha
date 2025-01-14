# Remko generated register definitions
FIELD_REGNUM = 0
FIELD_REGTYPE = 1
FIELD_UNIT = 2
FIELD_MINVALUE = 3
FIELD_MAXVALUE = 4

# Register as sensors
reg_id = {
    #  reg_id: ['reg#', 'type', 'unit', 'min', 'max'],
    "dhw_opmode": ["1079", "select_input", "", 0, 16],
    "water_temp_req": ["1082", "temperature_input", "ºC", 20.0, 60.0],
    "absence_mode": ["1893", "switch", "", "", ""],
    "party_mode": ["1894", "switch", "", "", ""],
    "main_mode": ["1951", "select_input", "", "", ""],
    "heating_circ_mode": ["1972", "switch", "", "", ""],
    "fixed_temp_req": ["1974", "temperature_input", "ºC", 20.0, 60.0],
    "opmode": ["5001", "sensor_mode", "", "", ""],
    "circulation_temp": ["5027", "temperature", "ºC", 0, 70],
    "out_temp": ["5032", "temperature", "ºC", 0, 40],
    "water_temp": ["5039", "temperature", "ºC", 0, 70],
    "heat_gen_status": ["5051", "binary_sensor", "", "", ""],
    "mixed_temp": ["5055", "temperature", "ºC", 0, 40],
    "heat_water_temp_req": ["5085", "temperature_input", "ºC", 20.0, 60.0],
    "heat_water_temp": ["5131", "temperature", "ºC", 0, 70],
    "el_consumption": ["5320", "sensor_el", "W", 0, 6000],
    "th_consumption": ["5321", "sensor_el", "W", 0, 20000],
    "dhw_heating": ["5693", "action", "", "", ""],
    "communication_status": ["communication_status", "generated_sensor", "", 0, 0],
}

# Translation dictionary
#  ['en', 'de']
id_names = {
    "absence_mode": ["Absence mode", "Abwesenheitssmodus"],
    "circulation_temp": ["Circulation temp.", "Zirkulation Temp."],
    "dhw_heating": ["1x DHW heating", "1x WW aufheizen"],
    "dhw_opmode": ["DHW mode", "WW Modus"],
    "el_consumption": ["Electr. power", "Leistung elektrisch"],
    "fixed_temp_req": ["fixed value temp.", "Festwert Temp."],
    "heating_circ_mode": ["Heating circuit mode", "Heizkreis Modus"],
    "heat_gen_status": ["Heat generator status", "Wärmeerzeuger Status"],
    "heat_water_temp": ["Heating water temp.", "Heizwasser Temp."],
    "heat_water_temp_req": ["Heating water temp. req.", "Heizwasser soll"],
    "main_mode": ["Room climate mode", "Raumklima Modus"],
    "mixed_temp": ["Mixed temp.", "Gemischte Temperatur"],
    "opmode": ["Operating mode", "Betriebsmodus"],
    "out_temp": ["Outside temp.", "Außentemperatur"],
    "party_mode": ["Party mode", "Partymodus"],
    "th_consumption": ["Therm. power", "Leistung thermisch"],
    "water_temp": ["Water temp.", "Warmwasser Temp."],
    "water_temp_req": ["Water temp. req.", "Warmwasser soll"],
    "mode1": ["Auto", "Auto"],
    "mode2": ["Heating", "Heizen"],
    "mode3": ["Standby", "Standby"],
    "mode4": ["Cooling", "Kühlen"],
    "dhwopmode0": ["Automatic comfort", "Automatik Komfort"],
    "dhwopmode1": ["Automatic eco", "Automatik Eco"],
    "dhwopmode2": ["Solar/PV only", "Nur Solar/PV"],
    "dhwopmode3": ["Off", "Aus"],
    "opmode1": ["Forced off", "Störung"],
    "opmode2": ["Defosting", "Abtauen"],
    "opmode3": ["Load defr. puffer", "Abtaupuffer"],
    "opmode4": ["DHW loading", "WW Puffer"],
    "opmode5": ["Storage energy", "Speicherenergie"],
    "opmode6": ["Heating", "Heizen"],
    "opmode7": ["Cooling", "Kühlen"],
    "opmode8": ["Pool heating", "Pool"],
    "opmode9": ["Idle", "Umwälzung"],
    "opmode10": ["Standby", "Standby"],
    "opmode11": ["Screed drying", "Estrichtrockung"],
    "opmode12": ["Frost protection", "Frostschutz"],
    "opmode13": ["Test mode", "Prüfbetrieb"],
    "opmode14": ["Blocking signal", "Sperrsignal"],
    "opmode15": ["Hygiene function", "Hygienefunktion"],
    "opmode16": ["Silent mode", "Silent Modus"],
}

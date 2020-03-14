import csv

from pygal.maps.world import World
from pygal.style import RotateStyle, LightColorizedStyle

from country_codes import get_country_code


filename = 'API_SH.TBS.INCD_DS2_en_csv_v2_824854.csv'

with open(filename) as f:
    reader = csv.reader(f)
    
    for row in range(5): # Salteo 5 filas que no me sirven
        header_row = next(reader)
    
    # Para saber qué columnas tomar:
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    # Me interesan columnas 0 (nombre país)y 62 (año 2018)
    
    #Crear los arrays:
    incidence_dict = {}
    for row in reader:
        try:
            country_name = row[0]
            value = int(float(row[62]))
            
            
        except ValueError:
            print(country_name, 'missing data')
        else:
            incidence_dict[country_name] = value
# ~ print(country_names)

# Crear diccionario para el mapa:
incidence_tuberculosis = {}
for country_name, value in incidence_dict.items():
    code = get_country_code(country_name)
    if code:
        incidence_tuberculosis[code] = value
    else:
        print(country_name)
        
# Dividir en grupos:
incidence_1, incidence_2, incidence_3 = {}, {}, {}
for country_code, value in incidence_tuberculosis.items():
    if value < 50:
        incidence_1[country_code] = value
    elif value < 100:
        incidence_2[country_code] = value
    else:
        incidence_3[country_code] = value

# Creo el mapa:
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle) # Le agrego color
wm = World(style=wm_style)
wm.title = 'Incidence of Tuberculosis in 2018, by Country'
wm.add('0-50', incidence_1)
wm.add('50-100', incidence_2)
wm.add('+100', incidence_3)

wm.render_to_file('world_tuberculosis.svg')
    

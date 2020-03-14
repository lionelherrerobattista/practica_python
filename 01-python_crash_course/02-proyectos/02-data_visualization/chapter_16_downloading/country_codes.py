from pygal.maps.world import COUNTRIES

fixed_countries = { 
    'AS':'American Samoa',
    'AG': 'Antigua and Barbuda',
    'AW' : 'Aruba',
    'BS' : 'Bahamas, The',
    'BB' : 'Barbados',  
    'BM' : 'Bermuda',
    'BO': 'Bolivia',
    'KY': 'Cayman Islands',
    'KM': 'Comoros',
    'CD': 'Congo, Dem. Rep.',
    'CG': 'Congo, Rep.',
    'CW': 'Curacao',
    'DM': 'Dominica',
    'EG': 'Egypt, Arab Rep.',
    'FO': 'Faeroe Islands',
    'FJ': 'Fiji',
    'PF': 'French Polynesia',
    'GM': 'Gambia, The',
    'GI': 'Gibraltar',
    'GD': 'Grenada',
    'HK': 'Hong Kong SAR, China',
    'IR': 'Iran, Islamic Rep.',
    'IM': 'Isle of Man',
    'KI': 'Kiribati',
    'KP': 'Korea, Dem. Rep.',
    'KR': 'Korea, Rep.',
    'KG': 'Kyrgyz Republic',
    'LA': 'Lao PDR',
    'LY': 'Libya',
    'MO': 'Macao SAR, China',
    'MK': 'Macedonia, FYR',
    'MD': 'Moldova',
    'SK': 'Slovak Republic',
    'TZ': 'Tanzania',
    'TG': 'Tonga',
    'VE': 'Venezuela, RB',
    'VN': 'Vietnam',
    'YE': 'Yemen, Rep.'
    }

def get_country_code(country_name):
    """Devuelve el código Pygal de dos dígitos para el país indicado"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code.lower()
    # Nombre distinto al diccionario:
    for code, name in fixed_countries.items():
        if name == country_name:
            return code.lower()
    # Si no se encontro al país
    return None
    


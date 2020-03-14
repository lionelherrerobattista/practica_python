import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter

# Hacer una llamada a la API y guardar la respuesta
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code: ", r.status_code)

# Procesar la información de cada submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Hacer una llamada a la API por cada submission
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
        str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()
    
    # Crear el diccionario para cada submission:
    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0) # 0 si no hay comentarios
    }
    
    # Agregar al diccionario de submissions:
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

names, plot_dicts = [], []

for submission_dict in submission_dicts:
    name = submission_dict['title']
    
    names.append(name)
    
    submission_dict = {
        'value':submission_dict['comments'],
        'xlink': submission_dict['link'],
    }
    
    plot_dicts.append(submission_dict)

# Hacer visualización:
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style) # Pasar configuración y estilo
chart.title = 'Most commented submissions on Hacker News'
chart.x_labels = names

chart.add('', plot_dicts)

file_name = 'hn_submissions_bar.svg'
chart.render_to_file(file_name)

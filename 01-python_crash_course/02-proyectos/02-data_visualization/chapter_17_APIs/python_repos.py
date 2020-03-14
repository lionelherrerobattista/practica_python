import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Hacer un llamada a la API y guardar la respuesta:
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url) # Guardo la request
print("Status code:", r.status_code) # Código 200, consulta exitosa

# Guardar la respuesta de la API en una variable (viene en JSON):
response_dict = r.json()
print("Total repositories: ", response_dict['total_count'])

# Explorar la información de los repositorios:
repo_dicts = response_dict['items'] # En items están todos los repositorios
print("Repositories returned:", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    #Buscar la descripción si está disponible
    description = repo_dict['description']
    if not description:
        description = "No description provided."
    
    # Generar el dict para el tooltip:
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url'], # Agregar un link    
        }
        
    plot_dicts.append(plot_dict)
    
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
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')


# Analizar el primer repositorio:
# ~ repo_dict = repo_dicts[0]

# ~ print("\nKeys:", len(repo_dict)) # Todas las claves de 1 repositorio
# ~ for key in sorted(repo_dict.keys()):
    # ~ print(key)
    
# ~ print("\nSelected information about first repository:")
# ~ print('Name: ', repo_dict['name'])
# ~ print('Owner: ', repo_dict['owner']['login'])
# ~ print('Stars: ', repo_dict['stargazers_count'])
# ~ print('Repository: ', repo_dict['html_url'])
# ~ print('Created: ', repo_dict['created_at'])
# ~ print('Updated: ', repo_dict['updated_at'])
# ~ print('Description: ', repo_dict['description'])



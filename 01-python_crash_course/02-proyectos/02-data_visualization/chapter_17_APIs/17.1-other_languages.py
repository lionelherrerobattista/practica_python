import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

languages = [
    "JavaScript",
    "Ruby",
    "C",
    "Java",
    "Perl",
    "Haskell",
    "Go"
]

for language in languages:
    # Hacer un llamada a la API y guardar la respuesta:
    url = ('https://api.github.com/search/repositories?q=language:' +
                language + '&sort=stars')
    r = requests.get(url) # Guardo la request
    print("\n" + language)
    print("\nStatus code:", r.status_code) # Código 200, consulta exitosa

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
    chart.title = 'Most-Starred ' + language + ' Projects on GitHub'
    chart.x_labels = names

    chart.add('', plot_dicts)
    
    file_name = language + '_repos.svg'
    chart.render_to_file(file_name)





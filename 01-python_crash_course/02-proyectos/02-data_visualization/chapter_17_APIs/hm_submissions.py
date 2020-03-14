import requests

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

# Mostrar la información de cada submission:
for submission_dict in submission_dicts:
    print("\nTitle: ", submission_dict['title'])
    print("Discussion link: ", submission_dict['link'])
    print("Comments: ", submission_dict['comments'])

from pygal.maps.world import World

wm = World() # Crea la instancia del mapa
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us']) # Agrega las zonas coloreadas
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg') # Crea el archio .svg con el mapa

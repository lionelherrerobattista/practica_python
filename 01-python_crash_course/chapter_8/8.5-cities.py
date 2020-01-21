def describe_city(country, name='Reykjavik'):
    print(name.title() + " is in " + country.title())
    
describe_city('Iceland')
describe_city('France','Paris')
describe_city(country='Russia', name='Moscow')

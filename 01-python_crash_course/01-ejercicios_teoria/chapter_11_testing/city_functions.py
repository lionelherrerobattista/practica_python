def get_formatted_city(city_name, country_name, population=''):
    """Generates a formatted city, country"""
    if population:
        formatted_city = city_name + ", " + country_name + " - population " + str(population)
    else:
        formatted_city = city_name + ", " + country_name
    return formatted_city.title()

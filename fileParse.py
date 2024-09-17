countryFilename = "country_data.txt"
countries = {}
with open(countryFilename) as countryFile:
    for row in countryFile:
        field = row.rstrip().split(';')
        country_code,country_name,capital,total_area,population,currency_code,currency_name,lang_name = field
        countries[country_name] = {
            'code': country_code,
            'capital': capital,
            'area': total_area,
            'population': population,
            'currency': currency_name,
            'currency_code': currency_code,
            'language': lang_name
        }

print(countries["France"]['population'])
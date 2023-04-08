from city_function import get_city_country

def test_city_country():
    formatted_city_country = get_city_country('santiago', 'chile')
    assert formatted_city_country == 'Santiago, Chile'

def test_city_country_population():
    formatted_city_country = get_city_country('santiago', 'chile', population=5000000)
    assert formatted_city_country == 'Santiago, Chile - population 5000000'
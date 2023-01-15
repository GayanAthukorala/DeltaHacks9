import requests

def RemoveBigCompanies(companies):
    companies = [['yes', 2], ['A&W', 3]]
    response = requests.get('http://127.0.0.1:8000/DeltaHacks9Big')
    list_of_big_business = response.json()
    for business in list_of_big_business:
        companies = [i for i in companies if i[0] != business['name']]
    print(companies)


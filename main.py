import requests

url = "https://weerlive.nl/api/weerlive_api_v2.php?key=demo&locatie=Amsterdam"
r = requests.get(url, auth=("", ""))  # geen login vereist voor demo data

if r.status_code != 200:
    print("Geen verbinding met de website " + url + ".")

data_dict = r.json()


for item in data_dict["liveweer"]:
    if item['wrschklr'] != 'groen':
        print('Geen code groen vandaag! PAS OP!')
    else:
        print('Vandaag is gewoon code groen, geen zorgen!')


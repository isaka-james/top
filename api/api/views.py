""" api views """

from flask import make_response, request
import requests as req
from api import app
from api.utils import *

@app.route('/')
def generate_svg():
    # Extract query parameters
    name = request.args.get('name', 'Unknown Username')
    country = request.args.get('country', 'Unknown Country')



    # Define the countries
    countries = ['afghanistan', 'albania', 'algeria', 'angola', 'argentina', 'armenia', 'australia', 'austria', 'azerbaijan', 'bahrain', 'bangladesh', 'belarus', 'belgium', 'benin', 'bolivia', 'botswana', 'brazil', 'bulgaria', 'burkina_faso', 'burundi', 'cambodia', 'cameroon', 'canada', 'chad', 'chile', 'china', 'colombia', 'congo_brazzaville', 'congo_kinshasa', 'croatia', 'cuba', 'cyprus', 'czech_republic', 'denmark', 'dominican_republic', 'ecuador', 'egypt', 'el_salvador', 'estonia', 'ethiopia', 'finland', 'france', 'gabon', 'germany', 'ghana', 'greece', 'guatemala', 'guinea', 'haiti', 'honduras', 'hong_kong', 'hungary', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'israel', 'italy', 'ivory_coast', 'japan', 'jordan', 'kazakhstan', 'kenya', 'kyrgyzstan', 'laos', 'latvia', 'lebanon', 'libya', 'lithuania', 'luxembourg', 'macau', 'macedonia', 'malawi', 'malaysia', 'mali', 'malta', 'mauritania', 'mexico', 'moldova', 'morocco', 'mozambique', 'myanmar', 'nepal', 'netherlands', 'new_zealand', 'nicaragua', 'niger', 'nigeria', 'norway', 'oman', 'pakistan', 'palestine', 'panama', 'papua_new_guinea', 'paraguay', 'peru', 'philippines', 'poland', 'portugal', 'qatar', 'romania', 'russia', 'rwanda', 'saudi_arabia', 'senegal', 'serbia', 'sierra_leone', 'singapore', 'slovakia', 'slovenia', 'somalia', 'south_africa', 'republic_of_korea', 'south_sudan', 'spain', 'sri_lanka', 'sudan', 'sweden', 'switzerland', 'syria', 'taiwan', 'tajikistan', 'tanzania', 'thailand', 'the_bahamas', 'togo', 'tunisia', 'turkey', 'turkmenistan', 'uae', 'uganda', 'uk', 'ukraine', 'united_states', 'uruguay', 'uzbekistan', 'venezuela', 'vietnam', 'worldwide', 'yemen', 'zambia', 'zimbabwe']

    long_names = {
      'afghanistan': 'Afghanistan',
      'albania': 'Albania',
      'algeria': 'Algeria',
      'angola': 'Angola',
      'argentina': 'Argentina',
      'armenia': 'Armenia',
      'australia': 'Australia',
      'austria': 'Austria',
      'azerbaijan': 'Azerbaijan',
      'bahrain': 'Bahrain',
      'bangladesh': 'Bangladesh',
      'belarus': 'Belarus',
      'belgium': 'Belgium',
      'benin': 'Benin',
      'bolivia': 'Bolivia',
      'botswana': 'Botswana',
      'brazil': 'Brazil',
      'bulgaria': 'Bulgaria',
      'burkina_faso': 'Burkina Faso',
      'burundi': 'Burundi',
      'cambodia': 'Cambodia',
      'cameroon': 'Cameroon',
      'canada': 'Canada',
      'chad': 'Chad',
      'chile': 'Chile',
      'china': 'China',
      'colombia': 'Colombia',
      'congo_brazzaville': 'Congo (Brazzaville)',
      'congo_kinshasa': 'Congo (Kinshasa)',
      'croatia': 'Croatia',
      'cuba': 'Cuba',
      'cyprus': 'Cyprus',
      'czech_republic': 'Czech Republic',
      'denmark': 'Denmark',
      'dominican_republic': 'Dominican Republic',
      'ecuador': 'Ecuador',
      'egypt': 'Egypt',
      'el_salvador': 'El Salvador',
      'estonia': 'Estonia',
      'ethiopia': 'Ethiopia',
      'finland': 'Finland',
      'france': 'France',
      'gabon': 'Gabon',
      'germany': 'Germany',
      'ghana': 'Ghana',
      'greece': 'Greece',
      'guatemala': 'Guatemala',
      'guinea': 'Guinea',
      'haiti': 'Haiti',
      'honduras': 'Honduras',
      'hong_kong': 'Hong Kong',
      'hungary': 'Hungary',
      'india': 'India',
      'indonesia': 'Indonesia',
      'iran': 'Iran',
      'iraq': 'Iraq',
      'ireland': 'Ireland',
      'israel': 'Israel',
      'italy': 'Italy',
      'ivory_coast': 'Ivory Coast',
      'japan': 'Japan',
      'jordan': 'Jordan',
      'kazakhstan': 'Kazakhstan',
      'kenya': 'Kenya',
      'kyrgyzstan': 'Kyrgyzstan',
      'laos': 'Laos',
      'latvia': 'Latvia',
      'lebanon': 'Lebanon',
      'libya': 'Libya',
      'lithuania': 'Lithuania',
      'luxembourg': 'Luxembourg',
      'macau': 'Macau',
      'macedonia': 'Macedonia',
      'malawi': 'Malawi',
      'malaysia': 'Malaysia',
      'mali': 'Mali',
      'malta': 'Malta',
      'mauritania': 'Mauritania',
      'mexico': 'Mexico',
      'moldova': 'Moldova',
      'morocco': 'Morocco',
      'mozambique': 'Mozambique',
      'myanmar': 'Myanmar',
      'nepal': 'Nepal',
      'netherlands': 'Netherlands',
      'new_zealand': 'New Zealand',
      'nicaragua': 'Nicaragua',
      'niger': 'Niger',
      'nigeria': 'Nigeria',
      'norway': 'Norway',
      'oman': 'Oman',
      'pakistan': 'Pakistan',
      'palestine': 'Palestine',
      'panama': 'Panama',
      'papua_new_guinea': 'Papua New Guinea',
      'paraguay': 'Paraguay',
      'peru': 'Peru',
      'philippines': 'Philippines',
      'poland': 'Poland',
      'portugal': 'Portugal',
      'qatar': 'Qatar',
      'romania': 'Romania',
      'russia': 'Russia',
      'rwanda': 'Rwanda',
      'saudi_arabia': 'Saudi Arabia',
      'senegal': 'Senegal',
      'serbia': 'Serbia',
      'sierra_leone': 'Sierra Leone',
      'singapore': 'Singapore',
      'slovakia': 'Slovakia',
      'slovenia': 'Slovenia',
      'somalia': 'Somalia',
      'south_africa': 'South Africa',
      'republic_of_korea': 'Republic of Korea',
      'south_sudan': 'South Sudan',
      'spain': 'Spain',
      'sri_lanka': 'Sri Lanka',
      'sudan': 'Sudan',
      'sweden': 'Sweden',
      'switzerland': 'Switzerland',
      'syria': 'Syria',
      'taiwan': 'Taiwan',
      'tajikistan': 'Tajikistan',
      'tanzania': 'Tanzania',
      'thailand': 'Thailand',
      'the_bahamas': 'The Bahamas',
      'togo': 'Togo',
      'tunisia': 'Tunisia',
      'turkey': 'Turkey',
      'turkmenistan': 'Turkmenistan',
      'uae': 'UAE',
      'uganda': 'Uganda',
      'uk': 'UK',
      'ukraine': 'Ukraine',
      'united_states': 'United States',
      'uruguay': 'Uruguay',
      'uzbekistan': 'Uzbekistan',
      'venezuela': 'Venezuela',
      'vietnam': 'Vietnam',
      'worldwide': 'Worldwide',
      'yemen': 'Yemen',
      'zambia': 'Zambia',
      'zimbabwe': 'Zimbabwe'
    }

    if country not in countries:
        # non-existing country!
        return wrong_inputs()

    if name:
      pass
    else:
      # username was not passed!
      return wrong_inputs()


    # Fetch the json from the server
    response = req.get(f"https://committers.top/rank_only/{country}.json")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the JSON data from the response
        result_server = response.json()
        
        # Extract the "user" list from the JSON data
        users = result_server.get("user", [])
        
        
    else:
        return wrong_inputs()

    
        
    # Find the index of "username" in the list
    user_index = users.index(f"{name}") if f"{name}" in users else -1
    
    # If "username" is found
    if user_index != -1:
        position=user_index+1
    else:
        return wrong_inputs()


    the_rank, the_percent, the_delay = get_individual(position)
    

    svg_content = get_full(the_rank,the_percent, the_delay, name, long_names[country], position)

    return show_results(svg_content)


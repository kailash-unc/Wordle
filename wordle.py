import requests
import json
import datetime


def get_word(i):

    url = 'https://www.nytimes.com/games-assets/v2/wordle.62da5783b1ae1a6be97242ffc54340ced8bf0e98.js'
    js = requests.get(url=url).text
    
    output = json.loads(js.split(',it=')[1].split(';var lt=')[0])

    known = [output.index('happy'), datetime.datetime.strptime('Nov 27 2022', '%b %d %Y')]
    
    current_index = known[0] + (datetime.datetime.now() - known[1]).days
    
    print('The wordle answer is "' + output[current_index + int(i)] + '"')

get_word(i = input())
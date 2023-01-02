import requests
import json
import datetime


def get_word(i):

    url = 'https://www.nytimes.com/games-assets/v2/wordle.62da5783b1ae1a6be97242ffc54340ced8bf0e98.js'
    js = requests.get(url=url).text
    
    output = json.loads(js.split(',it=')[1].split(';var lt=')[0])
    print(type(output))
    known = [output.index('happy'), datetime.datetime.strptime('Nov 27 2022', '%b %d %Y')]
    
    current_index = known[0] + (datetime.datetime.now() - known[1]).days
    
    print('\nThe wordle answer is "' + output[current_index + int(i)] + '"\n')

while(True):
    try:
        print('\nPlease enter a valid integer corresponding to a day')
        get_word(i = input('Ex: [1 = Tommorow, 0 = Today, -1 = Yesterday] \n\nEnter Number: '))
        break
    except:
        print('\n Error: Invalid integer')
       

# Wordle Solver
An application that scrapes The New York Times' Wordle Game js files to find the daily answer.

<img width="674" alt="Screen Shot 2022-11-27 at 7 03 00 PM" src="https://user-images.githubusercontent.com/69515228/204167044-0de489e9-8352-48f2-9453-708c3ae256d1.png">

## Usage

Enter the following into your command line

```
python wordle.py
```
Arguments: 

input() is a command line 'integer' input of the day's answer you are looking for.

1 = Tommorow

0 = Today

-1 = Yesterday

Input can be any [-14725+ to 130+] ('+' indicates expansion as new words are added to the bank)

## How

The program grabs the main javascript file url and, using the requests module, recieves a large string of the file data.

Then, the list string is accquired using split functions and json.loads is used to turn it into a list object.

Then using the datetime module cleverly, we are able to calculate a given day's wordle answer through simple arithmetic based on a known day's wordle word.


## Future Plans
  
The plan is to expand this project to then inject the wordle answer automatically into the wordle game to correctly solve the puzzle automatically.


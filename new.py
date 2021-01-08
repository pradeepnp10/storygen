import  random

input_name = input("What's your Name ? ")
input_age = int(input("what's your Age ? "))

places = ["Australia","London","USA","Chennai","Banglore"]
jobs = ["Software Developer","Data analysis","Doctor","Actor"]
earnings  = [12345566,783475836,348975362,35783546,7835404563]

ran_places = random.choice(places)
ran_jobs = random.choice(jobs)
ran_earnings = random.choice(earnings)


print(f"once upon a  Time there was man named  {input_name} he is {input_age} year 's old and he lives in {ran_places} and he working as a {ran_jobs} and his earning is {ran_earnings} ! ")

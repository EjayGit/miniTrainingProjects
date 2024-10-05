import random, os
from pathlib import Path

# Delete all .txt files in directory prior to writing new files.
os.chdir('quiz proj')
for file in os.listdir():
    if file.startswith('question') or file.startswith('answer'):
        os.unlink(file)


#   - TODO 1.1 - Ask from user the number of questions and the number of students in class
questionNum = int(input("How many questions per paper should there be? "))
studNum = int(input("Enter the number of students taking the test: "))

# 	- TODO 2.1 - Create empty countries dictionary
countries = {}

    #	- TODO 2.2 - Open country_data.txt file
with open('country_data.txt','r') as file:
    #	- TODO 2.3 - Parse data in countries dictionary
    for country in file:
        data = country.strip().split(';')
        country_name,capital = data[1], data[2]
        countries[country_name] = {
            'capital': capital
        }

for student in range(studNum):
    #	- TODO 3.1 - Generate questions files based on number of students
    with open(f'questions_{student+1}.txt', 'w') as qfile:

        #	- TODO 3.2 - Write header for the quiz in questions text files
        qfile.write(f'Name: \n\nDate: \n\n{" " * 20}Country Capitals Quiz Number {student+1}\n\n')
        
        #	- TODO 3.3 - Shuffle the order of countries based on random module
        countryList = list(countries.keys())
        random.shuffle(countryList)

        #	- TODO 3.4 - Loop through number of questions and make a question for each
        for questionNumber in range(questionNum):

            #	- TODO 4.1 - Get correct and wrong answers
            correctAns = countries[countryList[questionNum]]
            wrongAns = list(countries.values())
            del wrongAns[wrongAns.index(correctAns)]

	        #   - TODO 4.2 - Generate answer options
            ansList = list(random.sample(wrongAns,3))
            ansList.append(correctAns)

	        #   - TODO 4.3 - Randomize the answer options
            random.shuffle(ansList)
            
            #	- TODO 5.1 - Write questions and answer options to questions text file
            qfile.write(f"Question {questionNumber+1}: What is the capital of {countryList[questionNum]}?\n\n")
            for i in range(4):
                qfile.write(f"     {'ABCD'[i]}. {ansList[i]['capital']}\n")
                qfile.write('\n\n')
            
            #    - TODO 5.2 - Write correct answers to answers text file
            with open(f'answers{student+1}', 'w') as afile:
                afile.write(f"{questionNumber+1}.{'ABCD'[ansList.index(correctAns)]}\n")
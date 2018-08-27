#!/usr/bin/env python3
# coding=utf-8
# randomQuizGenerator.py - Creat quizzes with questions and answers in random
# order, along with the answer key.

import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 
            'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 
            'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 
            'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
            'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
    #TODO: Create the quiz and answer key files
    quizFile = open('capquiz%s.txt' % (quizNum+1), 'w')
    ansFile = open('capanswer%s.txt' % (quizNum+1), 'w')

    #TODO: Write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20) + 'State Capitals Quiz (From %s)' % (quizNum+1))
    quizFile.write('\n\n')

    #TODO: Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)
    #TODO: Loop through all 50 stattes, makeing a question for each
    for quesNum in range(50):
        # Get right and wrong answers
        correctAnswer = capitals[states[quesNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer, 3)
        answerOptions = [correctAnswer]+wrongAnswer
        random.shuffle(answerOptions)

        #TODO: Write the questions and answer optons to the quiz file
        quizFile.write('%s. What is the capital of %s?\n' % (quesNum+1, states[quesNum]))
        for i in range(4):
            quizFile.write('  %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')
        #TODO: Write the answer key to a file
        ansFile.write('%s. %s\n' %(quesNum+1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    ansFile.close()
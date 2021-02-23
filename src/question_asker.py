import os
import time
import random

#
questions = ["Tell us about yourself.",
            "Why do you want to work here?",
            "What interests you about this role?",
            "What are your greatest strengths?",
            "What are your greatest weaknesses?",
            "What experience do you have with Cloud IT?",
            "What experience do you have with containerized application development?",
            "What do you know about financial modelling concepts?",
            "Do you have any experience with linear programming techniques for decision support?",
            "What experience do you have with Forestry growth and yield modelling?",
            "Tell us about the role at your current job.",
            "Tell us about your time at UD4H",
            "Tell us about your time at the SUPR",
            "Do you have any questions for us?"]

# ask if they'd like to start
answer = input("Would you like to start the interview?")

# start while loop
while answer in ['Yes', 'yes', 'y']:
    # get a random list position
    random_index = random.randint(1, len(questions))

    # print the question
    print(questions[random_index-1])

    # remove the question from the pool of questions
    questions.pop(random_index-1)

    # ask if they'd like to continue
    answer = input("Would you like to continue?")

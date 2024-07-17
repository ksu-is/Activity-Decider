print("Welcome to the Activity Decider! This program will suggest a personalized adventure for you based on your answers.")
print("Please answer the following series of questions to get your result.")

questions = ("How many people are participating?: ",
             "How long do you wish for this activity to last?: ",
             "Do you wish to be indoors or outdoors?: ",
             "What is the budget range?: ")

options = (("A. One", "B. Two", "C. Three", "D. Four or more" ),
           ("A. 30 minutes", "B. 1-2 hour(s)", "C. Half of the day", "D. The whole day"),
           ("A. Either", "B. Indoors", "C. Outdoors"),
           ("A. $0 (Free)", "B. $1-$15", "C. $15-$30", "D. $30-$50", "E. $50+"))

indoors = ['Read a book','Workout','Bake or cook something','Karaoke','Throw a Party','Movie Marathon']
outdoors = ['Go out for a walk','Go to the movie theater','Go to a spa','Play a sport','Shopping']

while True:
    question_1 = input("How long do you wish for this activity to last?:\n(A) 30 minutes\n(B) 1-2 hour(s)\n(C) Half of the day\n(D) The whole day ")
    if question_1 == "A":
        del indoors[-1]
        del indoors[-1]
        del outdoors [1]
        break
    elif question_1 == "B":
        del indoors [-1]
        del indoors [-1]
        break
    elif question_1 == "C":
        del indoors[0]
        del indoors [0]
        del indoors [0]
        del indoors [0]
        del outdoors [0]
        break
    elif question_1 == "D":
        del indoors[0]
        del indoors [0]
        del indoors [0]
        del indoors [0]
        del outdoors [0]
        del outdoors [0]
        del outdoors [0]
        break
    else:
        print('[PLEASE PUT A VALID ANSWER]')

#indoors = ['Read a book','Workout','Bake or cook something','Karaoke','Throw a Party','Movie Marathon']
#outdoors = ['Go out for a walk','Go to the movie theater','Go to a spa','Play a sport','Shopping']

while True:
    question_2 = input("How many people are participating?:\n(A) One\n(B) Two\n(C) Three\n(D) Four or more ")
    if question_2 == "A":
        del indoors [-2]
        del outdoors [-2]
        break
    elif question_2 == "B":
        del indoors [0]
        del indoors [-2]
        break
    elif question_2 == "C":
        del indoors [0]
        break
    elif question_2 == "D":
        del indoors [0]
        break
    else:
        print('[PLEASE PUT A VALID ANSWER]')

#indoors = ['Read a book','Workout','Bake or cook something','Karaoke','Throw a Party','Movie Marathon']
#outdoors = ['Go out for a walk','Go to the movie theater','Go to a spa','Play a sport','Shopping']

while True:
    question_3 = input("What is the budget range?:\n(A) $0(Free)\n(B) $1-$15\n(C) $15-$30\n(D) $30-$50\n(E.) $50+ ")
    if question_3 == "A":
        del indoors [-2]
        del outdoors [1]
        del outdoors [1]
        del outdoors [-1]
        break
    elif question_3 == "B":
        del indoors [-2]
        del outdoors [0]
        del outdoors [1]
        break
    elif question_3 == "C":
        del indoors [0]
        del indoors [0]
        del outdoors [0]
        break
    elif question_3 == "D":
        del indoors [0]
        del indoors [0]
        del outdoors [0]
        break
    else:
        print('[PLEASE PUT A VALID ANSWER]')

        
while True:
    question_4 = input("Do you wish to be indoors or outdoors?:\n(A) Either\n(B) Indoors\n(C) Outdoors ")
    if question_4 == "B":
        outdoors.clear()
        break
    elif question_4 == "C":
        indoors.clear()
        break
    elif question_4 == "A":
        break
    else:
        print('[PLEASE PUT A VALID ANSWER]')

final = indoors + outdoors
print('Here are the option(s) for you:')

print(final)

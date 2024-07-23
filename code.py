print("----------------------------------------------------------------------------------------------------------------------------")
print("Welcome to the Activity Decider! This program will suggest a personalized adventure for you based on your answers.")
print("Please answer the following series of questions by using A, B, C, or D to successfully get your result.")
print("----------------------------------------------------------------------------------------------------------------------------")

questions = ("How many people are participating?: ",
             "How long do you wish for this activity to last?: ",
             "Do you wish to be indoors or outdoors?: ",
             "What is the budget range?: ")

options = (("A. One", "B. Two", "C. Three", "D. Four or more" ),
           ("A. 30 minutes", "B. 1-2 hour(s)", "C. Half of the day", "D. The whole day"),
           ("A. Either", "B. Indoors", "C. Outdoors"),
           ("A. $0 (Free)", "B. $1-$15", "C. $15-$30", "D. $30-$50"))

indoors = ['Read a book','Workout','Bake or cook something','Karaoke','Throw a Party','Movie Marathon']
outdoors = ['Go out for a walk','Go to the movie theater','Go to a spa','Play a sport','Shopping','Hiking']

q1_elimination_indoors = []
q1_elimination_outdoors = []

while True:
    question_1 = input("How long do you wish for this activity to last?:\n(A) 30 minutes\n(B) 1-2 hour(s)\n(C) Half of the day\n(D) The whole day ")
    if question_1 == "A":
        q1_elimination_indoors.append('Movie Marathon')
        q1_elimination_indoors.append('Throw a Party')
        q1_elimination_outdoors.append('Go to the movie theater')
        q1_elimination_outdoors.append('Hiking')
        break
    elif question_1 == "B":
        q1_elimination_indoors.append('Movie Marathon')
        q1_elimination_indoors.append('Throw a Party')
        break
    elif question_1 == "C":
        q1_elimination_indoors.append('Workout')
        q1_elimination_indoors.append('Bake or cook something')
        q1_elimination_indoors.append('Karaoke')
        q1_elimination_outdoors.append('Go out for a walk')
        break
    elif question_1 == "D":
        q1_elimination_indoors.append('Workout')
        q1_elimination_indoors.append('Bake or cook something')
        q1_elimination_indoors.append('Karaoke')
        q1_elimination_outdoors.append('Go out for a walk')
        q1_elimination_outdoors.append('Go to the movie theater')
        q1_elimination_outdoors.append('Go to a spa')
        break
    else:
        print("----------------------------------------------------------------------------------------------------------------------------")
        print('[PLEASE PUT A VALID ANSWER]')
        print("----------------------------------------------------------------------------------------------------------------------------")

#indoors = ['Read a book','Workout','Bake or cook something','Karaoke','Throw a Party','Movie Marathon']
#outdoors = ['Go out for a walk','Go to the movie theater','Go to a spa','Play a sport','Shopping','Hiking']

q2_elimination_indoors = []
q2_elimination_outdoors = []

while True:
    print("----------------------------------------------------------------------------------------------------------------------------")
    question_2 = input("How many people are participating?:\n(A) One\n(B) Two\n(C) Three\n(D) Four or more ")
    if question_2 == "A":
        q2_elimination_indoors.append('Throw a Party')
        q2_elimination_outdoors.append('Play a sport')
        break
    elif question_2 == "B":
        q2_elimination_indoors.append('Read a book')
        q2_elimination_outdoors.append('Throw a party')
        break
    elif question_2 == "C":
        q2_elimination_indoors.append('Read a book')
        break
    elif question_2 == "D":
        q2_elimination_indoors.append('Read a book')
        break
    else:
        print("----------------------------------------------------------------------------------------------------------------------------")
        print('[PLEASE PUT A VALID ANSWER]')

#indoors = ['Read a book','Workout','Bake or cook something','Karaoke','Throw a Party','Movie Marathon']
#outdoors = ['Go out for a walk','Go to the movie theater','Go to a spa','Play a sport','Shopping','Hiking']

q3_elimination_indoors = []
q3_elimination_outdoors = []

while True:
    print("----------------------------------------------------------------------------------------------------------------------------")
    question_3 = input("What is the budget range?:\n(A) $0(Free)\n(B) $1-$15\n(C) $15-$30\n(D) $30-$50 ")
    if question_3 == "A":
        q3_elimination_indoors.append('Throw a Party')
        q3_elimination_outdoors.append('Go to the movie theater')
        q3_elimination_outdoors.append('Go to a spa')
        q3_elimination_outdoors.append('Shopping')
        break
    elif question_3 == "B":
        q3_elimination_indoors.append('Throw a Party')
        q3_elimination_outdoors.append('Go out for a walk')
        q3_elimination_outdoors.append('Go to a spa')
        break
    elif question_3 == "C":
        q3_elimination_indoors.append('Read a book')
        q3_elimination_indoors.append('Workout')
        q3_elimination_outdoors.append('Go out for a walk')
        break
    elif question_3 == "D":
        q3_elimination_indoors.append('Read a book')
        q3_elimination_indoors.append('Workout')
        q3_elimination_outdoors.append('Go out for a walk')
        break
    else:
        print("----------------------------------------------------------------------------------------------------------------------------")
        print('[PLEASE PUT A VALID ANSWER]')

        
indoors_total_e = (q1_elimination_indoors + q2_elimination_indoors + q3_elimination_indoors)
indoors_minus = set(indoors_total_e)
indoors_set = set(indoors)
indoors_final = indoors_set - indoors_minus


outdoors_total_e = (q1_elimination_outdoors + q2_elimination_outdoors + q3_elimination_outdoors)
outdoors_minus = set(outdoors_total_e)
outdoors_set = set(outdoors)
outdoors_final = outdoors_set - outdoors_minus

either_total_e = (q1_elimination_indoors + q2_elimination_indoors + q3_elimination_indoors + q1_elimination_outdoors + q2_elimination_outdoors + q3_elimination_outdoors)
either_minus = set(either_total_e)
either_set = set(indoors + outdoors)
either_final = either_set - either_minus

while True:
    print("----------------------------------------------------------------------------------------------------------------------------")
    question_4 = input("Do you wish to be indoors or outdoors?:\n(A) Either\n(B) Indoors\n(C) Outdoors ")
    if question_4 == "B":
        outdoors_final.clear()
        break
    elif question_4 == "C":
        indoors_final.clear()
        break
    elif question_4 == "A":
        either_final
        break
    else:
        print("----------------------------------------------------------------------------------------------------------------------------")
        print('[PLEASE PUT A VALID ANSWER]')

final = indoors_final.union(outdoors_final)
final_either = either_final
print("----------------------------------------------------------------------------------------------------------------------------")
print('Thank you for answering! Here are your option(s):')
if question_4 == "A":
    print(final_either)
else:
    print(final)

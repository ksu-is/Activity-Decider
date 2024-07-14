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

# decide on tally or list type of answer??

question_1 = input("How many people are participating?:\n(A) One\n(B) Two\n(C) Three\n(D) Four or more ")
question_2 = input("How long do you wish for this activity to last?:\n(A) 30 minutes\n(B) 1-2 hour(s)\n(C) Half of the day\n(D) The whole day ")
question_3 = input("Do you wish to be indoors or outdoors?:\n(A) Either\n(B) Indoors\n(C) Outdoors ")
question_4 = input("What is the budget range?:\n(A) $0(Free)\n(B) $1-$15\n(C) $15-$30\n(D) $30-$50\n(E.) $50+ ")

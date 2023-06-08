from string import ascii_lowercase
import random 


NUM_QUESTIONS = 5
QUESTIONS = {

"in citizen kane, what is rosebud?":
['a sled', 'a horse', 'a secret club', 'a fast-casual dining experience'],
"who framed roger rabbit?": 
['judge doom', 'mickey mouse', 'that one cartoon baddie with with red hair', 'bob hoskins'],
"the movie 'the king and i' took place in which fictional country?":
 ['siam', 'xin zhao', 'tai shein', 'flushing'],
"call yourself a scorcese fan? name 5 of his movies lol":
 ['a', 'b', 'c'],
  "When was the first known use of the word 'quiz'":
  ["1781", "1771", "1871", "1881"],
  "Which built-in function can get information from the user":
  ["input", "get", "print", "write"],
  "Which keyword do you use to loop over a given list of elements":
  ["for", "while", "each", "loop"],
  "What's the purpose of the built-in zip() function": [
    "To iterate over two or more sequences at the same time",
    "To combine several strings into one",
    "To compress several files into one archive",
    "To get information from the user",
  ],
}


def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample((list(questions.items())), k=num_questions)

def get_answer(question, alternatives):
    print(f"{question}")
    labeled_alternatives = dict((zip(ascii_lowercase, alternatives)))

    for label, alternative in labeled_alternatives.items():
        print(f" {label}) {alternative}")

    while (answer_label := input("\nChoice: ")) not in labeled_alternatives:
        print("""
                don't be silly now. 
                please type a, b, c, or d.
                and remember, 
                    there is always 
                    room in hell 
                    for the Flippant.
              """)
        
    return labeled_alternatives[answer_label]

def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("""
            🌱 🌱 🌱 🌱 🌱
              🌱 🌱 🌱 🌱 🌱
               🌱 🌱 🌱 🌱 🌱
          
                  so good !  🫶
                 
                🌱 🌱 🌱 🌱 🌱
               🌱 🌱 🌱 🌱 🌱
              🌱 🌱 🌱 🌱 🌱
            """)
        return 1
    else:
        print(f"The answer is {correct_answer!r} la. Not {answer!r}")
        return 0
    

def run_quiz():
    questions = prepare_questions(QUESTIONS, num_questions=NUM_QUESTIONS)

    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"Question {num}: ")
        num_correct += ask_question(question, alternatives)
    
    print(f"you got {num_correct} / {num} questions correct. are you happy with yourself? ")

run_quiz()
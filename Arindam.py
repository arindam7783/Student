# Quiz Application

# Questions and answers
quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"],
        "answer": 3
    },
    {
        "question": "Which programming language is known as the 'language of AI'?",
        "options": ["1. Python", "2. Java", "3. C++", "4. Ruby"],
        "answer": 1
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["1. 0", "2. 1", "3. 2", "4. 3"],
        "answer": 3
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["1. Earth", "2. Mars", "3. Venus", "4. Jupiter"],
        "answer": 2
    }
]

def run_quiz():
    score = 0
    print("\n*** Welcome to the Quiz! ***\n")
    for i, q in enumerate(quiz):
        print(f"Question {i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        try:
            answer = int(input("Enter the number of your answer: "))
            if answer == q['answer']:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was {q['answer']}.\n")
        except ValueError:
            print("Invalid input! Please enter a number.\n")

    print(f"Quiz finished! Your score: {score}/{len(quiz)}")
    print("Thank you for playing!\n")

if __name__ == "__main__":
    run_quiz()

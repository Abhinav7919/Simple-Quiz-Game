questions = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "2 + 2 = ?", "answer": "4"},
    {"question": "What color do you get by mixing blue and yellow?", "answer": "green"},
    {"question": "What is the largest planet in our solar system?", "answer": "jupiter"},
    {"question": "How many continents are there?", "answer": "7"},
]

score = 0

print("Welcome to the Quiz Game!\n")

for q in questions:
    print(q["question"])
    user_answer = input("Your answer: ").lower().strip()

    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was '{q['answer']}'.\n")

print("Quiz finished!")
print(f"You scored {score} out of {len(questions)}")

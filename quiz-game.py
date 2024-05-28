questions = [
    {
        "prompt": "What year did the spanish explorers find America?",
        "options": ["A. 1492", "B. 1942", "C. 1092", "D. 1292"],
        "answer": "A"
    },
    {
        "prompt": "Which is the capital of Turkey?",
        "options": ["A. Istambul", "B. Adana", "C. Ankara", "D. Bursa"],
        "answer": "C"
    },
    {
        "prompt": "Which is the longest river?",
        "options": ["A. Amazonas", "B. Orinoco", "C. Mississippi", "D. Nile"],
        "answer": "D"
    },
    {
        "prompt": "How many planets are in the solar system?",
        "options": ["A. 8", "B. 9", "C. 7", "D. 10"],
        "answer": "A"
    },
    {
        "prompt": "Which is the tallest mountain?",
        "options": ["A. Mt Edna", "B. Everest", "C. Aconcagua", "D. Mutherhorn"],
        "answer": "B"
    },
    {
        "prompt": "How many players are in a voleyball team?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "B"
    },
]

def run_quiz(questions):
    score = 0
    for question in questions: 
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect, the correct answer is ", question["answer"], "\n")

    print(f"You reached a score of {score} out of {len(questions)} possible points")

run_quiz(questions)
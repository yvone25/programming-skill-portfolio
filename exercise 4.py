# Yvone Nicole B. Perlas | ID: 2023-904
# Exercise 4: Primitive quiz

# First, we need a list of questions and answers as tuples.
multiplequestions = [
    ("What is the capital of France?", "Paris"),
    ("What is the capital of the United Kingdom?", "London"),
    ("What is the capital of Spain?", "Madrid"),
    ("What is the capital of Italy?", "Rome"),
    ("What is the capital of Germany?", "Berlin"),
    ("What is the capital of Austria?", "Vienna"),
    ("What is the capital of Ukraine?", "Kyiv"),
    ("What is the capital of Greece?", "Athens"),
    ("What is the capital of Portugal?", "Lisbon"),
    ("What is the capital of Sweden?", "Stockholm")
]

# This is your score counter for the quiz, starting at 0.
score = 0

# Loop through each question and answer tuple.
for question, answer in multiplequestions:
    # Ask the user the question and get their answer.
    user_answer = input(question + " ").strip().lower()  # Collect input and convert to lowercase
    
    # Check if the answer is correct (case insensitive).
    if user_answer == answer.lower():
        print("You're Correct! :)")
        score += 1  # Increment score if the answer is correct
    else:
        print(f"Wrong answer :( The correct answer is: {answer}")

# Display the final score after all questions are answered.
print(f"Your final score is: {score} out of {len(multiplequestions)}")

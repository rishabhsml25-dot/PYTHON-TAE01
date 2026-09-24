import time
import random

sentences = [
    "Python is easy to learn and powerful.",
    "Practice makes your typing speed better.",
    "Coding helps improve problem solving skills.",
    "Consistency is the key to learning programming.",
    "Technology is changing the world every day."
]

last_sentence = ""

while True:

    available_sentences = []

    for sentence in sentences:
        if sentence != last_sentence:
            available_sentences.append(sentence)

    original_text = random.choice(available_sentences)
    last_sentence = original_text

    print("\n========================================")
    print("          TYPING TESTER - PHASE 2")
    print("========================================")

    print("\nType the following sentence:")
    print("----------------------------------------")
    print(original_text)
    print("----------------------------------------")

    input("\nPress ENTER to start typing...")

    start_time = time.time()
    typed_text = input("\nStart typing: ")
    end_time = time.time()

    time_taken = end_time - start_time
    time_minutes = time_taken / 60

    # Character accuracy
    correct_chars = 0
    wrong_chars = 0

    for i in range(min(len(original_text), len(typed_text))):
        if original_text[i] == typed_text[i]:
            correct_chars += 1
        else:
            wrong_chars += 1

    if len(original_text) > len(typed_text):
        wrong_chars += len(original_text) - len(typed_text)

    if len(typed_text) > len(original_text):
        wrong_chars += len(typed_text) - len(original_text)

    # Word count
    original_words = original_text.split()
    typed_words = typed_text.split()

    correct_words = 0
    wrong_words = 0

    for i in range(min(len(original_words), len(typed_words))):
        if original_words[i] == typed_words[i]:
            correct_words += 1
        else:
            wrong_words += 1

    if len(original_words) > len(typed_words):
        wrong_words += len(original_words) - len(typed_words)

    if len(typed_words) > len(original_words):
        wrong_words += len(typed_words) - len(original_words)

    words_typed = len(typed_words)

    # Accuracy
    if len(typed_text) > 0:
        accuracy = (correct_chars / len(typed_text)) * 100
    else:
        accuracy = 0

    # WPM
    if time_minutes > 0:
        wpm = (len(typed_text) / 5) / time_minutes
    else:
        wpm = 0

    print("\n========================================")
    print("             YOUR RESULTS")
    print("========================================")
    print(f"Sentence        : {original_text}")
    print(f"Time Taken      : {time_taken:.2f} seconds")
    print(f"Words Typed     : {words_typed}")
    print(f"Correct Words   : {correct_words}")
    print(f"Wrong Words     : {wrong_words}")
    print(f"Correct Chars   : {correct_chars}")
    print(f"Wrong Chars     : {wrong_chars}")
    print(f"Accuracy        : {accuracy:.2f}%")
    print(f"WPM             : {wpm:.2f}")

    print("\nPerformance:")

    if accuracy >= 90:
        print("Excellent Performance!")
    elif accuracy >= 70:
        print("Good Performance! Keep practicing.")
    else:
        print("Keep Practicing! Focus on accuracy.")

    print("========================================")

    choice = input("\nDo you want to try again? (Y/N): ")

    if choice.lower() != "y":
        print("\nThank you for using Typing Tester!")
        print("Keep practicing your typing skills.")
        break
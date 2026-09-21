import time

original_text = "Python is a powerful and easy to learn programming language."

while True:

    print("\n========================================")
    print("       TYPING TESTER - PHASE 2")
    print("========================================")

    print("\nType the following text:")
    print("----------------------------------------")
    print(original_text)
    print("----------------------------------------")

    input("\nPress ENTER to start typing...")

    start_time = time.time()
    typed_text = input("\nStart typing: ")
    end_time = time.time()

    time_taken = end_time - start_time
    time_minutes = time_taken / 60

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

    words_typed = len(typed_text.split())

    if len(typed_text) > 0:
        accuracy = (correct_chars / len(typed_text)) * 100
    else:
        accuracy = 0

    if time_minutes > 0:
        wpm = (len(typed_text) / 5) / time_minutes
    else:
        wpm = 0

    print("\n========================================")
    print("             YOUR RESULTS")
    print("========================================")
    print(f"Time Taken        : {time_taken:.2f} seconds")
    print(f"Words Typed       : {words_typed}")
    print(f"WPM               : {wpm:.2f}")
    print(f"Correct Characters: {correct_chars}")
    print(f"Wrong Characters  : {wrong_chars}")
    print(f"Accuracy          : {accuracy:.2f}%")

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
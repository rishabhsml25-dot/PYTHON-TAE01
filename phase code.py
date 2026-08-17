import time
original_text = "Python is a powerful and easy to learn programming language."

while True:

    print("\n========================================")
    print("          TYPING TESTER")
    print("========================================")

    print("\nType the following text:")
    print("----------------------------------------")
    print(original_text)
    print("----------------------------------------")

    input("\nPress ENTER to start typing...")

    # Start timer
    start_time = time.time()

    # Take user input
    typed_text = input("\nStart typing: ")

    # Stop timer
    end_time = time.time()

    # Calculate total time
    time_taken = end_time - start_time

    # Convert seconds to minutes
    time_minutes = time_taken / 60

    # Count correct characters
    correct_chars = 0

    # Compare characters
    for i in range(min(len(original_text), len(typed_text))):
        if original_text[i] == typed_text[i]:
            correct_chars += 1

    # Total characters typed
    total_typed_chars = len(typed_text)

    # Calculate accuracy
    if total_typed_chars > 0:
        accuracy = (correct_chars / total_typed_chars) * 100
    else:
        accuracy = 0

    # Calculate WPM
    if time_minutes > 0:
        wpm = (total_typed_chars / 5) / time_minutes
    else:
        wpm = 0

    # Display results
    print("\n========================================")
    print("             YOUR RESULTS")
    print("========================================")

    print(f"Time Taken : {time_taken:.2f} seconds")
    print(f"WPM        : {wpm:.2f}")
    print(f"Accuracy   : {accuracy:.2f}%")
    print(f"Correct Characters : {correct_chars}")

    # Performance feedback
    print("\nPerformance:")

    if accuracy >= 90:
        print("Excellent Performance! 🎉")
    elif accuracy >= 70:
        print("Good Performance! 👍")
    else:
        print("Keep Practicing! 💪")

    # Retry option
    choice = input("\nDo you want to try again? (Y/N): ")

    if choice.lower() != "y":
        print("\nThank you for using Typing Tester!")
        print("Keep practicing your typing skills. 🚀")
        break
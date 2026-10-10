import random
import time

SENTENCES = {
    "Easy": [
        "Python is easy to learn.",
        "Practice makes a person better.",
        "Small steps create big results.",
        "Keep learning and stay focused."
    ],
    "Medium": [
        "Consistent practice improves typing speed and accuracy.",
        "Programming teaches us how to solve problems logically.",
        "Every mistake is an opportunity to learn something useful.",
        "Good habits make difficult tasks easier over time."
    ],
    "Hard": [
        "A successful programmer combines patience, curiosity, and logical thinking.",
        "Accuracy is just as important as speed when writing reliable software.",
        "Learning consistently is more effective than studying only before an examination.",
        "Careful observation helps developers identify and fix unexpected errors."
    ]
}


def run_test(level):
    sentence = random.choice(SENTENCES[level])
    print("\nType the sentence exactly as shown:\n")
    print(sentence)
    input("\nPress Enter when you are ready...")
    start = time.time()
    typed = input("\nYour typing: ")
    elapsed = max(time.time() - start, 0.01)

    correct = sum(1 for a, b in zip(sentence, typed) if a == b)
    wrong = max(len(sentence), len(typed)) - correct
    accuracy = (correct / max(len(sentence), len(typed), 1)) * 100
    words = len(typed.split())
    wpm = words / (elapsed / 60)

    print("\n--- RESULT ---")
    print(f"Time: {elapsed:.2f} seconds")
    print(f"Words typed: {words}")
    print(f"Speed: {wpm:.2f} WPM")
    print(f"Correct characters: {correct}")
    print(f"Wrong/missing/extra characters: {max(wrong, 0)}")
    print(f"Accuracy: {accuracy:.2f}%")
    if accuracy >= 90:
        print("Feedback: Excellent! Keep it up.")
    elif accuracy >= 75:
        print("Feedback: Good work. Keep practising.")
    else:
        print("Feedback: Keep practising slowly and focus on accuracy.")
    return {"level": level, "wpm": wpm, "accuracy": accuracy, "time": elapsed}


def main():
    history = []
    print("=" * 42)
    print("       PYTHON CODE-STRENGTH CHECKER")
    print("              PHASE 3 - FINAL")
    print("=" * 42)

    while True:
        print("\n1. Start typing test")
        print("2. View attempt history")
        print("3. View best score")
        print("4. View final summary")
        print("5. Exit")
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            print("\nChoose difficulty: 1. Easy  2. Medium  3. Hard")
            levels = {"1": "Easy", "2": "Medium", "3": "Hard"}
            level_choice = input("Difficulty (1-3): ").strip()
            if level_choice not in levels:
                print("Invalid difficulty. Please choose 1, 2, or 3.")
                continue
            result = run_test(levels[level_choice])
            history.append(result)
        elif choice == "2":
            if not history:
                print("No attempts yet. Start a test first.")
            else:
                print("\nAttempt | Level | WPM | Accuracy | Time")
                for i, item in enumerate(history, 1):
                    print(f"{i:7} | {item['level']:6} | {item['wpm']:.2f} | "
                          f"{item['accuracy']:.2f}% | {item['time']:.2f}s")
        elif choice == "3":
            if not history:
                print("No score yet. Start a test first.")
            else:
                best = max(history, key=lambda item: item["wpm"])
                print(f"Best speed: {best['wpm']:.2f} WPM")
                print(f"Accuracy on best-speed attempt: {best['accuracy']:.2f}%")
                print(f"Difficulty: {best['level']}")
        elif choice == "4":
            if not history:
                print("No attempts recorded yet.")
            else:
                average_wpm = sum(x["wpm"] for x in history) / len(history)
                average_accuracy = sum(x["accuracy"] for x in history) / len(history)
                print("\n--- FINAL PERFORMANCE SUMMARY ---")
                print(f"Total attempts: {len(history)}")
                print(f"Average speed: {average_wpm:.2f} WPM")
                print(f"Average accuracy: {average_accuracy:.2f}%")
                print(f"Best speed: {max(x['wpm'] for x in history):.2f} WPM")
        elif choice == "5":
            print("Thanks for practising. Keep improving!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()

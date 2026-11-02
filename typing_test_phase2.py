"""Typing Test - Phase 2 / 70% (Python): word count, levels, punctuation, numbers, saved personal best."""
import json
import os
import random
import textwrap
import time

BEST_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "best.json")

WORDS = {
    "easy": ("the be to of and a in that have it for not on with he as you do at this but his by from "
             "they we say her she or an will my one all would there their what so up out if about who "
             "get which go me when make can like time no just him know take people into year your good "
             "some could them see other than then now look only come its over think also back after use "
             "two how our work first well way even new want because any these give day most us").split(),
    "medium": ("above accept achieve address advance allow amount animal answer appear around attention "
               "balance because before believe benefit between bright building careful century certain "
               "change choose company consider contain continue control country create culture decide "
               "deliver describe develop different direction discover distance during economy effort "
               "energy enough evening example explain family feature figure finish follow foreign forward "
               "friend future garden general health history imagine improve include increase industry "
               "interest journey knowledge language leader machine measure member message minute modern "
               "morning movement natural nothing number object office opinion parent pattern perfect "
               "picture plastic pleasure popular possible practice present problem produce project provide "
               "quality question reason receive recent record remember report result science season second "
               "service several simple society special station strategy student subject success support "
               "surface system teacher through together tomorrow traffic travel understand usually variety "
               "village weather without writing").split(),
    "hard": ("acknowledge algorithm ambiguous architecture asynchronous bureaucracy characteristic "
             "collaboration comprehensive concatenate consciousness contemporary convenience correspondence "
             "cryptography deliberately demonstrate determination developmental differentiate "
             "disproportionate documentation encyclopedia entrepreneur environmental extraordinary "
             "fundamentally gratification hypothetical implementation infrastructure instantaneous "
             "interdependent jurisdiction knowledgeable laboratory manufacturing miscellaneous nevertheless "
             "notwithstanding opportunity parliamentary pharmaceutical philosophical psychological "
             "questionnaire quintessential reconnaissance rehabilitation representative simultaneously "
             "sophisticated specification straightforward sustainability synchronization technological "
             "temperature transformation unprecedented vocabulary vulnerability").split(),
}

settings = {"words": 20, "level": "easy", "punc": False, "nums": False}


def make_text(cfg):
    out = []
    for _ in range(cfg["words"]):
        w = random.choice(WORDS[cfg["level"]])
        if cfg["nums"] and random.random() < 0.15:
            w = str(random.randint(0, 999))
        if cfg["punc"] and random.random() < 0.2:
            r = random.random()
            if r < 0.35:
                w = w.capitalize()
            elif r < 0.65:
                w += ","
            elif r < 0.85:
                w += "."
            else:
                w = '"' + w + '"'
        out.append(w)
    return " ".join(out)


def calc(target, typed, seconds):
    correct = sum(1 for a, b in zip(target, typed) if a == b)
    minutes = max(seconds, 0.01) / 60
    wpm = round(correct / 5 / minutes)
    raw = round(len(typed) / 5 / minutes)
    acc = round(correct / len(typed) * 100) if typed else 0
    mistakes = len(typed) - correct + max(0, len(target) - len(typed))
    return wpm, raw, acc, mistakes


def load_best():
    try:
        with open(BEST_FILE, encoding="utf8") as f:
            return int(json.load(f).get("best", 0))
    except (OSError, ValueError):
        return 0


def save_best(v):
    try:
        with open(BEST_FILE, "w", encoding="utf8") as f:
            json.dump({"best": v}, f)
    except OSError:
        pass


def ask_choice(title, options):
    print(f"\n{title}")
    for i, o in enumerate(options, 1):
        print(f"  {i}. {o}")
    while True:
        c = input("Choose: ").strip()
        if c.isdigit() and 1 <= int(c) <= len(options):
            return int(c) - 1


def settings_menu():
    counts = [10, 20, 30, 50]
    settings["words"] = counts[ask_choice("Kitne words?", [f"{c} words" for c in counts])]
    levels = ["easy", "medium", "hard"]
    settings["level"] = levels[ask_choice("Level?", ["Easy", "Medium", "Hard"])]
    settings["punc"] = ask_choice("Punctuation?", ["Off", "On"]) == 1
    settings["nums"] = ask_choice("Numbers?", ["Off", "On"]) == 1


def play():
    target = make_text(settings)
    print("\nNeeche ka text type karo aur Enter dabao:\n")
    print(textwrap.fill(target, 70))
    input("\nTaiyar ho? Enter dabao...")
    for n in (3, 2, 1):
        print(n, end=" ", flush=True)
        time.sleep(0.7)
    print("GO!\n")
    start = time.time()
    typed = input("> ")
    seconds = time.time() - start
    wpm, raw, acc, mistakes = calc(target, typed, seconds)
    print("\n--- Result ---")
    print(f"Time      : {seconds:.1f} sec")
    print(f"WPM       : {wpm}")
    print(f"Raw WPM   : {raw}")
    print(f"Accuracy  : {acc}%")
    print(f"Mistakes  : {mistakes}")
    if wpm > load_best():
        save_best(wpm)
        print(f"*** Naya personal best: {wpm} WPM ***")


def main():
    print("=== TYPING TESTER - Phase 2 ===")
    while True:
        s = settings
        print(f"\nPersonal best: {load_best() or '-'} WPM")
        print(f"Settings: {s['words']} words | {s['level']} | punctuation={'on' if s['punc'] else 'off'} | numbers={'on' if s['nums'] else 'off'}")
        c = ask_choice("Menu", ["Start test", "Change settings", "Exit"])
        if c == 0:
            play()
        elif c == 1:
            settings_menu()
        else:
            print("Bye!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nBye!")

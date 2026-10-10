import random
import time
import streamlit as st

st.set_page_config(page_title="Typing Tester | Phase 3", page_icon="⌨️", layout="centered")

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

if "history" not in st.session_state:
    st.session_state.history = []
if "active_sentence" not in st.session_state:
    st.session_state.active_sentence = None
if "started_at" not in st.session_state:
    st.session_state.started_at = None
if "last_result" not in st.session_state:
    st.session_state.last_result = None

st.title("⌨️ Python Code-Strength Checker")
st.caption("Phase 3 • Final Typing Performance Tracker")
st.write("Test your typing speed, improve accuracy, and review your progress.")

with st.sidebar:
    st.header("Test settings")
    level = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    st.markdown("**Scoring tips**")
    st.write("• Type the sentence exactly.")
    st.write("• Accuracy matters as much as speed.")
    st.write("• Each new test uses a random sentence.")

if st.button("Start new test", type="primary", use_container_width=True):
    st.session_state.active_sentence = random.choice(SENTENCES[level])
    st.session_state.started_at = time.time()
    st.session_state.last_result = None
    st.rerun()

if st.session_state.active_sentence:
    st.subheader(f"{level} challenge")
    st.info(st.session_state.active_sentence)
    typed = st.text_area("Type the sentence here", key=f"typed_{len(st.session_state.history)}")
    if st.button("Check my result", use_container_width=True):
        target = st.session_state.active_sentence
        elapsed = max(time.time() - st.session_state.started_at, 0.01)
        correct = sum(1 for a, b in zip(target, typed) if a == b)
        wrong = max(len(typed) - correct, 0)
        accuracy = correct / max(len(target), len(typed), 1) * 100
        words = len(typed.split())
        wpm = words / (elapsed / 60)
        result = {
            "Attempt": len(st.session_state.history) + 1,
            "Difficulty": level,
            "WPM": round(wpm, 2),
            "Accuracy (%)": round(accuracy, 2),
            "Correct characters": correct,
            "Wrong/extra characters": wrong,
            "Time (seconds)": round(elapsed, 2)
        }
        st.session_state.history.append(result)
        st.session_state.last_result = result
        st.session_state.active_sentence = None
        st.rerun()

if st.session_state.last_result:
    result = st.session_state.last_result
    st.subheader("Your result")
    c1, c2, c3 = st.columns(3)
    c1.metric("Typing speed", f"{result['WPM']:.2f} WPM")
    c2.metric("Accuracy", f"{result['Accuracy (%)']:.2f}%")
    c3.metric("Time", f"{result['Time (seconds)']:.2f}s")
    st.write(f"Correct characters: **{result['Correct characters']}**")
    st.write(f"Wrong/extra characters: **{result['Wrong/extra characters']}**")
    if result["Accuracy (%)"] >= 90:
        st.success("Excellent! Keep it up.")
    elif result["Accuracy (%)"] >= 75:
        st.info("Good work. Keep practising.")
    else:
        st.warning("Keep practising slowly and focus on accuracy.")

history = st.session_state.history
st.divider()
st.subheader("Performance dashboard")
if history:
    best = max(history, key=lambda item: item["WPM"])
    average_wpm = sum(item["WPM"] for item in history) / len(history)
    average_accuracy = sum(item["Accuracy (%)"] for item in history) / len(history)
    a, b, c = st.columns(3)
    a.metric("Total attempts", len(history))
    b.metric("Best speed", f"{best['WPM']:.2f} WPM")
    c.metric("Average accuracy", f"{average_accuracy:.2f}%")
    st.metric("Average typing speed", f"{average_wpm:.2f} WPM")
    st.dataframe(history, use_container_width=True, hide_index=True)
    st.download_button(
        "Download attempt history (CSV)",
        data=__import__("pandas").DataFrame(history).to_csv(index=False),
        file_name="typing_test_history.csv",
        mime="text/csv"
    )
else:
    st.write("Your attempts and scores will appear here after your first test.")

st.caption("Note: scores and history are kept for this browser session; they reset when the session ends.")

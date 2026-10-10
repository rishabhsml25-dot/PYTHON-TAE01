# PYTHON-TAE01 — Python Code-Strength Checker

A Python typing-speed and accuracy project developed in three phases. Phase 1 and Phase 2 are preserved; Phase 3 adds difficulty levels, attempt history, best score, and a performance summary.

## Project files
- **`phase 1.py`** — basic typing test, timer, WPM, accuracy, feedback, retry.
- **`phase 2.py`** — random sentences, words/characters correct and wrong, WPM, accuracy.
- **`phase 3.py`** — final console version with Easy/Medium/Hard levels, attempt history, best speed, average performance, and a menu.
- **`streamlit_app.py`** — browser-based version for online deployment.
- **`requirements.txt`** — packages needed for the web app.

## Run locally
Install Python 3.10 or newer. For the console versions:

```bash
python "phase 1.py"
python "phase 2.py"
python "phase 3.py"
```

To run the web app:

```bash
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

Then open the local URL printed in the terminal (usually http://localhost:8501).

## Phase 3 features
- Three difficulty levels with randomly selected sentences.
- Time, words typed, typing speed (WPM), correct and wrong/missing/extra character counts.
- Accuracy percentage and feedback (90%+ Excellent, 75–89.99% Good, below 75% Keep Practising).
- Attempt history, best speed, average speed and accuracy.
- CSV download for the web app's attempt history.

## Deploy online with Streamlit Community Cloud
1. Sign in at [Streamlit Community Cloud](https://share.streamlit.io/) using the GitHub account that can access this repository.
2. Select **Create app** / **Deploy an app**.
3. Choose repository **`rishabhsml25-dot/PYTHON-TAE01`**, branch **`main`**, and main file path **`streamlit_app.py`**.
4. Select **Deploy** and wait for the build to finish. Streamlit will show your live app URL once deployment succeeds.

**Important:** the code and deployment requirements are committed here, but the live website is not active until you complete the Streamlit sign-in and deployment step. Attempt history is kept in the current browser session and resets when that session ends.

## Project status
**Phase 3 — Final version committed.** The console project runs with Python; the browser version is prepared for Streamlit Community Cloud.

# CodeStrength — Python Code-Strength Checker

A responsive typing-speed and accuracy website backed by a Python Flask API. The project also keeps the original three Python console phases.

## Project files

- `index.html` — responsive website frontend for desktop, tablet and mobile.
- `app.py` — Python Flask API for challenges, scoring, accuracy and feedback.
- `requirements.txt` — Python dependencies.
- `render.yaml` — Render deployment configuration for the API.
- `phase 1.py` — basic typing test.
- `phase 2.py` — typing test with random sentences and score calculations.
- `phase 3.py` — final console version with difficulty levels and performance summary.
- `CM25046-project phase 1.docx` — project document.

## Deploy the website

### 1. Publish the frontend on GitHub Pages

1. Open this repository: https://github.com/rishabhsml25-dot/PYTHON-TAE01
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select branch **main** and folder **/(root)**, then press **Save**.
5. Wait for GitHub Pages to publish the website. Your site URL will appear on the Pages settings screen, usually in the form `https://rishabhsml25-dot.github.io/PYTHON-TAE01/`.

GitHub Pages hosts the HTML/CSS/JavaScript frontend only. It does not run Python server code.

### 2. Deploy the Python backend on Render

1. Sign in to https://render.com/ and connect the GitHub account that owns this repository.
2. Choose **New → Blueprint** and select repository `rishabhsml25-dot/PYTHON-TAE01`. Render will read `render.yaml`.
3. Create the web service and wait for deployment to finish.
4. Copy the service URL, for example `https://codestrength-python-api.onrender.com`. Use the actual URL Render gives you; the example may not be your URL.
5. Open the GitHub Pages website, paste the actual Render URL into **One-time setup**, and click **Connect backend**.

The website calls these API endpoints:
- `GET /api/health` — backend health check.
- `GET /api/challenge?level=easy|medium|hard` — get a sentence.
- `POST /api/score` — calculate WPM, accuracy and feedback.

**Note:** Render's free services may sleep after inactivity, so the first request can take a little while. Keep the backend URL exactly as provided by Render, with no extra path at the end.

## Run locally

Install Python 3.10 or newer.

Run a console phase:

```bash
python "phase 1.py"
python "phase 2.py"
python "phase 3.py"
```

Run the API locally:

```bash
python -m pip install -r requirements.txt
python app.py
```

The API will run at `http://127.0.0.1:5000`. To test the frontend locally, open `index.html` in your browser and enter that API URL. If the browser blocks a local-file request, use a simple local web server such as `python -m http.server 8000` and open `http://localhost:8000`.

## Phase 3 / website features

- Easy, Medium and Hard typing challenges.
- Responsive layout for mobile, tablet and desktop.
- Python API-based sentence selection and scoring.
- WPM, accuracy, correct characters, elapsed time and feedback.
- Recent attempts displayed during the current browser session.

## Deployment checklist

- [ ] Enable GitHub Pages from `main` / root.
- [ ] Deploy the Flask API on Render.
- [ ] Paste the real Render URL into the website and connect.
- [ ] Start a typing challenge and check that results appear.

The repository contains the deployment files, but the live website and API are not considered deployed until you complete the hosting steps above.

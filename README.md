# FY Engineering Admission Form

Streamlit implementation of the supplied engineering admission forms, with English labels and Marathi subtitles. FY is an editable form; SY, DSE, TY, and B.Tech display the supplied SY-style form reference.

The browser form supports online payment with a QR code or offline payment with a required receipt number. The Word download includes the office-use section; the browser form does not.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

The supplied paper form is shown in the sidebar as a visual reference.

## Deploy on Render or Railway

Use the following start command for a web service:

```bash
streamlit run app.py --server.address=0.0.0.0 --server.port=$PORT
```

Set the service runtime to Python and install dependencies with:

```bash
pip install -r requirements.txt
```

For Render, deploy with the included `render.yaml` Blueprint. It creates a PostgreSQL database and injects its connection string as `DATABASE_URL` into the web service. Submissions stored there survive browser refreshes, service restarts, and redeployments. If configuring Render manually, create a PostgreSQL database and add its connection string as the `DATABASE_URL` environment variable. Without it, local development uses `admission_records.csv` as a fallback; Render's default filesystem is temporary, so the CSV fallback is not persistent there.
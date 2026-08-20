# FY Engineering Admission Form

Streamlit implementation of the supplied first-year engineering admission form, with English labels and Marathi subtitles. Submitted admissions are stored locally in `admission_records.csv`.

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

The application writes submitted records to `admission_records.csv` in the running container. Use persistent storage or an external database if records must survive redeployments.
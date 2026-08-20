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
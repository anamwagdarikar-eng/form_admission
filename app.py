import io
from datetime import date

import streamlit as st


st.set_page_config(
    page_title="FY Engineering Admission Form",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed",
)


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Source+Sans+3:wght@400;600;700&display=swap');
    :root { --ink:#1c2429; --line:#445057; --paper:#fffdf7; --accent:#b52f3d; }
    .stApp { background: #e8e2d9; color: var(--ink); font-family: 'Source Sans 3', sans-serif; }
    .block-container { max-width: 1120px; padding: 2rem 1rem 4rem; }
    .paper { background:var(--paper); border:1px solid #bbb5aa; box-shadow:0 12px 34px #37302a24; padding:2rem 2.5rem; }
    .masthead { display:grid; grid-template-columns:92px 1fr 92px; gap:18px; align-items:center; border-bottom:2px solid var(--ink); padding-bottom:10px; text-align:center; }
    .seal { width:78px; height:78px; border:3px double var(--ink); border-radius:50%; display:grid; place-items:center; font:700 11px 'Libre Baskerville'; line-height:1.1; }
    .masthead h1 { font:700 18px 'Libre Baskerville'; margin:0 0 5px; letter-spacing:.2px; }
    .masthead p { margin:2px 0; font-size:11px; line-height:1.2; }
    .photo { border:1px solid var(--ink); height:96px; display:grid; place-items:center; font-size:11px; }
    .title { text-align:center; border-bottom:1px solid var(--ink); padding:8px 0 6px; margin-bottom:8px; font:700 14px 'Libre Baskerville'; }
    .section-title { font-weight:700; margin:10px 0 3px; font-size:14px; }
    .mr { color:#7d2630; font-size:12px; font-weight:600; display:block; line-height:1.1; }
    .paper hr { border:0; border-top:1px solid #777; margin:9px 0; }
    .paper [data-testid="stForm"] { border:0; padding:0; }
    .paper .stTextInput label, .paper .stNumberInput label, .paper .stDateInput label, .paper .stSelectbox label, .paper .stTextArea label { font-size:12px; color:var(--ink); }
    .paper .stTextInput, .paper .stNumberInput, .paper .stDateInput, .paper .stSelectbox, .paper .stTextArea { margin-bottom:-5px; }
    .paper .stTextInput input, .paper .stNumberInput input, .paper .stDateInput input, .paper .stSelectbox div[data-baseweb="select"], .paper textarea { border-radius:0; background:#fff; border-color:#879097; }
    .paper .stCheckbox label { font-size:12px; }
    .paper .stButton button { border-radius:2px; background:var(--accent); color:white; border:0; font-weight:700; }
    .note { color:#59636a; font-size:12px; margin:0 0 14px; }
    @media (max-width: 700px) { .paper { padding:1rem .85rem; } .masthead { grid-template-columns:58px 1fr 58px; gap:7px; } .seal { width:54px; height:54px; font-size:8px; } .masthead h1 { font-size:12px; } .masthead p { font-size:8px; } .photo { height:70px; font-size:9px; } }
    </style>
    """,
    unsafe_allow_html=True,
)


def label(text: str, marathi: str) -> str:
    return f"{text}  •  {marathi}"


def marks_table(prefix: str, title: str) -> None:
    st.markdown(f"**{title}**")
    columns = st.columns([1.2, 1, 1.8, 1, 1, .7, 1, .7])
    headers = ["", "Physics", "Chemistry / ______", "Maths", "PCM Total", "%", "Grand Total", "%"]
    for column, header in zip(columns, headers):
        column.markdown(f"<div style='font-size:11px;font-weight:700;text-align:center;height:28px'>{header}</div>", unsafe_allow_html=True)
    for row in ["Marks Obtained", "Out of"]:
        row_columns = st.columns([1.2, 1, 1.8, 1, 1, .7, 1, .7])
        row_columns[0].markdown(f"<div style='font-size:11px;padding-top:8px'>{row}</div>", unsafe_allow_html=True)
        for index, column in enumerate(row_columns[1:]):
            column.text_input(f"{prefix}_{row}_{index}", label_visibility="collapsed", key=f"{prefix}_{row}_{index}")


with st.sidebar:
    st.header("Reference")
    st.image("admission_form_FY.jpeg", width="stretch")
    st.caption("Original paper form supplied for layout reference.")

st.markdown('<div class="paper">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="masthead">
      <div class="seal">VVP<br>INSTITUTE<br>SEAL</div>
      <div><p>VIDYA VIKAS PRATISHTHAN'S</p><h1>VVP INSTITUTE OF ENGINEERING &amp; TECHNOLOGY, SOLAPUR</h1><p>NAAC Accredited &amp; ISO 9001 : 2015 Certified Institute</p><p>Approved by AICTE New Delhi &amp; Affiliated to DBATU, Lonere</p><p><b>72 / 2 B, Pratapnagar, Soregaon-Dongare Road, Solapur - 413008</b></p><p>Phone: 8380305555 &nbsp; Email: vvpiet@rediffmail.com &nbsp; Website: www.vvpengg.org</p></div>
      <div class="photo">PHOTO</div>
    </div>
    <div class="title">APPLICATION FORM FOR ADMISSION TO FIRST YEAR ENGINEERING COURSE (20 - 20 &nbsp;&nbsp; )</div>
    """,
    unsafe_allow_html=True,
)
st.caption("Fill in the details below. Fields follow the sequence and wording of the supplied paper form.")

with st.form("admission_form"):
    st.markdown(f"**1. Full Name: (In Block Letters)** <span class='mr'>पूर्ण नाव (ठळक अक्षरात)</span>", unsafe_allow_html=True)
    first, father, mother = st.columns(3)
    first.text_input(label("Candidate full name", "उमेदवाराचे पूर्ण नाव"))
    father.text_input(label("Father's full name", "वडिलांचे पूर्ण नाव"))
    mother.text_input(label("Mother's Name", "आईचे नाव"))

    st.markdown(f"**2. Address for Correspondence** <span class='mr'>पत्रव्यवहाराचा पत्ता</span>", unsafe_allow_html=True)
    st.text_area(label("Address", "पत्ता"), height=68)
    st.text_input(label("Pin Code", "पिन कोड"))
    st.markdown(f"**3. Permanent Address** <span class='mr'>कायमचा पत्ता</span>", unsafe_allow_html=True)
    st.text_area(label("Permanent address", "कायमचा पत्ता"), height=68)
    st.text_input(label("Permanent address Pin Code", "कायमचा पिन कोड"))

    contact = st.columns(4)
    contact[0].text_input(label("Res. Phone No.", "निवासी दूरध्वनी क्र."))
    contact[1].text_input(label("Parent No.", "पालकांचा क्र."))
    contact[2].text_input(label("Candidate No.", "उमेदवार क्र."))
    contact[3].text_input(label("E-Mail ID", "ई-मेल आयडी"))
    identity = st.columns(3)
    identity[0].selectbox(label("Sex", "लिंग"), ["Select", "Male", "Female"])
    identity[1].text_input(label("Nationality", "राष्ट्रीयत्व"))
    identity[2].text_input(label("Religion", "धर्म"))
    st.text_input(label("Caste: OPEN / SC / ST / SBC / VJNT / OBC / SEBC", "जात"))
    st.text_input(label("11. (a) Sub Caste", "पोटजात"))
    st.markdown(f"**12. Details of qualifying examination (HSC / Diploma / B.Sc.) Passed. Year of Passing** <span class='mr'>पात्रता परीक्षेचा तपशील व उत्तीर्ण वर्ष</span>", unsafe_allow_html=True)
    st.text_input(label("Year of Passing", "उत्तीर्ण वर्ष"))
    marks_table("qualifying", "Qualifying examination marks")
    st.markdown(f"**13. Details of qualifying examination MHT-CET-20 / JEE (Main) - 20** <span class='mr'>MHT-CET / JEE (मुख्य) परीक्षेचा तपशील</span>", unsafe_allow_html=True)
    marks_table("entrance", "Entrance examination marks")

    st.markdown(f"**14. Details of SSC Examination Passed:** <span class='mr'>SSC परीक्षेचा तपशील</span>", unsafe_allow_html=True)
    ssc = st.columns([2, 2, 1.4, 1.2])
    for index, (column, text) in enumerate(zip(ssc, ["Name of School", "Name of Board", "Year of Passing", "% of Marks"])):
        column.text_input(
            label(text, {"Name of School":"शाळेचे नाव", "Name of Board":"बोर्डचे नाव", "Year of Passing":"उत्तीर्ण वर्ष", "% of Marks":"गुणांची टक्केवारी"}[text]),
            key=f"ssc_{index}",
        )

    st.markdown(f"**15. Course / Branch Selected for F. Y. B. Tech. (Tick Mark Appropriate branch)** <span class='mr'>प्रथम वर्ष बी.टेक. साठी निवडलेला अभ्यासक्रम / शाखा</span>", unsafe_allow_html=True)
    branches = ["Artificial Intelligence & Data Science", "Computer Science & Engineering", "Civil Engineering", "Electrical Engineering", "Electronic & Telecommunication Engineering", "Mechanical Engineering"]
    branch_cols = st.columns(2)
    for index, branch in enumerate(branches):
        branch_cols[index % 2].checkbox(f"{index + 1}. {branch}")

    signatures = st.columns(4)
    signatures[0].date_input(label("Date", "दिनांक"), value=date.today())
    signatures[1].text_input(label("Place", "ठिकाण"))
    signatures[2].text_input(label("Signature of Student", "विद्यार्थ्याची सही"))
    signatures[3].text_input(label("Signature of Parent", "पालकांची सही"))

    st.markdown("---")
    st.markdown(f"<div style='text-align:center;font-weight:700'>For Office Use Only <span class='mr'>कार्यालयीन वापरासाठी</span></div>", unsafe_allow_html=True)
    office = st.columns([1.4, 2.5, 1.4])
    office[0].markdown("**Designation**")
    office[1].markdown("**Remarks / Particulars**")
    office[2].markdown("**Signature and Date**")
    for role in ["Admission Committee", "Account", "Registrar", "Principal"]:
        fields = st.columns([1.4, 2.5, 1.4])
        fields[0].markdown(f"{role}")
        fields[1].text_input(f"{role} remarks", label_visibility="collapsed")
        fields[2].text_input(f"{role} signature", label_visibility="collapsed")

    submitted = st.form_submit_button("Submit Admission Form")
    if submitted:
        st.success("Admission form submitted successfully. Review the entered details before printing.")

st.markdown("</div>", unsafe_allow_html=True)
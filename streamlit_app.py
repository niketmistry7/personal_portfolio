import streamlit as st
from PIL import Image
from fpdf import FPDF
import base64

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


with open("CV_Niket.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download Resume",
                    data=PDFbyte,
                    file_name="CV_Niket.pdf",
                    mime='application/octet-stream')

#####################
# Header 
st.write('''
# Niket B. Mistry
##### *Portfolio* 
''')

image = Image.open('linkedin_headshot.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Industrial Engineer with optimization and data science knowledge
- Passionate about solving complex problems by developing robuest solution based on data
- Demonstrated leadership experience in automotive and retail supply chains across planning and operations
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/niketmistry/" target="_blank">Niket Mistry</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

#####################
st.markdown('''
## Education
''')

txt('**Master of Science** (Industrial & Systems Engineering), *North Carolina State University*, Raleigh, North Carolina',
'2016-2018')
st.markdown('''
- Supply Chain Management Minor
''')

txt('**Bachelors of Engineering** (Mechanical Engineering), *KSV University*, India',
'2012-2016')
st.markdown('''
- Industrial Engineering Minor
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Consultant, Supply Chain Practice**, SRM Tech, Remote',
'2024-Present')
st.markdown('''
- Assist with gathering requirements from potential leads and existing clients
- Develop scope of work for SCM solution in partnership with external and internal stakeholders
- Identify and assist in creating the technical and domain requirements for recruitment both in India and US
- Partner with technical team to develop and implement SCM solutions – POC, MVP and final product
- Assist in demo'ing the solution to potential leads and existing clients
''')

txt('**Manager, Operations Excellence**, American Eagle Outfitters, Pittsburgh, PA',
'2021-Present')
st.markdown('''
- Developed production planning strategy for eight 3PL sites which resulted in 1MUSD+ yearly savings
- Responsible for new & exisiting site layout design, MHE selection, and process engineering
- Developed engineering labor standards for process and led various initiatives to improve site throughput by 20%
''')

txt('**Lead, Supply Chain Optimization**, Volvo Group, Greensboro, NC',
'2020-2021')
txt('**Analyst, Supply Chain Optimization**, Volvo Group, Greensboro, NC',
'2018-2020')
st.markdown('''
- After market supply chain plannig
- Inventory optimization & Demand forecasting models in R, Python
- S&OP Process, PowerBI dashboard development
''')


#####################
st.markdown('''
## Projects
''')
txt4('Volvo Group','Python models, Backorder allocation, Cost optimization, Spare part forecasting')
txt4('Volvo Group','Developed a production planning application by using streamlit')
txt4('Volvo Group','Safety Stock optimization for contruction equipment parts, ~million usd annual cost savings')
txt4('Volvo Group','Distribution center launch planning, multimillion inventory, 5% improved service level within launch')
txt4('Volvo Group','Risk mitigation planning, respositioning of invetory that ensured 80%+ service level during DC closure')
txt4('Volvo Group','PowerBI dashboards, Parts availability, forecast accuracy, dashboard architecture and automation')
txt4('Personal','Production and labor planning app by using streamlit')


#####################
st.markdown('''
## Skills
''')
txt3('Engineering', '`Time & Motion study`, `Value stream mapping`,`Lean Six Sigma`,`Root cause analysis`')
txt3('Business', '`Inventory Planning`, `Demand Forecasting`,`S&OP`,`Labor and Production Planning`')
txt3('Programming', '`Python`, `R`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

#####################
st.markdown('''
## Links
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/niketmistry/')
txt2('GitHub', 'https://github.com/niketmistry7/')

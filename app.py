from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Dann Guiller Cuapiaco"
PAGE_ICON = ":wave:"
NAME = "Dann Guiller Cuapiaco"
DESCRIPTION = """
Senior Software Engineer, providing technical solutions through high-quality service and support.
"""
EMAIL = "cuapiaco.dann@yahoo.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/dann-guiller-cuapiaco-613012133/",
    "GitHub": "https://github.com/daerco22",
	"Facebook": "https://www.facebook.com/danncuapiaco"
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 8 Years experience managing Production and Development Environments
- ✔️ Strong hands on experience and knowledge in Cloud Environment Administration
- ✔️ Good understanding of CI/CD build and process
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Terraform, Python and Bash
- 📊 Cloud Environment Administration: AWS and Microsoft Azure
- 🗄️ Operating System Administration: Linux and Windows
- 📚 CI/CD Pipelines Automation: Jenkins and GitLab
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Software Engineer | Infor PSSC Inc.**")
st.write("2018 - Present")
st.write(
    """
- ► Ensure the availability of Multi-Tenant Cloud Environment for Developers and Testers daily task
- ► Report any Application Errors or Interruptions that the Environment will encounter to respective teams
- ► Ensure the availability of Pipeline Environments for Quality Assurance Testing after the Daily Patch
- ► Ensure that the expected Application package versions are successfully patch the Pipeline Environments
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Devops Engineer | Stellar Loyalty**")
st.write("2017 - 2018")
st.write(
    """
- ► Manages and Maintain Cloud Environment of Production and Development
- ► Create scripts that can help the team to operate faster and efficient
- ► Create new environments for new clients using deployment scripts
- ► Update software patches for clients environments
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**System Administrator | Smart Communication Inc.**")
st.write("2014 - 2017")
st.write(
    """
- ► Installs software, applies patches, manages files systems, monitors performance and troubleshoots alerts, open source and locally developed monitoring tools
- ► Manages hardware and software migration and upgrades efforts of varying size and complexity
- ► Manages and Maintain Cloud Environment of Production and Development
"""
)


# --- Projects & Accomplishments ---
#st.write('\n')
#st.subheader("Projects & Accomplishments")
#st.write("---")
#for project, link in PROJECTS.items():
#    st.write(f"[{project}]({link})")

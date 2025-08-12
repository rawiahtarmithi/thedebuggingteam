import streamlit as st
from resume_utils import extract_text_from_pdf
from matcher import rank_resumes

st.title("Resume Matcher")

st.markdown("Upload a job description and resumes to find the best matches.")

job_description = st.text_area("Paste the Job Description Here:")

uploaded_files = st.file_uploader("Upload Resumes (PDF)", accept_multiple_files=True, type="pdf")

if st.button("Find Top Matches"):
    if not job_description or not uploaded_files:
        st.error("Please upload resumes and paste the job description.")
    else:
        resume_data = []
        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            resume_data.append((file.name, text))

        ranked = rank_resumes(job_description, resume_data)

        st.subheader("Top 5 Candidates:")
        for i, (name, score, text) in enumerate(ranked[:5]):
            st.markdown(f"**{i+1}. {name}** - Match Score: `{score:.2f}`")
            with st.expander("View Resume Text"):

                st.write(text) 

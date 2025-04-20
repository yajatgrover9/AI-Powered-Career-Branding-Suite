# -*- coding: utf-8 -*-
import streamlit as st
import docx2txt
from pypdf import PdfReader
from services.genai_services import llm
from dotenv import load_dotenv

load_dotenv()


def extract_text(file):
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    else:
        return None


st.title("🧠 Tech Interview Assistant")

st.header("Step 1: Upload Candidate Resume and Job Description")
resume_file = st.file_uploader(
    "Upload Candidate Resume (PDF or DOCX)", type=["pdf", "docx"]
)
jd_text = st.text_area("Enter Job Description Here")

if resume_file and jd_text:
    resume_text = extract_text(resume_file)
    if resume_text:
        st.success("Files uploaded and text extracted successfully.")

        st.header("Step 2: Resume Evaluation")
        if st.button("Evaluate Resume"):
            with st.spinner("Evaluating Resume..."):
                prompt_eval = f"""
                Evaluate the following candidate resume against the provided job description. Determine the suitability of the candidate for the role, highlighting strengths and areas of improvement.

                Job Description:
                {jd_text}

                Candidate Resume:
                {resume_text}

                Provide a detailed evaluation.
                """
                evaluation = llm.invoke(prompt_eval)
                st.write(evaluation)

        st.header("Step 3: Interview Questions and Responses")
        if st.button("Generate Interview Questions"):
            with st.spinner("Generating Interview Questions..."):
                prompt_questions = f"""
                Based on the candidate's resume and the job description, generate 10 interview questions. Ensure a mix of technical and non-technical questions to assess the candidate comprehensively.

                Job Description:
                {jd_text}

                Candidate Resume:
                {resume_text}

                List the questions.
                """
                questions = llm.invoke(prompt_questions)
                question_list = questions.strip().split("\n")
                responses = []
                for idx, question in enumerate(question_list, 1):
                    st.subheader(f"Question {idx}")
                    st.write(question)
                    response = st.text_area(
                        f"Candidate's Response to Question {idx}", key=f"response_{idx}"
                    )
                    responses.append((question, response))
                    if response:
                        if st.button(f"Generate Follow-up Question {idx}"):
                            with st.spinner(f"Generating Follow-up Question {idx}..."):
                                prompt_follow_up = f"""
                                Based on the following interview question and the candidate's response, generate an appropriate follow-up question to delve deeper into the candidate's competencies.

                                Question:
                                {question}

                                Candidate Response:
                                {response}

                                Provide the follow-up question.
                                """
                                follow_up = llm.invoke(prompt_follow_up)
                                st.write(f"Follow-up Question {idx}: {follow_up}")

        st.header("Step 4: Coding Challenge")
        if st.button("Generate Coding Challenge"):
            with st.spinner("Generating Coding Challenge..."):
                prompt_coding = f"""
                Create a easy coding challenge suitable for the candidate based on the job description. The challenge should assess relevant technical skills required for the role.

                Job Description:
                {jd_text}

                Provide the coding challenge.
                """
                coding_challenge = llm.invoke(prompt_coding)
                st.write(coding_challenge)
                code_input = st.text_area("Candidate's Code Submission", height=200)
                if code_input:
                    if st.button("Evaluate Code Submission"):
                        with st.spinner("Evaluating Code Submission..."):
                            prompt_code_eval = f"""
                            Evaluate the following code submission for the given coding challenge. Provide feedback on correctness, efficiency, and coding style.

                            Coding Challenge:
                            {coding_challenge}

                            Candidate's Code:
                            {code_input}

                            Provide the evaluation.
                            """
                            code_evaluation = llm.invoke(prompt_code_eval)
                            st.write(code_evaluation)

        st.header("Step 5: Final Evaluation")
        if st.button("Generate Final Evaluation"):
            with st.spinner("Generating Final Evaluation..."):
                all_responses = ""
                for idx in range(1, 11):
                    question = st.session_state.get(f"response_{idx}_question", "")
                    response = st.session_state.get(f"response_{idx}", "")
                    if question and response:
                        all_responses += (
                            f"Question {idx}: {question}\nResponse: {response}\n\n"
                        )

                prompt_final_eval = f"""
                Based on the candidate's resume, responses to interview questions, follow-up questions, and performance on the coding challenge, provide a comprehensive evaluation of the candidate's suitability for the role.

                Job Description:
                {jd_text}

                Candidate Resume:
                {resume_text}

                Candidate Responses:
                {all_responses}

                Coding Challenge Submission:
                {code_input if 'code_input' in locals() else 'No submission provided.'}

                Provide the final evaluation.
                """
                final_evaluation = llm.invoke(prompt_final_eval)
                st.write(final_evaluation)
    else:
        st.error("Error extracting text from the uploaded resume.")
else:
    st.warning("Please upload the candidate's resume and enter the job description.")

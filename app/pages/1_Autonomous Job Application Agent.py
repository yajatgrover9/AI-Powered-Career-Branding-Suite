# -*- coding: utf-8 -*-
import os
import streamlit as st
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool

load_dotenv()

st.title("🚀 AI Job Hunter with CrewAI & Watsonx")

user_command = st.text_input(
    "What would you like help with?",
    placeholder="e.g. Analyze my resume or find ML jobs in Bangalore",
)
resume = ""  # to be implemented
role = st.text_input("Target Role", value="Data Scientist")
location = st.text_input("Preferred Job Location", value="")
experience = st.slider("Years of Experience", 0, 30, 3)

search_tool = SerperDevTool()

llm = LLM(
    model="watsonx/meta-llama/llama-3-3-70b-instruct",
    api_key=os.getenv("WATSONX_APIKEY"),
)

resume_analyzer = Agent(
    role="Resume Expert",
    goal="Analyze resumes and suggest improvements",
    backstory="An expert recruiter trained on thousands of top-performing resumes.",
    verbose=True,
    llm=llm,
)

job_finder = Agent(
    role="Job Research Assistant",
    goal="Find jobs matching user preferences",
    backstory="An assistant that can perform real-time web searches for jobs.",
    tools=[search_tool],
    verbose=True,
    llm=llm,
)

application_strategy = Agent(
    role="Application Coach",
    goal="Write professional cover letters tailored to job roles",
    backstory="A language expert who crafts compelling job applications.",
    verbose=True,
    llm=llm,
)

task_selector_agent = Agent(
    role="Task Classifier",
    goal="Understand user's input and decide the tasks",
    backstory="An AI assistant that intelligently chooses which job-related task to run.",
    verbose=True,
    llm=llm,
)

if st.button("Execute Smart Agent"):
    with st.spinner("Working on your request..."):

        selection_task = Task(
            description=f"""Classify the user's input into one or more of the following tasks:
            - analyze_resume
            - find_jobs
            - generate_letter

            Input: {user_command}

            Return a comma-separated list of task IDs (e.g., analyze_resume,find_jobs).""",
            agent=task_selector_agent,
            expected_output="Comma-separated task IDs like: analyze_resume,find_jobs",
        )

        selection_crew = Crew(
            agents=[task_selector_agent], tasks=[selection_task], verbose=False
        )

        selected_tasks_output = selection_crew.kickoff()
        selected_tasks = [selected_tasks_output.raw]
        print("=======================")
        print(selected_tasks)
        print("=======================")

        task_pool = {
            "find_jobs": Task(
                description=f"""Search for the latest 5 job listings for the role '{role}' in '{location}' with around {experience} years of experience.
                Focus on relevant, remote-friendly listings if possible. Include job title and links.""",
                agent=job_finder,
                expected_output="Top 5 job listings with titles, companies, and URLs.",
            ),
            "analyze_resume": Task(
                description=f"""Review the following resume:\n\n{resume}\n\nSuggest missing skills and formatting improvements.""",
                agent=resume_analyzer,
                expected_output="Missing skills and resume formatting suggestions.",
            ),
            "generate_letter": Task(
                description=f"""Based on the resume:\n\n{resume}\n\nWrite a personalized cover letter for a {role} position in {location}.
                Tone should be professional but friendly.""",
                agent=application_strategy,
                expected_output="Tailored cover letter for job application.",
            ),
        }

        selected_task_objs = [task_pool[task_id] for task_id in selected_tasks]

        if selected_task_objs:
            crew = Crew(
                agents=[resume_analyzer, job_finder, application_strategy],
                tasks=selected_task_objs,
                verbose=True,
            )

            results = crew.kickoff()
            st.success("✅ Tasks completed!")

            for i, task_id in enumerate(selected_tasks):
                if task_id == "find_jobs":
                    st.subheader("🔍 Job Listings")
                elif task_id == "analyze_resume":
                    st.subheader("📝 Resume Analysis")
                elif task_id == "generate_letter":
                    st.subheader("📨 Cover Letter")

                st.write(results.raw)
        else:
            st.warning(
                "🤔 Couldn't determine what task to run. Try rephrasing your command."
            )

# -*- coding: utf-8 -*-
import os
import requests
import streamlit as st
from dotenv import load_dotenv
from services.genai_services import genai_response
from services.prompt import resume_builder_prompt

load_dotenv()

proxycurl_api_key = os.getenv("PROXYCURL_API_KEY")

st.set_page_config(page_title="Smart Resume Builder", layout="wide")
st.title("AI-Driven Resume & Portfolio Builder")

st.markdown(
    """
Fetch your LinkedIn profile and generate a resume using AI.
"""
)

username = st.text_input("Enter your LinkedIn username (e.g. johndoe)")

if st.button("Submit"):
    if username:
        linkedin_url = f"https://www.linkedin.com/in/{username}"
        headers = {
            "Authorization": f"Bearer {proxycurl_api_key}",
        }
        params = {
            "url": linkedin_url,
            "use_cache": "if-present",
        }

        with st.spinner("Fetching LinkedIn profile..."):
            response = requests.get(
                "https://nubela.co/proxycurl/api/v2/linkedin",
                params=params,
                headers=headers,
            )

        if response.status_code == 200:
            data = response.json()

            with st.spinner("Generating Portfolio..."):
                res = genai_response(resume_builder_prompt(data))["res"]
                print(res)
                response = requests.post(os.getenv("SCRIPT_URL"), json=data)
                doc_link = response.json().get("link")
            st.success("✅ Digital Portfolio Created!")
            st.markdown(
                f"[📄 View your generated portfolio here ]({doc_link})",
                unsafe_allow_html=True,
            )

        else:
            st.error(f"❌ Failed to fetch profile. Status Code: {response.status_code}")
    else:
        st.error("❌ Please enter username")

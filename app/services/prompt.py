# -*- coding: utf-8 -*-
sample_data = {
    "name": "Bill Gates",
    "headline": "Chair, Gates Foundation and Founder, Breakthrough Energy",
    "location": "Seattle, Washington, US",
    "email": "bill@example.com",
    "summary": "Chair of the Gates Foundation. Founder of Breakthrough Energy. Co-founder of Microsoft.",
    "experience": "- Co-chair at Gates Foundation\n- Founder at Breakthrough Energy\n- Co-founder at Microsoft",
    "education": "- Harvard University\n- Lakeside School",
}


def resume_builder_prompt(resume_data):
    prompt = f"""
Please take the provided data and format it into a professional resume / digital portfolio.

### Input Data:
{resume_data}

### Expected Output Format:
Return the result as a **Python dictionary** with a single key `res`, like this:

{{
  "res": {{
    "name": "Bill Gates",
    "headline": "Chair, Gates Foundation and Founder, Breakthrough Energy",
    "location": "Seattle, Washington, US",
    "email": "bill@example.com",
    "summary": "Chair of the Gates Foundation. Founder of Breakthrough Energy. Co-founder of Microsoft.",
    "experience": "- Co-chair at Gates Foundation\\n- Founder at Breakthrough Energy\\n- Co-founder at Microsoft",
    "education": "- Harvard University\\n- Lakeside School"
  }}
}}

If any fields are missing or not found in the input, return `"NA"` as the value.
"""
    return prompt

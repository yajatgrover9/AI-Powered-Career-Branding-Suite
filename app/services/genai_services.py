# -*- coding: utf-8 -*-
import os
from langchain_ibm import WatsonxLLM
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames
from dotenv import load_dotenv

load_dotenv()

parameters = {
    GenTextParamsMetaNames.DECODING_METHOD: "greedy",
    GenTextParamsMetaNames.MAX_NEW_TOKENS: 500,
    GenTextParamsMetaNames.MIN_NEW_TOKENS: 1,
    GenTextParamsMetaNames.TEMPERATURE: 0.1,
    GenTextParamsMetaNames.TOP_K: 50,
    GenTextParamsMetaNames.TOP_P: 1,
}
llm = WatsonxLLM(
    model_id="meta-llama/llama-3-3-70b-instruct",
    project_id=os.getenv("WATSONX_PROJECT_ID"),
    params=parameters,
)


def genai_response(prompt):
    """
    Function to generate AI response
    """
    response = llm.invoke(prompt)
    return response

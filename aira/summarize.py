from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langgraph.graph import StateGraph, START, END
import os
import dotenv


def convertnotes(data):

    # Extract the notes from the input dictionary

    # print(data["visit_history"])

    notes = data["visit_history"][-1]["ClinicalNotes"]  # Assuming the last visit's notes are to be summarized

    dotenv.load_dotenv()

    llm = OpenAI(temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"))

    prompt = PromptTemplate(
            input_variables=notes,
            template="""
            You are a clinical assistant who is tasked with converting raw clinical notes into a SOAP format

            Notes:
            {notes}


            Please summarize the notes in a SOAP format
            Subjective:
            Objective: 
            Assessment: 
            Plan sections:
            """,
        )

    # Now we will chain the LLM with the prompt using the pipe operator
    chain = prompt | llm  # Chain the prompt and the LLM
    return chain.invoke(notes)  # Invoke the chain with the input notes








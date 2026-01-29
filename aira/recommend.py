import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate    
from langchain.chains import LLMChain
from langgraph.graph import StateGraph, START, END
import dotenv


def invokerecommendation(data):

    print("******************************Referral Recommendation***************************")
    print("Input data for referral recommendation:", data)
    # print(data["visit_history"][-1]["summary"])


    transcription = data["transcription"] # Extract the summary from the input dictionary


    print("******************************printing transcription in referral recommendation***************************")
    print([transcription])

    dotenv.load_dotenv()
    llm = OpenAI(temperature = 0.7, openai_api_key= os.getenv("OPENAI_API_KEY"))

    prompt = PromptTemplate(
    input_variables = [transcription],
    template = """
   
    You are a clinical AI assistant tasked with analyzing a patient’s clinical journey based on their transcription history, which includes visit details, clinical notes, referrals, and doctor decisions.

    Your job is to:
    1. Understand the patient’s condition based on the provided transcription.
    2. Determine whether a referral to a specialist (Be specific about specialist such as cardiologist, pulmonologist) or further diagnostic testing is necessary.
    3. If the patient has already been referred to a specialist for the current condition (check that in the transcript conversation), do not suggest another referral.
    4. If the current specialist is capable of handling the case (e.g., general physician for common illnesses), provide a treatment recommendation instead of a referral.
    5. Recommend only necessary follow-up actions (e.g., blood test, CT scan, medication) appropriate to the current visit.

    {transcription}
    
    Recommendation:
    """,
    )

    recommendation_chain = prompt | llm  # Chain the prompt and the LLM

    recommend = recommendation_chain.invoke({"transcription": transcription})

    print("******************************Referral recommendation generated successfully!***************************")
    print(recommend)

    while True:
        print("\n******************************Decision Making***************************")
 
        decision = input("\nDo you want to accept the recommendation? (yes/no): ").strip().lower()

        if decision == 'yes':
            result = "Referral to the specialist will be made based on the recommendation"
            # data.update({"recommendation": recommend, "decision": result})
            # return data
            return {"recommendation": recommend, "recommended": True}
        elif decision == 'no':
            result = "No referral needed at this time."
            # data.update({"recommendation": recommend, "decision": result})
            return {"recommendation": recommend, "recommended": False}
        elif decision != 'yes' or decision != 'no':
            print ("Invalid input. Please enter 'yes' or 'no'.")
      # Return the updated data with the recommendation and decision
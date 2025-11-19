# AIRA_MedAssist
AI-powered healthcare assistant that helps doctors streamline clinical documentation, summarize EHR data, and automate patient referral notes using natural language processing and contextual memory. Built with LangChain, LangGraph, and MCP principles for intelligent conversational workflows.


# AIRA MedAssist – AI-Powered Clinical Documentation Assistant  

![AIRA MedAssist Banner](/mnt/data/A_2D_digital_graphic_design_illustrates_Flight_Pri.png)

![LangChain](https://img.shields.io/badge/Framework-LangChain-blue)
![LangGraph](https://img.shields.io/badge/Engine-LangGraph-green)
![OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI-ffcc00)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

## Overview  

AIRA MedAssist (AI-Enabled Referral & Assessment Medical Assistant) is a conversational clinical documentation system that assists doctors in summarizing patient notes, generating SOAP-formatted reports, and recommending referrals to specialists.  

The system integrates LangChain, LangGraph, and OpenAI’s LLMs to automate the clinical documentation process and streamline Electronic Health Record (EHR) updates, ensuring accuracy and efficiency in patient care.

---

## Objectives  

- Automate the conversion of unstructured clinical notes into structured SOAP (Subjective, Objective, Assessment, Plan) format.  
- Assist healthcare professionals by generating referral recommendations using AI reasoning.  
- Store and retrieve patient visit history for contextualized follow-ups.  
- Enhance clinical decision-making with context-aware documentation memory.

---

## Features  

- AI-Powered Summarization: Converts clinical notes into SOAP format using OpenAI’s LLM.  
- Conversational Workflow: Built using LangGraph and LangChain Memory for contextual interactions.  
- Referral Recommendation: Suggests specialist referrals or diagnostic actions.  
- Patient Database Management: Stores and retrieves visit history using unique health card IDs.  
- JSON-Based EHR Storage: Automatically saves visit transcripts and summaries for reuse.  
- Automated Workflow Graph: Executes each stage (collect → summarize → recommend → store) sequentially.  

---

## System Workflow  

1. Collect Patient Details  
   - Doctor enters basic info (name, specialization, patient ID, clinical notes).  
   - System checks existing records or creaes a new one.  

2. Summarize Clinical Notes  
   - The `summarize.py` module converts raw notes into SOAP format via an OpenAI model.  

3. Generate Referral Recommendation  
   - The `recommend.py` module uses transcription data and doctor context to suggest referrals or tests.  

4. Save Updated Record  
   - Processed data is stored as a structured JSON file in the `patient_db/` folder for future retrieval.  

---

## Architecture  

```mermaid
flowchart TD
A[Start] --> B[Collect Patient Details]
B --> C[Summarize Clinical Notes]
C --> D[Generate Referral Recommendation]
D --> E[Save to patient_db JSON]
E --> F[End]

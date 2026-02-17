from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from PIL import Image
import io
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze")
async def analyze_malware(
    file: UploadFile = File(...), 
    stated_purpose: str = Form(...)
):
    try:
        image_data = await file.read()
        app_screenshot = Image.open(io.BytesIO(image_data))
        
        
        prompt = f"""
        You are an elite Mobile Threat Intelligence Analyst. 
        The developer claims this application is a: "{stated_purpose}".
        
        Analyze the provided iOS app screenshot. 
        Task: Determine if the visual UI matches the stated purpose of the app, or if it exhibits UI deception, phishing, or credential harvesting (e.g., a flashlight app showing a bank login).
        
        Output your response in STRICT JSON format with NO markdown formatting. 
        You MUST use exactly these three keys: 
        1. "Threat_Score": An integer from 0 to 100 (where 100 is critical malware, and 0 is perfectly safe).
        2. "Classification": A short category name (e.g., 'Phishing', 'Benign').
        3. "Analysis": A concise, 2 to 3 sentence explanation of why the UI does or does not match the stated purpose.
        """
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[prompt, app_screenshot]
        )
        
        clean_text = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_text)
        
    except Exception as e:
        print(f"\n[ERROR] Backend crashed: {e}")
        return {
            "Threat_Score": "ERR", 
            "Classification": "Backend Error", 
            "Analysis": f"Error: {str(e)}"
        }
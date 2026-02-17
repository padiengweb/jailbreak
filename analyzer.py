import json
import os
from dotenv import load_dotenv
from PIL import Image
from google import genai

# 1. Securely load the API key from the .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# 2. Initialize the new modern GenAI client
client = genai.Client(api_key=API_KEY)

def analyze_sandbox_behavior(image_path, system_logs):
    print(f"[*] Loading sandbox visual snapshot: {image_path}")
    
    try:
        app_screenshot = Image.open(image_path)
    except FileNotFoundError:
        return f"[!] Error: Could not find '{image_path}'. Make sure the image is in the same folder!"
    
    prompt = f"""
    You are an elite Mobile Threat Intelligence Analyst. 
    Analyze the provided iOS app screenshot and cross-reference it with the following sandbox system logs.
    
    RAW SANDBOX LOGS:
    {json.dumps(system_logs, indent=2)}
    
    Task: Determine if the visual UI matches the background code behavior. 
    Specifically look for UI deception, phishing, credential harvesting, or unauthorized network access.
    
    Output your response in strict JSON format with the following keys:
    - "Threat_Score": (0-100)
    - "Classification": (e.g., 'Benign', 'Phishing', 'Spyware')
    - "Analysis": (A 2-sentence explanation of the discrepancy)
    """
    
    print("[*] Sending multimodal payload (Image + Logs) to AI for analysis...")
    
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=[prompt, app_screenshot]
    )
    
    return response.text

if __name__ == "__main__":
    
    
    mock_system_logs = {
        "timestamp": "2026-02-17T17:45:00Z",
        "app_name": "FlashlightPlus",
        "events": [
            {"action": "UI_RENDER", "element": "Apple ID Login Prompt"},
            {"action": "KEYCHAIN_ACCESS", "status": "DENIED"},
            {"action": "NETWORK_REQUEST", "destination": "http://194.55.2.1/login.php", "method": "POST", "payload": "plaintext"}
        ]
    }

    print("--- JAILBREAK: MULTIMODAL SANDBOX ANALYSIS ---")
    result = analyze_sandbox_behavior("fake_login.jpg", mock_system_logs)
    print("\n[+] THREAT INTELLIGENCE REPORT:")
    print(result)
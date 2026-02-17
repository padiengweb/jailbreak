# 🛡️ Jailbreak: Multimodal AI Threat Analysis Pipeline

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.103.0-009688.svg)](https://fastapi.tiangolo.com/)
[![AI](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-orange.svg)]()
[![Security](https://img.shields.io/badge/Security-Threat%20Intel-red.svg)]()

> **Jailbreak is an enterprise-grade threat intelligence sandbox that defeats mobile malware, UI deception, and credential harvesting by performing dynamic Intent vs. Behavior analysis using Google's multimodal AI.**

🎥 **[Watch the Video](https://www.youtube.com/watch?v=1YLxUnbBVO8)**

---

## 🔐 The Solution: Intent vs. Behavior
1. **The Stated Intent:** The threat analyst inputs what the suspicious application claims to do (e.g., "A basic calculator"). 
2. **The Visual Payload:** A screenshot of the application running in an isolated sandbox is uploaded to the system. 
3. **Multimodal Analysis:** Google's Gemini 2.5 Flash AI instantly cross-references the app's visual UI behavior against its stated purpose.
4. **Anomaly Detection:** If an application lies about its intent (e.g., a flashlight app rendering a pixel-perfect fake Apple ID login), the system catches the behavioral mismatch, bypasses visual deception, and dynamically flags the threat.

---

## 🏗️ Enterprise Threat Analysis Pipeline
Modern threat intelligence requires structured, machine-readable outputs. Jailbreak is built with a streamlined AI pipeline that transforms visual anomalies into strict, classified JSON threat data for SOC teams.

* **Frontend Dashboard:** HTML/JS interface for secure analyst input and multimodal payload uploads.
* **API Backend:** Python FastAPI server handling payload validation and strict prompt engineering constraints.
* **AI Engine:** Google Gemini 2.5 Flash performing multimodal intent analysis.
* **Threat Intelligence Feed:** Strict JSON output containing a severity score (0-100), classification category, and analysis summary.

<img width="100%" alt="Jailbreak Architecture Diagram" src="images/readmejailbreak.png" />

---

## 💻 How to Run Locally

**1. Clone the repository**
```bash
git clone [https://github.com/padiengweb/jailbreak.git](https://github.com/padiengweb/jailbreak.git)
cd jailbreak
create a .env file get your api key
pip install fastapi uvicorn google-genai pillow python-dotenv python-multipart
uvicorn main:app --reload --port 8888 (I used this port because of admin access issues)

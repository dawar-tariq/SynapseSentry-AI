# 🛡️ SynapseSentry AI
### Autonomous Code Vulnerability Reasoning & Self-Healing Sentry
**An Official Submission for the Nebius × NVIDIA Global AI Hackathon**  
**Lead Architect & Developer:** Dawar Tariq

---

## 📌 Executive Summary
**SynapseSentry AI** is an autonomous security intelligence and self-healing remediation agent created by **Dawar Tariq**. Powered by **NVIDIA Nemotron (`nvidia/llama-3.1-nemotron-70b-instruct`)** on **Nebius Token Factory**, SynapseSentry continuously inspects source code for zero-days, logic flaws, and OWASP Top 10 exploits, calculates a dynamic Security Health Index, and autonomously produces unified `git diff` patch files ready for immediate deployment.

SynapseSentry is built with a lightweight, zero-overhead architecture capable of running entirely in lightweight developer workflows, including mobile developer environments (Android via **Termux** and **Acode**), local workstations, or cloud environments.

---

## 🏆 Hackathon Alignment
- **Track:** Coding and Agentic Engineering / Best Apps and Agents
- **Bonus Track Eligibility:** **Best Use of Tavily ($3,000 Prize)**
- **Core Model:** NVIDIA Nemotron-70B-Instruct (`nvidia/llama-3.1-nemotron-70b-instruct`)
- **Infrastructure:** Nebius Token Factory & NVIDIA NIM
- **Threat Intelligence:** Tavily Real-Time Search API
- **License:** MIT Open Source License

---

## ⚡ Key Capabilities
1. **Autonomous Vulnerability Decomposition:** Pinpoints critical flaws including SQL Injection (CWE-89), Command Injection / RCE (CWE-78), and Plaintext Credential Exposure (CWE-798).
2. **Live Threat Intelligence Feed (Tavily AI):** Automatically queries live global CVE databases (NVD, MITRE, SentinelOne) via the Tavily Search API to pull up-to-the-minute exploitation bulletins for every identified flaw.
3. **1-Click Auto-Remediation & Score Jump:** When security vulnerabilities are identified, developers can click **"⚡ Load & Test Safe Code"** to immediately inject AI-hardened code and watch their Security Health Index jump from **Critical (44/100) to 100/100 Safe**.
4. **Unified Self-Healing Git Diffs:** Synthesizes standard `git apply`-compatible patches that replace dangerous functions with safe prepared statements and environment variables.
5. **Mobile & Termux Ready:** Built with pure Python 3 and modern CSS/HTML — zero heavy build chains or native compilation required.

---

## 🚀 Quickstart & Setup Guide

### 1. Requirements
- Python 3.10+
- `pip install -r requirements.txt`

### 2. Configure Environment (`.env`)
```bash
cp .env.example .env
```
Edit `.env` with your API credentials:
```ini
AI_PROVIDER=nebius
NEBIUS_API_KEY=your_nebius_api_key_here
NEBIUS_BASE_URL=https://api.tokenfactory.nebius.com/v1
NEBIUS_MODEL=nvidia/llama-3.1-nemotron-70b-instruct

# Alternative NVIDIA NIM endpoint
NVIDIA_API_KEY=your_nvidia_api_key_here
```

### 3. Launch Sentry
```bash
python app.py
```
Visit `http://localhost:8000` in any web browser.

---

## 📱 Mobile Workflow (Termux + Acode)
1. Open Termux:
   ```bash
   pkg update && pkg install python git -y
   git clone <your-repo>
   cd nemoguard-sentry
   pip install -r requirements.txt
   python app.py
   ```
2. Open `http://localhost:8000` in your mobile browser.
3. Edit source code on the go using **Acode editor**.

---

## 🎥 3-Minute Video Demo Script (For Devpost)

- **0:00 – 0:30 (Problem):** Introduce the exponential rise of software supply chain and code-level vulnerabilities, and how manual reviews create massive delivery bottlenecks.
- **0:30 – 1:15 (Architecture):** Introduce **SynapseSentry AI**. Explain how it leverages **NVIDIA Nemotron-70B** on **Nebius Token Factory** to perform chain-of-thought semantic decomposition and vulnerability reasoning.
- **1:15 – 2:15 (Live Demo):** 
  1. Show the clean Web UI.
  2. Click **"Analyze & Auto-Remediate"**.
  3. Highlight the calculated Security Health Score, the breakdown of CWE-89 (SQLi) and CWE-78 (RCE), and the auto-generated Git patch diff.
  4. Demonstrate copying the patch and applying it.
- **2:15 – 2:45 (Mobile & Open Infrastructure):** Highlight that the entire system is lightweight enough to run directly on an Android device via Termux + Acode while communicating with open GPU infrastructure.
- **2:45 – 3:00 (Conclusion):** Reiterate the mission: autonomous self-healing software security powered by NVIDIA and Nebius.

---

## 📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

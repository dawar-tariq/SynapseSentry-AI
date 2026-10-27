import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from agent import SynapseSentryEngine
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="SynapseSentry AI", version="10.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AuditRequest(BaseModel):
    code: str
    filename: Optional[str] = "auth_controller.py"

ULTRA_TIER_UI = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>SynapseSentry AI — World-Class Autonomous Cybersecurity Agent</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-deep: #03060a;
      --bg-surface: rgba(10, 14, 24, 0.7);
      --bg-surface-elevated: rgba(16, 23, 38, 0.85);
      --bg-code: #05070d;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-active: rgba(118, 185, 0, 0.4);
      --nvidia-green: #76b900;
      --nvidia-bright: #98e800;
      --nvidia-glow: rgba(118, 185, 0, 0.35);
      --nvidia-dim: rgba(118, 185, 0, 0.12);
      --cyan: #38bdf8;
      --cyan-glow: rgba(56, 189, 248, 0.3);
      --purple: #c084fc;
      --purple-dim: rgba(192, 132, 252, 0.12);
      --danger: #ff4757;
      --danger-dim: rgba(255, 71, 87, 0.14);
      --warning: #ffa502;
      --warning-dim: rgba(255, 165, 2, 0.14);
      --success: #10b981;
      --success-dim: rgba(16, 185, 129, 0.14);
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 18px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    body {
      background-color: var(--bg-deep);
      background-image: 
        radial-gradient(circle at 15% 0%, rgba(118, 185, 0, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 85% 100%, rgba(56, 189, 248, 0.08) 0%, transparent 50%),
        linear-gradient(180deg, rgba(3, 6, 10, 0.8) 0%, #03060a 100%);
      color: var(--text);
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }

    /* Ambient Cyber Background Grid */
    body::before {
      content: "";
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background-image: linear-gradient(rgba(255, 255, 255, 0.015) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
      background-size: 40px 40px;
      pointer-events: none;
      z-index: 0;
    }

    /* Top Cyber Command Header */
    header {
      background: rgba(8, 12, 20, 0.82);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border-bottom: 1px solid var(--border-subtle);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 12px 24px;
    }

    .nav-container {
      max-width: 1560px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      position: relative;
      z-index: 1;
    }

    .brand-cluster {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .brand-icon-shield {
      width: 42px;
      height: 42px;
      border-radius: 11px;
      background: linear-gradient(135deg, rgba(118, 185, 0, 0.25) 0%, rgba(118, 185, 0, 0.03) 100%);
      border: 1px solid var(--nvidia-green);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 25px var(--nvidia-glow);
      position: relative;
    }

    .brand-icon-shield svg {
      width: 24px;
      height: 24px;
      fill: var(--nvidia-bright);
    }

    .brand-text h1 {
      font-size: 19px;
      font-weight: 800;
      letter-spacing: -0.6px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .brand-text h1 span {
      background: linear-gradient(135deg, #76b900 0%, #a3e635 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .brand-meta {
      font-size: 11px;
      color: var(--text-muted);
      font-weight: 500;
      letter-spacing: 0.3px;
    }

    .header-badges {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .status-capsule {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 11px;
      font-weight: 600;
      font-family: 'JetBrains Mono', monospace;
      background: rgba(118, 185, 0, 0.08);
      border: 1px solid rgba(118, 185, 0, 0.3);
      color: var(--nvidia-bright);
    }

    .pulse-emitter {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--nvidia-green);
      box-shadow: 0 0 10px var(--nvidia-green);
      animation: pulseAnim 2s infinite ease-in-out;
    }

    @keyframes pulseAnim {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.3; transform: scale(0.8); }
    }

    /* Main Grid */
    main {
      flex: 1;
      max-width: 1560px;
      width: 100%;
      margin: 0 auto;
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 20px;
      position: relative;
      z-index: 1;
    }

    /* Telemetry HUD Strip */
    .telemetry-strip {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 14px;
    }

    .telemetry-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      backdrop-filter: blur(16px);
      display: flex;
      flex-direction: column;
      gap: 4px;
      position: relative;
      overflow: hidden;
      transition: all 0.25s ease;
    }

    .telemetry-card:hover {
      border-color: rgba(255, 255, 255, 0.18);
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }

    .telemetry-card::before {
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0; height: 1px;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    }

    .telemetry-label {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.7px;
      color: var(--text-dim);
    }

    .telemetry-value {
      font-size: 20px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.4px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* 2-Column Split Console */
    .console-split {
      display: grid;
      grid-template-columns: 1fr;
      gap: 20px;
    }

    @media(min-width: 1100px) {
      .console-split {
        grid-template-columns: 1.02fr 0.98fr;
      }
    }

    /* Glass Panels */
    .glass-deck {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      backdrop-filter: blur(20px);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
    }

    .deck-header {
      padding: 14px 20px;
      background: rgba(16, 23, 38, 0.65);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .deck-title {
      font-size: 13px;
      font-weight: 700;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .deck-chip {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      background: var(--bg-code);
      border: 1px solid var(--border-subtle);
      color: var(--cyan);
      padding: 4px 10px;
      border-radius: 6px;
    }

    .deck-body {
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      flex: 1;
    }

    /* Interactive Self-Healing Banner */
    .self-healing-banner {
      display: none;
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.15) 0%, rgba(118, 185, 0, 0.15) 100%);
      border: 1px solid rgba(56, 189, 248, 0.45);
      border-radius: var(--radius-sm);
      padding: 14px 18px;
      justify-content: space-between;
      align-items: center;
      gap: 14px;
      box-shadow: 0 0 25px rgba(56, 189, 248, 0.2);
      animation: slideDown 0.3s ease;
    }

    @keyframes slideDown {
      from { opacity: 0; transform: translateY(-8px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .banner-left {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }

    .banner-heading {
      font-size: 13px;
      font-weight: 800;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .banner-desc {
      font-size: 11px;
      color: var(--text-muted);
    }

    .btn-remediate-instant {
      background: linear-gradient(135deg, #06b6d4 0%, #0284c7 100%);
      color: #ffffff;
      border: none;
      padding: 9px 18px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 0 16px var(--cyan-glow);
      transition: all 0.2s;
      white-space: nowrap;
    }

    .btn-remediate-instant:hover {
      background: linear-gradient(135deg, #22d3ee 0%, #0369a1 100%);
      transform: scale(1.02);
    }

    /* Terminal Console */
    .cyber-console {
      background: var(--bg-code);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      flex: 1;
      min-height: 420px;
      box-shadow: inset 0 3px 14px rgba(0, 0, 0, 0.7);
    }

    .console-chrome {
      padding: 9px 16px;
      background: rgba(255, 255, 255, 0.025);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: var(--text-dim);
    }

    .window-controls {
      display: flex;
      gap: 6px;
    }

    .circle-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
    }
    .c-red { background: #ff5f56; }
    .c-yellow { background: #ffbd2e; }
    .c-green { background: #27c93f; }

    textarea#codeEditor {
      flex: 1;
      width: 100%;
      background: transparent;
      border: none;
      color: #f1f5f9;
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      line-height: 1.6;
      padding: 16px;
      outline: none;
      resize: none;
    }

    /* Action Strip */
    .action-matrix {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }

    .btn-primary-trigger {
      flex: 1;
      min-width: 220px;
      background: linear-gradient(135deg, #76b900 0%, #5d9300 100%);
      color: #03060a;
      border: none;
      border-radius: var(--radius-sm);
      padding: 14px 24px;
      font-size: 14px;
      font-weight: 800;
      letter-spacing: 0.3px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      box-shadow: 0 4px 25px var(--nvidia-glow);
      transition: all 0.25s ease;
    }

    .btn-primary-trigger:hover {
      background: linear-gradient(135deg, #88d600 0%, #6da900 100%);
      transform: translateY(-2px);
      box-shadow: 0 8px 32px rgba(118, 185, 0, 0.5);
    }

    .btn-primary-trigger:disabled {
      opacity: 0.6;
      cursor: not-allowed;
      transform: none;
    }

    .btn-preset-load {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      border-radius: var(--radius-sm);
      padding: 14px 20px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }

    .btn-preset-load:hover {
      background: rgba(255, 255, 255, 0.1);
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.2);
    }

    /* Right Panel HUD */
    .health-telemetry-box {
      background: linear-gradient(135deg, rgba(16, 23, 38, 0.75) 0%, rgba(10, 14, 24, 0.95) 100%);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 18px 22px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }

    .score-summary-col {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .score-header-label {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--text-dim);
    }

    .risk-tag-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 13px;
      font-weight: 800;
      padding: 4px 12px;
      border-radius: 6px;
      width: fit-content;
    }

    .tag-Critical, .tag-High {
      background: var(--danger-dim);
      color: var(--danger);
      border: 1px solid rgba(255, 71, 87, 0.4);
    }

    .tag-Safe, .tag-Low {
      background: var(--success-dim);
      color: var(--success);
      border: 1px solid rgba(16, 185, 129, 0.4);
    }

    .circular-dial {
      width: 82px;
      height: 82px;
      border-radius: 50%;
      border: 4px solid var(--danger);
      box-shadow: 0 0 25px rgba(255, 71, 87, 0.3);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: var(--bg-code);
      transition: all 0.35s ease;
    }

    .circular-dial.dial-safe {
      border-color: var(--success);
      box-shadow: 0 0 25px rgba(16, 185, 129, 0.3);
    }

    .dial-val {
      font-size: 28px;
      font-weight: 800;
      color: #ffffff;
      font-family: 'JetBrains Mono', monospace;
      line-height: 1;
    }

    .dial-max {
      font-size: 9px;
      color: var(--text-dim);
      font-weight: 600;
      margin-top: 2px;
    }

    /* Tavily Live Threat Bulletin */
    .tavily-card-intel {
      display: none;
      background: linear-gradient(135deg, rgba(192, 132, 252, 0.1) 0%, rgba(147, 51, 234, 0.05) 100%);
      border: 1px solid rgba(192, 132, 252, 0.4);
      border-radius: var(--radius-sm);
      padding: 14px 18px;
      font-size: 12px;
      line-height: 1.55;
      color: #f3e8ff;
      animation: slideDown 0.3s ease;
    }

    .tavily-top-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }

    .tavily-title {
      font-weight: 700;
      color: #e9d5ff;
      font-size: 12px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .tavily-verified-chip {
      font-size: 10px;
      font-weight: 700;
      background: rgba(192, 132, 252, 0.25);
      border: 1px solid rgba(192, 132, 252, 0.4);
      color: #f3e8ff;
      padding: 2px 8px;
      border-radius: 4px;
    }

    /* Executive Synthesis Card */
    .executive-card {
      background: var(--bg-code);
      border: 1px solid var(--border-subtle);
      border-left: 3px solid var(--cyan);
      border-radius: var(--radius-sm);
      padding: 14px 16px;
      font-size: 13px;
      line-height: 1.6;
      color: #cbd5e1;
    }

    /* Section Subtitle */
    .subhead-label {
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--text-dim);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    /* Vulnerabilities Stream */
    .findings-container {
      display: flex;
      flex-direction: column;
      gap: 10px;
      max-height: 220px;
      overflow-y: auto;
      padding-right: 4px;
    }

    .finding-card {
      background: var(--bg-code);
      border: 1px solid var(--border-subtle);
      border-left: 3px solid var(--danger);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      transition: all 0.2s;
    }

    .finding-card:hover {
      border-color: rgba(255, 255, 255, 0.2);
      transform: translateX(2px);
    }

    .finding-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .finding-title {
      font-size: 13px;
      font-weight: 700;
      color: #ffffff;
    }

    .finding-severity {
      font-size: 10px;
      font-weight: 800;
      text-transform: uppercase;
      padding: 2px 7px;
      border-radius: 4px;
      background: var(--danger-dim);
      color: var(--danger);
      border: 1px solid rgba(255, 71, 87, 0.35);
    }

    .finding-meta {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: var(--cyan);
      display: flex;
      gap: 10px;
    }

    .finding-rec {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: #94a3b8;
      background: rgba(255, 255, 255, 0.03);
      padding: 6px 10px;
      border-radius: 4px;
    }

    /* Unified Git Diff Terminal */
    .diff-deck {
      background: var(--bg-code);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }

    .diff-deck-header {
      padding: 8px 14px;
      background: rgba(255, 255, 255, 0.03);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: var(--text-dim);
    }

    .btn-copy-unified {
      background: var(--nvidia-dim);
      border: 1px solid rgba(118, 185, 0, 0.35);
      color: var(--nvidia-bright);
      font-weight: 700;
      font-size: 11px;
      padding: 4px 12px;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.2s;
    }

    .btn-copy-unified:hover {
      background: var(--nvidia-green);
      color: #000;
    }

    pre.diff-output-pre {
      padding: 14px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      line-height: 1.6;
      color: #cbd5e1;
      overflow-x: auto;
      max-height: 180px;
      white-space: pre;
    }

    /* Enterprise Footer */
    footer {
      border-top: 1px solid var(--border-subtle);
      background: rgba(3, 6, 10, 0.98);
      padding: 16px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12px;
      color: var(--text-dim);
      flex-wrap: wrap;
      gap: 12px;
      position: relative;
      z-index: 1;
    }

    footer a { color: var(--nvidia-bright); text-decoration: none; font-weight: 600; }

    /* Custom Scrollbars */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.12); border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(255, 255, 255, 0.25); }
  </style>
</head>
<body>

  <!-- Navigation -->
  <header>
    <div class="nav-container">
      <div class="brand-cluster">
        <div class="brand-icon-shield">
          <svg viewBox="0 0 24 24">
            <path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-9-5zm0 18c-3.75-1.07-6.72-5.07-6.97-9.5h13.94c-.25 4.43-3.22 8.43-6.97 9.5z"/>
          </svg>
        </div>
        <div class="brand-text">
          <h1>SynapseSentry <span>AI</span></h1>
          <div class="brand-meta">Autonomous Zero-Day & Auto-Remediation Sentry</div>
        </div>
      </div>

      <div class="header-badges">
        <span class="status-capsule">
          <span class="pulse-emitter"></span>
          NVIDIA Nemotron 70B
        </span>
        <span class="status-capsule" style="border-color: rgba(56, 189, 248, 0.35); color: var(--cyan); background: rgba(56, 189, 248, 0.1);">
          Nebius Token Factory
        </span>
        <span class="status-capsule" style="border-color: rgba(192, 132, 252, 0.35); color: var(--purple); background: var(--purple-dim);">
          Tavily Live Threat Feed Active
        </span>
      </div>
    </div>
  </header>

  <main>
    <!-- Telemetry HUD Strip -->
    <section class="telemetry-strip">
      <div class="telemetry-card">
        <span class="telemetry-label">Reasoning Engine</span>
        <span class="telemetry-value" style="color: var(--nvidia-bright);">Nemotron-70B</span>
      </div>
      <div class="telemetry-card">
        <span class="telemetry-label">Cloud Infrastructure</span>
        <span class="telemetry-value" style="color: var(--cyan);">Nebius Cloud</span>
      </div>
      <div class="telemetry-card">
        <span class="telemetry-label">Remediation Mode</span>
        <span class="telemetry-value">1-Click Auto-Patch</span>
      </div>
      <div class="telemetry-card">
        <span class="telemetry-label">Track Eligibility</span>
        <span class="telemetry-value" style="font-size: 15px;">Coding & Agentic Eng.</span>
      </div>
    </section>

    <!-- Console Split Workspace -->
    <div class="console-split">
      
      <!-- Left Panel: Target Inspector -->
      <section class="glass-deck">
        <div class="deck-header">
          <div class="deck-title">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
            <span>Target Code Inspector</span>
          </div>
          <span class="deck-chip" id="bufferTag">auth_controller.py</span>
        </div>

        <div class="deck-body">
          
          <!-- 1-Click Interactive Self-Healing Banner -->
          <div class="self-healing-banner" id="healingBanner">
            <div class="banner-left">
              <span class="banner-heading">🛡️ Autonomous Self-Healing Patch Ready!</span>
              <span class="banner-desc">Nemotron synthesized hardened code eliminating all detected vulnerabilities.</span>
            </div>
            <button class="btn-remediate-instant" onclick="injectSafeCode()">
              <span>⚡ Load & Test Safe Code</span>
            </button>
          </div>

          <!-- Console Terminal -->
          <div class="cyber-console">
            <div class="console-chrome">
              <div class="window-controls">
                <span class="circle-dot c-red"></span>
                <span class="circle-dot c-yellow"></span>
                <span class="circle-dot c-green"></span>
              </div>
              <span id="bufferStatus">PYTHON 3.13 • BUFFER: UNCOMMITTED</span>
            </div>
            <textarea id="codeEditor" spellcheck="false"></textarea>
          </div>

          <div class="action-matrix">
            <button class="btn-primary-trigger" id="auditActionBtn" onclick="triggerAudit()">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
              <span id="triggerText">Trigger SynapseSentry Audit</span>
            </button>
            <button class="btn-preset-load" onclick="loadVulnerableSample()">Load Exploit Sample</button>
          </div>
        </div>
      </section>

      <!-- Right Panel: Sentry Assessment & Patch -->
      <section class="glass-deck">
        <div class="deck-header">
          <div class="deck-title">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
            <span>Sentry Intelligence & Remediation</span>
          </div>
          <span id="speedBadge" style="font-size: 11px; color: var(--text-dim); font-family: 'JetBrains Mono', monospace;">Telemetry Standby</span>
        </div>

        <div class="deck-body">
          
          <!-- Dynamic Score Telemetry Box -->
          <div class="health-telemetry-box">
            <div class="score-summary-col">
              <span class="score-header-label">Security Health Index</span>
              <div id="riskContainer">
                <span class="risk-tag-badge tag-High" id="riskBadge">Awaiting Audit</span>
              </div>
              <span style="font-size: 12px; color: var(--text-dim);" id="vulnCountSummary">Trigger audit to evaluate threat surfaces.</span>
            </div>
            <div class="circular-dial" id="healthDial">
              <span class="dial-val" id="dialScore">--</span>
              <span class="dial-max">/ 100</span>
            </div>
          </div>

          <!-- Tavily Real-Time Threat Intelligence Card -->
          <div class="tavily-card-intel" id="tavilyIntelCard">
            <div class="tavily-top-bar">
              <div class="tavily-title">
                <span>🌐 Live Threat Intelligence Bulletin (Powered by Tavily)</span>
              </div>
              <span class="tavily-verified-chip">NVD / MITRE Feed</span>
            </div>
            <div id="intelTitle" style="font-weight: 700; color: #ffffff; margin-bottom: 2px;"></div>
            <div id="intelSnippet" style="color: #cbd5e1; font-size: 11px;"></div>
            <a id="intelUrl" href="#" target="_blank" style="color: var(--cyan); font-size: 11px; text-decoration: underline; display: inline-block; margin-top: 5px;">View Global CVE Advisory →</a>
          </div>

          <!-- Executive Reasoning Card -->
          <div class="executive-card" id="summaryBlock">
            The SynapseSentry cognitive agent decomposes Abstract Syntax Trees (AST) using NVIDIA Nemotron-70B reasoning to locate zero-day injection sinks, credential leaks, and logic flaws, generating immediate verified Git patches.
          </div>

          <!-- Exploitable Findings List -->
          <div class="subhead-label">
            <span>Isolated Vulnerabilities (<span id="findingsCount">0</span>)</span>
            <span style="font-size: 11px; color: var(--cyan); font-family: 'JetBrains Mono', monospace;">CWE / CVE Mapped</span>
          </div>

          <div class="findings-container" id="findingsFeed">
            <div style="text-align: center; color: var(--text-dim); padding: 30px; font-size: 12px;">
              Ready. Click <strong>"Trigger SynapseSentry Audit"</strong> to begin agentic decomposition.
            </div>
          </div>

          <!-- Unified Git Patch View -->
          <div class="subhead-label">
            <span>Autonomous Self-Healing Git Diff</span>
            <span style="font-size: 11px; color: var(--text-dim);">Ready for <code style="color: var(--cyan);">git apply</code></span>
          </div>

          <div class="diff-deck">
            <div class="diff-deck-header">
              <span>UNIFIED DIFF FORMAT</span>
              <button class="btn-copy-unified" onclick="copyPatch()">Copy Patch</button>
            </div>
            <pre class="diff-output-pre" id="diffViewer"># Automated git diff will be synthesized here...</pre>
          </div>

        </div>
      </section>

    </div>
  </main>

  <!-- Modern Enterprise Footer -->
  <footer>
    <div>
      <strong>SynapseSentry AI</strong> • Developed by <strong>Dawar Tariq</strong> for the <strong>Nebius × NVIDIA Global AI Hackathon</strong>
    </div>
    <div>
      Powered by <strong>NVIDIA Nemotron-70B</strong> on <strong>Nebius AI Cloud</strong> & <strong>Tavily Intelligence</strong>
    </div>
  </footer>

  <script>
    const VULNERABLE_CODE = `import os
import sqlite3
import subprocess

API_SECRET = "sk-live-94a18df7261b092ce"

def authenticate_user(username, password):
    # CRITICAL: Vulnerable to SQL Injection
    conn = sqlite3.connect("production_users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM accounts WHERE user = '{username}' AND pass = '{password}'"
    cursor.execute(query)
    return cursor.fetchone()

def execute_network_diagnostics(target_ip):
    # CRITICAL: Arbitrary Remote Command Execution (RCE)
    os.system(f"ping -c 1 {target_ip}")
`;

    let activeSafeCode = "";

    function loadVulnerableSample() {
      document.getElementById("codeEditor").value = VULNERABLE_CODE;
      document.getElementById("healingBanner").style.display = "none";
      document.getElementById("bufferStatus").innerText = "PYTHON 3.13 • BUFFER: UNCOMMITTED (VULNERABLE SAMPLE)";
      document.getElementById("bufferTag").innerText = "auth_controller.py";
    }

    loadVulnerableSample();

    async function triggerAudit() {
      const btn = document.getElementById("auditActionBtn");
      const btnText = document.getElementById("triggerText");
      btn.disabled = true;
      btnText.innerHTML = `<span style="display:inline-block; animation: pulseAnim 1s infinite;">Reasoning with Nemotron 70B & Tavily...</span>`;

      try {
        const res = await fetch("/api/audit", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            code: document.getElementById("codeEditor").value,
            filename: document.getElementById("bufferTag").innerText
          })
        });

        const data = await res.json();
        renderAuditDashboard(data);
      } catch (err) {
        alert("Sentry Error: " + err.message);
      } finally {
        btn.disabled = false;
        btnText.innerText = "Trigger SynapseSentry Audit";
      }
    }

    function renderAuditDashboard(data) {
      document.getElementById("speedBadge").innerText = `${data.execution_time_ms}ms • ${data.engine || 'NVIDIA Nemotron'}`;

      // Dial & Banner
      const dial = document.getElementById("healthDial");
      const dialScore = document.getElementById("dialScore");
      dialScore.innerText = data.security_score;

      const banner = document.getElementById("healingBanner");

      if (data.security_score < 75) {
        dial.className = "circular-dial";
        banner.style.display = "flex";
        activeSafeCode = data.remediated_code || "";
      } else {
        dial.className = "circular-dial dial-safe";
        banner.style.display = "none";
      }

      // Risk Tag
      const riskBadge = document.getElementById("riskBadge");
      riskBadge.className = `risk-tag-badge tag-${data.risk_level}`;
      riskBadge.innerText = `${data.risk_level} Risk Level`;

      // Tavily Threat Intel Bulletin
      const intelCard = document.getElementById("tavilyIntelCard");
      if (data.threat_intelligence) {
        intelCard.style.display = "block";
        document.getElementById("intelTitle").innerText = data.threat_intelligence.title || "Live Vulnerability Bulletin";
        document.getElementById("intelSnippet").innerText = data.threat_intelligence.snippet || "";
        const intelLink = document.getElementById("intelUrl");
        intelLink.href = data.threat_intelligence.url || "#";
        intelLink.innerText = `View Official Advisory (${data.threat_intelligence.url.slice(0, 36)}...) →`;
      } else {
        intelCard.style.display = "none";
      }

      document.getElementById("vulnCountSummary").innerText = `${data.vulnerabilities.length} exploitable vectors isolated.`;
      document.getElementById("summaryBlock").innerText = data.summary;
      document.getElementById("findingsCount").innerText = data.vulnerabilities.length;

      // Findings Feed
      const feed = document.getElementById("findingsFeed");
      feed.innerHTML = "";

      if (data.vulnerabilities.length === 0) {
        feed.innerHTML = `<div style="text-align: center; color: var(--success); padding: 25px; font-weight: 700;">✅ Clean codebase verified. Zero exploitable vectors detected. (Health Index: 100/100)</div>`;
      } else {
        data.vulnerabilities.forEach(item => {
          const card = document.createElement("div");
          card.className = "finding-card";
          card.innerHTML = `
            <div class="finding-top">
              <span class="finding-title">${item.title}</span>
              <span class="finding-severity">${item.severity}</span>
            </div>
            <div class="finding-meta">
              <span>${item.id}</span>
              <span>•</span>
              <span>Line ${item.line_number}</span>
              <span>•</span>
              <span>${item.cve_reference || 'CWE'}</span>
            </div>
            <div class="finding-rec"><strong>Remediation:</strong> ${item.recommendation}</div>
          `;
          feed.appendChild(card);
        });
      }

      document.getElementById("diffViewer").innerText = data.patch_diff || "# No patch required.";
    }

    function injectSafeCode() {
      if (!activeSafeCode) return;
      document.getElementById("codeEditor").value = activeSafeCode;
      document.getElementById("bufferStatus").innerText = "PYTHON 3.13 • BUFFER: REMEDIATED (NEMOTRON HARDENED)";
      document.getElementById("bufferTag").innerText = "auth_controller_secure.py";
      document.getElementById("healingBanner").style.display = "none";
      triggerAudit();
    }

    function copyPatch() {
      const patch = document.getElementById("diffViewer").innerText;
      navigator.clipboard.writeText(patch);
      alert("Git Unified Patch copied to clipboard! Ready to apply with 'git apply'.");
    }
  </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def serve_dashboard():
    return ULTRA_TIER_UI

@app.post("/api/audit")
async def handle_audit(request: AuditRequest):
    try:
        report = SynapseSentryEngine.audit(
            code=request.code,
            filename=request.filename or "auth_controller.py"
        )
        return JSONResponse(content=report)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

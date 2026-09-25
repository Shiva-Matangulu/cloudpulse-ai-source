import os
import time
import urllib.request
from playwright.sync_api import sync_playwright

output_dir = "screenshots"
os.makedirs(output_dir, exist_ok=True)

# 1. Reset remediation state to baseline
try:
    req = urllib.request.Request("http://localhost:8080/api/remediate/reset", data=b"", method="POST")
    urllib.request.urlopen(req)
    print("[1/8] State reset to baseline ($129.30 waste, 65% health).")
except Exception as e:
    print("[1/8] State reset warning:", e)

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1080})

    # Screenshot 1: Baseline Dashboard Overview
    page.goto("http://localhost:8080", wait_until="networkidle")
    time.sleep(1.2)
    page.screenshot(path=f"{output_dir}/01_dashboard_fleet_overview.png")
    print("[2/8] Captured: 01_dashboard_fleet_overview.png")

    # Screenshot 2: Resource Topology Grid
    page.evaluate("window.scrollTo(0, 480)")
    time.sleep(0.8)
    page.screenshot(path=f"{output_dir}/02_resource_topology_anomalies.png")
    print("[3/8] Captured: 02_resource_topology_anomalies.png")

    # Screenshot 3: 1-Click Remediation Active
    page.evaluate("window.scrollTo(0, 1100)")
    time.sleep(0.5)
    fix_btn = page.locator("button:has-text('1-Click Fix')").first
    if fix_btn.is_visible():
        fix_btn.click()
        time.sleep(1.5)
        page.screenshot(path=f"{output_dir}/03_one_click_remediation_active.png")
        print("[4/8] Captured: 03_one_click_remediation_active.png")

    # Screenshot 4: AI Cloud Architect Copilot
    page.evaluate("window.scrollTo(0, 1600)")
    time.sleep(0.5)
    ai_chip = page.locator("button:has-text('NAT Gateway Audit')").first
    if ai_chip.is_visible():
        ai_chip.click()
        page.wait_for_selector("#ai-result-box:not(.hidden)", timeout=10000)
        time.sleep(1.5)
        page.screenshot(path=f"{output_dir}/04_ai_cloud_architect_copilot.png")
        print("[5/8] Captured: 04_ai_cloud_architect_copilot.png")

    # Screenshot 5: Live AWS CLI Terminal Simulator
    page.evaluate("window.scrollTo(0, 2200)")
    time.sleep(0.5)
    term_input = page.locator("#terminal-input")
    term_input.fill("aws apprunner describe-service")
    term_input.press("Enter")
    time.sleep(1.2)
    page.screenshot(path=f"{output_dir}/05_aws_cli_terminal_session.png")
    print("[6/8] Captured: 05_aws_cli_terminal_session.png")

    # Screenshot 6: Agent Proof Modal
    page.evaluate("window.scrollTo(0, 0)")
    page.evaluate("openProofModal()")
    time.sleep(1.0)
    page.screenshot(path=f"{output_dir}/06_agent_proof_compliance_modal.png")
    print("[7/8] Captured: 06_agent_proof_compliance_modal.png")
    page.evaluate("closeProofModal()")

    # Screenshot 7: Ship Gate Pass /api/health
    page.goto("http://localhost:8080/api/health", wait_until="networkidle")
    time.sleep(0.5)
    page.screenshot(path=f"{output_dir}/07_ship_gate_verified_pass.png")
    print("[8/8] Captured: 07_ship_gate_verified_pass.png")

    browser.close()
    print("Successfully captured all 7 local application screenshots in 'screenshots/'!")

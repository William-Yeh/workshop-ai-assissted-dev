from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from commerce_platform.checkout.eligibility import evaluate_checkout_eligibility
from commerce_platform.profiles.service import build_profile_payload, get_user_record

app = FastAPI(title="Module 1 Integrated Teaching Repo")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/profile/{user_id}")
def get_profile(user_id: int) -> dict[str, str | None]:
    user = get_user_record(user_id)
    payload = build_profile_payload(user)
    return {
        "name": payload.name,
        "email": payload.email,
    }


@app.get("/checkout-eligibility/{user_id}")
def get_checkout_eligibility(user_id: int) -> dict[str, str | int | bool]:
    user = get_user_record(user_id)
    result = evaluate_checkout_eligibility(user_id, user)
    return {
        "user_id": result.user_id,
        "eligible": result.eligible,
        "reason": result.reason,
    }


@app.get("/demo/profile-ui", response_class=HTMLResponse)
def profile_ui_demo() -> str:
    return """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Profile UI Demo</title>
    <style>
      :root {
        color-scheme: light dark;
        font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }
      body {
        max-width: 760px;
        margin: 40px auto;
        padding: 0 16px;
        line-height: 1.5;
      }
      .controls {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin: 16px 0 24px;
      }
      button {
        border: 1px solid #8885;
        border-radius: 10px;
        background: transparent;
        padding: 8px 12px;
        cursor: pointer;
      }
      .panel {
        border: 1px solid #8884;
        border-radius: 14px;
        padding: 16px;
      }
      .label {
        font-size: 0.9rem;
        opacity: 0.75;
      }
      .value {
        font-size: 1.15rem;
        font-weight: 600;
      }
      .warning {
        color: #b45309;
        font-weight: 700;
      }
      .error {
        color: #b91c1c;
        font-weight: 700;
      }
      code {
        font-size: 0.95rem;
      }
    </style>
  </head>
  <body>
    <h1>Profile UI Demo</h1>
    <p>
      This tiny frontend is intentionally simple. It helps learners see the difference between:
      <strong>a hard backend failure</strong> and <strong>a successful response that still creates a UI problem</strong>.
    </p>

    <ul>
      <li><code>1</code>: old payload, works</li>
      <li><code>2</code>: new payload, works</li>
      <li><code>3</code>: nested email missing, backend returns 500</li>
      <li><code>4</code>: invited user, request succeeds and UI shows missing email safely</li>
      <li><code>5</code>: active verified user, request succeeds but the same missing-email UI now hides a real downstream problem</li>
    </ul>

    <div class="controls">
      <button type="button" onclick="loadProfile(1)">Load user 1</button>
      <button type="button" onclick="loadProfile(2)">Load user 2</button>
      <button type="button" onclick="loadProfile(3)">Load user 3</button>
      <button type="button" onclick="loadProfile(4)">Load user 4</button>
      <button type="button" onclick="loadProfile(5)">Load user 5</button>
    </div>

    <div class="panel">
      <div class="label">Result</div>
      <pre id="result">Click one of the buttons above.</pre>
      <div class="label">Rendered UI</div>
      <div id="rendered" class="value">—</div>
    </div>

    <script>
      async function loadProfile(userId) {
        const result = document.getElementById("result");
        const rendered = document.getElementById("rendered");

        result.textContent = "Loading...";
        rendered.className = "value";
        rendered.textContent = "—";

        const response = await fetch(`/profile/${userId}`);
        let body = null;

        try {
          body = await response.json();
        } catch {
          body = null;
        }

        result.textContent = JSON.stringify(
          { status: response.status, body },
          null,
          2
        );

        if (!response.ok) {
          rendered.className = "value error";
          rendered.textContent = "UI cannot render email because the backend request failed.";
          return;
        }

        if (!body || !body.email) {
          rendered.className = "value warning";
          rendered.textContent = "Email missing in UI even though the request itself succeeded.";
          return;
        }

        rendered.className = "value";
        rendered.textContent = `${body.name} <${body.email}>`;
      }
    </script>
  </body>
</html>
"""

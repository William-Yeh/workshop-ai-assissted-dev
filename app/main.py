from __future__ import annotations

import html

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from commerce_platform.checkout.eligibility import evaluate_checkout_eligibility
from commerce_platform.profiles.service import build_profile_payload, get_user_record

app = FastAPI(title="AI Collaboration Course Repo")


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




@app.get("/demo/module1", response_class=HTMLResponse)
def module1_demo_index() -> str:
    intro = (
        "This page is a lightweight teaching index for Module 1. "
        "Use it to start from task definition, context, and output framing before moving to Module 2."
    )
    return f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Module 1 Demo Index</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body {{ font-family: system-ui, sans-serif; margin: 0; padding: 24px; background: #f7f7fb; color: #1d2430; line-height: 1.5; }}
    main {{ max-width: 960px; margin: 0 auto; }}
    .card {{ border: 1px solid #d9dce3; background: white; border-radius: 16px; padding: 18px; margin-top: 16px; }}
    code {{ font-family: ui-monospace, monospace; }}
    a {{ color: #2446f5; text-decoration: none; }}
  </style>
</head>
<body>
  <main>
    <h1>Module 1 Demo Index</h1>
    <p>{html.escape(intro)}</p>
    <div class="card">
      <h2>Suggested entry</h2>
      <ol>
        <li>Open <a href="/demo/profile-ui">/demo/profile-ui</a></li>
        <li>Compare user <code>3</code>, user <code>4</code>, and checkout user <code>5</code></li>
        <li>Use Module 1 materials to practice task brief, minimum useful context, and output framing</li>
      </ol>
    </div>
  </main>
</body>
</html>
"""

@app.get("/demo/module2", response_class=HTMLResponse)
def module2_demo_index() -> str:
    intro = (
        "This page is a lightweight teaching index for Module 2. It does not replace the repo "
        "workbench in VSCode or Cline. It helps the instructor move through the main case, the "
        "two micro transfers, and the recommended git checkpoints without losing the room."
    )
    return f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Module 2 Demo Index</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    :root {{
      color-scheme: light dark;
      --bg: #f7f7fb;
      --card: #ffffff;
      --border: #d9dce3;
      --muted: #5f6673;
      --text: #1d2430;
      --accent: #2446f5;
      --soft: rgba(36,70,245,0.08);
    }}
    @media (prefers-color-scheme: dark) {{
      :root {{
        --bg: #0d1117;
        --card: #161b22;
        --border: #30363d;
        --muted: #97a3b6;
        --text: #e6edf3;
        --accent: #7aa2ff;
        --soft: rgba(122,162,255,0.12);
      }}
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; padding: 24px; font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: var(--bg); color: var(--text); line-height: 1.5; }}
    main {{ max-width: 1100px; margin: 0 auto; }}
    h1, h2, h3 {{ margin: 0 0 12px; }}
    p {{ margin: 0 0 12px; }}
    .lead {{ color: var(--muted); max-width: 920px; }}
    .grid {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; margin-top: 20px; }}
    @media (max-width: 960px) {{ .grid {{ grid-template-columns: 1fr; }} }}
    .card {{ border: 1px solid var(--border); border-radius: 16px; padding: 18px; background: var(--card); }}
    .pill {{ display: inline-block; margin-bottom: 10px; padding: 4px 10px; border-radius: 999px; background: var(--soft); color: var(--accent); font-size: 13px; font-weight: 600; }}
    .subtle {{ color: var(--muted); font-size: 14px; }}
    code {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 0.95em; }}
    ul {{ margin: 10px 0 0 18px; padding: 0; }}
    li {{ margin: 6px 0; }}
    .steps {{ margin-top: 24px; border: 1px solid var(--border); border-radius: 16px; padding: 18px; background: var(--card); }}
    .callout {{ margin-top: 18px; border-left: 4px solid var(--accent); padding: 10px 14px; background: var(--soft); border-radius: 10px; }}
    a {{ color: var(--accent); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
  <main>
    <h1>Module 2 Demo Index</h1>
    <p class="lead">{html.escape(intro)}</p>

    <div class="steps">
      <h2>Suggested teaching sequence</h2>
      <ol>
        <li>Start from <code>m2-baseline</code> or <code>m2-main-case-start</code>.</li>
        <li>Use the main case to separate <strong>symptom</strong>, <strong>candidate causes</strong>, and <strong>still-missing information</strong>.</li>
        <li>Use micro transfer 1 to clarify <strong>consumer-specific expectation</strong> and whether a small guardrail test is worth adding.</li>
        <li>Use micro transfer 2 to produce <strong>first-layer quality delivery</strong>: review notes, test sketch, style consistency review, or PR summary.</li>
      </ol>
      <div class="callout">This module is not a full debug workshop. It is about shrinking the problem, ordering validation, and delivering a first-layer quality version.</div>
    </div>

    <div class="grid">
      <section class="card">
        <div class="pill">Main case</div>
        <h3>Profile migration incident</h3>
        <p class="subtle">Goal: see the symptom first, then order validation.</p>
        <ul>
          <li>Use <a href="/demo/profile-ui">/demo/profile-ui</a></li>
          <li>Compare user <code>3</code> and user <code>4</code></li>
          <li>Do not patch yet; first separate facts from guesses</li>
          <li>Suggested tag: <code>m2-main-case-start</code></li>
        </ul>
      </section>

      <section class="card">
        <div class="pill">Micro transfer 1</div>
        <h3>Checkout eligibility</h3>
        <p class="subtle">Goal: the same missing email does not mean the same consumer rule.</p>
        <ul>
          <li>Compare <code>/checkout-eligibility/4</code> and <code>/checkout-eligibility/5</code></li>
          <li>Ask whether the difference is a symptom issue or an expectation issue</li>
          <li>Suggested tag: <code>m2-micro1-start</code></li>
          <li>Suggested branch: <code>m2-test-gap-work</code></li>
        </ul>
      </section>

      <section class="card">
        <div class="pill">Micro transfer 2</div>
        <h3>Review / test reinforcement</h3>
        <p class="subtle">Goal: turn analysis into first-layer quality delivery.</p>
        <ul>
          <li>Review style drift and first-layer quality notes</li>
          <li>Use the repo materials under <code>materials/module2/</code></li>
          <li>Suggested tags: <code>m2-micro2-start</code>, <code>m2-style-demo-bad</code>, <code>m2-style-demo-better</code></li>
          <li>Suggested branches: <code>m2-style-bad-patch</code>, <code>m2-style-better-patch</code></li>
        </ul>
      </section>
    </div>
  </main>
</body>
</html>
"""


@app.get("/demo/module3", response_class=HTMLResponse)
def module3_demo_index() -> str:
    intro = (
        "This page is a lightweight teaching index for Module 3. It helps the instructor "
        "turn proven individual AI usage into shared templates, checklists, and handoff-ready "
        "assets without jumping too early into team-level workflow governance."
    )
    return f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Module 3 Demo Index</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    :root {{
      color-scheme: light dark;
      --bg: #f7f7fb;
      --card: #ffffff;
      --border: #d9dce3;
      --muted: #5f6673;
      --text: #1d2430;
      --accent: #2446f5;
      --soft: rgba(36,70,245,0.08);
    }}
    @media (prefers-color-scheme: dark) {{
      :root {{
        --bg: #0d1117;
        --card: #161b22;
        --border: #30363d;
        --muted: #97a3b6;
        --text: #e6edf3;
        --accent: #7aa2ff;
        --soft: rgba(122,162,255,0.12);
      }}
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; padding: 24px; font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: var(--bg); color: var(--text); line-height: 1.5; }}
    main {{ max-width: 1100px; margin: 0 auto; }}
    h1, h2, h3 {{ margin: 0 0 12px; }}
    p {{ margin: 0 0 12px; }}
    .lead {{ color: var(--muted); max-width: 920px; }}
    .grid {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; margin-top: 20px; }}
    @media (max-width: 960px) {{ .grid {{ grid-template-columns: 1fr; }} }}
    .card {{ border: 1px solid var(--border); border-radius: 16px; padding: 18px; background: var(--card); }}
    .pill {{ display: inline-block; margin-bottom: 10px; padding: 4px 10px; border-radius: 999px; background: var(--soft); color: var(--accent); font-size: 13px; font-weight: 600; }}
    .subtle {{ color: var(--muted); font-size: 14px; }}
    code {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 0.95em; }}
    ul {{ margin: 10px 0 0 18px; padding: 0; }}
    li {{ margin: 6px 0; }}
    .steps {{ margin-top: 24px; border: 1px solid var(--border); border-radius: 16px; padding: 18px; background: var(--card); }}
    .callout {{ margin-top: 18px; border-left: 4px solid var(--accent); padding: 10px 14px; background: var(--soft); border-radius: 10px; }}
    a {{ color: var(--accent); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
  <main>
    <h1>Module 3 Demo Index</h1>
    <p class="lead">{html.escape(intro)}</p>

    <div class="steps">
      <h2>Suggested teaching sequence</h2>
      <ol>
        <li>Start from the proven outputs of <a href="/demo/module1">/demo/module1</a> and <a href="/demo/module2">/demo/module2</a>.</li>
        <li>Pick one repeated pattern worth keeping: task brief, validation handoff, or style consistency review.</li>
        <li>Turn that pattern into a template pack with <strong>usage conditions</strong>, <strong>required inputs</strong>, <strong>output structure</strong>, and <strong>validation / handoff points</strong>.</li>
        <li>Add an <strong>AI can do / cannot outsource</strong> boundary so the pack is safe to share.</li>
      </ol>
      <div class="callout">This module is not yet about workflow gates or automated rules. It is about turning one-off wins into a template pack the team can actually reuse.</div>
    </div>

    <div class="grid">
      <section class="card">
        <div class="pill">Pack 1</div>
        <h3>Shared task brief template</h3>
        <p class="subtle">Goal: convert personal prompt craft into a reusable team format.</p>
        <ul>
          <li>Use <code>materials/module3/shared_task_brief_template.md</code></li>
          <li>Lock in purpose, when to use, minimum useful context, and final line</li>
          <li>Best bridge from Module 1</li>
        </ul>
      </section>

      <section class="card">
        <div class="pill">Pack 2</div>
        <h3>Validation / handoff template</h3>
        <p class="subtle">Goal: preserve diagnosis quality when work changes hands.</p>
        <ul>
          <li>Use <code>materials/module3/validation_handoff_template.md</code></li>
          <li>Keep symptom, candidate causes, missing info, and validation order separated</li>
          <li>Best bridge from Module 2</li>
        </ul>
      </section>

      <section class="card">
        <div class="pill">Pack 3</div>
        <h3>Style review + boundary table</h3>
        <p class="subtle">Goal: make style consistency and responsibility boundaries shareable.</p>
        <ul>
          <li>Use <code>materials/module3/style_consistency_team_template.md</code></li>
          <li>Pair with <code>materials/module3/ai_outsource_judgment_table.md</code></li>
          <li>Do not turn this into policy enforcement yet</li>
        </ul>
      </section>
    </div>
  </main>
</body>
</html>
"""

@app.get("/demo/profile-ui", response_class=HTMLResponse)
def profile_ui_demo() -> str:
    intro = (
        "This tiny frontend is intentionally simple. It helps learners see the difference "
        "between: a hard backend failure, a successful response that still creates a UI "
        "problem, and a downstream consumer that is stricter than the profile UI."
    )
    note = (
        "Teaching focus: profile UI fallback and checkout eligibility are not the same contract. "
        "User 4 and user 5 are especially useful for Module 1 prompt comparison."
    )
    return f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Profile UI Demo</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    :root {{
      color-scheme: light dark;
      --bg: #f7f7fb;
      --card: #ffffff;
      --border: #d9dce3;
      --muted: #5f6673;
      --text: #1d2430;
      --ok-bg: #eef8ef;
      --ok-fg: #116530;
      --warn-bg: #fff7e8;
      --warn-fg: #8a5a00;
      --bad-bg: #fff0f0;
      --bad-fg: #9d1c1c;
      --accent: #2446f5;
    }}
    @media (prefers-color-scheme: dark) {{
      :root {{
        --bg: #0d1117;
        --card: #161b22;
        --border: #30363d;
        --muted: #97a3b6;
        --text: #e6edf3;
        --ok-bg: #0f2b18;
        --ok-fg: #7ee787;
        --warn-bg: #31200d;
        --warn-fg: #f2cc60;
        --bad-bg: #321111;
        --bad-fg: #ffb3ba;
        --accent: #7aa2ff;
      }}
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      padding: 24px;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.45;
    }}
    main {{
      max-width: 1200px;
      margin: 0 auto;
    }}
    h1, h2 {{
      margin: 0 0 12px;
    }}
    .lead {{
      color: var(--muted);
      max-width: 920px;
    }}
    .callout {{
      margin: 16px 0 24px;
      padding: 14px 16px;
      border: 1px solid var(--border);
      border-radius: 12px;
      background: var(--card);
    }}
    .users {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 18px 0 24px;
    }}
    button {{
      cursor: pointer;
      border: 1px solid var(--border);
      background: var(--card);
      color: var(--text);
      border-radius: 999px;
      padding: 10px 14px;
      font-size: 14px;
    }}
    button:hover {{
      border-color: var(--accent);
    }}
    button.active {{
      border-color: var(--accent);
      background: var(--accent);
      color: #fff;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 16px;
    }}
    @media (max-width: 960px) {{
      .grid {{ grid-template-columns: 1fr; }}
    }}
    .card {{
      border: 1px solid var(--border);
      background: var(--card);
      border-radius: 16px;
      padding: 16px;
      min-height: 280px;
    }}
    .subtle {{
      color: var(--muted);
      font-size: 14px;
      margin-bottom: 8px;
    }}
    pre {{
      white-space: pre-wrap;
      word-break: break-word;
      margin: 0;
      padding: 12px;
      border-radius: 12px;
      border: 1px solid var(--border);
      background: rgba(127,127,127,0.08);
      overflow-x: auto;
      font-size: 13px;
    }}
    .status {{
      display: inline-block;
      padding: 4px 10px;
      border-radius: 999px;
      font-size: 13px;
      font-weight: 600;
      margin-bottom: 10px;
    }}
    .status.ok {{
      background: var(--ok-bg);
      color: var(--ok-fg);
    }}
    .status.warn {{
      background: var(--warn-bg);
      color: var(--warn-fg);
    }}
    .status.bad {{
      background: var(--bad-bg);
      color: var(--bad-fg);
    }}
    .mini {{
      font-size: 13px;
      color: var(--muted);
    }}
    ul {{
      margin: 10px 0 0 18px;
      padding: 0;
    }}
  </style>
</head>
<body>
  <main>
    <h1>Profile UI Demo</h1>
    <p class="lead">{html.escape(intro)}</p>

    <div class="callout">
      <strong>Teaching focus</strong>
      <div class="mini">{html.escape(note)}</div>
      <ul>
        <li><code>1</code>: old payload, works</li>
        <li><code>2</code>: new payload, works</li>
        <li><code>3</code>: nested email missing, backend returns 500</li>
        <li><code>4</code>: invited user, request succeeds and profile UI can safely fallback</li>
        <li><code>5</code>: active verified user, request succeeds but the same missing-email UI now hides a real downstream problem</li>
      </ul>
    </div>

    <div class="users">
      <button onclick="loadUser(1)">Load user 1</button>
      <button onclick="loadUser(2)">Load user 2</button>
      <button onclick="loadUser(3)">Load user 3</button>
      <button onclick="loadUser(4)">Load user 4</button>
      <button onclick="loadUser(5)">Load user 5</button>
    </div>

    <div class="grid">
      <section class="card">
        <h2>Profile API Result</h2>
        <div class="subtle">Visible backend response for <code>/profile/{'{'}user_id{'}'}</code></div>
        <div id="profile-status" class="status warn">Click one of the buttons above.</div>
        <pre id="profile-result">—</pre>
      </section>

      <section class="card">
        <h2>Rendered Profile UI</h2>
        <div class="subtle">What the profile-facing consumer would likely render.</div>
        <div id="ui-status" class="status warn">Waiting for user selection</div>
        <pre id="ui-result">—</pre>
      </section>

      <section class="card">
        <h2>Checkout Eligibility</h2>
        <div class="subtle">A stricter downstream consumer reading the same user state.</div>
        <div id="checkout-status" class="status warn">Waiting for user selection</div>
        <pre id="checkout-result">—</pre>
      </section>
    </div>
  </main>

  <script>
    function setBadge(el, kind, text) {{
      el.className = `status ${{kind}}`;
      el.textContent = text;
    }}

    function renderProfileUi(profileData, profileOk) {{
      if (!profileOk) {{
        return {{
          state: "Hard backend failure",
          kind: "bad",
          details: {{
            outcome: "The profile UI cannot safely render because the backend request failed.",
            next_step: "This is a strong prompt candidate for: summarize facts, likely causes, missing information, and verification order before coding."
          }}
        }};
      }}

      const email = profileData.email;
      if (email) {{
        return {{
          state: "Renderable with real email",
          kind: "ok",
          details: {{
            name: profileData.name,
            email_label: email,
            note: "Profile UI contract is satisfied."
          }}
        }};
      }}

      return {{
        state: "Renderable with safe fallback",
        kind: "warn",
        details: {{
          name: profileData.name,
          email_label: "Email missing",
          note: "Safe fallback may be acceptable for some user states in the profile UI."
        }}
      }};
    }}

    async function loadUser(userId) {{
      document.querySelectorAll(".users button").forEach(b => b.classList.remove("active"));
      document.querySelector(`.users button[onclick="loadUser(${{userId}})"]`).classList.add("active");

      const profileStatus = document.getElementById("profile-status");
      const profileResult = document.getElementById("profile-result");
      const uiStatus = document.getElementById("ui-status");
      const uiResult = document.getElementById("ui-result");
      const checkoutStatus = document.getElementById("checkout-status");
      const checkoutResult = document.getElementById("checkout-result");

      setBadge(profileStatus, "warn", `Loading /profile/${{userId}} …`);
      setBadge(uiStatus, "warn", "Waiting for profile result …");
      setBadge(checkoutStatus, "warn", `Loading /checkout-eligibility/${{userId}} …`);

      let profileOk = false;
      let profileData = null;

      try {{
        const profileResp = await fetch(`/profile/${{userId}}`);
        const profileText = await profileResp.text();

        if (!profileResp.ok) {{
          setBadge(profileStatus, "bad", `/profile/${{userId}} → ${{profileResp.status}}`);
          profileResult.textContent = profileText || "Server error";
        }} else {{
          profileData = JSON.parse(profileText);
          profileOk = true;
          setBadge(profileStatus, "ok", `/profile/${{userId}} → ${{profileResp.status}}`);
          profileResult.textContent = JSON.stringify(profileData, null, 2);
        }}
      }} catch (err) {{
        setBadge(profileStatus, "bad", "Profile request failed");
        profileResult.textContent = String(err);
      }}

      const uiView = renderProfileUi(profileData, profileOk);
      setBadge(uiStatus, uiView.kind, uiView.state);
      uiResult.textContent = JSON.stringify(uiView.details, null, 2);

      try {{
        const checkoutResp = await fetch(`/checkout-eligibility/${{userId}}`);
        const checkoutData = await checkoutResp.json();
        const checkoutKind = checkoutData.eligible ? "ok" : "warn";
        const checkoutLabel = checkoutData.eligible
          ? `/checkout-eligibility/${{userId}} → eligible`
          : `/checkout-eligibility/${{userId}} → not eligible`;
        setBadge(checkoutStatus, checkoutKind, checkoutLabel);
        checkoutResult.textContent = JSON.stringify(checkoutData, null, 2);
      }} catch (err) {{
        setBadge(checkoutStatus, "bad", "Checkout request failed");
        checkoutResult.textContent = String(err);
      }}
    }}
  </script>
</body>
</html>
"""

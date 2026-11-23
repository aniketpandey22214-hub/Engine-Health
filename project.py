import streamlit as st
import pandas as pd
import joblib
import streamlit.components.v1 as components
from pathlib import Path

# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="Tractor Engine Health Monitor",
    page_icon="🚜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).resolve().parent

# Build the small gauge interface automatically from this single Python file.
DIAL_DIR = BASE_DIR / "tractor_dial_component"
DIAL_DIR.mkdir(exist_ok=True)
DIAL_HTML = '<!doctype html>\n<html>\n<head>\n<meta charset="utf-8">\n<style>\n  html, body { margin:0; padding:0; background:transparent; overflow:hidden;\n    font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }\n  .wrap { width:100%; height:205px; display:flex; align-items:center; justify-content:center; }\n  svg { width:100%; max-width:310px; height:205px; overflow:visible; touch-action:none; user-select:none; }\n  .track { fill:none; stroke:#263d57; stroke-width:18; stroke-linecap:butt; }\n  .progress { fill:none; stroke:#38bdf8; stroke-width:7; stroke-linecap:butt; }\n  .needle { stroke:#2dd4bf; stroke-width:3.5; stroke-linecap:round; }\n  .hub { fill:#2dd4bf; stroke:#0b1220; stroke-width:2; }\n  .tick { stroke:#8ca4bd; stroke-width:1; opacity:.8; }\n  .tick-label { fill:#9fb2c9; font-size:9px; }\n  .value { fill:#e7eef8; font-size:21px; font-weight:600; text-anchor:middle; }\n  .title { fill:#a9bfd3; font-size:11px; text-anchor:middle; font-weight:600; letter-spacing:.3px; }\n  .hit { fill:transparent; stroke:transparent; stroke-width:42; cursor:grab; }\n  .hit:active { cursor:grabbing; }\n</style>\n</head>\n<body>\n<div class="wrap">\n<svg id="dial" viewBox="0 0 300 205" role="img" aria-label="Adjustable semicircular gauge">\n  <path id="track" class="track"></path>\n  <path id="progress" class="progress"></path>\n  <g id="ticks"></g>\n  <text id="title" class="title" x="150" y="18"></text>\n  <text id="value" class="value" x="150" y="145"></text>\n  <line id="needle" class="needle"></line>\n  <circle id="hub" class="hub" r="5"></circle>\n  <path id="hit" class="hit"></path>\n</svg>\n</div>\n<script>\n(function () {\n  const svg = document.getElementById("dial");\n  const track = document.getElementById("track");\n  const progress = document.getElementById("progress");\n  const ticks = document.getElementById("ticks");\n  const title = document.getElementById("title");\n  const valueText = document.getElementById("value");\n  const needle = document.getElementById("needle");\n  const hub = document.getElementById("hub");\n  const hit = document.getElementById("hit");\n  const cx = 150, cy = 150, radius = 116;\n  let min = 0, max = 100, value = 50, step = 1, suffix = "", dragging = false;\n\n  function point(deg, r) {\n    const a = deg * Math.PI / 180;\n    return { x: cx + r * Math.cos(a), y: cy + r * Math.sin(a) };\n  }\n  function arcPath(r, start, end) {\n    const p1 = point(start, r), p2 = point(end, r);\n    return `M ${p1.x} ${p1.y} A ${r} ${r} 0 0 1 ${p2.x} ${p2.y}`;\n  }\n  function fmt(v) {\n    const decimals = step < 1 ? Math.max(1, (String(step).split(".")[1] || "").length) : 0;\n    return Number(v).toFixed(decimals) + suffix;\n  }\n  function render() {\n    const ratio = Math.max(0, Math.min(1, (value - min) / (max - min)));\n    const angle = 180 + ratio * 180;\n    track.setAttribute("d", arcPath(radius, 180, 360));\n    progress.setAttribute("d", arcPath(radius, 180, angle));\n    title.textContent = titleText;\n    valueText.textContent = fmt(value);\n    const p = point(angle, radius - 1);\n    const inner = point(angle, radius - 19);\n    needle.setAttribute("x1", inner.x); needle.setAttribute("y1", inner.y);\n    needle.setAttribute("x2", p.x); needle.setAttribute("y2", p.y);\n    hub.setAttribute("cx", cx); hub.setAttribute("cy", cy);\n    ticks.innerHTML = "";\n    for (let i = 0; i <= 4; i++) {\n      const a = 180 + i * 45, p1 = point(a, radius + 4), p2 = point(a, radius + 11);\n      const label = point(a, radius + 24);\n      const line = document.createElementNS("http://www.w3.org/2000/svg", "line");\n      line.setAttribute("x1",p1.x); line.setAttribute("y1",p1.y);\n      line.setAttribute("x2",p2.x); line.setAttribute("y2",p2.y);\n      line.setAttribute("class","tick"); ticks.appendChild(line);\n      const t = document.createElementNS("http://www.w3.org/2000/svg","text");\n      t.setAttribute("x",label.x); t.setAttribute("y",label.y+3);\n      t.setAttribute("text-anchor","middle"); t.setAttribute("class","tick-label");\n      t.textContent = Number(min + (max-min)*i/4).toFixed(step < 1 ? 1 : 0);\n      ticks.appendChild(t);\n    }\n    hit.setAttribute("d", arcPath(radius, 180, 360));\n  }\n  function sendValue(v) {\n    const snapped = Math.min(max, Math.max(min, min + Math.round((v-min)/step)*step));\n    const decimals = step < 1 ? Math.max(1, (String(step).split(".")[1] || "").length) : 0;\n    value = Number(snapped.toFixed(decimals));\n    render();\n    window.parent.postMessage({\n      isStreamlitMessage: true,\n      type: "streamlit:setComponentValue",\n      value: value\n    }, "*");\n  }\n  function setFromPointer(evt) {\n    const pt = svg.createSVGPoint(); pt.x = evt.clientX; pt.y = evt.clientY;\n    const screen = pt.matrixTransform(svg.getScreenCTM().inverse());\n    let a = Math.atan2(screen.y-cy, screen.x-cx) * 180/Math.PI;\n    // Map the lower semicircle from left (180°) to right (360°).\n    if (a < 0) a += 360;\n    a = Math.max(180, Math.min(360, a));\n    sendValue(min + ((a-180)/180)*(max-min));\n  }\n  hit.addEventListener("pointerdown", e => {\n    dragging = true; hit.setPointerCapture(e.pointerId); setFromPointer(e);\n  });\n  hit.addEventListener("pointermove", e => { if (dragging) setFromPointer(e); });\n  hit.addEventListener("pointerup", () => { dragging = false; });\n  hit.addEventListener("pointercancel", () => { dragging = false; });\n\n  let titleText = "GAUGE";\n  function onRender(event) {\n    const d = event.data || {};\n    if (d.type !== "streamlit:render") return;\n    const args = d.args || {};\n    min = Number(args.min_value ?? 0);\n    max = Number(args.max_value ?? 100);\n    step = Number(args.step ?? 1);\n    suffix = args.suffix || "";\n    titleText = args.label || "GAUGE";\n    value = Math.min(max, Math.max(min, Number(args.value ?? min)));\n    render();\n    window.parent.postMessage({isStreamlitMessage:true,type:"streamlit:setFrameHeight",height:205},"*");\n  }\n  window.addEventListener("message", onRender);\n  window.parent.postMessage({isStreamlitMessage:true,type:"streamlit:componentReady",apiVersion:1},"*");\n})();\n</script>\n</body>\n</html>'
(DIAL_DIR / "index.html").write_text(DIAL_HTML, encoding="utf-8")

# Interactive semicircular automotive-style gauge component
_dial_component = components.declare_component(
    "tractor_interactive_dial", path=str(BASE_DIR / "tractor_dial_component")
)

# =====================================================
# 2. CUSTOM DASHBOARD THEME
# =====================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #0b1220;
    --panel: #121e30;
    --panel2: #17263b;
    --line: #263a52;
    --text: #e7eef8;
    --muted: #91a4bb;
    --cyan: #38bdf8;
    --teal: #2dd4bf;
}
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
.stApp {
    background:
      radial-gradient(circle at 12% 0%, rgba(14,165,233,.13), transparent 28%),
      radial-gradient(circle at 90% 10%, rgba(45,212,191,.09), transparent 25%),
      #0b1220;
    color: var(--text);
}
.block-container {
    max-width: 1450px;
    padding-top: 1.8rem;
    padding-bottom: 3rem;
}
h1, h2, h3, p, label, span {
    color: var(--text);
}
h1 { font-weight: 800 !important; letter-spacing: -1.2px; }
h2, h3 { font-weight: 700 !important; }
[data-testid="stHeader"] { background: transparent; }
[data-testid="stToolbar"] { right: 1rem; }
section[data-testid="stSidebar"] { background: #101b2b; }
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(18,30,48,.88);
    border: 1px solid var(--line);
    border-radius: 18px;
}
div[data-testid="stMetric"] {
    background: #142238;
    border: 1px solid #29415d;
    padding: 14px 16px;
    border-radius: 14px;
}
div[data-testid="stMetricLabel"] { color: #9fb2c9 !important; }
div[data-testid="stMetricValue"] { color: #e7f5ff !important; }
.stButton > button {
    width: 100%;
    min-height: 3.1rem;
    border: 0;
    border-radius: 12px;
    color: #061321;
    font-weight: 800;
    background: linear-gradient(100deg, #38bdf8, #2dd4bf);
    transition: all .2s ease;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(45,212,191,.22);
    color: #061321;
}
div[data-baseweb="select"] > div,
div[data-testid="stNumberInput"] input {
    background: #17263b !important;
    color: #edf6ff !important;
    border: 1px solid #344b66 !important;
    border-radius: 10px !important;
}
div[data-testid="stNumberInput"] button {
    background: #223750 !important;
    color: #e7eef8 !important;
}
hr { border-color: #263a52; }
.eyebrow {
    color: #38bdf8;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: .75rem;
    font-weight: 800;
}
.hero {
    padding: 24px 28px;
    border-radius: 20px;
    border: 1px solid #29445f;
    background: linear-gradient(115deg, rgba(20,40,63,.98), rgba(16,49,64,.88));
    margin-bottom: 22px;
}
.hero-sub { color: #a9bfd3; font-size: .98rem; }
.section-note { color: #91a4bb; font-size: .85rem; margin-top: -8px; }
.result-good {
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #167c68;
    background: linear-gradient(120deg, rgba(6,78,59,.45), rgba(18,30,48,.95));
}
.result-bad {
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #a94452;
    background: linear-gradient(120deg, rgba(127,29,29,.42), rgba(18,30,48,.95));
}
.result-title { font-size: 1.45rem; font-weight: 800; }
.small-muted { color: #9fb2c9; font-size: .85rem; }
</style>
""", unsafe_allow_html=True)


# =====================================================
# 3. LOAD TRAINED MODELS AND PREPROCESSING FILES
# =====================================================
try:
    health_model = joblib.load(BASE_DIR / "SVC_tractor3.pkl")
    fault_model = joblib.load(BASE_DIR / "fault_type_model.pkl")
    scaler = joblib.load(BASE_DIR / "scalers_tractor3.pkl")
    expected_columns = joblib.load(BASE_DIR / "columns_tractor3.pkl")
except Exception as e:
    st.error(f"Could not load the model files: {e}")
    st.info(
        "Keep SVC_tractor3.pkl, fault_type_model.pkl, "
        "scalers_tractor3.pkl and columns_tractor3.pkl "
        "in the same folder as this Python file."
    )
    st.stop()


# =====================================================
# 4. FEATURE CONFIGURATION — KEEP TRAINING ORDER
# =====================================================
numerical_cols = list(scaler.feature_names_in_)
model_columns = list(health_model.feature_names_in_)
fault_columns = list(fault_model.feature_names_in_)

if list(expected_columns) != model_columns:
    st.error("Saved feature columns do not match the health model.")
    st.stop()

if model_columns != fault_columns:
    st.error("Health and fault model feature orders do not match.")
    st.stop()

brand_mapping = {
    "John Deere": 0,
    "Mahindra": 1,
    "Swaraj": 2
}

engine_models = [
    "5039 D", "5050 D", "5310", "575 DI", "585 DI",
    "735 FE", "744 FE", "855 FE", "Arjun 605"
]

fault_descriptions = {
    "excessive_vibration": "Excessive Vibration",
    "general_anomaly": "General Engine Anomaly",
    "high_exhaust_temperature": "High Exhaust Temperature",
    "overheating": "Engine Overheating"
}

fault_explanations = {
    "excessive_vibration":
        "The model classified the input as excessive engine vibration.",
    "general_anomaly":
        "The model classified the input as a general engine anomaly.",
    "high_exhaust_temperature":
        "The model classified the input as high exhaust temperature.",
    "overheating":
        "The model classified the input as possible engine overheating."
}


# =====================================================
# 5. INTERACTIVE GAUGE HELPER
# =====================================================
def _sync_number_from_dial(key):
    """Callback: when a gauge is dragged, update its paired number input."""
    st.session_state[f"{key}_number"] = st.session_state[f"{key}_dial"]


def show_gauge(column, title, value, minimum, maximum, suffix="", key=None, step=1):
    """Render a draggable semicircular gauge linked to its number input."""
    with column:
        dial_key = f"{key}_dial"
        st.session_state.setdefault(dial_key, value)
        _dial_component(
            label=title,
            value=float(value),
            min_value=float(minimum),
            max_value=float(maximum),
            step=float(step),
            suffix=suffix,
            key=dial_key
        )


def _sync_dial_from_number(key):
    """When a number field changes, move its matching gauge needle."""
    st.session_state[f"{key}_dial"] = st.session_state[key]


# Gauge changes are stored by Streamlit under each component key.
# Copy those values into number-input state before the inputs are created.
for _control_key in [
    "rpm", "load", "coolant_temp", "exhaust_temp",
    "oil_pressure", "oil_temp", "vibration", "fuel_rate"
]:
    _dial_key = f"{_control_key}_dial"
    if _dial_key in st.session_state:
        st.session_state[_control_key] = st.session_state[_dial_key]


# =====================================================
# 6. DASHBOARD HEADER
# =====================================================
st.markdown("""
<div class="hero">
  <div class="eyebrow">Predictive maintenance • Machine learning system</div>
  <h1 style="margin:8px 0 5px 0;">🚜 Tractor Engine Health Monitor</h1>
  <div class="hero-sub">
    Enter engine operating conditions, review the live instrument panel,
    and run the trained models to obtain an engine-health prediction.
  </div>
</div>
""", unsafe_allow_html=True)


# =====================================================
# 7. TRACTOR DETAILS
# =====================================================
st.markdown("### 01  |  Tractor identification")
details_col1, details_col2, details_col3 = st.columns([1, 1, 2])

with details_col1:
    brand = st.selectbox("Tractor brand", list(brand_mapping.keys()))

with details_col2:
    model_name = st.selectbox("Engine model", engine_models)

with details_col3:
    st.markdown(
        f"""
        <div style="background:#142238;border:1px solid #29415d;
                    border-radius:13px;padding:13px 17px;margin-top:7px;">
          <div class="small-muted">SELECTED MACHINE</div>
          <div style="font-size:1.15rem;font-weight:750;color:#e7eef8;">
            {brand} · {model_name}
          </div>
          <div class="small-muted">Model inputs are supplied manually</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")


# =====================================================
# 8. ENGINE INPUTS — NUMBER INPUTS INSTEAD OF SLIDERS
# =====================================================
st.markdown("### 02  |  Engine operating parameters")
st.markdown(
    '<div class="section-note">Enter the operating values below. '
    'The instrument gauges update as you change the values.</div>',
    unsafe_allow_html=True
)

left, middle, right = st.columns(3, gap="large")

with left:
    st.markdown("#### ⚙️ Performance")
    rpm = st.number_input("Engine speed (RPM)", min_value=500, max_value=2400,
                          value=1800, step=50, key="rpm", on_change=_sync_dial_from_number, args=("rpm",))
    load = st.number_input("Engine load (%)", min_value=0, max_value=100,
                           value=50, step=5, key="load", on_change=_sync_dial_from_number, args=("load",))
    fuel_rate = st.number_input("Fuel rate (L/h)", min_value=0.0, max_value=50.0,
                                value=5.0, step=0.5, format="%.1f", key="fuel_rate", on_change=_sync_dial_from_number, args=("fuel_rate",))
    operating_hours = st.number_input("Operating hours (h)", min_value=0,
                                      max_value=20000, value=100, step=100, key="operating_hours")

with middle:
    st.markdown("#### 🌡️ Temperature")
    ambient_temp = st.number_input("Ambient temperature (°C)", min_value=0,
                                   max_value=60, value=25, step=1, key="ambient_temp")
    coolant_temp = st.number_input("Coolant temperature (°C)", min_value=0,
                                   max_value=150, value=90, step=1, key="coolant_temp", on_change=_sync_dial_from_number, args=("coolant_temp",))
    exhaust_temp = st.number_input("Exhaust temperature (°C)", min_value=0,
                                   max_value=600, value=400, step=5, key="exhaust_temp", on_change=_sync_dial_from_number, args=("exhaust_temp",))
    oil_temp = st.number_input("Oil temperature (°C)", min_value=0,
                               max_value=200, value=100, step=1, key="oil_temp", on_change=_sync_dial_from_number, args=("oil_temp",))

with right:
    st.markdown("#### 🛠️ Lubrication & condition")
    oil_pressure = st.number_input("Oil pressure (bar)", min_value=0.0,
                                   max_value=10.0, value=3.5, step=0.1,
                                   format="%.1f", key="oil_pressure", on_change=_sync_dial_from_number, args=("oil_pressure",))
    vibration = st.number_input("Vibration RMS (mm/s)", min_value=0.0,
                                max_value=10.0, value=1.0, step=0.1,
                                format="%.1f", key="vibration", on_change=_sync_dial_from_number, args=("vibration",))
    maintenance_days_ago = st.number_input(
        "Days since last maintenance", min_value=0, max_value=600,
        value=30, step=5, key="maintenance_days_ago"
    )

st.markdown("---")


# =====================================================
# 9. LIVE INSTRUMENT PANEL
# =====================================================
st.markdown("### 03  |  Live engine instrument panel")
st.markdown(
    '<div class="section-note">These gauges visualise the values entered above; '
    'they are not live sensor readings from a tractor.</div>',
    unsafe_allow_html=True
)

g1, g2, g3, g4 = st.columns(4)
show_gauge(g1, "ENGINE SPEED", rpm, 500, 2400, " rpm", key="rpm", step=25)
show_gauge(g2, "ENGINE LOAD", load, 0, 100, "%", key="load", step=1)
show_gauge(g3, "COOLANT TEMPERATURE", coolant_temp,
           0, 150, " °C", key="coolant_temp", step=1)
show_gauge(g4, "EXHAUST TEMPERATURE", exhaust_temp,
           0, 600, " °C", key="exhaust_temp", step=5)

g5, g6, g7, g8 = st.columns(4)
show_gauge(g5, "OIL PRESSURE", oil_pressure, 0, 10,
           " bar", key="oil_pressure", step=0.1)
show_gauge(g6, "OIL TEMPERATURE", oil_temp, 0,
           200, " °C", key="oil_temp", step=1)
show_gauge(g7, "VIBRATION RMS", vibration, 0, 10,
           " mm/s", key="vibration", step=0.1)
show_gauge(g8, "FUEL RATE", fuel_rate, 0, 50,
           " L/h", key="fuel_rate", step=0.5)

m1, m2, m3 = st.columns(3)
m1.metric("Ambient temperature", f"{ambient_temp} °C")
m2.metric("Operating hours", f"{operating_hours:,} h")
m3.metric("Days since maintenance", f"{maintenance_days_ago} days")

st.markdown("---")


# =====================================================
# 10. PREDICTION — ORIGINAL MODEL PIPELINE PRESERVED
# =====================================================
st.markdown("### 04  |  Run engine diagnosis")
predict_clicked = st.button("⚡  PREDICT ENGINE HEALTH", type="primary")

if predict_clicked:
    raw_input = {
        "brand": brand_mapping[brand],
        "rpm": rpm,
        "load_pct": load,
        "ambient_temp_c": ambient_temp,
        "operating_hours": operating_hours,
        "maintenance_days_ago": maintenance_days_ago,
        "coolant_temp_c": coolant_temp,
        "exhaust_temp_c": exhaust_temp,
        "oil_pressure_bar": oil_pressure,
        "oil_temp_c": oil_temp,
        "vibration_rms_mm_s": vibration,
        "fuel_rate_lph": fuel_rate
    }

    input_df = pd.DataFrame([raw_input])

    # Create engine-model dummy variables.
    # 5039 D is the reference category, as in the original app.
    for col in expected_columns:
        if col.startswith("engine_model_"):
            input_df[col] = 0

    if model_name != "5039 D":
        selected_dummy = "engine_model_" + model_name
        if selected_dummy not in expected_columns:
            st.error(
                f"Feature not found in the trained model: {selected_dummy}")
            st.stop()
        input_df[selected_dummy] = 1

    # Match the exact feature order used during model training.
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    # Preserve the original preprocessing from the uploaded application:
    # cast numerical inputs to int, then float, then apply the saved scaler.
    numerical_input = (
        input_df.loc[:, numerical_cols]
        .astype(int)
        .astype(float)
    )
    scaled_values = scaler.transform(numerical_input)
    scaled_df = pd.DataFrame(
        scaled_values,
        columns=numerical_cols,
        index=input_df.index
    )

    for col in numerical_cols:
        input_df[col] = scaled_df[col].astype(float)

    input_df = input_df.loc[:, model_columns]

    # Model 1: health classification
    health_prediction = health_model.predict(input_df)[0]

    st.markdown("---")
    st.markdown("### 05  |  Engine diagnosis report")

    st.markdown(
        f'<div class="small-muted">MACHINE: {brand} · {model_name}</div>',
        unsafe_allow_html=True
    )

    if health_prediction == 1:
        st.markdown("""
        <div class="result-good">
          <div class="eyebrow">Model 1 • Health classification</div>
          <div class="result-title">🟢 ENGINE CONDITION: HEALTHY</div>
          <div style="color:#b7d9d1;margin-top:7px;">
            The health model predicts a healthy engine condition.
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### Fault classification")
        st.success(
            "No fault classification was run because the health model predicted HEALTHY.")

    elif health_prediction == 0:
        st.markdown("""
        <div class="result-bad">
          <div class="eyebrow">Model 1 • Health classification</div>
          <div class="result-title">🔴 ENGINE CONDITION: ABNORMAL</div>
          <div style="color:#f3c4c9;margin-top:7px;">
            The health model predicts an abnormal engine condition.
          </div>
        </div>
        """, unsafe_allow_html=True)

        # Model 2: fault classification, run only for abnormal prediction.
        fault_prediction = fault_model.predict(input_df)[0]
        fault_name = fault_descriptions.get(
            fault_prediction, str(fault_prediction))
        explanation = fault_explanations.get(
            fault_prediction,
            "Further engine inspection is recommended."
        )

        st.markdown("#### Possible fault category")
        st.warning(f"Predicted fault type: **{fault_name}**")
        st.write(explanation)

    st.caption(
        "The health and fault outputs are predictions from two separately trained SVC models."
    )

    st.warning(
        "Important: These models were trained using a synthetic dataset. "
        "The outputs are educational and illustrative, not validated mechanical diagnoses. "
        "Do not use them as the sole basis for real maintenance or safety decisions."
    )

else:
    st.info(
        "Adjust the operating values, review the instrument panel, "
        "then select **PREDICT ENGINE HEALTH** to run the trained models."
    )

st.markdown(
    '<div style="text-align:center;color:#71869e;font-size:.78rem;'
    'padding-top:25px;">TRACTOR ENGINE HEALTH MONITOR · MACHINE LEARNING DEMONSTRATOR</div>',
    unsafe_allow_html=True
)


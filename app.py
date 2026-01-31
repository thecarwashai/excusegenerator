import random
import streamlit as st

# -------------------------------------------------
# Page config (default Streamlit look)
# -------------------------------------------------
st.set_page_config(
    page_title="Excuse Generator",
    page_icon="🙃",
    layout="centered"
)

# -------------------------------------------------
# SAFE CSS RESET (keeps Streamlit defaults)
# -------------------------------------------------
st.markdown(
    """
    <style>
    html, body, [data-testid="stApp"] {
        background-color: #ffffff;
        color: #000000;
    }

    p, span, div, label, h1, h2, h3, h4 {
        color: #000000;
    }

    input, textarea, select {
        background-color: #ffffff;
        color: #000000;
    }

    button {
        background-color: #f0f2f6;
        color: #000000;
        border: 1px solid #cccccc;
        border-radius: 6px;
    }

    button:hover {
        background-color: #e6e6e6;
        color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# Header
# -------------------------------------------------
st.title("🙃 Excuse Generator")
st.caption("Pick a tone. Sound human.")

# -------------------------------------------------
# Excuse banks (REALISTIC)
# -------------------------------------------------
CASUAL = [
    "Sorry, just saw this.",
    "My bad — long day.",
    "Just catching up on texts.",
    "Sorry, work got busy.",
    "Just now seeing this.",
    "Lost track of time earlier.",
    "Was away from my phone for a bit.",
    "Got distracted and forgot to respond.",
    "Today got away from me.",
    "Finally checking my phone.",
    "Busy stretch earlier.",
    "Just resurfacing now.",
    "Phone’s been ignored most of the day.",
    "Sorry — hectic day.",
    "Just now sitting down.",
    "Didn’t mean to disappear.",
    "Catching up now.",
    "Was running around all day.",
    "Just got a second to breathe.",
    "Sorry about the delay."
]

FLIRTY = [
    "Worth the wait though 🙂",
    "Okay hi — I’m back now.",
    "Survived the day. What’d I miss?",
    "Late reply, same interest.",
    "Back from the chaos.",
    "Okay, I’m here now.",
    "Hi again 👋",
    "Delayed response, still curious.",
    "Hope your day’s going well.",
    "Alright, your turn.",
    "Back online and behaving.",
    "Made it through the day.",
    "Late, but intentional.",
    "Okay, talk to me.",
    "Back from real life.",
    "Worth circling back to this.",
    "Late reply, honest smile included.",
    "Hi — long day.",
    "Okay, caught up now.",
    "Still here."
]

HONEST = [
    "Honestly, I needed a break from my phone.",
    "Today was heavier than expected.",
    "Was in a weird headspace earlier.",
    "Didn’t have the energy to reply before.",
    "Needed some offline time.",
    "Had a lot going on today.",
    "I tend to disappear when I’m overwhelmed.",
    "Just didn’t want to half-reply earlier.",
    "I reply better once the day slows down.",
    "Took some quiet time today.",
    "Was mentally checked out for a bit.",
    "Trying to be more present now.",
    "I’m not great at texting during busy days.",
    "Needed to reset earlier.",
    "Thanks for the patience."
]

FUNNY = [
    "I replied in my head. Technology failed me.",
    "I was busy doing absolutely nothing.",
    "Sorry — I was buffering.",
    "I meant to reply and then forgot I exist.",
    "Time slipped away aggressively.",
    "I disappeared briefly for character development.",
    "I delayed replying for suspense.",
    "I was stuck choosing emojis.",
    "I thought about replying, which counts.",
    "I vanished and reappeared — classic me.",
    "Reply postponed by destiny.",
    "I was socially buffering.",
    "I got distracted by everything else.",
    "Reply delayed for dramatic effect.",
    "I was fighting autocorrect."
]

# -------------------------------------------------
# Tone selector
# -------------------------------------------------
tone = st.radio(
    "Select tone",
    ["Casual", "Flirty", "Honest", "Funny (Not real)"],
    horizontal=True
)

# -------------------------------------------------
# State
# -------------------------------------------------
if "current_excuse" not in st.session_state:
    st.session_state.current_excuse = "Click generate."

def generate_excuse():
    if tone == "Casual":
        st.session_state.current_excuse = random.choice(CASUAL)
    elif tone == "Flirty":
        st.session_state.current_excuse = random.choice(FLIRTY)
    elif tone == "Honest":
        st.session_state.current_excuse = random.choice(HONEST)
    else:
        st.session_state.current_excuse = random.choice(FUNNY)

# -------------------------------------------------
# Excuse display (neutral card)
# -------------------------------------------------
st.markdown(
    f"""
    <div style="
        padding:16px;
        background-color:#ffffff;
        color:#000000;
        border:1px solid #dddddd;
        border-radius:8px;
        margin-bottom:12px;
        font-size:16px;">
        {st.session_state.current_excuse}
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 1])

with col1:
    st.button("Generate 🙃", on_click=generate_excuse)

with col2:
    st.markdown(
        f"""
        <button onclick="navigator.clipboard.writeText(`{st.session_state.current_excuse}`)">
            Copy 📋
        </button>
        """,
        unsafe_allow_html=True
)

st.caption("Funny mode = jokes only. Others sound like real texts.")

import random
import streamlit as st

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Excuse Generator",
    page_icon="🙃",
    layout="centered"
)

# -----------------------------
# Force white background + black text
# -----------------------------
st.markdown(
    """
    <style>
    html, body, [data-testid="stApp"] {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    * {
        color: #000000 !important;
    }
    button {
        background-color: #111111 !important;
        color: #ffffff !important;
        border-radius: 10px !important;
        border: none !important;
        font-size: 16px !important;
    }
    button:hover {
        background-color: #333333 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Header
# -----------------------------
st.title("🙃 Excuse Generator")
st.caption("Pick a tone. Sound human. Or don’t.")

# -----------------------------
# CASUAL (realistic)
# -----------------------------
CASUAL = [
    "Sorry, just saw this.",
    "My bad — long day.",
    "Just catching up on texts.",
    "Sorry, work got busy.",
    "Just now seeing this.",
    "My bad, I knocked out.",
    "Was away from my phone for a bit.",
    "Got distracted and forgot to respond.",
    "Lost track of time earlier.",
    "Today moved faster than expected.",
    "Just resurfacing now.",
    "Phone’s been ignored all day, my bad.",
    "Long story short: busy day.",
    "Just now sitting down.",
    "Didn’t mean to disappear.",
    "Finally checking my phone.",
    "Today got away from me.",
    "Catching up now.",
    "Was running around most of the day.",
    "Just got a second to breathe.",
    "Sorry — hectic day.",
    "Totally slipped my mind.",
    "Just getting back to my phone.",
    "Got pulled into a few things.",
    "Busy stretch earlier.",
    "Just seeing this now.",
    "Long afternoon, my bad.",
    "Didn’t mean to reply so late.",
    "Work kind of took over.",
    "Busy day but free now.",
    "Just getting around to messages.",
    "Lost track of time today.",
    "Sorry — didn’t mean to lag.",
    "Just finished up some stuff.",
    "Phone was ignored earlier.",
    "Just catching this.",
    "Today was packed.",
    "Got caught up with things.",
    "Sorry — didn’t see this earlier.",
    "Just got out of work mode.",
    "Today flew by.",
    "Got sidetracked earlier.",
    "Just now checking messages.",
    "Didn’t mean to leave you hanging.",
    "Busy but here now.",
    "Just resurfacing from today.",
    "Sorry — phone was neglected.",
    "Just wrapping things up.",
    "Got tied up for a bit.",
    "Just seeing your message.",
    "Lost track of my phone.",
    "Late reply, my bad.",
]

# -----------------------------
# FLIRTY (subtle, not cringe)
# -----------------------------
FLIRTY = [
    "Worth the wait though 🙂",
    "Okay hi — I’m back now.",
    "Survived the day. What’d I miss?",
    "Back from the chaos.",
    "Late reply, same interest.",
    "Okay, I’m here now.",
    "Hi again 👋",
    "I disappeared briefly — my bad.",
    "Hope your day’s going well.",
    "Alright, your turn.",
    "Back online and behaving.",
    "Made it through the day.",
    "Delayed response, not delayed interest.",
    "I owe you a reply and probably coffee.",
    "Okay, catching up now.",
    "Sorry — had to re-enter society.",
    "Back from real life.",
    "Worth circling back to this.",
    "Late, but intentional.",
    "Hi — survived the day.",
    "Okay, I’m listening now.",
    "Back from adulting.",
    "Had to disappear briefly.",
    "Alright, talk to me.",
    "I’m better at this now.",
    "Late reply, honest smile included.",
    "Okay, back in the chat.",
    "Hope today treated you well.",
    "Sorry — life interrupted.",
    "Back and curious.",
    "Okay, what’d I miss?",
    "Had to step away for a bit.",
    "I’m here now, promise.",
    "Delayed but present.",
    "Back from the day.",
    "Hi — long day.",
    "Sorry, got pulled away.",
    "Okay, caught up.",
    "Late reply, still here.",
    "Back from chaos mode.",
    "Okay, your move.",
]

# -----------------------------
# HONEST (direct + emotionally mature)
# -----------------------------
HONEST = [
    "Honestly, I needed a break from my phone.",
    "Today was heavier than expected.",
    "Was in a weird headspace earlier.",
    "Didn’t have the energy to reply before.",
    "Needed some offline time.",
    "Had a lot going on today.",
    "I tend to disappear when I’m overwhelmed.",
    "Just didn’t want to half-reply earlier.",
    "I’m better at replying once the day slows down.",
    "Took some quiet time today.",
    "Was mentally checked out for a bit.",
    "Trying to be more present now.",
    "I’m not great at texting during busy days.",
    "Needed to reset earlier.",
    "I wanted to reply when I could focus.",
    "Was dealing with a lot today.",
    "Didn’t have much social energy earlier.",
    "Just being honest — today drained me.",
    "I’m more responsive in the evenings.",
    "Thanks for the patience.",
    "Today took more out of me than expected.",
    "Needed to step away for a bit.",
    "Had to unplug earlier.",
    "I wasn’t in a great headspace earlier.",
    "Trying to pace myself today.",
    "Didn’t want to rush a response.",
    "Needed some quiet time.",
    "I’m not ignoring you.",
    "Today was a lot.",
    "Had to take care of some things.",
    "Was prioritizing some offline stuff.",
    "Just getting back into texts.",
    "I reply better when I can be present.",
    "Thanks for understanding.",
    "Just being upfront.",
]

# -----------------------------
# FUNNY / NOT REAL (clearly unserious)
# -----------------------------
FUNNY = [
    "Sorry — I was fighting for my life (mentally).",
    "I meant to reply but time simply refused.",
    "I disappeared to preserve the mystery.",
    "I replied in my head. Technology failed me.",
    "I was busy doing nothing, aggressively.",
    "Sorry — I was buffering.",
    "I got distracted by absolutely everything.",
    "I was unavailable due to vibes.",
    "I accidentally took a nap with no exit plan.",
    "I vanished briefly for character development.",
    "I was caught in a staring contest with my ceiling.",
    "I meant to reply sooner but forgot I exist.",
    "Time slipped through my fingers dramatically.",
    "I was trapped in the ‘just one more scroll’ loop.",
    "I disappeared to reset my personality.",
    "I was offline emotionally and spiritually.",
    "I thought about replying, which counts, right?",
    "I delayed replying for suspense.",
    "I was busy pretending to be productive.",
    "I disappeared for plot reasons.",
    "I went to reply and immediately panicked.",
    "I was busy overthinking punctuation.",
    "I vanished briefly to recharge my vibe.",
    "I got distracted by snacks.",
    "I disappeared to maintain balance in the universe.",
    "I was stuck in a nap dimension.",
    "I was unavailable due to poor planning.",
    "I meant to reply and then didn’t.",
    "I was buffering socially.",
    "I got distracted by my own thoughts.",
    "I vanished briefly to avoid responsibility.",
    "I was fighting autocorrect.",
    "I delayed my reply artistically.",
    "I disappeared and reappeared — classic me.",
    "I forgot how conversations work.",
]

# -----------------------------
# Tone selector
# -----------------------------
tone = st.radio(
    "Select tone",
    ["Casual", "Flirty", "Honest", "Funny / Not Real"],
    horizontal=True
)

# -----------------------------
# State
# -----------------------------
if "current_excuse" not in st.session_state:
    st.session_state.current_excuse = "Click the button."

def generate_excuse():
    if tone == "Casual":
        st.session_state.current_excuse = random.choice(CASUAL)
    elif tone == "Flirty":
        st.session_state.current_excuse = random.choice(FLIRTY)
    elif tone == "Honest":
        st.session_state.current_excuse = random.choice(HONEST)
    else:
        st.session_state.current_excuse = random.choice(FUNNY)

# -----------------------------
# Excuse card
# -----------------------------
st.markdown(
    f"""
    <div id="excuse-box" style="
        font-size:18px;
        padding:22px;
        background-color:#ffffff;
        color:#000000;
        border-radius:14px;
        box-shadow:0 6px 20px rgba(0,0,0,0.1);
        margin-bottom:16px;">
        {st.session_state.current_excuse}
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 1])

with col1:
    st.button("Generate Excuse 🙃", on_click=generate_excuse)

with col2:
    st.markdown(
        f"""
        <button onclick="navigator.clipboard.writeText(`{st.session_state.current_excuse}`)">
            Copy 📋
        </button>
        """,
        unsafe_allow_html=True
)

st.caption("Funny mode is jokes. Casual/Flirty/Honest are real texts.")

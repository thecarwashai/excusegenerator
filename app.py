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
# FORCE LIGHT MODE STYLES
# -----------------------------
st.markdown(
    """
    <style>
    html, body, [data-testid="stApp"] {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    /* Remove dark mode overrides */
    * {
        color: #000000 !important;
    }

    /* Button styling */
    button[kind="primary"], button {
        background-color: #ff7a18 !important;
        color: #ffffff !important;
        border-radius: 10px !important;
        border: none !important;
        font-size: 16px !important;
    }

    button:hover {
        background-color: #e96b0f !important;
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# App Header
# -----------------------------
st.title("🙃 Excuse Generator")
st.caption("For when honesty feels… aggressive.")

# -----------------------------
# Humor-first excuses (120+)
# -----------------------------
EXCUSES = [
    "Sorry for the late reply — my brain put this message in airplane mode.",
    "I meant to reply earlier but accidentally stared at the wall for 20 minutes.",
    "I opened your message, smiled, and immediately forgot how time works.",
    "I was busy pretending I have my life together.",
    "Sorry I’m late — I got stuck in a very intense internal monologue.",
    "I replied in my head. Sadly, that version of me is unreliable.",
    "I was about to text back and then my phone watched me fail.",
    "I got distracted doing something extremely important (scrolling).",
    "I was offline emotionally, spiritually, and technologically.",
    "My phone was right next to me. I chose chaos instead.",
    "I took a ‘quick break’ and woke up in a new personality.",
    "I didn’t ghost — I lightly evaporated.",
    "I was busy overthinking a response that did not need overthinking.",
    "I started typing and then panicked about punctuation.",
    "Sorry — my social battery went into low power mode.",
    "I was busy convincing myself I’d reply ‘in a minute.’",
    "I accidentally treated your message like a bookmark.",
    "I got lost in the endless loop of ‘I’ll respond after this.’",
    "I was doing nothing, but very intensely.",
    "I was distracted by the idea of being productive.",
    "I forgot to reply because I’m built different (badly).",
    "I was buffering.",
    "My brain said ‘reply later’ and never specified when.",
    "I got emotionally sidetracked by snacks.",
    "I was busy having a main character moment.",
    "I replied mentally and expected technology to respect that.",
    "I got trapped in a nap that had no exit strategy.",
    "Sorry — I thought I replied. Confidence was high. Accuracy was low.",
    "I was caught in a staring contest with my ceiling.",
    "I was busy reorganizing my thoughts alphabetically.",
    "I disappeared briefly to recharge my personality.",
    "I got distracted trying to remember what I was distracted by.",
    "I was on mute in real life.",
    "I saw your text and then time fast-forwarded.",
    "I didn’t ignore you — I underestimated myself.",
    "I was emotionally unavailable to my own phone.",
    "I accidentally opened 47 mental tabs.",
    "I was busy overestimating my ability to multitask.",
    "I had to consult my inner committee. They were unhelpful.",
    "I got delayed by an unexpected vibe check.",
    "I went to reply and fell into the ‘just one more scroll’ trap.",
    "I was stuck choosing between being funny or being on time.",
    "I had the intention. The execution escaped.",
    "I was busy thinking of a clever excuse. Mission accomplished.",
    "I vanished briefly to maintain mystery. Nailed it.",
    "I was late because I thought I had time. I did not have time.",
    "I got distracted by the concept of replying.",
    "I was practicing self-care (avoiding responsibility).",
    "I was lost in thought. It was poorly organized.",
    "I got delayed by my own procrastination tutorial.",
    "I tried to reply earlier but life said ‘no ❤️’.",
    "I was busy having a staring contest with my phone.",
    "I meant to respond sooner, but my motivation left the chat.",
    "I was buffering socially.",
    "I took a break that aggressively overstayed.",
    "I was trapped in a loop of ‘I’ll respond after this song.’",
    "I got distracted building a fake personality in my head.",
    "I accidentally ghosted myself too.",
    "I was temporarily unavailable due to vibes.",
    "I got caught in traffic… mentally.",
    "I forgot because I am, at my core, just a guy.",
    "I was doing something important (thinking about nothing).",
    "I replied late because I respect suspense.",
    "I disappeared to preserve the mystery (and failed).",
    "I was briefly offline to avoid my responsibilities.",
    "I got distracted by the idea of becoming a better person.",
    "I forgot to reply because time is a suggestion.",
    "I was stuck in ‘do I reply now or later’ paralysis.",
    "I was busy overthinking the word ‘hey.’",
    "I delayed my response to seem mysterious. I overshot it.",
    "I had my phone. I lacked discipline.",
    "I went to reply and immediately forgot how conversations work.",
    "I was practicing being low effort ironically.",
    "I accidentally treated your message like a to-do item.",
    "I was busy losing track of time professionally.",
    "I got distracted by my own thoughts. They were loud.",
    "I disappeared briefly to reset my personality settings.",
    "I was unavailable due to poor time management.",
    "I forgot to reply because my brain went into power-saving mode.",
    "I was stuck choosing emojis.",
    "I delayed my reply to avoid sounding eager. I failed spectacularly.",
    "I got distracted trying to remember if I replied already.",
    "I was busy doing absolutely nothing.",
    "I accidentally opened Instagram and lost 30 minutes.",
    "I was socially buffering.",
    "I thought about replying, which is basically replying.",
    "I got delayed by a surprise nap.",
    "I vanished briefly to maintain balance in the universe.",
    "I was busy ignoring my responsibilities — including replying.",
    "I got distracted by my own reflection.",
    "I forgot because my brain runs on trial software.",
    "I was temporarily unavailable due to vibes and poor planning.",
    "I went to reply and immediately lost confidence.",
    "I delayed responding to keep things interesting. Oops.",
    "I was stuck in analysis paralysis over punctuation.",
    "I forgot to reply because I am not built for urgency.",
    "I was busy existing.",
    "I got distracted by literally anything else.",
    "I was offline emotionally and my phone respected that.",
    "I delayed replying because my brain needed a reboot.",
    "I vanished briefly to reset my social skills.",
    "I forgot to respond because time is fake.",
]

# -----------------------------
# State
# -----------------------------
if "current_excuse" not in st.session_state:
    st.session_state.current_excuse = "Click the button."

def generate_excuse():
    st.session_state.current_excuse = random.choice(EXCUSES)

# -----------------------------
# Excuse Card
# -----------------------------
st.markdown(
    f"""
    <div style="
        font-size:18px;
        padding:22px;
        background-color:#ffffff;
        color:#000000;
        border-radius:14px;
        box-shadow:0 6px 20px rgba(0,0,0,0.1);
        margin-bottom:16px;
        font-weight:500;">
        {st.session_state.current_excuse}
    </div>
    """,
    unsafe_allow_html=True
)

st.button("Generate Excuse 🙃", on_click=generate_excuse)

st.caption("Use responsibly. Or irresponsibly. I’m not your manager.")

import streamlit as st

# =========================
# BASIC CONFIG
# =========================
st.set_page_config(
    page_title="For You, My Love 🌹",
    page_icon="🌹",
    layout="wide",
)
with st.sidebar:
    st.image(
        "WhatsApp Image 2025-11-16 at 18.46.54.jpeg",        # path to your image
        use_container_width=True
    )
with st.sidebar:
    st.video(
        "WhatsApp Video 2025-11-16 at 20.14.37.mp4",        # path to your image
        
    )
# =========================
# EXTREMELY ROMANTIC THEME (CSS)
# =========================

ROMANTIC_NIGHT_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;500;600;700&family=Poppins:wght@300;400;500;600&display=swap');

html, body, [class*="css"]  {
    font-family: "Poppins", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* Cosmic rose background */
.stApp {
    background: radial-gradient(circle at top, #3b0029 0, #120014 35%, #050008 75%);
    color: #fef5ff;
}

/* Hide menu/footer for clean look */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Soft scroll */
body {
    scroll-behavior: smooth;
}

/* Glowing background overlay */
.body-background:before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    background-image:
        radial-gradient(circle at 10% 20%, rgba(255, 105, 180, 0.16) 0, transparent 55%),
        radial-gradient(circle at 80% 10%, rgba(255, 182, 193, 0.12) 0, transparent 55%),
        radial-gradient(circle at 20% 80%, rgba(186, 85, 211, 0.18) 0, transparent 55%);
    z-index: -1;
}

/* HERO SECTION */
.hero-wrap {
    padding: 2.4rem 0 1.4rem 0;
    text-align: center;
}

.hero-to {
    font-family: "Playfair Display", serif;
    font-size: 1.3rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #ffd9eb;
    margin-bottom: 0.5rem;
}

.hero-title {
    font-family: "Great Vibes", cursive;
    font-size: 4.4rem;
    color: #ffd1e6;
    text-shadow: 0 0 18px rgba(255, 105, 180, 0.7);
    margin-bottom: 0.2rem;
}

.hero-subtitle {
    font-family: "Playfair Display", serif;
    font-size: 1.2rem;
    color: #f7c3de;
    opacity: 0.92;
    margin-bottom: 1.0rem;
}

.hero-from {
    font-size: 0.95rem;
    color: #ffbcd1;
    opacity: 0.85;
}

/* Big glowing heart */
.glow-heart {
    font-size: 2.4rem;
    text-shadow: 0 0 20px rgba(255, 192, 203, 0.9);
    animation: pulseHeart 1.8s ease-in-out infinite;
}

@keyframes pulseHeart {
    0% { transform: scale(1); opacity: 0.9; }
    50% { transform: scale(1.12); opacity: 1; }
    100% { transform: scale(1); opacity: 0.9; }
}

/* Glassmorphism cards */
.glass-card {
    background: radial-gradient(circle at top left, rgba(255, 192, 203, 0.11), rgba(0, 0, 0, 0.45));
    border-radius: 26px;
    padding: 1.6rem 1.9rem;
    border: 1px solid rgba(255, 182, 193, 0.32);
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.65);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    margin-bottom: 1.4rem;
}

/* Section titles */
.section-label {
    font-size: 0.78rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: #ffb3d8;
    margin-bottom: 0.3rem;
}

.section-title {
    font-family: "Playfair Display", serif;
    font-size: 1.7rem;
    font-weight: 600;
    color: #ffe5f4;
    margin-bottom: 0.5rem;
}

/* Text */
.main-text {
    font-size: 0.98rem;
    color: #ffe0f5;
    line-height: 1.7;
}

/* Divider */
.heart-divider {
    text-align: center;
    font-size: 1.6rem;
    margin: 1.4rem 0 1rem 0;
    color: #ff9ac5;
    text-shadow: 0 0 16px rgba(255, 105, 180, 0.7);
}

/* Timeline */
.timeline-chip {
    font-size: 0.75rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #ffafc9;
    margin-bottom: 0.2rem;
}

.timeline-title {
    font-weight: 600;
    color: #ffe8f5;
    font-size: 1.05rem;
    margin-bottom: 0.2rem;
}

.timeline-text {
    font-size: 0.94rem;
    color: #ffe4f8;
}

.timeline-dot {
    width: 14px;
    height: 14px;
    border-radius: 999px;
    background: radial-gradient(circle, #ff5f9a 0, #ff005f 75%);
    box-shadow: 0 0 18px rgba(255, 105, 180, 0.9);
    margin-top: 0.4rem;
}

.timeline-line {
    width: 2px;
    background: linear-gradient(to bottom, rgba(255, 182, 193, 0.4), rgba(255, 105, 180, 0.12));
    flex-grow: 1;
    margin: 0.18rem auto;
}

/* Reasons grid */
.reason-number {
    font-weight: 600;
    color: #ffbedb;
    margin-right: 0.35rem;
    font-size: 0.95rem;
}

.reason-text {
    font-size: 0.95rem;
    color: #ffe7f6;
}

/* Love letter */
.love-letter {
    font-size: 1rem;
    color: #ffeefc;
    line-height: 1.8;
    white-space: pre-wrap;
}

.locked {
    filter: blur(5px);
    opacity: 0.84;
    user-select: none;
    pointer-events: none;
}

/* Small notes */
.small-note {
    font-size: 0.84rem;
    color: #ffc2e4;
    opacity: 0.85;
    margin-top: 0.6rem;
}

/* Final CTA */
.final-cta {
    text-align: center;
    font-size: 1.35rem;
    font-weight: 600;
    color: #ffd6f1;
    margin-top: 0.8rem;
}

/* Buttons */
.stButton>button {
    border-radius: 999px;
    padding: 0.5rem 1.4rem;
    background: radial-gradient(circle at top left, #ff85b3, #ff2e7a);
    color: #fff;
    border: none;
    box-shadow: 0 0 18px rgba(255, 105, 180, 0.7);
    font-weight: 500;
}

.stButton>button:hover {
    background: radial-gradient(circle at top left, #ff97c6, #ff3e86);
    box-shadow: 0 0 30px rgba(255, 105, 180, 0.9);
}

/* Input */
.stTextInput>div>div>input {
    background-color: rgba(10, 0, 20, 0.75);
    border-radius: 999px;
    border: 1px solid rgba(255, 182, 193, 0.5);
    color: #ffe6f7;
}

/* NAV RADIO */
.nav-container {
    padding: 0.2rem 1rem 1.4rem 1rem;
}

.nav-container > div[role="radiogroup"] {
    background: radial-gradient(circle at top left, rgba(255, 192, 203, 0.12), rgba(0,0,0,0.45));
    border-radius: 999px;
    padding: 0.3rem 0.8rem;
    border: 1px solid rgba(255, 182, 193, 0.35);
    display: flex;
    justify-content: center;
    gap: 0.5rem;
}

.nav-container label {
    color: #ffcee4 !important;
    font-size: 0.86rem;
}

/* hide radio dots */
.nav-container input[type="radio"] {
    display: none;
}
</style>
"""
st.markdown('<div class="body-background"></div>', unsafe_allow_html=True)
st.markdown(ROMANTIC_NIGHT_CSS, unsafe_allow_html=True)

# =========================
# DATA TO CUSTOMIZE 💌
# =========================

GF_NAME = "Khushi"       # <-- put her real name
NICKNAME = "Dove "   # <-- your nickname for her
YOUR_NAME = "Ray"    # <-- your name / nickname she uses
SECRET_ANSWER = "dove"   # <-- answer to unlock letter (lowercase)

# Timeline memories
TIMELINE = [
    {
        "label": "The first spark",
        "title": "When you came out of home during COVID and waved at me, OMG.",
        "text": "I remember how pretty you were looking, the way your HELLO sounded, and how my brain went a little quiet when you smiled.",
    },
    {
        "label": "Right now",
        "title": "You, here, reading this",
        "text": "And now you’re on this page I made just for you, and my chest feels full just knowing you’re here and you are just MINE.",
    },
]

# Reasons you love her
LOVE_REASONS = [
    "You are extremely well-spoken, well-mannered, and incredibly smart.",
    "You treat everyone with respect and kindness, and someone like you deserves even more kindness in return.",
    "You listen to your heart, and that honesty makes you beautiful from the inside.",
    "You are the prettiest girls God has ever created.",
    "You have an amazing dressing sense that always makes you look elegant.",
    "Your beautiful, thick hair that I absolutely adore.",
    "Your humbleness, especially in the way you treat me.",
    "The way you share everything with me and make me feel trusted.",
    "How you forgive me when I make small mistakes.",
    "You are genuinely funny.....I love your jokes and the way you make me laugh.",
    "That you’re you. Just you. And somehow, unbelievably, you’re here with me."
]

# Love letter
LOVE_LETTER = f"""
Dear {GF_NAME},  

First go down and play the song that I have dedicated to you, and listen to that while reading this letter.

I am a soft hearted person with a huge dreams. I have had crushes in my life before until,
I saw you that evening during COVID. You with that amazing smile and that amzing outfit coming out of your house.
Th first time my heart started to beat for you was that day. I loved all the times spent with you. Every single day, I used to think of you.
You were so kind to me, you respceted me a lot, you have such an amazing heart sweetheart, and I am thankful to God and your mom and dad to give birth to such a precious human being.
Even after I proposed you and we were not in relationship, I never had hatred for you, just a little jealously that why do I don't have such an amazing person as my partner. 
Thank you so much sweetheart you shared yourr feelings with me on 3rd Septemeber. I love you and I swear to myself, I will love you till my last breathe. 
Let's forget what has happened in the past, in our individual lives, and keep making new chapters in our love story. I want to be the reason behind your smile, 
the one who holds your hand through every up and down, and the person you can always count on.
I will always support you sweeetheart, in your dreams, in your goals, and in your happiness. I want to be the one who stands by you through every challenge.
You can put your head on your chest and sleep peacefully, knowing that I will always be there to protect you, to love you, and to cherish you.
I LOVE YOU SO MUCH MY DOVE. I am so grateful to have you in my life, and I promise to do everything I can to make you happy and to show you how much you mean to me.


I have decidated a song for you. It is not written by me, but it expresses my feelings for you in a way that words sometimes can’t.

I LOVE YOU SO SO SO SO MUCH.

With all of my heart.
{YOUR_NAME} 🌹
"""

# Date / surprise plan
DATE_IDEA = """
Here’s what I’m dreaming about for us in Mumbai:

• A night that belongs only to us......no rush, no alarms, no ‘what time is it?’  
• Your favorite food (lot of chatpata food)  
• A playlist I made just for you, playing softly in the background and watch a movie together and do mast-mast shopping in Colaba and Marine Drive.
• A walk, a view, a quiet corner where we can just exist next to each other  

I love you 
"""

# =========================
# SESSION STATE
# =========================

if "letter_unlocked" not in st.session_state:
    st.session_state.letter_unlocked = False

# =========================
# HERO SECTION
# =========================

st.markdown(
    f"""
<div class="hero-wrap">
    <div class="hero-to">TO MY BABY</div>
    <div class="hero-title">Khushi</div>
    <div class="section-label">
        a small universe of words and pixels, coded at ridiculous hours,  
        just to say one simple thing: <span class="glow-heart">♥</span> i love you
    </div>
    <div class="hero-from">FROM: {"Ray Manvendra" }</div>
</div>
""",
    unsafe_allow_html=True,
)

# =========================
# NAVIGATION (MULTIPLE PAGES)
# =========================

nav_labels = [
    "Prologue 🕯️",
    "Our Story 📖",
    "Reasons I Love You 💗",
    "Letter ✉️",
    "The Question 🌙",
]

page_map = {
    "Prologue 🕯️": "welcome",
    "Our Story 📖": "story",
    "Reasons I Love You 💗": "reasons",
    "Letter ✉️": "letter",
    "The Question 🌙": "surprise",
}

st.markdown('<div class="nav-container">', unsafe_allow_html=True)
try:
    selected_label = st.radio(
        "Navigate",
        nav_labels,
        key="nav_choice",
        horizontal=True,
        label_visibility="collapsed",
    )
except TypeError:
    # fallback if horizontal isn't supported
    selected_label = st.radio(
        "Navigate",
        nav_labels,
        key="nav_choice",
        label_visibility="collapsed",
    )
st.markdown('</div>', unsafe_allow_html=True)

current_page = page_map[selected_label]

# =========================
# PAGE FUNCTIONS
# =========================

def page_welcome():
    col = st.container()
    with col:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-label">CHAPTER I</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Our little universe</div>', unsafe_allow_html=True)
        st.markdown(
            f"""
<p class="main-text">
Somewhere between the random conversations, the teasing, the comfort,  
and the way your name started to feel like a safe place in my head,  
we quietly built a little universe that exists only between you and me.  

In that universe, it’s just <b>you</b>, <b>me</b>, and a thousand small moments  
that I never want to forget.
</p>
""",
            unsafe_allow_html=True,
        )
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-label">NOTE</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">How to read this</div>', unsafe_allow_html=True)
        st.markdown(
            """
<p class="main-text">
Use the glowing menu above to move through each chapter.  
There’s no rush. Read it slowly, maybe with your favorite song on,  
and remember that every line here is just another way of saying:  
<b>I am so, so happy it’s you.</b>
</p>
""",
            unsafe_allow_html=True,
        )
        st.markdown('</div>', unsafe_allow_html=True)


def page_story():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">CHAPTER II</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Polaroids in my head</div>', unsafe_allow_html=True)
    st.markdown(
        '<p class="main-text">If I could print my favorite memories with you like polaroids, some of them would look like this:</p>',
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    for item in TIMELINE:
        row = st.columns([0.22, 0.1, 1.7])
        with row[0]:
            st.markdown(f'<div class="timeline-chip">{item["label"].upper()}</div>', unsafe_allow_html=True)
        with row[1]:
            st.markdown('<div class="timeline-dot"></div>', unsafe_allow_html=True)
            st.markdown('<div class="timeline-line"></div>', unsafe_allow_html=True)
        with row[2]:
            st.markdown(f'<div class="timeline-title">{item["title"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="timeline-text">{item["text"]}</div>', unsafe_allow_html=True)
            st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def page_reasons():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">CHAPTER III</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Some of the reasons why I love you babe</div>', unsafe_allow_html=True)
    st.markdown(
        '<p class="main-text">If I tried to list every reason I love you, this page would never end. But here are a few:</p>',
        unsafe_allow_html=True,
    )

    cols = st.columns(2)
    for i, reason in enumerate(LOVE_REASONS, start=1):
        col = cols[(i - 1) % 2]
        with col:
            st.markdown(
                f"""
<div style="margin-bottom:0.7rem;">
    <span class="reason-number">{i:02d}.</span>
    <span class="reason-text">{reason}</span>
</div>
""",
                unsafe_allow_html=True,
            )
    st.markdown('</div>', unsafe_allow_html=True)


def page_letter():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">CHAPTER IV</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">A letter only for you</div>', unsafe_allow_html=True)
    st.markdown(
        """
<p class="main-text">
There’s a letter here that’s a little more private.  
To open it, type the nickname I gave you..
</p>
""",
        unsafe_allow_html=True,
    )

    answer = st.text_input("Type it here (all lowercase, no pressure):", key="unlock_input")

    if answer:
        if answer.strip().lower() == SECRET_ANSWER.strip().lower():
            st.session_state.letter_unlocked = True
            st.success("You opened it. Of course you did. 🌹")
            st.balloons()
        else:
            st.warning("Not the word I wrote… but still kind of cute. Try again? 🥺")

    if st.session_state.letter_unlocked:
        st.markdown(f'<div class="love-letter">{LOVE_LETTER}</div>', unsafe_allow_html=True)
        st.audio("Everglow.mp3")
    else:
        st.markdown(f'<div class="love-letter locked">{LOVE_LETTER}</div>', unsafe_allow_html=True)
        

    st.markdown('</div>', unsafe_allow_html=True)


def page_surprise():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">CHAPTER V</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">The part where I ask you something</div>', unsafe_allow_html=True)
    st.markdown(
        f'<p class="main-text">{DATE_IDEA}</p>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="heart-divider">✧  ✧  ✧</div>', unsafe_allow_html=True)
    st.markdown(
        '<p class="final-cta">So… will you go on this date with me?</p>',
        unsafe_allow_html=True,
    )

    if st.button("Yes. Obviously. 🌙"):
        st.balloons()
        st.snow()
        st.success("Can't wait to meet in May in Mumbai, my love! 🌹")

    st.markdown(
        '<div class="small-note">By pressing that button, you also agree to at least one unreasonably long hug.</div>',
        unsafe_allow_html=True,
    )


# =========================
# ROUTER
# =========================

if current_page == "welcome":
    page_welcome()
elif current_page == "story":
    page_story()
elif current_page == "reasons":
    page_reasons()
elif current_page == "letter":
    page_letter()
elif current_page == "surprise":
    page_surprise()

import random
import streamlit as st

st.set_page_config(page_title="Number Guessing Game", page_icon="🎯", layout="centered")

st.markdown("""
<style>
.stApp {background:linear-gradient(135deg,#0F172A,#1E1B4B);color:white;}
.made-by {text-align:center;color:#A5B4FC;font-size:15px;font-weight:bold;letter-spacing:2px;margin-bottom:15px;}
.game-title {text-align:center;font-size:40px;font-weight:800;color:#818CF8;margin-bottom:5px;}
.game-subtitle {text-align:center;color:#CBD5E1;font-size:16px;margin-bottom:30px;}
.game-card {background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);padding:25px;border-radius:18px;text-align:center;margin:20px 0;}
.result-box {background:linear-gradient(135deg,#4F46E5,#7C3AED);padding:25px;border-radius:18px;text-align:center;color:white;margin-top:20px;}
.result-box h1 {font-size:50px;margin:10px;}
div.stButton > button {width:100%;height:48px;border-radius:10px;background:#4F46E5;color:white;font-weight:bold;border:none;}
div.stButton > button:hover {background:#6366F1;color:white;}
</style>
""", unsafe_allow_html=True)

# Initialize game state
if "python_number" not in st.session_state:
    st.session_state.python_number = random.randint(1, 10)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "game_status" not in st.session_state:
    st.session_state.game_status = "playing"
if "message" not in st.session_state:
    st.session_state.message = ""
if "guess_history" not in st.session_state:
    st.session_state.guess_history = []

# Header
st.markdown('<div class="made-by">✦ MADE BY SWASTIK ✦</div>', unsafe_allow_html=True)
st.markdown('<div class="game-title">🎯 Number Guessing Game</div>', unsafe_allow_html=True)
st.markdown('<div class="game-subtitle">Can you guess the secret number between 1 and 10?</div>', unsafe_allow_html=True)
st.divider()

# Game information
remaining = 3 - st.session_state.attempts
col1, col2 = st.columns(2)
col1.metric("TOTAL CHANCES", 3)
col2.metric("CHANCES LEFT", remaining)

st.markdown("""
<div class="game-card">
    <h2>🤖 Computer has selected a number!</h2>
    <p>Guess the correct number to win the game.</p>
    <p>⚡ You have only 3 chances!</p>
</div>
""", unsafe_allow_html=True)

# Number input
st.subheader("🔢 Enter Your Guess")
guess = st.number_input(
    "Choose a number between 1 and 10",
    min_value=1,
    max_value=10,
    value=5,
    step=1,
    disabled=st.session_state.game_status != "playing"
)
guess_value = int(guess) if guess is not None else 0

# Submit guess
if st.button("🚀 SUBMIT YOUR GUESS", disabled=st.session_state.game_status != "playing"):
    st.session_state.attempts += 1

    if guess_value == st.session_state.python_number:
        st.session_state.game_status = "won"
        st.session_state.message = "🎉 Congratulations! You won the game!"
    else:
        st.session_state.guess_history.append(guess_value)
        if st.session_state.attempts == 3:
            st.session_state.game_status = "lost"
            st.session_state.message = "😢 No chances left! Game Over!"
        else:
            st.session_state.message = (
                f"❌ Wrong guess! Try again. "
                f"{3 - st.session_state.attempts} chances left."
            )
    st.rerun()

# Display result
if st.session_state.message:
    st.divider()
    if st.session_state.game_status == "won":
        st.success(st.session_state.message)
        st.balloons()
        st.markdown(f"""
        <div class="result-box">
            <h2>🏆 YOU WON!</h2>
            <h1>{st.session_state.python_number}</h1>
            <p>Excellent guessing!</p>
            <p>Correct number: {st.session_state.python_number}</p>
        </div>
        """, unsafe_allow_html=True)
    elif st.session_state.game_status == "lost":
        st.error(st.session_state.message)
        st.markdown(f"""
        <div class="result-box">
            <h2>GAME OVER</h2>
            <h1>{st.session_state.python_number}</h1>
            <p>The correct number was {st.session_state.python_number}</p>
            <p>Better luck next time!</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning(st.session_state.message)

# Guess history
if st.session_state.guess_history:
    st.subheader("📜 Previous Wrong Guesses")
    st.write(" | ".join(map(str, st.session_state.guess_history)))

# New game
st.divider()
if st.button("🔄 START NEW GAME"):
    st.session_state.python_number = random.randint(1, 10)
    st.session_state.attempts = 0
    st.session_state.game_status = "playing"
    st.session_state.message = ""
    st.session_state.guess_history = []
    st.rerun()

# Footer
st.divider()
st.markdown("""
<center style="color:#94A3B8;">
Made with ❤️ using Python & Streamlit
<br><br>
© 2026 | Number Guessing Game | Swastik
</center>
""", unsafe_allow_html=True)

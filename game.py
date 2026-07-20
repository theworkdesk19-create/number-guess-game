import random
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Number Guessing Game", page_icon="🎮")

# Title and Intro Messages
st.title("🎮 Number Guessing Game")
st.subheader("Welcome to the number guess game!")
st.write("Let's play it with my bot. Let's start!")
st.write("Guess a secret number between **1 and 55**.")

# 1. Initialize State Variables (preserves variables across UI clicks)
if "owner_number" not in st.session_state:
    st.session_state.owner_number = random.randint(1, 55)

if "a" not in st.session_state:
    st.session_state.a = 0

if "game_over" not in st.session_state:
    st.session_state.game_over = False

# 2. Input Form for User
with st.form(key="guess_form"):
    number = st.number_input(
        "Enter the number:",
        min_value=1,
        max_value=55,
        step=1,
        disabled=st.session_state.game_over,
    )
    submit_button = st.form_submit_button(
        label="Submit Guess", disabled=st.session_state.game_over
    )

# 3. Game Logic Execution
if submit_button and not st.session_state.game_over:
    st.session_state.a += 1

    if st.session_state.owner_number > number:
        st.warning(f"❌ **too low!** (Attempts: {st.session_state.a})")
    elif st.session_state.owner_number < number:
        st.warning(f"❌ **too high!** (Attempts: {st.session_state.a})")
    else:
        st.success("🎉 **correct answer!**")
        st.info(f"You found it in **{st.session_state.a}** attempts!")
        st.balloons()
        st.session_state.game_over = True

# 4. Play Again Option
if st.session_state.game_over:
    if st.button("Play Again 🔄"):
        st.session_state.owner_number = random.randint(1, 55)
        st.session_state.a = 0
        st.session_state.game_over = False
        st.rerun()
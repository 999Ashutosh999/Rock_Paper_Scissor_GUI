import json
import random

import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(layout="wide")

r, p, s, i = None, None, None, None

l = ["rock", "paper", "scissor"]
a = random.choice(l)
# logic begins from here
col1, col2, col3, col4 = st.columns(4)
with col3:
    st.markdown('<h1 style="font-size: 35px; margin-left: -200px;">Rock - Paper - Scissor</h1>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<h1 style='color: #dc143c; margin-left: 550px;'>Choose one...</h1>", unsafe_allow_html=True)

with col4:
    # noinspection PyRedeclaration
    with open("rps.json") as s:
        c = json.load(s)
    st_lottie(c, width=300, key="1a")
with col1:
    with open("rps.json") as s:
        c = json.load(s)
    st_lottie(c, width=300, key="1")

c1, c2, c3, c4, c5 = st.columns(5)
with c2:
    with open("stone.json") as s:
        e = json.load(s)
        st_lottie(e, width=150, height=150, key="singh")
        # noinspection PyRedeclaration
        if st.button(label="Rock"):
            if a == "paper":
                with open("loos.json") as s:
                    e = json.load(s)
                    st_lottie(e, width=150, key="yadav0")
                st.markdown("YOU LOOSE! TRY AGAIN...")
                st.markdown("<p style= 'font-size: 22px; color: #e9967a'> YOU CHOOSE: ROCK COMPUTER CHOOSE: PAPER</p>",unsafe_allow_html=True)
            elif a == "scissor":
                with open("win.json") as s:
                    e = json.load(s)
                    st_lottie(e, width=150, key="shukla0")
                st.markdown("YOU WIN!")
                st.markdown("<p style= 'font-size: 22px; color: #de5d83'> YOU CHOOSE: ROCK COMPUTER CHOOSE: SCISSOR</p>",unsafe_allow_html=True)


            else:
                with open("draw1.json") as s:
                    e = json.load(s)
                    st_lottie(e, width=150, key="tripathi2")
                    st.markdown("MATCH DRAW!")
                    st.markdown("<p style= 'font-size: 22px; color: #ffcba4'> YOU CHOOSE: ROCK COMPUTER CHOOSE: "
                                "ROCK</p>",unsafe_allow_html=True)

with c3:
    with open("paper.json") as s:
        e = json.load(s)
        st_lottie(e, width=150, key="tiwari")
        # noinspection PyRedeclaration
        if st.button(label="Paper"):
            if a == "scissor":
                with open("loos.json") as s:
                    e = json.load(s)
                    st_lottie(e, width=150, key="yadav1")
                st.markdown("YOU LOOSE! TRY AGAIN...")
                st.markdown("<p style= 'font-size: 22px; color: #08e8de'> YOU CHOOSE: PAPER COMPUTER CHOOSE: "
                            "SCISSOR</p>",unsafe_allow_html=True)
            elif a == "rock":
                with open("win.json") as s:
                    e = json.load(s)
                    st_lottie(e, width=150, key="shukla1")
                st.markdown("YOU WIN!")
                st.markdown("<p style= 'font-size: 22px; color: #8a2be2'> YOU CHOOSE: PAPER COMPUTER CHOOSE: ROCK</p>",unsafe_allow_html=True)
            else:
                with open("draw1.json") as s:
                    e = json.load(s)
                    st_lottie(e, width=150, key="tripathi2")
                    st.markdown("MATCH DRAW!")
                    st.markdown("<p style= 'font-size: 22px; color: #ffff00'> YOU CHOOSE: PAPER COMPUTER CHOOSE: PAPER</p>",unsafe_allow_html=True)
with c4:
    with open("scissor.json") as s:
        e = json.load(s)

        st_lottie(e, width=150, key="vatsya")
        # noinspection PyRedeclaration
        if st.button(label="Scissor"):
            if a == "paper":
                with open("win.json") as s:
                    e = json.load(s)
                    st_lottie(e, width=150, key="yadav2")
                st.markdown("YOU WIN!")
                st.markdown("<p style= 'font-size: 22px; color: #b784a7'> YOU CHOOSE: SCISSOR COMPUTER CHOOSE: PAPER</p>",
                            unsafe_allow_html=True)
            elif a == "rock":
                with open("loos.json") as s:
                    e = json.load(s)
                    st_lottie(e, width=150, key="shukla2")
                st.markdown("YOU LOOSE! TRY AGAIN...")
                st.markdown("<p style= 'font-size: 22px; color: #8b008b'> YOU CHOOSE: SCISSOR COMPUTER CHOOSE: ROCK</p>",unsafe_allow_html=True)
            else:
                with open("draw1.json") as s:
                    e = json.load(s)
                    st_lottie(e, width=150, key="tripathi2")
                    st.markdown("MATCH DRAW!")
                    st.markdown("<p style= 'font-size: 22px; color: #ffa812'> YOU CHOOSE: SCISSOR COMPUTER CHOOSE: "
                                "SCISSOR</p>",unsafe_allow_html=True)
with open("rps.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.markdown("<p style= 'margin-left: 1195px; color: purple;'> :by ASHUTOSH TRIPATHI </p>",unsafe_allow_html=True)
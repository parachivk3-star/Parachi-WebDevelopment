import streamlit as st

st.markdown("""
<style>
.stApp {
    background-color: #C8A2C8;
    color: black;
}
</style>
""", unsafe_allow_html=True)


st.title("🐾 What Animal Matches Your Lifestyle?")

st.write(
    "Answer these questions about your daily habits and "
    "find out which animal matches your lifestyle!"
)

owl = 0
bear = 0
squirrel = 0
cat = 0


sleep = st.slider(
    "How many hours do you usually sleep?",
    4, 12, 8
)

if sleep >= 10:
    bear += 2
    cat += 2
elif sleep >= 8:
    bear += 1
    cat += 1
else:
    squirrel += 2


active_time = st.radio(
    "When are you usually most energetic?",
    ["Morning", "Afternoon", "Night"]
)

if active_time == "Morning":
    squirrel += 2
elif active_time == "Afternoon":
    bear += 2
else:
    owl += 2


diet = st.selectbox(
    "Which option best describes your diet?",
    ["Vegetarian", "Omnivore", "Mostly meat"]
)

if diet == "Vegetarian":
    squirrel += 2
elif diet == "Omnivore":
    bear += 2
else:
    owl += 1
    cat += 1


social = st.slider(
    "How social are you?",
    1, 10, 5
)

if social >= 8:
    squirrel += 2
elif social >= 5:
    bear += 2
else:
    cat += 2


activities = st.multiselect(
    "What do you enjoy doing?",
    [
        "Sleeping",
        "Exercising",
        "Going out with friends",
        "Being alone",
        "Eating",
        "Staying up late"
    ]
)

if "Sleeping" in activities:
    cat += 1
    bear += 1

if "Exercising" in activities:
    squirrel += 1

if "Going out with friends" in activities:
    squirrel += 1

if "Being alone" in activities:
    cat += 1

if "Eating" in activities:
    bear += 1

if "Staying up late" in activities:
    owl += 2


if st.button("Find My Animal 🐾"):

    highest_score = max(owl, bear, squirrel, cat)

    if highest_score == owl:
        st.header("🦉 You are an Owl!")
        st.write(
            "You come alive at night and enjoy having time "
            "to yourself. You're independent and observant."
        )
        st.image("images/owl.webp")

    elif highest_score == bear:
        st.header("🐻 You are a Bear!")
        st.write(
            "You enjoy your rest, your food, and a balanced "
            "lifestyle. You're relaxed but still social."
        )
        st.image("images/bear.avif")

    elif highest_score == squirrel:
        st.header("🐿️ You are a Squirrel!")
        st.write(
            "You're energetic, active, and ready to start "
            "your day early. You enjoy staying busy."
        )
        st.image("images/squirrel.jpg")

    else:
        st.header("🐱 You are a Cat!")
        st.write(
            "You value your sleep and independence. You enjoy "
            "your own space but still appreciate good company."
        )
        st.image("images/cat.avif")

    st.balloons()


st.badge("Hope you like the quiz!", icon=":material/star:", color="red")



import random
import streamlit as st
from hangman_art import logo, stages
from hangman_words import word_list

# Game initialization
if 'chosen_word' not in st.session_state:
    st.session_state.chosen_word = random.choice(word_list)
    st.session_state.word_length = len(st.session_state.chosen_word)
    st.session_state.display = ["_"] * st.session_state.word_length
    st.session_state.lives = 6
    st.session_state.guessed = set()
    st.session_state.end_of_game = False

st.title('Hangman Game')
st.markdown(f"```{logo}```")

# Display the current state of the word
st.subheader('Current Word')
st.write(' '.join(st.session_state.display))

# Allow the user to guess a letter
guess = st.text_input('Guess a letter').lower()

if guess and guess not in st.session_state.guessed and not st.session_state.end_of_game:
    st.session_state.guessed.add(guess)
    if guess in st.session_state.display:
        st.write(f"You have already guessed {guess}")

    if guess in st.session_state.chosen_word:
        for position in range(st.session_state.word_length):
            letter = st.session_state.chosen_word[position]
            if letter == guess:
                st.session_state.display[position] = letter
    else:
        st.session_state.lives -= 1
        st.write(f"You have {st.session_state.lives} lives left")

    if "_" not in st.session_state.display:
        st.session_state.end_of_game = True
        st.success("You Won!")
    
    if st.session_state.lives == 0:
        st.session_state.end_of_game = True
        st.error(f"You Lose! The word was: {st.session_state.chosen_word}")

# Display the hangman stages
st.markdown(f"```{stages[st.session_state.lives]}```")

# Reset the game
if st.session_state.end_of_game:
    if st.button('Play Again'):
        st.session_state.chosen_word = random.choice(word_list)
        st.session_state.word_length = len(st.session_state.chosen_word)
        st.session_state.display = ["_"] * st.session_state.word_length
        st.session_state.lives = 6
        st.session_state.guessed = set()
        st.session_state.end_of_game = False

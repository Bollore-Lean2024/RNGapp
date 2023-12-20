'''
Created on Tue Dec 19 2023
@author: He Zhenyu , GitHub ID: zhenyu1311
@Bollore Logistics Asia-Pacific , Supply Chain Management Intern , He Zhenyu
Last Update on Wed Dec 20 2023 2:30pm
'''

import streamlit as st
import pandas as pd
import random

df = pd.read_csv('data.csv')

# Create a Streamlit app
st.title("🐍 Snake and Ladder RNG 🎲")

# Initialize session state variables
if 'question_generated' not in st.session_state:
    st.session_state.question_generated = False

if 'question_index' not in st.session_state:
    st.session_state.question_index = 0

if 'show_answer_and_explanation' not in st.session_state:
    st.session_state.show_answer_and_explanation = False

if 'current_question' not in st.session_state:
    st.session_state.current_question = ""

if 'selected_level' not in st.session_state:
    st.session_state.selected_level = None

if 'selected_topic' not in st.session_state:
    st.session_state.selected_topic = None

# Box to group elements
st.markdown("""
<div style="border: 2px solid #ccc; padding: 10px; border-radius: 10px;">
    <h2>Select Level and Topic</h2>
    <p>Choose a level, a topic, and click 'Generate Question.'</p>
    
    <!-- Prompt user for difficulty level -->
    <h3>Select Level</h3>
    """, unsafe_allow_html=True)

# Prompt user for difficulty level
selected_level = st.selectbox("", df['Level'].dropna().unique())

# Save selected level in session state
st.session_state.selected_level = selected_level

# Filter data based on difficulty level
filtered_df = df[df['Level'] == st.session_state.selected_level]

# Prompt user for category
selected_topic = st.selectbox("Select Topic", filtered_df['Topic'].unique(), key='topic')

# Save selected topic in session state
st.session_state.selected_topic = selected_topic

# Button to generate question
generate_button = st.button("Generate Question")

# Generate a new question when the "Generate Question" button is clicked
if generate_button:
    # Filter data based on selected topic
    filtered_df = filtered_df[filtered_df['Topic'] == st.session_state.selected_topic]

    # Generate a random question index
    st.session_state.question_index = random.randint(0, filtered_df.shape[0] - 1)

    # Update session state variables
    st.session_state.question_generated = True
    st.session_state.show_answer_and_explanation = False

    # Format and display the random question
    question_number = filtered_df.iloc[st.session_state.question_index]['No.']
    question_text = filtered_df.iloc[st.session_state.question_index]['True or False - Question']
    st.session_state.current_question = f"{question_number} - {question_text}"
    st.markdown("""
    <div style="border: 2px solid #ccc; padding: 10px; border-radius: 10px; margin-top: 10px;">
        <h3>🤔 Question:</h3>
        <p>{}</p>
    </div>
    """.format(st.session_state.current_question), unsafe_allow_html=True)

# Buttons for user to answer the question
if st.session_state.question_generated:
    # Use columns to place buttons side by side
    col1, col2 = st.columns(2)

    # TRUE button
    with col1:
        true_button = st.button("TRUE ✅", key="true_button", help="Click for TRUE (Green)")
        if true_button:
            # Process user's answer
            user_answer = True
            correct_answer = str(filtered_df.iloc[st.session_state.question_index]['T/F'])

            # Convert both to lowercase for case-insensitive comparison
            user_answer_str = str(user_answer).lower()
            correct_answer_str = correct_answer.lower()

            # Display result
            if user_answer_str == correct_answer_str:
                result_message = "✅ Correct! Well done! 🎉"
            else:
                result_message = f"❌ Wrong. The correct answer is {correct_answer}."

            st.write(f"Your Answer: {user_answer}")
            st.write(result_message)

    # FALSE button
    with col2:
        false_button = st.button("FALSE ❌", key="false_button", help="Click for FALSE (Red)")
        if false_button:
            # Process user's answer
            user_answer = False
            correct_answer = str(filtered_df.iloc[st.session_state.question_index]['T/F'])

# Convert both to lowercase for case-insensitive comparison
            user_answer_str = str(user_answer).lower()
            correct_answer_str = correct_answer.lower()

            # Display result
            if user_answer_str == correct_answer_str:
                result_message = "✅ Correct! Well done! 🎉"
            else:
                result_message = f"❌ Wrong. The correct answer is {correct_answer}."

            st.write(f"Your Answer: {user_answer}")
            st.write(result_message)

# Button to show answer and explanation
show_answer_button = st.button("Show Answer and Explanation")

# Display answer and explanation if the button is clicked
if show_answer_button and st.session_state.question_generated:
    # Update session state variable
    st.session_state.show_answer_and_explanation = True

    # Display the question
    st.markdown("""
    <div style="border: 2px solid #ccc; padding: 10px; border-radius: 10px; margin-top: 10px;">
        <h3>🤔 Question:</h3>
        <p>{}</p>
    </div>
    """.format(st.session_state.current_question), unsafe_allow_html=True)

    # Display the answer
    st.markdown("""
    <div style="border: 2px solid #ccc; padding: 10px; border-radius: 10px; margin-top: 10px;">
        <h3>📚 Answer:</h3>
        <p>{}</p>
    </div>
    """.format(filtered_df.iloc[st.session_state.question_index]['T/F']), unsafe_allow_html=True)

    # Display the explanation
    st.markdown("""
    <div style="border: 2px solid #ccc; padding: 10px; border-radius: 10px; margin-top: 10px;">
        <h3>🔍 Explanation:</h3>
        <p>{}</p>
    </div>
    """.format(filtered_df.iloc[st.session_state.question_index]['Answer']), unsafe_allow_html=True)

# Button to reset
reset_button = st.button("Reset")
if reset_button:
    # Reset session state variables
    st.session_state.question_generated = False
    st.session_state.question_index = 0
    st.session_state.show_answer_and_explanation = False
    st.session_state.current_question = ""
    st.session_state.selected_level = None
    st.session_state.selected_topic = None






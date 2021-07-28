import streamlit as st

st.write("This is a software to calculate GCS score")
st.write("Welcome to the GCS score calculator  - copyright Dr Hrishikesh Sarkar")
st.write("About me [link](https://getdrsarkar.com)")


st.write("Enter level of consciousness")

eye = { 
    4: "Spontaneous",
    3: "To call",
    2: "To pain",
    1: "Nil",
    }   

mode1 = st.radio(
    label="Choose an eye option:",
    options= (4, 3, 2, 1), 
    format_func=lambda x: eye.get(x),
    )   


motor = { 
    6: "Obeying",
    5: "Localising",
    4: "Withdawal",
    3: "Flexion",
    2: "Extension",
    1: "Nil",
    }   

mode2 = st.radio(
    label="Choose a motor option:",
    options= (6, 5, 4, 3, 2, 1), 
    format_func=lambda x: motor.get(x),
    )   


verbal = { 
    5: "Oriented",
    4: "Confused",
    3: "Inappropriate words",
    2: "Sounds",
    1: "Nil",
    }   

mode3 = st.radio(
    label="Choose a verbal option:",
    options= (5, 4, 3, 2, 1), 
    format_func=lambda x: verbal.get(x),
    )   



gcs = mode1 + mode2 + mode3

#st.write(gcs)

with st.form(key='my_form'):
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write(gcs)




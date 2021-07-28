import streamlit as st
from PIL import Image

st.title("GCS Calculator - A web app by Dr Hrishikesh Sarkar (Updated 07/21)")
image = Image.open('head.jpeg')
st.image(image)

st.subheader("This is a web app to calculate GCS score (Glasgow Coma Scale), which is used to measure level of consciousness in patients with head injury. Apart from GCS, it categorises severity of head injury, proposed management and prognosis")
st.subheader("It is my first app which is shareable and developed with Python, Streamlit and Github!")

st.write("About me [link](https://getdrsarkar.com)")

eye = { 
    4: "Spontaneous",
    3: "To call",
    2: "To pain",
    1: "Nil",
    }   

mode1 = st.radio(
    label="Choose an option relevent to eye opening:",
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
    st.write("The GCS score of the patient is", gcs)
    if gcs<=8:
        st.write("This is a severe head injury. Consider airway protection and urgent neurosurgical consultation. Guarded prognosis.")
    if gcs>13:
        st.write("This is a mild head injury. Needs close neurological oberservation and imaging. Excellent prognosis.")
    if gcs>8 and gcs<13:
        st.write("This is a moderate head injury. Needs neurosurgical consultation. Good prognosis.")


st.write("Disclaimer: Content purely representative and not to be taken as medical advice.")



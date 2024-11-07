import streamlit as st
import pickle
import numpy as np

# Load the model
def load_model():
    with open('C:/Users/ASUS/Desktop/ml-g6/ST -4052/Final Project/saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
model = data["model"]
pca = data["pca"]

def show_predict_page():
    # Apply custom CSS for labels, button text, and prediction result color
    st.markdown(
        """
        <style>
        /* Make labels white and bold */
        .stNumberInput label {
            color: white !important;
            font-weight: bold;
        }
        /* Make the Predict button text black */
        div.stButton > button {
            color: black !important;
        }
        /* Custom style for the result text to make it white */
        .st-success {
            color: white !important;
            background-color: #4CAF50 !important;  /* Optional: Change background color */
            padding: 10px;
            border-radius: 5px;
            font-size: 16px;
        }
        /* Style for number inputs */
        .stNumberInput input {
            color: black !important;
            background-color: #f0f0f0 !important;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    st.title("Rice Class Prediction")
    st.write("### Please enter the following information to predict the rice class")

    # Form for user input
    area = st.number_input("Area", min_value=0.0)
    major_axis_length = st.number_input("Major Axis Length", min_value=0.0)
    minor_axis_length = st.number_input("Minor Axis Length", min_value=0.0)
    eccentricity = st.number_input("Eccentricity", min_value=0.0)
    convex_area = st.number_input("Convex Area", min_value=0.0)
    equiv_diameter = st.number_input("Equivalent Diameter", min_value=0.0)
    extent = st.number_input("Extent", min_value=0.0)
    perimeter = st.number_input("Perimeter", min_value=0.0)
    roundness = st.number_input("Roundness", min_value=0.0)
    aspect_ratio = st.number_input("Aspect Ratio", min_value=0.0)

    if st.button("Predict"):
        data = np.array([[area, major_axis_length, minor_axis_length, eccentricity, convex_area, equiv_diameter, extent, perimeter, roundness, aspect_ratio]])
        data_scaled = pca.transform(data)
        prediction = model.predict(data_scaled)
        
        # Display the prediction with customized CSS
        if prediction == 1:
            st.markdown('<p class="st-success">The predicted rice class is: <strong>Jasmine</strong></p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="st-success">The predicted rice class is: <strong>Gonen</strong></p>', unsafe_allow_html=True)

# Call the function to run the predict page
if __name__ == "__main__":
    show_predict_page()










import streamlit as st
import base64
from predict_page import show_predict_page
from explore_page import show_explore_page  # Import the explore page function
import time

# Function to convert image to base64 encoding
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Sidebar Content Styling - Apply globally
def enhance_sidebar():
    # Add a title with an emoji for fun
    st.sidebar.title("🌾 Rice Varieties Exploration 🌾")

    # Add a fun description or slogan
    st.sidebar.markdown("Welcome to the Rice World! 🌍 Let's explore the most delicious rice varieties 🍚")

    # Add a call-to-action button
    st.sidebar.markdown("### 🔍 Explore or Predict")
    page = st.sidebar.selectbox("Choose an option:", ("Predict", "Explore"))

    # Fun tips
    st.sidebar.markdown("✨ **Tip:** Use 'Explore' to discover rice varieties and 'Predict' to use our AI predictions.")
    
    return page

# Function to add background image with low transparency, ensuring the content is still interactable
def add_background(image_path, transparency=0.2):
    img_base64 = image_to_base64(image_path)
    st.markdown(
        f"""
        <style>
        .stApp {{
            position: relative;
            background-image: url("data:image/jpeg;base64,{img_base64}"); 
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            min-height: 100vh;
        }}
        .background-overlay {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, {transparency});
            z-index: -1;
        }}
        
        /* Change the main content text color to white */
        .stApp .block-container {{
            color: white !important;
        }}
        </style>
        """, 
        unsafe_allow_html=True
    )
    st.markdown('<div class="background-overlay"></div>', unsafe_allow_html=True)

# Dummy animation example
def show_loading_animation():
    with st.spinner("Loading... 🌀"):
        time.sleep(2)  # Simulate loading time

# Engaging Text Effects
def show_text_effects():
    st.markdown(
        """
        <style>
        .fade-in-text {
            font-size: 24px;
            font-weight: bold;
            animation: fadeIn 3s ease-in-out;
        }

        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        </style>
        <div class="fade-in-text">✨ Welcome to the Rice Prediction App! 🌾</div>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        .hover-btn {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            cursor: pointer;
            font-size: 18px;
            transition: background-color 0.3s ease;
        }

        .hover-btn:hover {
            background-color: #45a049;
        }
        </style>
        <div class="hover-btn">🔮 Click to Predict the Rice Class</div>
        """, unsafe_allow_html=True
    )

# Show the sidebar with enhanced content
page = enhance_sidebar()

# Show the respective page based on the selection
if page == "Predict":
    # Add a background image for the Predict page with low transparency
    add_background("pred_bg.jpg", transparency=0.3)  # Background image for the Predict page
    
    # Show dummy loading animation
    show_loading_animation()

    # Add floating rice grain emojis for a dynamic feel
    st.markdown(
        """
        <style>
        .floating-rice {
            animation: float 2s ease-in-out infinite;
            font-size: 24px;
        }

        @keyframes float {
            0% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0); }
        }
        </style>
        <div class="floating-rice">🍚 Rice Grains Floating...</div>
        """, unsafe_allow_html=True
    )

    # Display engaging text for the user
    show_text_effects()

    # Call the prediction page
    show_predict_page()

elif page == "Explore":
    # Add a background image for the Explore page with low transparency
    add_background("explore_bg.jpg", transparency=0.3)  # Background image for the Explore page
    
    # Display some cool fading text effect
    st.markdown(
        """
        <style>
        .fade-in-text {
            font-size: 20px;
            font-weight: bold;
            animation: fadeIn 3s ease-in-out;
        }

        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        </style>
        <div class="fade-in-text">💡 Explore Rice Varieties by Clicking on the Options Above! 💡</div>
        """, unsafe_allow_html=True
    )

    # Add more dummy elements (rice grain animation)
    st.markdown(
        """
        <style>
        .floating-rice {
            animation: float 3s ease-in-out infinite;
            font-size: 20px;
        }

        @keyframes float {
            0% { transform: translateY(0); }
            50% { transform: translateY(-15px); }
            100% { transform: translateY(0); }
        }
        </style>
        <div class="floating-rice">🍚 Rice Grains Floating...</div>
        """, unsafe_allow_html=True
    )
    
    # Call the explore page
    show_explore_page()

# **Global CSS for Sidebar Text Color (black)** - Applied globally
st.markdown(
    """
    <style>
    /* Change text color of the sidebar */
    .sidebar .sidebar-content, .stSidebar .sidebar-content {
        color: black !important;
    }
    </style>
    """, unsafe_allow_html=True
)





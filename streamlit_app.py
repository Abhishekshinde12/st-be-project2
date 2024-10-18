import streamlit as st
from PIL import Image
import base64

# Set page config
st.set_page_config(page_title="MindLyst.ai - Next-Gen AI Mental Health Solutions", layout="wide")

# Custom CSS
def local_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Header
st.markdown("""
    <header>
        <nav>
            <div class="logo">MindLyst.ai</div>
        </nav>
    </header>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <section class="hero">
        <div class="hero-content">
            <h1>Redefining Mental Health with AI</h1>
            <p>Experience the future of personalized mental wellness</p>
        </div>
    </section>
""", unsafe_allow_html=True)

# Features Section
st.markdown("<h2>Cutting-Edge Features</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="feature-card">
            <h3>AI-Powered Analysis</h3>
            <p>Advanced algorithms for precise mental health assessment</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="feature-card">
            <h3>Real-Time Insights</h3>
            <p>Instant feedback for patients and therapists</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <h3>Multimodal Integration</h3>
            <p>Comprehensive analysis of facial, vocal, and textual data</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="feature-card">
            <h3>Secure Therapist Portal</h3>
            <p>Advanced tools for patient monitoring and intervention</p>
        </div>
    """, unsafe_allow_html=True)

# How It Works Section
st.markdown("<h2>The MindLyst Process</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="step">
            <div class="step-number">01</div>
            <h3>Data Collection</h3>
            <p>Secure and non-invasive gathering of multimodal data</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="step">
            <div class="step-number">02</div>
            <h3>AI Processing</h3>
            <p>Advanced analysis using state-of-the-art AI models</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="step">
            <div class="step-number">03</div>
            <h3>Personalized Insights</h3>
            <p>Actionable recommendations for improved mental wellness</p>
        </div>
    """, unsafe_allow_html=True)

# Contact Section
st.markdown("""
    <section class="cta">
        <h2>Ready to Transform Mental Health Care?</h2>
        <p>Join the AI-driven revolution in mental wellness</p>
    </section>
""", unsafe_allow_html=True)

if st.button("Contact Us"):
    st.write("Thank you for your interest! We'll be in touch soon.")

# Footer

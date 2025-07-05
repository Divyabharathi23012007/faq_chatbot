import streamlit as st
from faq_chatbot import get_faq_response

st.set_page_config(page_title="AI FAQ Assistant", page_icon="🤖", layout="wide")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        * {
            font-family: 'Inter', sans-serif;
        }
        
        .main {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .stApp {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        .container {
            max-width: 700px;
            margin: 0 auto;
            padding: 25px 20px;
        }
        
        .title {
            text-align: center;
            color: white;
            font-size: 1.8rem;
            font-weight: 600;
            margin-bottom: 35px;
            text-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }
        
        .boxes-container {
            display: flex;
            gap: 20px;
            margin-bottom: 25px;
        }
        
        .box {
            flex: 1;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.2);
            border: 1px solid rgba(255, 255, 255, 0.3);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            min-height: 150px;
        }
        
        .box:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.3);
        }
        
        .box-header {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 2px solid #f0f0f0;
        }
        
        .box-icon {
            font-size: 1.3rem;
            margin-right: 8px;
        }
        
        .box-title {
            font-size: 1rem;
            font-weight: 600;
            color: #333;
            margin: 0;
        }
        
        .input-box .box-icon {
            color: #4CAF50;
        }
        
        .response-box .box-icon {
            color: #2196F3;
        }
        
        .stTextInput>div>div>input {
            font-size: 13px;
            padding: 10px 14px;
            border-radius: 6px;
            border: 2px solid #e0e0e0;
            background: white;
            color: #333;
            transition: all 0.3s ease;
            width: 100%;
        }
        
        .stTextInput>div>div>input:focus {
            border-color: #4CAF50;
            box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.1);
            outline: none;
        }
        
        .stTextInput>div>div>input::placeholder {
            color: #999;
        }
        
        .response-content {
            min-height: 70px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #666;
            font-style: italic;
            font-size: 13px;
        }
        
        .ai-response {
            background: #f8f9fa;
            border-radius: 6px;
            padding: 12px;
            border-left: 3px solid #2196F3;
            color: #333;
            line-height: 1.4;
            font-size: 13px;
        }
        
        .footer {
            text-align: center;
            color: rgba(255, 255, 255, 0.8);
            font-size: 0.75rem;
            margin-top: 20px;
        }
        
        /* Hide default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Responsive design */
        @media (max-width: 768px) {
            .boxes-container {
                flex-direction: column;
                gap: 12px;
            }
            
            .title {
                font-size: 1.6rem;
            }
            
            .container {
                padding: 12px 10px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Main container
with st.container():
    st.markdown('<div class="container">', unsafe_allow_html=True)
    
    # Title
    st.markdown('<h1 class="title">🤖 AI FAQ Assistant</h1>', unsafe_allow_html=True)
    
    # Two boxes container
    st.markdown('<div class="boxes-container">', unsafe_allow_html=True)
    
    # Input box (left)
    st.markdown("""
        <div class="box input-box">
            <div class="box-header">
                <span class="box-icon">💬</span>
                <h3 class="box-title">Your Question</h3>
            </div>
    """, unsafe_allow_html=True)
    
    user_input = st.text_input("Question", placeholder="Type your question here...", key="user_input", label_visibility="collapsed")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Response box (right)
    st.markdown("""
        <div class="box response-box">
            <div class="box-header">
                <span class="box-icon">🤖</span>
                <h3 class="box-title">AI Response</h3>
            </div>
            <div class="response-content">
    """, unsafe_allow_html=True)
    
    if user_input:
        with st.spinner("🤖 AI is thinking..."):
            response = get_faq_response(user_input)
        
        st.markdown(f'<div class="ai-response">{response}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="response-content">Your AI response will appear here...</div>', unsafe_allow_html=True)
    
    st.markdown('</div></div>', unsafe_allow_html=True)
    
    # Close boxes container
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
        <div class="footer">
            <p>Powered by AI • Built with Streamlit</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

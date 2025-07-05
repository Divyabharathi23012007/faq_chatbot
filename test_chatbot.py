#!/usr/bin/env python3
"""
Test script to verify the FAQ chatbot is working correctly
"""

from faq_chatbot import get_faq_response

def test_chatbot():
    """Test the chatbot with various questions"""
    print("🤖 Testing FAQ Chatbot...\n")
    
    test_questions = [
        "What is your return policy?",
        "How do I track my order?",
        "Do you ship internationally?",
        "How can I contact support?",
        "Can I cancel my order?",
        "What is the weather like today?"  # This should return the default response
    ]
    
    for question in test_questions:
        print(f"❓ Question: {question}")
        response = get_faq_response(question)
        print(f"🤖 Answer: {response}")
        print("-" * 50)
    
    print("\n✅ Chatbot test completed!")

if __name__ == "__main__":
    test_chatbot() 
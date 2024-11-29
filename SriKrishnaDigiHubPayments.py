import streamlit as st

# Streamlit page configuration
st.set_page_config(page_title="Sri Krishna Digital Hub Payments", page_icon=":money_with_wings:", layout="centered")

# Page Title
st.title("Sri Krishna Digital Hub Payments")
st.write("""
    Welcome to **Sri Krishna Digital Hub** – a trusted platform for digital payments and services.
    We make your digital transactions seamless and secure.
    
    Please click the button below to proceed with your payment. You will be redirected to your UPI app for a secure transaction.
""")

# Predefined UPI Payment URL
upi_url = "upi://pay?pa=8367772921@postbank&pn=DAMA%20HARI&cu=INR&mode=02&orgId=159768&sign=MEYCIQD+XkSoNXcZ87f48VnmF4Tbx4zVn3xuQ0kqBheTiQ8OOQIhAOgV2H8VhcLrSCetd92zEnLd/mYVQm4CyAkxbmsNOXKS"

# Instructions section with a subtle background color
st.markdown("""
    <div style="background-color:#f1f1f1; padding:15px; border-radius:8px;">
        <h3 style="color:#333333;">How to Make a Payment:</h3>
        <ul style="font-size:16px; color:#555555;">
            <li>Click the button below to open the UPI payment interface.</li>
            <li>Confirm the details in your UPI app and complete the transaction securely.</li>
            <li>Once payment is successful, you will receive a confirmation notification.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Spacer for better readability
st.markdown("<br><br>", unsafe_allow_html=True)

# UPI Payment Button
st.markdown(f'''
    <a href="{upi_url}" target="_blank">
        <button style="
            background-color: #008CBA; 
            color: white; 
            font-size: 18px; 
            padding: 15px 30px; 
            border-radius: 10px; 
            border: none; 
            cursor: pointer; 
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: background-color 0.3s ease;
        " 
        onmouseover="this.style.backgroundColor='#005f73';" 
        onmouseout="this.style.backgroundColor='#008CBA';">
            Pay Now
        </button>
    </a>
''', unsafe_allow_html=True)

# Footer with contact information and a professional touch
st.markdown("""
    <div style="background-color:#333333; color:white; padding:20px; text-align:center; border-radius:8px; margin-top:30px;">
        <p style="font-size:14px;">For support, please contact us at <a href="mailto:info@skdhub.com" style="color:white; text-decoration:underline;">info@skdhub.com</a></p>
        <p style="font-size:12px;">© 2024 Sri Krishna Digital Hub. All rights reserved.</p>
    </div>
""", unsafe_allow_html=True)

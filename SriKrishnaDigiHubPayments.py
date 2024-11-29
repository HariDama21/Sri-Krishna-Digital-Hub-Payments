import streamlit as st

# Streamlit page configuration
st.set_page_config(page_title="Sri Krishna Digital Hub Payments", page_icon=":money_with_wings:", layout="wide")

# Page title
st.title("Welcome to Sri Krishna Digital Hub Payments")
st.write("Click the button below to proceed with the payment.")


# HTML button to trigger the UPI payment link
st.markdown(f'''
    <a href="upi://pay?pa=8367772921@postbank&pn=DAMA%20HARI&cu=INR&mode=02&orgId=159768&sign=MEYCIQD+XkSoNXcZ87f48VnmF4Tbx4zVn3xuQ0kqBheTiQ8OOQIhAOgV2H8VhcLrSCetd92zEnLd/mYVQm4CyAkxbmsNOXKS" target="_blank">
        <button style="background-color: #008CBA; color: white; font-size: 16px; padding: 10px 20px; border-radius: 5px; border: none; cursor: pointer;">
            Click to Pay
        </button>
    </a>
''', unsafe_allow_html=True)

# Footer information
st.markdown("""
    ---
    **Sri Krishna Digital Hub** – Your trusted platform for digital payments and services.
    
    For support, contact us at: [info@skdhub.com](mailto:info@skdhub.com).
""")

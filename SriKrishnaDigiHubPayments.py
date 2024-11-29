import streamlit as st

# Function to generate UPI URL dynamically based on the amount
def generate_upi_url(amount):
    upi_id = "someone@upi"  # Replace with actual UPI ID
    transaction_note = "Payment for services at Sri Krishna Digital Hub"
    upi_url = f"upi://pay?pa={upi_id}&am={amount}&cu=INR&tn={transaction_note}"
    return upi_url

# Streamlit page configuration
st.set_page_config(page_title="Sri Krishna Digital Hub Payments", page_icon=":money_with_wings:", layout="wide")

# Page title
st.title("Welcome to Sri Krishna Digital Hub Payments")
st.write("Please enter the amount you wish to pay and click the button to generate a UPI payment link.")

# User input for amount
amount = st.number_input("Enter Amount (INR)", min_value=1, format="%.2f", step=0.01)

# Button to generate UPI payment link
if st.button("Generate Payment Link"):
    if amount > 0:
        upi_url = generate_upi_url(amount)  # Generate the UPI URL based on the amount
        # Display the dynamic clickable UPI payment button
        st.markdown(f'<a href="{upi_url}" target="_blank"><button style="background-color: #008CBA; color: white; font-size: 16px; padding: 10px 20px; border-radius: 5px; border: none; cursor: pointer;">Click to Pay ₹{amount}</button></a>', unsafe_allow_html=True)
        st.success(f"Payment link for ₹{amount} has been generated. Click the button to proceed.")
    else:
        st.error("Please enter a valid amount greater than zero.")

# Footer information
st.markdown("""
    ---
    **Sri Krishna Digital Hub** – Your trusted platform for digital payments and services.
    
    For support, contact us at: [info@skdhub.com](mailto:info@skdhub.com).
""")

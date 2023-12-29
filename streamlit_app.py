import streamlit as st

def main():
    st.title("Name Submission App")

    # Text input for the user's name
    name = st.text_input("Enter your name:")

    # Submit button
    if st.button("Submit"):
        if name:
            st.success(f"Hello, {name}! Submission successful.")
        else:
            st.warning("Please enter your name before submitting.")

if __name__ == "__main__":
    main()
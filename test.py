import streamlit as st

def main():
    st.title("Text Display App")

    # Create a placeholder for the text input
    input_placeholder = st.empty()

    # Get user input from a text field in the main section
    user_input = input_placeholder.text_input("Enter text:")

    # Check the length of user_input
    if len(user_input) > 3:
        # If length is greater than 3, clear the text input
        input_placeholder.empty()
        st.sidebar.write("You entered:", user_input)
    else:
        # Display the input in the sidebar
        st.sidebar.write("You entered:", user_input)

if __name__ == "__main__":
    main()
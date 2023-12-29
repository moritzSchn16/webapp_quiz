import streamlit as st
from streamlit_gsheets import GSheetsConnection
import gspread

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



    # Open the Google Sheet by title or URL (no authentication needed for public sheets)
    sheet = gspread.open("https://docs.google.com/spreadsheets/d/1Qh5L61LQPMMuhn6YsaAbVBZnwlYl8PJxKzSxTnjXwiA/edit?usp=sharing")

    # Select a specific worksheet within the spreadsheet
    worksheet = sheet.get_worksheet(0)  # Index 0 corresponds to the first worksheet

    # Read data from the worksheet
    all_values = worksheet.get_all_values()

    # Display the read data
    for row in all_values:
        print(row)

if __name__ == "__main__":
    main()
import streamlit as st

# Funktion zum Verarbeiten von Button-Klicks und Aktualisieren der Sequenzliste
def handle_button_press(button):
    st.session_state.button_sequence.append(button)
    st.session_state.total_button_clicks += 1
    save_sequence_to_file(st.session_state.button_sequence, st.session_state.user_name)
    x = 0
    for i in st.session_state.button_sequence:
        st.sidebar.write(f"Frage:{x}, Antwort: {i}")
        x += 1

# Funktion zum Speichern der aktuellen Sequenz in einer Textdatei
def save_sequence_to_file(sequence, user_name):
    filename = f"{user_name}_button_sequence.txt"
    with open(filename, "w") as file:
        file.write("Name: {}\n".format(user_name))
        file.write("Button-Sequenz: {}\n".format(",".join(sequence)))


# Initialisiere leere Listen, um die Button-Klicks und Zähler zu speichern
if 'button_sequence' not in st.session_state:
    st.session_state.button_sequence = []
if 'total_button_clicks' not in st.session_state:
    st.session_state.total_button_clicks = 0

# Vordefinierte Sequenz zum Vergleich
predefined_sequence = ["A", "A", "B", "C", "A"]

# Streamlit App-Layout
def main():

    st.title("Das Quiz 2023 - APP")

    # Zeige die Gesamtanzahl der Button-Klicks an
    st.title(f"Frage: {st.session_state.total_button_clicks} / 70")

    # Create a placeholder for the text input
    input_placeholder = st.empty()

    # Get user input from a text field in the main section
    user_name = input_placeholder.text_input("Name:")

    # Check the length of user_input
    if len(user_name) > 3:
        # If length is greater than 3, clear the text input
        input_placeholder.empty()
        st.sidebar.write("You entered:", user_name)
    else:
        # Display the input in the sidebar
        st.sidebar.write("You entered:", user_name)

    if len(user_name) > 3:
        # Überprüfe, ob der Benutzername bereits in session_state gespeichert ist
        if 'user_name' not in st.session_state:
            st.session_state.user_name = user_name

        # Erstelle die Buttons A, B, C und D im 2x2-Format
        col1, col2 = st.columns(2)
        with col1:
            button_a = st.button("Antwort: A", key="button_a", on_click=handle_button_press, args=("A",), help="button")
            button_b = st.button("Antwort: B", key="button_b", on_click=handle_button_press, args=("B",), help="button")
        with col2:
            button_c = st.button("Antwort: C", key="button_c", on_click=handle_button_press, args=("C",), help="button")
            button_d = st.button("Antwort: D", key="button_d", on_click=handle_button_press, args=("D",), help="button")


        # Zeige die aktuelle Button-Sequenz an
        if len(st.session_state.button_sequence) > 0:
            st.write("Letzte Antwort: ", ",".join(st.session_state.button_sequence[-1]))
        else:
            st.write("Bitte Antwort geben!")

        col1, col2 = st.columns(2)
        with col1:
            #Button zum Löschen von dummen Antworten
            if st.button("Letzte Antwort Löschen"):
                if len(st.session_state.button_sequence) > 0:
                    st.session_state.button_sequence.pop()
                    st.session_state.total_button_clicks += -1
                x = 0
                for i in st.session_state.button_sequence:
                    st.sidebar.write(f"Frage:{x}, Antwort: {i}")
                    x += 1
        with col2:
            # Button zum Drucken der Sequenz
            if st.button("Antworten in Sidebar anzeigen"):
                st.write("Antworten in Sidebar")
                #st.write("Sequenz: ", ",".join(st.session_state.button_sequence))
                x = 0
                for i in st.session_state.button_sequence:
                    st.sidebar.write(f"Frage:{x}, Antwort: {i}")
                    x += 1

        st.write('Am Ende des Quizzes')
        # Überprüfe, ob die Sequenzlänge 5 ist
        if len(st.session_state.button_sequence) == 5:
            # Button zum Überprüfen, wie viele Elemente mit der vordefinierten Sequenz übereinstimmen
            if st.button("Sequenz überprüfen"):
                match_count = sum([1 for a, b in zip(st.session_state.button_sequence, predefined_sequence) if a == b])
                st.write(f"Übereinstimmende Elemente: {match_count}")
if __name__ == "__main__":
    main()

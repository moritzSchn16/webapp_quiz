import streamlit as st

# Initialisiere leere Listen, um die Button-Klicks und Zähler zu speichern
if 'button_sequence' not in st.session_state:
    st.session_state.button_sequence = []
if 'total_button_clicks' not in st.session_state:
    st.session_state.total_button_clicks = 0

# Vordefinierte Sequenz zum Vergleich
predefined_sequence = ["A", "A", "B", "C", "A"]

# Streamlit App-Layout
def main():
    st.title("Das Quiz 2023 - App")

    # Zeige die Gesamtanzahl der Button-Klicks an
    st.write(f"Frage: {st.session_state.total_button_clicks}")

    # Überprüfe, ob der Benutzername bereits in session_state gespeichert ist
    if 'user_name' not in st.session_state:
        st.session_state.user_name = st.text_input("Geben Sie Ihren Namen ein:")

    # Zeige den Benutzernamen im Hauptbereich an
    st.write(f"Name: {st.session_state.user_name}")

    # Zeige den Benutzernamen in der Seitenleiste an
    st.sidebar.write(f"Name: {st.session_state.user_name}")

    # Erstelle die Buttons A, B, C und D im 2x2-Format
    col1, col2 = st.columns(2)
    with col1:
        button_a = st.button("A", key="button_a", on_click=handle_button_press, args=("A",), help="button")
        button_b = st.button("B", key="button_b", on_click=handle_button_press, args=("B",), help="button")
    with col2:
        button_c = st.button("C", key="button_c", on_click=handle_button_press, args=("C",), help="button")
        button_d = st.button("D", key="button_d", on_click=handle_button_press, args=("D",), help="button")



    # Zeige die aktuelle Button-Sequenz an
    st.write("Button-Sequenz: ", ",".join(st.session_state.button_sequence))

    # Überprüfe, ob die Sequenzlänge 5 ist
    if len(st.session_state.button_sequence) == 5:
        # Button zum Überprüfen, wie viele Elemente mit der vordefinierten Sequenz übereinstimmen
        if st.button("Sequenz überprüfen"):
            match_count = sum([1 for a, b in zip(st.session_state.button_sequence, predefined_sequence) if a == b])
            st.write(f"Übereinstimmende Elemente: {match_count}")

    # Button zum Drucken der Sequenz
    if st.button("Sequenz drucken"):
        st.write("Sequenz: ", ",".join(st.session_state.button_sequence))

# Funktion zum Verarbeiten von Button-Klicks und Aktualisieren der Sequenzliste
def handle_button_press(button):
    st.session_state.button_sequence.append(button)
    st.session_state.total_button_clicks += 1
    save_sequence_to_file(st.session_state.button_sequence, st.session_state.user_name)

# Funktion zum Speichern der aktuellen Sequenz in einer Textdatei
def save_sequence_to_file(sequence, user_name):
    filename = f"{user_name}_button_sequence.txt"
    with open(filename, "w") as file:
        file.write("Name: {}\n".format(user_name))
        file.write("Button-Sequenz: {}\n".format(",".join(sequence)))

if __name__ == "__main__":
    main()

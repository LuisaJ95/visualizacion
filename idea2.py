import streamlit as st
from streamlit import session_state


class Dashboard:
    def __init__(self):
        self.reset()

    def reset(self):
        self.form1_data = {"nombre": "", "edad": 0}
        self.form2_data = {"email": "", "telefono": ""}
        self.form3_data = {"pregunta": ""}

    def show_menu(self):
        st.sidebar.title("Secciones")
        options = ["Inicio", "Formulario 1", "Formulario 2", "Formulario 3"]
        if "choice" not in session_state:
            session_state.choice = "Inicio"
        choice = st.sidebar.selectbox(
            "Selecciona una sección", options, options.index(session_state.choice)
        )
        session_state.choice = choice

        if choice == "Inicio":
            self.show_inicio()
        elif choice == "Formulario 1":
            self.show_formulario_1()
        elif choice == "Formulario 2":
            self.show_formulario_2()
        elif choice == "Formulario 3":
            self.show_formulario_3()

        if st.sidebar.button("Restablecer"):
            self.reset()
            session_state.choice = "Inicio"

    def show_inicio(self):
        st.title("Página de inicio")
        st.write("¡Bienvenido a la página de inicio!")

    def show_formulario_1(self):
        st.title("Formulario 1")
        nombre = st.text_input("Nombre", self.form1_data["nombre"])
        edad = st.number_input(
            "Edad", min_value=0, max_value=100, value=self.form1_data["edad"]
        )
        if st.button("Enviar"):
            self.form1_data = {"nombre": nombre, "edad": edad}
            st.success("Formulario 1 enviado")

    def show_formulario_2(self):
        st.title("Formulario 2")
        email = st.text_input("Email", self.form2_data["email"])
        telefono = st.text_input("Teléfono", self.form2_data["telefono"])
        if st.button("Enviar"):
            self.form2_data = {"email": email, "telefono": telefono}
            st.success("Formulario 2 enviado")

    def show_formulario_3(self):
        st.title("Formulario 3")
        pregunta = st.text_area("Pregunta", self.form3_data["pregunta"])
        if st.button("Enviar"):
            self.form3_data = {"pregunta": pregunta}
            st.success("Formulario 3 enviado")


dashboard = Dashboard()

if __name__ == "__main__":
    dashboard.show_menu()


import streamlit as st

class StreamlitApp:
    def __init__(self):
        self.reset_page()
    
    def reset_page(self):
        self.show_form1 = False
        self.show_form2 = False
        self.numbers_form1 = [0, 0, 0, 0]
        self.numbers_form2 = [0, 0, 0, 0]
    
    def run(self):
        st.title("Página Principal")
        
        # Barra lateral
        st.sidebar.title("Panel de Opciones")
        
        # Checkbox para mostrar/ocultar formulario 1
        self.show_form1 = st.sidebar.checkbox("Mostrar Formulario 1", value=self.show_form1)
        
        # Checkbox para mostrar/ocultar formulario 2
        self.show_form2 = st.sidebar.checkbox("Mostrar Formulario 2", value=self.show_form2)
        
        # Botón para restablecer la página
        if st.sidebar.button("Restablecer Página"):
            self.reset_page()
        
        if self.show_form1:
            self.show_form1_inputs()
        
        if self.show_form2:
            self.show_form2_inputs()
        
        if st.sidebar.button("Generar Resultados"):
            suma_result = [
                self.numbers_form1[i] + self.numbers_form2[i] for i in range(4)
            ]
            multiplicacion_result = [
                self.numbers_form1[i] * self.numbers_form2[i] for i in range(4)
            ]
            
            st.title("Resultados")
            st.write("Resultado de la suma:", suma_result)
            st.write("Resultado de la multiplicación:", multiplicacion_result)
    
    def show_form1_inputs(self):
        st.title("Formulario 1")
        for i in range(4):
            self.numbers_form1[i] = st.number_input(f"Número {i+1}", value=self.numbers_form1[i], key=f"form1-{i}")
    
    def show_form2_inputs(self):
        st.title("Formulario 2")
        for i in range(4):
            self.numbers_form2[i] = st.number_input(f"Número {i+1}", value=self.numbers_form2[i], key=f"form2-{i}")

# Crear una instancia de la clase StreamlitApp
app = StreamlitApp()

# Ejecutar la aplicación
app.run()

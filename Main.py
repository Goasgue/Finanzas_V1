import streamlit as st
import sys
from streamlit import cli as stcli
from Funciones import *


def main():
    st.title("Finanzas Personales")
    menu = ["Control Archivo", "Ingresos", "Egresos", "Analisis"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Control Archivo":
        st.subheader("Control del Archivo")
        file_name = st.file_uploader("Cargar planilla")
        if file_name:
            show_excel_info(file_name=file_name)

    elif choice == "Ingresos":
        st.subheader("Registrar Ingresos")
        filename = "data/finanzas.xlsx"
        ingresos(filename)

    elif choice == "Egresos":
        st.subheader("Registrar Gastos")
        filename = "data/finanzas.xlsx"
        gastos(filename)
   
    elif choice == "Analisis":
        st.subheader("Analisis de Datos")
        file_name = "data/finanzas.xlsx"
        analisis(file_name=file_name)

    else:
        st.subheader("En progreso")
        dashboard()


if __name__ == "__main__":
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())

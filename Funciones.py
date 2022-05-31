import streamlit as st
import pandas as pd
import plotly.express as px


def show_excel_info(file_name):
    xl_file = pd.ExcelFile(file_name)
    sheets = xl_file.sheet_names

    sheet_name = st.selectbox("Select a sheet", sheets)
    df = pd.read_excel(file_name, engine="openpyxl", sheet_name=sheet_name)

    # cols = tuple(df.columns)
    select_x = st.selectbox("Select x axis", df.columns)
    select_y = st.selectbox("Select y axis", df.columns)

    st.dataframe(df.describe())
    st.dataframe(df.isnull().sum())

    fig = px.bar(
        df,
        x=select_x,
        y=select_y,
    )

    st.plotly_chart(fig)

def ingresos(file_name):
    xl_file = pd.ExcelFile(file_name)
    sheets = xl_file.sheet_names

    sheet_selected = "Ingresos"
    date = st.date_input("Fecha")
    category = st.selectbox(
        "Categoria",
        [
            "Sueldo",
            "Acciones",
            "Inversiones",
            "Otros"
            ,
        ],
    )
    amount = st.number_input("Ingresar Monto", min_value=1, max_value=10000000)

    new_data = {
        "Fecha": date,
        "Categoria": category,
        "Monto": amount,
    }

    btn = st.button("Añadir")
    df = pd.read_excel(file_name, engine="openpyxl", sheet_name=sheet_selected)
    df = df.append(new_data, ignore_index=True)
    df_group = df.groupby(["Categoria"], as_index=False).sum()

    if btn:
        writer = pd.ExcelWriter(
            file_name,
            mode="a",
            if_sheet_exists="overlay",
            engine="openpyxl",
        )

        df.to_excel(writer, index=False, sheet_name=sheet_selected)
        writer.close()

        fig = px.bar(
            df_group,
            x="Categoria",
            y="Monto",
            title="<b>Analisis de Gastos</b>",
        )

        st.plotly_chart(fig)


def gastos(file_name):
    xl_file = pd.ExcelFile(file_name)
    sheets = xl_file.sheet_names

    sheet_selected = "Egresos"
    date = st.date_input("Fecha")
    category = st.selectbox(
        "Categoria",
        [
            "Accesorios",
            "Entretenimiento",
            "Restaurante",
            "Servicios",
            "Supermercado",
            "Suscripciones",
            "Otros"
            ,
        ],
    )
    amount = st.number_input("Ingresar Monto", min_value=1, max_value=10000000)

    new_data = {
        "Fecha": date,
        "Categoria": category,
        "Monto": amount,
    }

    btn = st.button("Añadir")
    df = pd.read_excel(file_name, engine="openpyxl", sheet_name=sheet_selected)
    df = df.append(new_data, ignore_index=True)
    df_group = df.groupby(["Categoria"], as_index=False).sum()

    if btn:
        writer = pd.ExcelWriter(
            file_name,
            mode="a",
            if_sheet_exists="overlay",
            engine="openpyxl",
        )

        df.to_excel(writer, index=False, sheet_name=sheet_selected)
        writer.close()

        fig = px.bar(
            df_group,
            x="Categoria",
            y="Monto",
            title="<b>Analisis de Gastos</b>",
        )

        st.plotly_chart(fig)


def analisis(file_name):
    xl_file = pd.ExcelFile(file_name)
    sheets = xl_file.sheet_names

    sheet_name = st.selectbox("Seleccionar", sheets)
    
    df = pd.read_excel(file_name, sheet_name=sheet_name, usecols="A:C", header=0)
    df_presupuesto = pd.read_excel(file_name, sheet_name=sheet_name, usecols="A:C", header=0)
    df_presupuesto.dropna(inplace=True)

    item = df["Categoria"].unique().tolist()
    monto = df["Monto"].unique().tolist()

    pie_chart = px.pie(
        df_presupuesto,
        title="Analisis por Item",
        values="Monto",
        names="Categoria",
    )

    st.plotly_chart(pie_chart)
    bar_chart = px.bar(
        df_presupuesto,
        x="Fecha",
        y="Monto",
        color="Categoria",
        template="plotly_white",
    )
    st.plotly_chart(bar_chart)


    rango_gastos = st.slider("Monto:", min_value=min(monto), max_value=max(monto), value=(min(monto), max(monto)))
    st.write(rango_gastos)

    item_selection = st.multiselect("Categoria:", item, default=item)
    mask = (df["Monto"].between(rango_gastos[0], rango_gastos[1])) & (df["Categoria"].isin(item_selection))
    number_of_result = df[mask].shape[0]
    st.markdown(f"*Numero de entradas: {number_of_result}*")

    df_grouped = df[mask].groupby(by=["Categoria"]).count()["Monto"]
    st.write(df_grouped)

    df_grouped2 = df[mask].groupby(by=["Categoria"]).sum()["Monto"]
    st.write(df_grouped2)
    st.dataframe(df[mask])


def dashboard():
    pass


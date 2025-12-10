import streamlit as st
import pandas as pd

def proceso_csv_piva():
    st.subheader("Importación a Portal IVA")
    uploaded_file = st.file_uploader("Selecciona un archivo para importar a Portal IVA", type=["csv"], key="csv_piva")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, sep=';')
        st.write("Vista previa del archivo CSV cargado:")
        st.dataframe(df.head())
        # Aquí puedes agregar la lógica específica para el proceso de Portal IVA
        # Por ejemplo, transformación, validación, exportación, etc.
        output = st.download_button(
            label="Descargar CSV para Portal IVA",
            data=df.to_csv(index=False, sep=';').encode('utf-8'),
            file_name="csv_portal_iva.csv",
            mime="text/csv"
        )

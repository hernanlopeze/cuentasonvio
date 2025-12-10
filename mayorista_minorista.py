import pandas as pd
import os

def proceso_mayorista_minorista(df):
    # Leer comprobantes B
    path_b = os.path.join("assets", "comprobantes_b.csv")
    comprobantes_b = pd.read_csv(path_b, sep=",", encoding="utf-8")
    codigos_b = set(comprobantes_b[comprobantes_b.columns[0]].astype(str).str.strip())

    # Agregar columnas al final
    df["Importe Reg Esp 1 (AFIP - Mis Comprobantes)"] = ""
    df["Importe Reg Esp 2 (AFIP - Mis Comprobantes)"] = ""
    df["Importe Reg Esp 3 (AFIP - Mis Comprobantes)"] = ""
    df["Importe Reg Esp 4 (AFIP - Mis Comprobantes)"] = ""
    # Asignar VTAMIN si Tipo de Comprobante (por código) está en comprobantes_b.csv, si no VTAMAY
    if "Tipo de Comprobante" in df.columns:
        df["Código de Concepto/Artículo"] = df["Tipo de Comprobante"].apply(lambda x: "VTAMIN" if str(x).strip() in codigos_b else "VTAMAY")
    else:
        df["Código de Concepto/Artículo"] = "VTAMAY"
    return df

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_parquet("/home/sebastian/estudio/datasets/mercado_central_flat.parquet")

st.header('Fruits and vegetables price evolution')

productos_dict= pd.read_csv("/home/sebastian/estudio/datasets/productos.csv")
prod_options = productos_dict.columns[4:10]

user_prod = st.sidebar.selectbox('Choose an product', prod_options)
col1, col2, col3 = st.columns(3)

with col1:
    if user_prod != '':
        st.write(f"Product: {user_prod}")
    else:
        st.write('👈 Please choose a product!')

    h_dict = productos_dict[user_prod]
    data = df[
        (df.ESP == h_dict[0])&
        (df.VAR == h_dict[1])&
        (df.GRADO == h_dict[2])
        &(df.PROC == h_dict[3])
        ].reset_index(drop=True)
    print(len(data))
    data.sort_values(by=["fecha"], inplace=True)


fig, ax = plt.subplots()
ax.plot(data.fecha, data["MOPK"])
ax.set_xlabel("Date")  
ax.set_ylabel("Price Argentinian peso / Kg ")   
ax.set_title(f"{user_prod} price evolution")  
st.pyplot(fig)
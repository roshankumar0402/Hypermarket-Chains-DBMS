import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_admin,view_store, view_distributor,view_sales, view_stock,view_stord


def read_admin():
    result = view_admin()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Admin ID', 'PASSWORD'])
    with st.expander("View all Admins"):
        st.dataframe(df)

def read_distributor():
    result = view_distributor()
    # st.write(result)
    df = pd.DataFrame(result, columns=['DID','DNAME','DPASS','DTYPE','DLOC'])
    with st.expander("View all Distributors"):
        st.dataframe(df)

def read_sales():
    result = view_sales()
    # st.write(result)
    df = pd.DataFrame(result, columns=['SALESID','SDATE','SCOST','SID'])
    with st.expander("View all Sales"):
        st.dataframe(df)

def read_stock():
    result = view_stock()
    # st.write(result)
    df = pd.DataFrame(result, columns=['CRY','SCRY','Quant','SID'])
    with st.expander("View all Stock"):
        st.dataframe(df)

def read_store():
    result = view_store()
    # st.write(result)
    df = pd.DataFrame(result, columns=['SID', 'SPASS', 'SBRANCHNAME', 'SCITY', 'SREGION', 'SSTATE', 'SPCODE'])
    with st.expander("View all Store"):
        st.dataframe(df)        

def read_stord():
    result = view_stord()
    # st.write(result)
    df = pd.DataFrame(result, columns=['ORDID', 'SID', 'DID', 'ORDDATE', 'PMYSTAT', 'SHPMODE', 'SHPSTAT'])
    with st.expander("View all Store Orders"):
        st.dataframe(df)        
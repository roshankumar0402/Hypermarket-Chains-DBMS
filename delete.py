import pandas as pd
import streamlit as st
from database import view_admin, view_only_admin_names, delete_admin_data, view_distributor, view_only_distributor_did, delete_dist_data,view_sales, delete_sales_data,view_only_sales_salesid,view_stock,view_only_scry,delete_stock_data,view_store,view_only_store_sid,view_store,delete_store_data,view_stord,view_only_ordid,delete_stord_data
def delete_admin():
    result = view_admin()
    df = pd.DataFrame(result, columns=['Admin ID', 'Password'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_admins = [i[0] for i in view_only_admin_names()]
    selected_admin = st.selectbox("Admin to Delete", list_of_admins)
    st.warning("Do you want to delete ::{}".format(selected_admin))
    if st.button("Delete Admin"):
        delete_admin_data(selected_admin)
        st.success("Admin has been deleted successfully")
    new_result = view_admin()
    df2 = pd.DataFrame(new_result, columns=['Admin ID', 'Password'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_dist():
    result = view_distributor()
    df = pd.DataFrame(result, columns=['DID','DNAME','DPASS','DTYPE','DLOC'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_distributor = [i[0] for i in view_only_distributor_did()]
    selected_distributor = st.selectbox("Distributor to Delete", list_of_distributor)
    st.warning("Do you want to delete ::{}".format(selected_distributor))
    if st.button("Delete distributor"):
        delete_dist_data(selected_distributor)
        st.success("Distributor has been deleted successfully")
    new_result = view_distributor()
    df2 = pd.DataFrame(new_result, columns=['DID','DNAME','DPASS','DTYPE','DLOC'])
    with st.expander("Updated data"):
        st.dataframe(df2)        

def delete_sales():
    result = view_sales()
    df = pd.DataFrame(result, columns=['SALESID','SDATE','SCOST','SID'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_sales = [i[0] for i in view_only_sales_salesid()]
    selected_sales = st.selectbox("Sales to Delete", list_of_sales)
    st.warning("Do you want to delete ::{}".format(selected_sales))
    if st.button("Delete sales"):
        delete_sales_data(selected_sales)
        st.success("Sales has been deleted successfully")
    new_result = view_sales()
    df2 = pd.DataFrame(new_result, columns=['SALESID','SDATE','SCOST','SID'])
    with st.expander("Updated data"):
        st.dataframe(df2)             

def delete_stock():
    result = view_stock()
    df = pd.DataFrame(result, columns=['CRY','SCRY','Quant','SID'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_stock = [i[0] for i in view_only_scry()]
    selected_stock = st.selectbox("Stock to Delete", list_of_stock)
    st.warning("Do you want to delete ::{}".format(selected_stock))
    if st.button("Delete stock"):
        delete_stock_data(selected_stock)
        st.success("Stock has been deleted successfully")
    new_result = view_stock()
    df2 = pd.DataFrame(new_result, columns=['CRY','SCRY','Quant','SID'])
    with st.expander("Updated data"):
        st.dataframe(df2) 

def delete_store():
    result = view_store()
    df = pd.DataFrame(result, columns=['SID', 'SPASS', 'SBRANCHNAME', 'SCITY', 'SREGION', 'SSTATE', 'SPCODE'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_store = [i[0] for i in view_only_store_sid()]
    selected_store = st.selectbox("Store to Delete", list_of_store)
    st.warning("Do you want to delete ::{}".format(selected_store))
    if st.button("Delete store"):
        delete_store_data(selected_store)
        st.success("Store has been deleted successfully")
    new_result = view_store()
    df2 = pd.DataFrame(new_result, columns=['SID', 'SPASS', 'SBRANCHNAME', 'SCITY', 'SREGION', 'SSTATE', 'SPCODE'])
    with st.expander("Updated data"):
        st.dataframe(df2)  

def delete_stord():
    result = view_stord()
    df = pd.DataFrame(result, columns=['ORDID', 'SID', 'DID', 'ORDDATE', 'PMYSTAT', 'SHPMODE', 'SHPSTAT'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_stord = [i[0] for i in view_only_ordid()]
    selected_stord = st.selectbox("Store order to Delete", list_of_stord)
    st.warning("Do you want to delete ::{}".format(selected_stord))
    if st.button("Delete store order"):
        delete_stord_data(selected_stord)
        st.success("Store order has been deleted successfully")
    new_result = view_stord()
    df2 = pd.DataFrame(new_result, columns=['ORDID', 'SID', 'DID', 'ORDDATE', 'PMYSTAT', 'SHPMODE', 'SHPSTAT'])
    with st.expander("Updated data"):
        st.dataframe(df2)              
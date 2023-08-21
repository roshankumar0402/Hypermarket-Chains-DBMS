import datetime

import pandas as pd
import streamlit as st
from database import view_admin, view_only_admin_names, edit_admin_details,get_admin, view_distributor,get_dist, edit_dist_details, view_only_distributor_did, edit_sales_details, view_only_sales_salesid,view_sales,get_sales, view_only_scry, get_stock,edit_stock_details,view_stock,view_only_store_sid,view_store,edit_store_details,get_store,view_stord,view_only_ordid,get_stord,edit_stord_details

def update_admin_info():
    result = view_admin()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Admin ID', 'Password'])
    with st.expander("Current Admin Info"):
        st.dataframe(df)
    list_of_admins = [i[0] for i in view_only_admin_names()]
    selected_admin = st.selectbox("Admin to Edit", list_of_admins)
    selected_result = get_admin(selected_admin)
    # st.write(selected_result)
    if selected_result:
        admin_id = selected_result[0][0]
        password = selected_result[0][1]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_admin_id = st.text_input("Admin ID:", admin_id)
        with col2:
            new_password = st.text_input("Password:",password)

        if st.button("Update Admin Info"):
            edit_admin_details(new_admin_id, new_password, admin_id)
            st.success(f"Successfully updated {new_admin_id}")

    # result2 = view_admin()
    # df2 = pd.DataFrame(result2, columns=['Admin ID', 'Password'])
    # with st.expander("Updated admin"):
    #     st.dataframe(df2)

def update_distributor_info():
    result = view_distributor()
    # st.write(result)
    df = pd.DataFrame(result, columns=['DID','DNAME','DPASS','DTYPE','DLOC'])
    with st.expander("Current Distributor Information"):
        st.dataframe(df)
    list_of_distributor = [i[0] for i in view_only_distributor_did()]
    selected_distributor = st.selectbox("Distributor to Edit", list_of_distributor)
    selected_result = get_dist(selected_distributor)
    # st.write(selected_result)
    if selected_result:
        did = selected_result[0][0]
        dname = selected_result[0][1]
        dpass = selected_result[0][2]
        dtype = selected_result[0][3]
        dloc = selected_result[0][4]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_dname = st.text_input("Name:", dname)
            new_dpass = st.text_input("Password",dpass)
        with col2:
            new_dtype = st.text_input("Type:", dtype)
            new_dloc = st.text_input("Location",dloc)

        if st.button("Update Distributor"):
            edit_dist_details(new_dname, new_dpass, new_dtype,new_dloc, did)
            st.success(f"Successfully updated {did}")


def update_sales_info():
    result = view_sales()
    # st.write(result)
    df = pd.DataFrame(result, columns=['SALESID','SDATE','SCOST','SID'])
    with st.expander("Current sales information"):
        st.dataframe(df)
    list_of_sales = [i[0] for i in view_only_sales_salesid()]
    selected_sales = st.selectbox("sales to Edit", list_of_sales)
    selected_result = get_sales(selected_sales)
    # st.write(selected_result)
    if selected_result:
        salesid = selected_result[0][0]
        sdate = selected_result[0][1]
        scost = selected_result[0][2]
        sid = selected_result[0][3]

        # Layout of Create

        new_sdate = st.date_input("Date:",sdate)
        new_scost = st.number_input("Sales Cost",scost)
        

        if st.button("Update Sales"):
            edit_sales_details(salesid,new_sdate, new_scost,sid)
            st.success(f"Successfully updated {salesid}")


def update_stock_info():
    result = view_stock()
    # st.write(result)
    df = pd.DataFrame(result, columns=['CRY','SCRY','Quant','SID'])
    with st.expander("Current stock information"):
        st.dataframe(df)
    list_of_stock = [i[0] for i in view_only_scry()]
    selected_stock = st.selectbox("stock to Edit", list_of_stock)
    selected_result = get_stock(selected_stock)
    # st.write(selected_result)
    if selected_result:
        cry = selected_result[0][0]
        scry = selected_result[0][1]
        quant = selected_result[0][2]
        sid = selected_result[0][3]

        # Layout of Create

        new_cry = st.text_input("Category:",cry)
        new_quant = st.number_input("Quantity",quant)
        

        if st.button("Update Stock"):
            edit_stock_details(scry,new_cry, new_quant,sid)
            st.success(f"Successfully updated {scry}")

def update_store_info():
    result = view_store()
    # st.write(result)
    df = pd.DataFrame(result, columns=['SID', 'SPASS', 'SBRANCHNAME', 'SCITY', 'SREGION', 'SSTATE', 'SPCODE'])
    with st.expander("Current Store Information"):
        st.dataframe(df)
    list_of_store= [i[0] for i in view_only_store_sid()]
    selected_store = st.selectbox("Store to Edit", list_of_store)
    selected_result = get_store(selected_store)
    # st.write(selected_result)
    if selected_result:
        sid = selected_result[0][0]
        spass = selected_result[0][1]
        sbranchname = selected_result[0][2]
        scity = selected_result[0][3]
        sregion = selected_result[0][4]
        sstate = selected_result[0][5]
        spcode = selected_result[0][6]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_spass = st.text_input("Password:", spass)
            new_sbranchname = st.text_input("Branch name",sbranchname)
            new_scity = st.text_input("City:", scity)
            new_sregion = st.text_input("Region:", sregion)
        with col2:
            new_sstate = st.text_input("State:", sstate)
            new_spcode = st.number_input("Pin Code",spcode)

        if st.button("Update Store"):
            edit_store_details(sid, new_spass, new_sbranchname,new_scity, new_sregion,new_sstate,new_spcode)
            st.success(f"Successfully updated {sid}")

def update_stord_info():
    result = view_stord()
    # st.write(result)
    df = pd.DataFrame(result, columns=['ORDID', 'SID', 'DID', 'ORDDATE', 'PMYSTAT', 'SHPMODE', 'SHPSTAT'])
    with st.expander("Current Store Order Information"):
        st.dataframe(df)
    list_of_stord= [i[0] for i in view_only_ordid()]
    selected_stord = st.selectbox("Store Order to Edit", list_of_stord)
    selected_result = get_stord(selected_stord)
    # st.write(selected_result)
    if selected_result:
        ordid = selected_result[0][0]
        sid = selected_result[0][1]
        did = selected_result[0][2]
        orddate = selected_result[0][3]
        pmystat = selected_result[0][4]
        shpmode = selected_result[0][5]
        shpstat = selected_result[0][6]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_orddate = st.date_input("Order Date:",orddate)
            new_pmystat = st.text_input("Payment Status",pmystat)
        with col2:
            new_shpmode = st.text_input("Shipping Mode:", shpmode)
            new_shpstat = st.text_input("Shipping status",shpstat)

        if st.button("Update Store Order"):
            edit_stord_details(ordid,new_orddate,new_shpmode,new_shpstat,new_pmystat)
            st.success(f"Successfully updated {ordid}")            

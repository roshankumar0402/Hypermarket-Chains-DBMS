import streamlit as st
from database import add_admin, add_distributor,view_admin,view_only_admin_names,get_admin,edit_admin_details,delete_admin_data,view_distributor,add_sales,add_stock,view_stock,add_store,add_stord
import pandas as pd
from update import update_distributor_info,update_sales_info,update_stock_info, update_store_info,update_stord_info
from delete import delete_dist,delete_sales, delete_stock,delete_store,delete_stord
from read import read_distributor, read_sales, read_stock, read_store,read_stord
def create_admin():
    # tab1, tab2, tab3,tab4 = st.tabs(["Add Admin","Update Admin","View Admin","Delete Admin"])
    menu = ["Add Admin","View Admin","Update Admin","Delete Admin"]
    choice = st.selectbox("Menu",menu)

    if choice == "Add Admin":
        col1, col2 = st.columns(2)
        with col1:
            admin_id = st.text_input("Admin ID:")
            if len(admin_id)== 0:
                st.error("please enter admin ID")
        with col2:
            admin_password = st.text_input("Admin Password: ")
            if len(admin_password)== 0:
                st.error("please enter password")
        if st.button("Add Admin"):
           add_admin(admin_id, admin_password)
           st.success(f"Admin {admin_id} added Succesfully!")

    elif choice == "View Admin":
        result = view_admin()
        # st.write(result)
        df = pd.DataFrame(result, columns=['Admin ID', 'PASSWORD'])
        with st.expander("View all Admins"):
            st.dataframe(df)

    elif choice == "Update Admin":
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
            # col1, col2 = st.columns(2)
            # with col1:
            #     new_admin_id = st.text_input("Admin ID:", admin_id)
            # with col2:
            new_password = st.text_input("Password:",password)

            if st.button("Update Admin Info"):
                edit_admin_details(admin_id, new_password, admin_id)
                st.success(f"Successfully updated {admin_id}")
    
    elif choice == "Delete Admin":
        result = view_admin()
        df = pd.DataFrame(result, columns=['Admin ID', 'Password'])
        with st.expander("Current data"):
            st.dataframe(df)
        list_of_admins = [i[0] for i in view_only_admin_names()]
        selected_admin = st.selectbox("Admin to Delete", list_of_admins,key=2)
        st.warning("Do you want to delete ::{}".format(selected_admin))
        if st.button("Delete Admin",key=4):
            delete_admin_data(selected_admin)
            st.success("Admin has been deleted successfully")
        new_result = view_admin()
        df2 = pd.DataFrame(new_result, columns=['Admin ID', 'Password'])
        with st.expander("Updated data"):
            st.dataframe(df2)


def create_dist():
    menu = ["Add Distributor","View Distributor","Update Distributor","Delete Distributor"]
    choice = st.selectbox("menu", menu)
    if choice == "Add Distributor":
        col1, col2 = st.columns(2)
        with col1:
            did = st.number_input("Distributor ID:")
            d_name = st.text_input("Distributor Name:")
            d_pass = st.text_input("Distributor Password:")
        with col2:
            d_type = st.text_input("Distributor Type:")
            d_loc = st.text_input("Distributor Location:")


        if st.button("Add Distributor"):
            add_distributor(did, d_name, d_pass, d_type, d_loc )
            st.success("Successfully added Distributor: {}".format(d_name))
    
    elif choice =="View Distributor":
        read_distributor()
    
    elif choice =="Update Distributor":
        update_distributor_info()
    
    elif choice =="Delete Distributor":
        delete_dist()

def create_sales():
    menu = ["Add Sales","View Sales","Update Sales","Delete Sales"]
    choice = st.selectbox("menu", menu)
    if choice == "Add Sales":
        col1, col2 = st.columns(2)
        with col1:
            salesid = st.number_input("Sales ID:")
            sdate= st.date_input("Sales Date:")
        with col2:
            scost = st.number_input("Sales cost:")
            sid = st.number_input("Store ID:")


        if st.button("Add Sales"):
            add_sales(salesid, sdate, scost, sid)
            st.success("Successfully added Sales: {}".format(salesid))
    
    elif choice =="View Sales":
        read_sales()
    
    elif choice =="Update Sales":
        update_sales_info()
    
    elif choice =="Delete Sales":
        delete_sales()     

def create_stock():
    menu = ["Add Stock","View Stock","Update Stock","Delete Stock"]
    choice = st.selectbox("menu", menu)
    if choice == "Add Stock":
        col1, col2 = st.columns(2)
        with col1:
            cry = st.text_input("Category:")
            scry= st.text_input("Store Category:")
        with col2:
            quant = st.number_input("Quantity:")
            sid = st.number_input("Store ID:")


        if st.button("Add Stock"):
            add_stock(cry, scry, quant, sid)
            st.success("Successfully added")
    
    elif choice =="View Stock":
        read_stock()
    
    elif choice =="Update Stock":
        update_stock_info()
    
    elif choice =="Delete Stock":
        delete_stock()             

def create_store():
    menu = ["Add Store","View Store","Update Store","Delete Store"]
    choice = st.selectbox("menu", menu)
    if choice == "Add Store":
        col1, col2 = st.columns(2)
        with col1:
            sid = st.number_input("Store ID:")
            spass = st.text_input("Store Password:")
            sbranchname = st.text_input("Store Branch Name:")
            scity = st.text_input("Store city:")
        with col2:
            sregion = st.text_input("Store region:")
            sstate = st.text_input("Store state:")
            spcode = st.number_input("Store Pin Code:")

        if st.button("Add Store"):
            add_store(sid, spass, sbranchname, scity, sregion, sstate, spcode )
            st.success("Successfully added Store: {}".format(sid))
    
    elif choice =="View Store":
        read_store()
    
    elif choice =="Update Store":
        update_store_info()
    
    elif choice =="Delete Store":
        delete_store() 

def create_st_orders():
    menu = ["Add Store Order","View Store Order","Update Store Order","Delete Store Order"]
    choice = st.selectbox("menu", menu)
    if choice == "Add Store Order":
        col1, col2 = st.columns(2)
        with col1:
            ordid = st.number_input("Order ID:")
            sid = st.number_input("Store ID:")
            did = st.number_input("Distributor ID:")
            orddate = st.date_input("Order Date:")
        with col2:
            pmystat = st.text_input("Payment Status:")
            shpmode = st.text_input("Shipping mode:")
            shpstat = st.text_input("Shipping Status:")

        if st.button("Add Store Order"):
            add_stord(ordid, sid, did, orddate, pmystat, shpmode, shpstat )
            st.success("Successfully added Store order: {}".format(ordid))
    
    elif choice =="View Store Order":
        read_stord()
    
    elif choice =="Update Store Order":
        update_stord_info()
    
    elif choice =="Delete Store Order":
        delete_stord()               
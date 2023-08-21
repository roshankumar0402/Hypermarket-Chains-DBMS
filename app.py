import streamlit as st
import mysql.connector

from create import create_admin, create_dist, create_sales, create_stock,create_store,create_st_orders
from database import create_table, view_admin,execute_
# from delete import *
# from read import read_admin, read_distributor
# from update import update_admin_info, update_distributor_info

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
c = mydb.cursor()

def main():
    st.title("Hypermarket management system")
    query = st.text_area("Query Box:")
    if st.button("Run"):

        result = execute_(query)
        st.write(result)
    # menu = ["Admin", "Distributor", "Edit Admin Info", "Remove Admin","Add Distributor", "View Distributor","Edit Distributor Info", "Remove Distributor"]
    menu = ["Admin", "Distributor", "Sales","Stock","Store","Store Orders"]

    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
    if choice == "Admin":
        st.subheader("Admin:")
        create_admin()

    elif choice == "Distributor":
        st.subheader("Distributor:")
        create_dist()

    elif choice == "Sales":
        st.subheader("Sales:")
        create_sales()

    elif choice == "Stock":
        st.subheader("Stock:")
        create_stock()
    

    elif choice == "Store":
        st.subheader("Store:")
        create_store()

    elif choice == "Store Orders":
        st.subheader("Store Orders:")
        create_st_orders()

    # elif choice == "Remove Admin":
    #     st.subheader("Delete Admin:")
    #     delete_admin()

    # elif choice == "Remove Distributor":
    #     st.subheader("Delete Distributor:")
    #     delete_dist()

    else:
        st.subheader("About Admin")


if __name__ == '__main__':
    main()
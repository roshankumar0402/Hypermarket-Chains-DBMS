import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hypermarket_582"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS ADMIN (ANAME varchar(30), APASS varchar(30));')

def execute_(query):
    c.execute(query)
    result = c.fetchall()
    return result

def add_admin(ANAME, APASS):
    c.execute('INSERT INTO ADMIN (ANAME, APASS) VALUES (%s,%s);',
              (ANAME, APASS))
    mydb.commit()

def add_distributor(did, d_name, d_pass, d_type, d_loc):
    c.execute('INSERT INTO dist (DID,DNAME,DPASS,DTYPE,DLOC) VALUES (%s,%s,%s,%s,%s);',
              (did, d_name, d_pass, d_type, d_loc))
    mydb.commit()

def add_sales(salesid, sdate, scost, sid):
    c.execute('INSERT INTO sales (salesid, sdate, scost, sid) VALUES (%s,%s,%s,%s);',
              (salesid, sdate, scost, sid))
    mydb.commit()

def add_stock(cry, scry, quant, sid):
    c.execute('INSERT INTO stock (cry, scry, quant, sid) VALUES (%s,%s,%s,%s);',
              (cry, scry, quant, sid))
    mydb.commit()    

def add_store(sid, spass, sbranchname, scity, sregion, sstate, spcode):
    c.execute('INSERT INTO store (sid, spass, sbranchname, scity, sregion, sstate, spcode) VALUES (%s,%s,%s,%s,%s,%s,%s);',
              (sid, spass, sbranchname, scity, sregion, sstate, spcode))
    mydb.commit()

def add_stord(ordid, sid, did, orddate, pmystat, shpmode, shpstat):
    c.execute('INSERT INTO st_orders (ordid, sid, did, orddate, pmystat, shpmode, shpstat) VALUES (%s,%s,%s,%s,%s,%s,%s);',
              (ordid, sid, did, orddate, pmystat, shpmode, shpstat))
    mydb.commit()    

def view_admin():
    c.execute('SELECT * FROM ADMIN')
    data = c.fetchall()
    return data

def view_distributor():
    c.execute('SELECT * FROM dist')
    data = c.fetchall()
    return data

def view_sales():
    c.execute('SELECT * FROM sales')
    data = c.fetchall()
    return data 

def view_stock():
    c.execute('SELECT * FROM stock')
    data = c.fetchall()
    return data 

def view_store():
    c.execute('SELECT * FROM store')
    data = c.fetchall()
    return data

def view_stord():
    c.execute('SELECT * FROM st_orders')
    data = c.fetchall()
    return data

def view_only_admin_names():
    c.execute('SELECT ANAME FROM ADMIN')
    data = c.fetchall()
    return data

def view_only_distributor_did():
    c.execute('SELECT Did FROM dist')
    data = c.fetchall()
    return data

def view_only_sales_salesid():
    c.execute('SELECT SALESID FROM Sales')
    data = c.fetchall()
    return data


def view_only_scry():
    c.execute('SELECT scry FROM Stock')
    data = c.fetchall()
    return data

def view_only_store_sid():
    c.execute('SELECT sid FROM Store')
    data = c.fetchall()
    return data    

def view_only_ordid():
    c.execute('SELECT ordid FROM st_orders')
    data= c.fetchall()
    return data

def get_admin(id):
    c.execute(f'SELECT * FROM ADMIN WHERE ANAME="{id}";')
    data=c.fetchall()
    return data

def get_dist(id):
    c.execute(f'SELECT * FROM dist WHERE DID="{id}";')
    data=c.fetchall()
    return data

def get_store(id):
    c.execute(f'SELECT * FROM store WHERE SID="{id}";')
    data=c.fetchall()
    return data

def get_sales(id):
    c.execute(f'SELECT * FROM sales WHERE salesID="{id}";')
    data=c.fetchall()
    return data    

def get_stock(scry):
    c.execute(f'SELECT * FROM stock WHERE scry="{scry}";')
    data=c.fetchall()
    return data 

def get_stord(ordid):
    c.execute(f'SELECT * FROM st_orders WHERE ordid="{ordid}";')
    data=c.fetchall()
    return data    

def edit_admin_details(ANAME, APASS, admin_id):
    c.execute(f"UPDATE ADMIN SET ANAME='{ANAME}', APASS='{APASS}' WHERE ANAME='{admin_id}'")
    mydb.commit()

def edit_dist_details(new_dname, new_dpass, new_dtype,new_dloc, did):
    c.execute(f"UPDATE dist SET DNAME='{new_dname}', DPASS='{new_dpass}',DTYPE='{new_dtype}', DLOC='{new_dloc}' WHERE did={did}")
    mydb.commit()

def edit_sales_details(salesid,new_sdate, new_scost,sid):
    c.execute(f"UPDATE sales SET scost='{new_scost}', Sdate='{new_sdate}' WHERE salesid={salesid}")
    mydb.commit()

def edit_stock_details(scry,new_cry, new_quant,sid):
    c.execute(f"UPDATE stock SET cry = '{new_cry}',quant={new_quant} WHERE SCRY ='{scry}'")
    mydb.commit()

def edit_store_details(sid, new_spass, new_sbranchname,new_scity, new_sregion,new_sstate,new_spcode):
    c.execute(f"UPDATE store SET spass = '{new_spass}',sbranchname='{new_sbranchname}',scity='{new_scity}',sregion='{new_sregion}',sstate='{new_sstate}',spcode={new_spcode} WHERE SID ='{sid}'")
    mydb.commit()

def edit_stord_details(ordid,new_orddate,new_shpmode,new_shpstat,new_pmystat):
    c.execute(f"UPDATE st_orders SET orddate = '{new_orddate}',shpmode='{new_shpmode}',shpstat='{new_shpstat}',pmystat='{new_pmystat}' WHERE ORDID ='{ordid}'")
    mydb.commit()

def delete_admin_data(selected_admin):
    c.execute('DELETE FROM ADMIN WHERE ANAME="{}"'.format(selected_admin))
    mydb.commit()

def delete_dist_data(selected_did):
    c.execute('DELETE FROM dist WHERE did="{}"'.format(selected_did))
    mydb.commit()   


def delete_sales_data(selected_salesid):
    c.execute('DELETE FROM sales WHERE salesid="{}"'.format(selected_salesid))
    mydb.commit()      

def delete_stock_data(scry):
    c.execute('DELETE FROM stock WHERE scry="{}"'.format(scry))
    mydb.commit() 

def delete_store_data(sid):
    c.execute('DELETE FROM store WHERE sid="{}"'.format(sid))
    mydb.commit()     

def delete_stord_data(ordid):
    c.execute('DELETE FROM st_orders WHERE ordid="{}"'.format(ordid))
    mydb.commit()    
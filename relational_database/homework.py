from typing import List


def task_1_add_new_record_to_db(con) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """
    with con.cursor() as cur:
        cur.execute("INSERT INTO customers (CustomerName, contactname, address, city, postalcode, country)"
                    "VALUES ('Thomas', 'David', 'Some Address', 'London', '774', 'Singapore');")
    con.commit()



def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    cur.execute("SELECT * FROM Customers;")
    return cur.fetchall()


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute("SELECT * FROM Customers WHERE Country = 'Germany';")
    return cur.fetchall()


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """
    with con.cursor() as cur:
        cur.execute("UPDATE customers SET customername = 'Johnny Depp' WHERE  customerid IN "
                    "(SELECT customerid FROM customers ORDER BY customerid LIMIT 1);")
    con.commit()


def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    with con.cursor() as cur:
        cur.execute("DELETE FROM customers WHERE customerid IN "
                    "(SELECT customerid FROM customers ORDER BY customerid DESC LIMIT 1);")
    con.commit()


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    cur.execute("SELECT country FROM Suppliers;")
    return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    cur.execute("SELECT country FROM Suppliers ORDER BY country DESC;")
    return cur.fetchall()


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    json Example:
    "count": 3,
    "city": "Madrid"

    """
    cur.execute("SELECT COUNT(customerid), city FROM Customers GROUP BY city;")
    return cur.fetchall()


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute("SELECT COUNT(customerid), country FROM Customers GROUP BY country HAVING COUNT(country) > 10;")
    return cur.fetchall()


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    cur.execute("SELECT * FROM Customers WHERE customerid < 11;")
    return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute("SELECT * FROM Customers WHERE customerid > 11;")
    return cur.fetchall()


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    cur.execute("SELECT supplierid, suppliername, contactname, city, country "
                "FROM Suppliers WHERE country = 'USA' OR country = 'UK' OR country = 'Japan';")
    return cur.fetchall()


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute("SELECT products.productname FROM products "
                "JOIN suppliers ON products.supplierid = suppliers.supplierid "
                "WHERE suppliers.country = 'SWEDEN';")
    return cur.fetchall()


def task_14_list_products_with_supplier_information(cur):   #FAILED, money type issue
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records

    json Example:
    "productid": 1,
    "productname": "Chais",
    "unit": "10 boxes x 20 bags",
    "price": "$18.00",
    "country": "UK",
    "city": "Londona",
    "suppliername": "Exotic Liquid"

    """
    cur.execute("SELECT products.productid, products.productname, products.unit, products.price, "
                "suppliers.country, suppliers.city, suppliers.suppliername "
                "FROM products "
                "JOIN suppliers ON suppliers.supplierid = products.supplierid;")
    return cur.fetchall()


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records

    json Example:
    "customername": "Old World Delicatessen",
    "contactname": "Rene Phillips",
    "country": "USA",
    "orderid": 13
    """
    cur.execute("SELECT customers.customername, customers.contactname, customers.country, orders.orderid "
                "FROM customers "
                "FULL OUTER JOIN orders ON customers.customerid = orders.customerid;")
    return cur.fetchall()


def task_16_match_all_customers_and_suppliers_by_country(cur):  #FAILED
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records

    json Example:
    "customername": "Cactus Comidas para llevar",
    "address": "Cerrito 333",
    "customercountry": "Argentina",
    "suppliercountry": null,
    "suppliername": null
    """
    cur.execute("SELECT customers.customername, customers.address, customers.country, "
                "suppliers.country, suppliername "
                "FROM customers "
                "JOIN suppliers ON customers.country = suppliers.country;")
    return cur.fetchall()   # returns <class 'psycopg2.extras.RealDictRow'> instead of Dict, why?



"""
looks like predicted output from tasks_[8,14].json not matches to actual tests results
"""
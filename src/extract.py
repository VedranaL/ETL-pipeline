import psycopg2
import pandas as pd


def connect_to_redshift(dbname, host, port, user, password):
    """Method that connects to redshift. This gives a warning so will look for another solution"""

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )

    print("connection to redshift made")

    return connect


def extract_transaction_data(dbname, host, port, user, password):
    # connect to redshift
    connect = connect_to_redshift(dbname, host, port, user, password)

    # read sql query with transformation tasks

    query = """
    SELECT ot.invoice, 
        ot.stock_code,
        ot.quantity,
        CAST(invoice_date As DateTime) AS invoice_date,
        ot.price,
        ot.customer_id,
        ot.country,
       CASE WHEN s.description IS NULL THEN 'Unknown'
            ELSE s.description END AS description,
        ot.price*ot.quantity as order_value
FROM bootcamp.online_transactions ot
/* this is a subquery that removes '?' from the stock_description table */
LEFT JOIN ( SELECT *
            FROM bootcamp.stock_description
            WHERE description <> '?') AS s
ON ot.stock_code = s.stock_code
WHERE ot.customer_id <> ''
AND ot.stock_code NOT IN ('BANK CHARGES', 'POST', 'D', 'M', 'CRUK')
"""

    online_trans_cleaned = pd.read_sql(query, connect)

    print("The shape of transformed data is:", online_trans_cleaned.shape)

    return online_trans_cleaned

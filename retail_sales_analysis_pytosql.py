import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL
conn = mysql.connector.connect(
     host="127.0.0.1",        # correct from Workbench
    port=3306,               # MySQL default port
    user="root",             # your username
    password="root",# replace with your root password
    database="employees"   
)

# Query 1: Monthly Sales
query = """
SELECT DATE_FORMAT(STR_TO_DATE(`Order Date`, '%d-%m-%Y'), '%Y-%m') AS Month,
       SUM(Sales) AS Monthly_Sales
FROM retail_sales
GROUP BY Month
ORDER BY Month;
"""
df_monthly = pd.read_sql(query, conn)

# Plot Monthly Sales
plt.figure(figsize=(10,5))
plt.plot(df_monthly['Month'], df_monthly['Monthly_Sales'], marker='o')
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.show()

# Query 2: Sales by Category
query2 = """
SELECT Category, SUM(Sales) AS Total_Sales
FROM retail_sales
GROUP BY Category
ORDER BY Total_Sales DESC;
"""
df_category = pd.read_sql(query2, conn)

# Plot Sales by Category
plt.figure(figsize=(8,5))
plt.bar(df_category['Category'], df_category['Total_Sales'])
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.show()

# Close connection
conn.close()

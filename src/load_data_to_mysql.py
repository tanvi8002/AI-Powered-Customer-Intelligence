
import pandas as pd
from pathlib import Path
from getpass import getpass
from sqlalchemy import create_engine, URL, text

# Project folder
project_folder = Path(__file__).resolve().parent.parent

# Cleaned CSV file
file_path = project_folder / "data" / "processed" / "telco_customer_churn_cleaned.csv"

# Load cleaned dataset
df = pd.read_csv(file_path)

print("Dataset loaded:", df.shape)

# Ask for MySQL password
mysql_password = getpass("Enter your ai_project MySQL password: ")

# Create database connection
connection_url = URL.create(
    drivername="mysql+pymysql",
    username="ai_project",
    password=mysql_password,
    host="127.0.0.1",
    port=3306,
    database="ai_customer_intelligence"
)

engine = create_engine(connection_url)

try:
    # Import dataset into MySQL
    df.to_sql(
        name="customers",
        con=engine,
        if_exists="replace",
        index=False,
        chunksize=1000
    )

    print("\nData imported successfully!")

    # Verify imported records
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT COUNT(*) FROM customers")
        )
        print("Total records in MySQL:", result.scalar())

    print("MySQL table: customers")

except Exception as error:
    print("Import failed:", error)

finally:
    engine.dispose()

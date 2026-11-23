
import pandas as pd
from pathlib import Path
from getpass import getpass
from sqlalchemy import create_engine, URL, text

# Project folder
project_folder = Path(__file__).resolve().parent.parent

# Load customer risk report
file_path = project_folder / "data" / "processed" / "customer_risk_report.csv"
df = pd.read_csv(file_path)

print("Risk report loaded:", df.shape)

# MySQL password
mysql_password = getpass("Enter your ai_project MySQL password: ")

# Connect to MySQL
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
    # Import report into MySQL
    df.to_sql(
        name="customer_risk_predictions",
        con=engine,
        if_exists="replace",
        index=False,
        chunksize=1000
    )

    print("\nRisk report imported successfully!")

    # Verify imported records
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT COUNT(*) FROM customer_risk_predictions")
        )
        print("Records in MySQL:", result.scalar())

    print("MySQL table: customer_risk_predictions")

except Exception as error:
    print("Import failed:", error)

finally:
    engine.dispose()

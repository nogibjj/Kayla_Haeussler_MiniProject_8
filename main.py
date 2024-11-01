import sqlite3
import csv
import argparse


# Function to create a table
def create_table(conn, table_name):
    create_query = f"""
    CREATE TABLE IF NOT EXISTS "{table_name}" (
        competitorname TEXT PRIMARY KEY,
        chocolate INTEGER NOT NULL,
        fruity INTEGER NOT NULL,
        caramel INTEGER NOT NULL,
        peanutyalmondy INTEGER NOT NULL,
        nougat INTEGER NOT NULL,
        crispedricewafer INTEGER NOT NULL,
        hard INTEGER NOT NULL,
        bar INTEGER NOT NULL,
        pluribus INTEGER NOT NULL
    )
    """
    conn.execute(create_query)
    conn.commit()
    print(f"Table '{table_name}' created successfully.")


# Function to execute a query and print results
def query_exec(conn, query_string):
    cursor = conn.execute(query_string)
    rows = cursor.fetchall()

    for row in rows:
        print(
            "Competitor Name: {}, Chocolate: {}, Fruity: {}, Caramel: {}, Peanuty/Almondy: {}, "
            "Nougat: {}, Crisper Rice/Wafer: {}, Hard Candy: {}, Bar: {}, One of Many in a Bag/Box: {}".format(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9],
            )
        )
    return rows


# Function to drop a table
def drop_table(conn, table_name):
    drop_query = f"DROP TABLE IF EXISTS {table_name}"
    conn.execute(drop_query)
    conn.commit()
    print(f"Table '{table_name}' dropped successfully.")


# Function to load data from a CSV file to a table
def load_data_from_csv(conn, table_name, file_path):
    with open(file_path, "r") as file:
        rdr = csv.reader(file)
        insert_query = f"""
        INSERT INTO "{table_name}" (competitorname, chocolate, fruity, caramel, peanutyalmondy, nougat,
        crispedricewafer, hard, bar, pluribus) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        for record in rdr:
            if (
                not record or len(record) < 10
            ):  # Skip empty rows or rows with insufficient columns
                continue
            competitorname = record[0]
            chocolate = int(record[1])
            fruity = int(record[2])
            caramel = int(record[3])
            peanutyalmondy = int(record[4])
            nougat = int(record[5])
            crispedricewafer = int(record[6])
            hard = int(record[7])
            bar = int(record[8])
            pluribus = int(record[9])

            conn.execute(
                insert_query,
                (
                    competitorname,
                    chocolate,
                    fruity,
                    caramel,
                    peanutyalmondy,
                    nougat,
                    crispedricewafer,
                    hard,
                    bar,
                    pluribus,
                ),
            )
        conn.commit()
        print(f"Data loaded successfully from '{file_path}' into table '{table_name}'.")


def main():
    parser = argparse.ArgumentParser(description="SQLite CLI for managing candy data.")
    subparsers = parser.add_subparsers(dest="command")

    # Create command
    create_parser = subparsers.add_parser(
        "create", aliases=["c"], help="Create a new table"
    )
    create_parser.add_argument(
        "table_name", type=str, help="Name of the table to create"
    )

    # Query command
    query_parser = subparsers.add_parser("query", aliases=["q"], help="Execute a query")
    query_parser.add_argument("query", type=str, help="SQL query to execute")

    # Delete command
    delete_parser = subparsers.add_parser(
        "delete", aliases=["d"], help="Delete a table"
    )
    delete_parser.add_argument(
        "delete_query", type=str, help="Name of the table to delete"
    )

    # Load command
    load_parser = subparsers.add_parser(
        "load", aliases=["l"], help="Load data from a CSV file into a table"
    )
    load_parser.add_argument(
        "table_name", type=str, help="Name of the table to load data into"
    )
    load_parser.add_argument("file_path", type=str, help="Path to the CSV file")

    # Update command
    update_parser = subparsers.add_parser(
        "update", aliases=["u"], help="Update a row in a table"
    )
    update_parser.add_argument(
        "table_name", type=str, help="Name of the table to update"
    )
    update_parser.add_argument("set_clause", type=str, help="SET clause for the update")
    update_parser.add_argument("condition", type=str, help="Condition for the update")

    args = parser.parse_args()

    # Create a database connection
    conn = sqlite3.connect("my_database.db")

    # Execute the appropriate command
    if args.command == "create":
        create_table(conn, args.table_name)
    elif args.command == "query":
        query_exec(conn, args.query)
    elif args.command == "delete":
        drop_table(conn, args.delete_query)
    elif args.command == "load":
        load_data_from_csv(conn, args.table_name, args.file_path)
    elif args.command == "update":
        query = (
            f"UPDATE {args.table_name} SET {args.set_clause} WHERE {args.condition};"
        )
        query_exec(conn, query)

    # Close the connection
    conn.close()


if __name__ == "__main__":
    main()

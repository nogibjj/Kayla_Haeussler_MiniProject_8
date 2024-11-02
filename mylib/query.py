"""Query the database using SQLITE"""

import sqlite3
from mylib.timing import measure_time_and_memory


@measure_time_and_memory
def create():
    """Create fake data"""
    conn = sqlite3.connect("Candy_DB.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Candy_DB VALUES "
        "('Data Engineering','0','0','0','0', '0','0','0','0', '0','0','0','0')"
    )
    conn.commit()
    conn.close()
    return "Sucessfully created!"


@measure_time_and_memory
def read():
    """Read and print the database for all the rows of the candy table"""
    conn = sqlite3.connect("Candy_DB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Candy_DB")
    print(cursor.fetchall())
    conn.close()
    return "Successfully read!"


@measure_time_and_memory
def update():
    """Update competior name to be loser where winpercent <50%"""
    conn = sqlite3.connect("Candy_DB.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Candy_DB SET competitorname = 'LOSER' WHERE winpercent < '50';"
    )
    conn.commit()
    conn.close()
    return "Successfully updated!"


@measure_time_and_memory
def delete():
    """Delete all rows we marked as loser in the update"""
    conn = sqlite3.connect("Candy_DB.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Candy_DB WHERE competitorname == 'LOSER';")
    conn.commit()
    conn.close()
    return "Sucessfully deleted!"


if __name__ == "__main__":
    create()
    read()
    update()
    delete()

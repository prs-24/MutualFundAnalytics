"""
Database Creation Module

This module initializes the SQLite database for the
Mutual Fund Analytics project.

It creates the database and executes the SQL schema
defined in schema.sql to generate the required tables.
"""

import sqlite3


DATABASE_PATH = "database/bluestock_mf.db"
SCHEMA_FILE = "database/schema.sql"


def create_database():
    """
    Create the SQLite database and execute the schema script.

    Returns
    -------
    None
    """

    connection = None

    try:
        # Establish database connection
        connection = sqlite3.connect(
            DATABASE_PATH
        )

        # Read schema file
        with open(
            SCHEMA_FILE,
            "r"
        ) as schema_file:

            schema_sql = schema_file.read()

        # Execute SQL schema
        connection.executescript(
            schema_sql
        )

        connection.commit()

        print(
            "Database created successfully."
        )

    except FileNotFoundError:
        print(
            f"Error: Schema file '{SCHEMA_FILE}' not found."
        )

    except sqlite3.Error as error:
        print(
            f"SQLite error occurred: {error}"
        )

    except Exception as error:
        print(
            f"An unexpected error occurred: {error}"
        )

    finally:
        if connection:
            connection.close()


def main():
    """
    Execute database creation process.
    """

    create_database()


if __name__ == "__main__":
    main()
#imports from standard packages
import shelve
import sqlite3
"""
The data_management.py file contains functions related to data management only.
Generic functions: savedata(data, datafilename) and readdata(datafile).  Currently, these are not being used.

Specific functions read_candidate_data(), save_candidate_data(), read_studydata() and save_study_data() are used to get/save candidate data and study setup data respectively.
"""
"""
#Generic functions
def savedata(data, datafilename):
    db = shelve.open(datafilename)
    for key in data:
        db[data[key].uid] = data[key]
    db.close()


def readdata(datafile):
    db = shelve.open(datafile)  #TODO check is db.close() is needed (may be automatic)
    return db
"""



"""
GENERIC FUNCTIONS
"""

def database_execute(database, query, data):
    """
    Function that opens the SQLite database, executes a query and then close
    the connection.

    :param database: name of the database
     :type database: str
    :param query: the query to execute
     :type query: str
    :param data: if defined, the data to use to execute the statement
     :type data: list

    """

    # Connect to the database
    conn = sqlite3.connect(database)
    c    = conn.cursor()

    # Execute the query
    if (data):
        c.execute(query, data)
    else:
        c.execute(query)

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

def database_executemany(database, query, data):
    """
    Function that opens the SQLite database, executes a query on multiple lines
    of data and then close the connection.

    :param database: name of the database
     :type database: str
    :param query: the query to execute
     :type query: str
    :param data: if defined, the data to use to execute the statement
     :type data: list

    """


    # Connect to the database
    conn = sqlite3.connect(database)
    c    = conn.cursor()

    # Execute the query
    if (data):
        c.executemany(query, data)
    else:
        c.executemany(query)

    # Commit the change and close the database connection
    conn.commit()
    conn.close()

def database_selectall_table(database, table):
    """
    Function that reads a table of the SQLite database and returns selected
    rows.

    :param database: name of the database
     :type database: str
    :param table: name of the table from which to select data
     :type table: str

    :return rows_list: rows that where returned by the select statement
     :type rows_list: list

    """


    # Create select query
    selectall_query = """
        SELECT *
        FROM
    """
    selectall_query += table

    # Connect to the database
    conn = sqlite3.connect(database)
    c    = conn.cursor()

    # Execute the query and get the results in the list rows_list
    rows_list = []
    for row in c.execute(selectall_query):
        rows_list.append(row)

    # Close the connection
    conn.close()

    # Return the list of rows
    return rows_list


"""
SPECIFIC FUNCTIONS
"""

def create_new_database(database):
    """
    Create a new database using SQLite3

    :param database: name of the database to create
     :type database: str

    """

    # Create query for the project table
    create_project_table_query = '''
        CREATE TABLE project
            (ProjectID          INTEGER UNIQUE NOT NULL,
             Name               TEXT,
             RecruitementTarget INTEGER
            )
    '''

    # Create query for the visit windows table
    create_visit_windows_table_query = '''
        CREATE TABLE visit_windows
            (VisitLabel         TEXT    NOT NULL,
             ProjectID          INTEGER,
             PreviousVisitLabel TEXT,
             NextVisitLabel     TEXT,
             WindowMinDays      INTEGER,
             WindowMaxDays      INTEGER
            )
    '''

    # Create query for the candidate table
    create_candidate_table_query = '''
        CREATE TABLE candidate
            (PSCID      TEXT    UNIQUE NOT NULL,
             CandID     INTEGER UNIQUE NOT NULL,
             Status     TEXT,
             Firstname  TEXT,
             Middlename TEXT,
             Lastname   TEXT,
             Phone      TEXT
            )
    '''

    # Create query for the session table
    create_session_table_query = '''
        CREATE TABLE session
            (CandID        INTEGER,
             VisitLabel    TEXT,
             ProjectID     INTEGER,
             VisitDate     TEXT,
             VisitLocation TEXT,
             VisitStatus   TEXT
            )
    '''

    # Create the tables
    database_execute(database, create_project_table_query, None)
    database_execute(database, create_visit_windows_table_query, None)
    database_execute(database, create_candidate_table_query, None)
    database_execute(database, create_session_table_query, None)

def save_project_data(database, data):
    """
    Function that saves the project information in the SQLite database.

    :param database: name of the database
     :type database: str
    :param data: if defined, the data to use to execute the statement
     :type data: list

    """

    # Create the insert query
    insert_project_query = '''
        INSERT INTO project
            (ProjectID, Name, RecruitementTarget)
            VALUES
            (?, ?, ?)
    '''
    if (isinstance(data[0], tuple)):
        database_executemany(database,insert_project_query, data)
    else:
        database_execute(database, insert_project_query, data)

def save_visit_windows_data(database, data):
    """
    Function that saves the visit windows information in the SQLite database.

    :param database: name of the database
     :type database: str
    :param data: if defined, the data to use to execute the statement
     :type data: list

    """

    # Create the insert query
    insert_visit_windows_query = '''
        INSERT INTO visit_windows
            (ProjectID,      VisitLabel,     PreviousVisitLabel,
             NextVisitLabel, WindowMinDays,  WindowMaxDays
            )
            VALUES (?, ?, ?,
                    ?, ?, ?
                   )
    '''

    # Execute insert query with values stored in data
    if (isinstance(data[0], tuple)):
        database_executemany(database,insert_visit_windows_query, data)
    else:
        database_execute(database, insert_visit_windows_query, data)

def save_candidate_data(database, data):
    """
    Function that saves the candidate's information in the SQLite database.

    :param database: name of the database
     :type database: str
    :param data: if defined, the data to use to execute the statement
     :type data: list

    """

    # Create the insert query
    insert_candidate_query = '''
        INSERT INTO candidate
            (PSCID,     CandID,     Status,
             Firstname, Middlename, Lastname,
             Phone
            )
            VALUES (?, ?, ?,
                    ?, ?, ?,
                    ?
                   )
    '''

    # Execute insert query with values stored in data
    if (isinstance(data[0], tuple)):
        database_executemany(database, insert_candidate_query, data)
    else:
        database_execute(database, insert_candidate_query, data)


""" OLD FUNCTION FROM PIERRE-EMMANUEL MORIN
def read_candidate_data():
    db = shelve.open("candidatedata")
    return db

def save_candidate_data(data):
    db = shelve.open("candidatedata")
    for key in data:
        db[data[key].uid] = data[key]
    db.close()

def read_studydata():
    db = shelve.open("studydata")
    return db

def save_study_data(data):
    db = shelve.open("studydata")
    for key in data:
        db[data[key].uid] = data[key]
    db.close()
"""


#self-test "module"  TODO remove
if __name__ == '__main__':
    print 'testing module:  datamanagement.py'
    data=dict(read_candidate_data());
    print data;

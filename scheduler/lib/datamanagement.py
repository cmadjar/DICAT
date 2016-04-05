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

    :return result_list: list of data dictionary with results of the select
    statement
      :type result_list: list

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
    c.execute(selectall_query)
    rows_list = c.fetchall()

    # Initialize the list of results from the select statement
    # Each row of the list will contain a data dictionary of the results
    result_list = []
    # Loop through returned rows
    for row_idx in range(len(rows_list)):
        # Loop through columns
        data_dict = {}  # Initialize data dictionary for the row
        for col_idx in range(len(c.description)):
            data_dict[c.description[col_idx][0]] = rows_list[row_idx][col_idx]
        result_list.append(data_dict)

    # Close the connection
    conn.close()

    # Return the list of rows
    return result_list

def database_selectwhere_table(database, table, where_close, data):
    """
    Function that reads a table of the SQLite database with a where close
    and returns selected rows.

    :param database: name of the database
     :type database: str
    :param table: name of the table from which to select data
     :type table: str
    :param where_close: the where statement to be used to select data
     :type where_close: str
    :param data: the value of the data to use in the where close
     :type data: list

    :return result_list: list of data dictionary with results of the select
    statement
      :type result_list: list

    """


    # Create select query
    selectwhere_query = """
        SELECT *
        FROM
    """
    selectwhere_query = selectwhere_query + " " + table + " " + where_close

    # Connect to the database
    conn = sqlite3.connect(database)
    c    = conn.cursor()

    # Execute the query and get the results in the list rows_list
    c.execute(selectwhere_query, data)
    rows_list = c.fetchall()

    # Initialize the list of results from the select statement
    # Each row of the list will contain a data dictionary of the results
    result_list = []
    # Loop through returned rows
    for row_idx in range(len(rows_list)):
        data_dict = {}  # Initialize data dictionary for the row
        # Loop through columns
        for col_idx in range(len(c.description)):
            data_dict[c.description[col_idx][0]] = rows_list[row_idx][col_idx]
        result_list.append(data_dict)

    # Close the connection
    conn.close()

    # Return the data dictionary with column names and values
    return result_list

def database_update_table(database, table, update_fields, where_fields, data):

    # Create update query
    update_query = "UPDATE "  + table + \
                    " SET "   + update_fields + \
                    " WHERE " + where_fields

    # Connect to the database
    conn = sqlite3.connect(database)
    c    = conn.cursor()

    # Execute the query and get the results in the list rows_list
    c.execute(update_query, data)

    # Commit the change and close the connection
    conn.commit()
    conn.close()


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
            (ProjectID          INTEGER,
             VisitLabel         TEXT     NOT NULL,
             VisitRank          INTEGER,
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
             VisitTime     TEXT,
             VisitLocation TEXT,
             VisitWithWhom TEXT,
             VisitStatus   TEXT
            )
    '''

    # Create the tables
    database_execute(database, create_project_table_query,       None)
    database_execute(database, create_visit_windows_table_query, None)
    database_execute(database, create_candidate_table_query,     None)
    database_execute(database, create_session_table_query,       None)

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
            (ProjectID,      VisitLabel,     VisitRank,
             WindowMinDays,  WindowMaxDays
            )
            VALUES (?, ?, ?,
                    ?, ?
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

def save_visit_data(database, data):
    """
    Function that saves visit's information in the SQLite database.

    :param database: name of the database
     :type database: str
    :param data: if defined, the data to use to execute the statement
     :type data: list

    """

    # Create the insert query
    insert_session_query = '''
        INSERT INTO session
            (CandID,        VisitLabel, ProjectID,
             VisitDate,     VisitTime,  VisitLocation,
             VisitWithWhom, VisitStatus
            )
            VALUES (?, ?, ?,
                    ?, ?, ?,
                    ?, ?
                   )
    '''

    # Execute insert query with values stored in data
    if (isinstance(data[0], tuple)):
        database_executemany(database, insert_session_query, data)
    else:
        database_execute(database, insert_session_query, data)

def fetch_projectID(database, projectname):
    """
    Function that fetch candidate's information in the candidate table
    based on the PSCID given as an argument

    :param database: name of the database to connect to
     :type database: str
    :param PSCID: PSCID of the candidate
     :type PSCID: str

    :return candidate_list[0]: dictionary with candidate's information
      :type candidate_list[0]: dict

    """

    project_list = database_selectwhere_table(database,
                                              "project",
                                              "WHERE Name = ?",
                                              (projectname,)
                                             )

    # Return the projectID

    return project_list[0]['ProjectID']

def fetch_candidate_info(database, pscid):
    """
    Function that fetch candidate's information in the candidate table
    based on the PSCID given as an argument

    :param database: name of the database to connect to
     :type database: str
    :param PSCID: PSCID of the candidate
     :type PSCID: str

    :return candidate_list[0]: dictionary with candidate's information
      :type candidate_list[0]: dict

    """

    where_data = (pscid,)
    candidate_list = database_selectwhere_table(database,
                                                "candidate",
                                                "WHERE PSCID = ?",
                                                where_data
                                               )

    # Return only the first row which corresponds to the data dictionary of
    # the candidate's information
    return candidate_list[0]





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

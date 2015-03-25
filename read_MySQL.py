import MySQLdb


def read():
    # Open database connection
    db = MySQLdb.connect("sql3.freemysqlhosting.net","sql371550","cE9*wE8*","sql371550")
    # Host, User, Password, Database

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    #cursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    #data = cursor.fetchone()

    # Drop table if it already exist using execute() method.
    cursor.execute("DROP TABLE IF EXISTS SENSORS_1")

    # Create table as per requirement
    sql = """CREATE TABLE SENSORS_1 (
             NODE_ID INT NOT NULL,
             STATE TINYINT)"""

    cursor.execute(sql)

    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO SENSORS_1(NODE_ID, STATE)
             VALUES (1001,1)"""
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM SENSORS_1"

    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       for row in results:
          node_id = row[0]
          state = row[1]
          # Now print fetched result
          print "NODE_ID: %d, STATE: %d" % \
                 (node_id,state)
    except:
       print "Error: unable to fecth data"

    # print "Database version : %s " % data

    # disconnect from server
    db.close()
    return (node_id,state)


if __name__ == "__main__":
    read()

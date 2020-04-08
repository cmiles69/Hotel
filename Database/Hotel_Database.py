#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# https://www.sqlitetutorial.net/sqlite-python
# https://www.youtube.com/watch?v=RaESMr2DnGM -> Captain D.j Oamen
# 45:00, 52:08, 55:08, 1:00:18

# Craig Miles -> cmiles69@hushmail.com

import sqlite3

db_file = ( r'/home/miles/Documents/Python/Hotel/hotel.sqlite3' )

def get_conn():
    con = None
    try:
        con = sqlite3.connect( db_file,
        detect_types = sqlite3.PARSE_COLNAMES | sqlite3.PARSE_DECLTYPES )
        print( conn )
        print( sqlite3.version )
        print( 'Successfull Connection!' )
        return con
    except sqlite3.Error as e:
        print( e )

def create_table( conn, sql_script ):
    ''' Create a database table from an sql statement'''

    try:
        db_cursor = conn.cursor()
        db_cursor.execute( sql_script )
        print( 'Create booking table success!' )
    except sqlite3.Error as e:
        print( e ) 

def create_hotel_booking_table():
    ''' Create entire Hotel database including tables '''

    sql_create_hotel_booking_table = '''CREATE TABLE IF NOT EXISTS booking(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Customer_ID TEXT NOT NULL,
                                Firstname   TEXT NOT NULL,
                                Surname     TEXT NOT NULL,
                                Address     TEXT NOT NULL,
                                Gender      TEXT,
                                Mobile      TEXT,
                                Nationality TEXT,
                                Type_Of_ID  TEXT,
                                DateIn      TEXT,
                                DateOut     TEXT,
                                Email       TEXT );'''

    # Create a database connection.
    conn = get_conn()

    # Create tables
    if conn is not None:
        # Create Hotel table
        create_table( conn, sql_create_hotel_booking_table )
        conn.commit()
        conn.close()

    else:
        print( 'Error!, Cannot create the database connection!' )
        conn = None

def insert_hotel_booking( conn, booking ):
    ''' Insert a new Hotel booking into the booking table '''

    sql_booking = ''' INSERT INTO booking(Customer_ID,
                                          Firstname,
                                          Surname,
                                          Address,
                                          Gender,
                                          Mobile,
                                          Nationality,
                                          Type_Of_ID,
                                          DateIn,
                                          DateOut,
                                          Email)
                      VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    db_cursor = conn.cursor()
    db_cursor.executemany( sql_booking, booking )
    conn.commit()
    db_cursor.close()
    conn.close()
    return db_cursor.lastrowid

#     # insert multiple records using the more secure "?" method
# albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
#           ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
#           ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
#           ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
# cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
# conn.commit()

def view_hotel_booking_record():
    conn = get_conn()
    db_cursor = conn.cursor()
    db_cursor.execute( 'SELECT * FROM booking' )
    table_data = db_cursor.fetchall()
    db_cursor.close()  # No conn.commit() needed here. Only viewing.
    conn.close()
    return table_data

def delete_hotel_booking_record( id ):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute( '''DELETE FROM booking WHERE id = ?''', ( id, ) )
    conn.commit()
    cursor.close()
    conn.close()

def search_hotel_booking_record( Customer_ID,
                                 Firstname,
                                 Surname,
                                 Address,
                                 Gender,
                                 Mobile,
                                 Nationality,
                                 Type_Of_ID,
                                 DateIn,
                                 DateOut,
                                 Email):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.executemany( '''SELECT * FROM booking WHERE
                           Customer_ID = ? OR
                           Firstname   = ? OR
                           Surname     = ? OR
                           Address     = ? OR
                           Gender      = ? OR
                           Mobile      = ? OR
                           Nationality = ? OR
                           Type_Of_ID  = ? OR
                           DateIn      = ? OR
                           DateOut     = ? OR
                           Email       = ?''' )
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return items

def update_hotel_booking_record( id, booking_data ):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.executemany( ''' UPDATE booking SET
                           Customer_ID = ?,
                           Firstname   = ?,
                           Surname     = ?,
                           Address     = ?,
                           Gender      = ?,
                           Mobile      = ?,
                           Nationality = ?,
                           Type_Of_ID  = ?,
                           DateIn      = ?,
                           DateOut     = ?,
                           Email       = ?
                        WHERE id       = ?''',
                        booking_data, ( id, ) )
    conn.commit()
    cursor.close()
    conn.close()
if __name__ == '__main__':
    pass

    #create_hotel_booking_table()
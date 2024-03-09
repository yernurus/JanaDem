import sqlite3

with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    
    # query = """ CREATE TABLE IF NOT EXISTS Users(
    #     user_id INTEGER PRIMARY KEY,
    #     first_name TEXT NOT NULL,
    #     second_name TEXT NOT NULL,
    #     phone_number INTEGER NULL,
    #     email TEXT DEFAULT "@mail.ru",
    #     user_type TEXT NOT NULL, 
    #     password TEXT NOT NULL,
    #     account_created_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    #     profile_pic BLOB NULL
    #     ) """
    # cursor.execute(query)
    query = """ CREATE TABLE IF NOT EXISTS Issues(
        issue_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT Default 1,
        images BLOB NULL,
        user_id INTEGER,
        location_id INTEGER FOREIGN KEY REFERENCES Locations(location_id), 
        district_name INTEGER FOREIGN KEY REFERENCES District(district_id),
        issue_created_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        ) """
    cursor.execute(query)
    
    
    
    # Drop table
    # query = "Drop table Users"
    # cursor.execute(query)
    
    # query = """ INSERT INTO Users (user_id, first_name, second_name, phone_number, email, user_type, password, account_created_time, profile_pic)
    # VALUES(2, "Dias", "Aziz", 87777752535, "azizdias@mail.ru", "Citizen", "diasaziz00", '09-03-24',NULL
    # ) """
    # cursor.execute(query)
    # db.commit()
    
    # Delete row
    # query = """ delete from Users where user_id=2 """
    # cursor.execute(query)
    # db.commit()
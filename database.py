import sqlite3

with sqlite3.connect('db2.sqlite3') as db:
    cursor = db.cursor()
    
    query = """ CREATE TABLE IF NOT EXISTS Users(
        user_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        second_name TEXT NOT NULL,
        phone_number INTEGER NULL,
        email TEXT DEFAULT "@mail.ru",
        user_type TEXT NOT NULL, 
        password TEXT NOT NULL,
        account_created_time TIMESTAMP,
        profile_pic BLOB NULL
        ) """
    cursor.execute(query)
    
    query2 = """ CREATE TABLE IF NOT EXISTS Issues(
        issue_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT Default 1,
        issue_type TEXT,
        user_id INTEGER,
        location_id INTEGER , 
        district_name INTEGER ,
        issue_created_time TIMESTAMP,
        images BLOB NULL,
        FOREIGN KEY (user_id) REFERENCES User(user_id),
        FOREIGN KEY (location_id) REFERENCES Location(location_id),
        FOREIGN KEY (district_name) REFERENCES District(district_name)
        ) """
    cursor.execute(query2)
    
    query3 = """ CREATE TABLE IF NOT EXISTS Rating(
        rating_id INTEGER PRIMARY KEY,
        rating_value TEXT NOT NULL,
        timestamp TIMESTAMP,
        images BLOB NULL,
        district_id INTEGER,
        FOREIGN KEY (district_id) REFERENCES District(district_id)
        ) """
    cursor.execute(query3)
    
    query4 = """ CREATE TABLE IF NOT EXISTS District(
        district_id INTEGER PRIMARY KEY,
        district_name TEXT NOT NULL
        ) """
    cursor.execute(query4)
    
    query5 = """ CREATE TABLE IF NOT EXISTS Location(
        location_id INTEGER PRIMARY KEY,
        location_name TEXT NOT NULL,
        district_name TEXT,
        street TEXT NOT NULL,
        house_number INTEGER,
        district_id INTEGER,
        FOREIGN KEY (district_id) REFERENCES District(district_id)
        ) """
    cursor.execute(query5)
    
    query6 = """ CREATE TABLE IF NOT EXISTS PhotoReport(
        report_id INTEGER PRIMARY KEY,
        images BLOB NULL,
        description TEXT NOT NULL,
        timestamp TIMESTAMP,
        issue_id INTEGER,
        akims_id INTEGER,
        FOREIGN KEY (issue_id) REFERENCES Issue(issue_id),
        FOREIGN KEY (akims_id) REFERENCES Akims(akims_id)
        ) """
    cursor.execute(query6)
    
    query7 = """ CREATE TABLE IF NOT EXISTS Akims(
        akims_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone_number INTEGER,
        email TEXT NOT NULL,
        region TEXT NOT NULL,
        position TEXT NOT NULL
        ) """
    cursor.execute(query7)
    
    query8 = """ CREATE TABLE IF NOT EXISTS Civic_Engagement_History(
        record_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        action TEXT NOT NULL,
        points_earned INTEGER,
        progress boolean,
        timestamp TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES User(user_id)
        ) """
    cursor.execute(query8)

    
    query = """ INSERT INTO Users (user_id, first_name, second_name, phone_number, email, user_type, password, account_created_time, profile_pic)
    VALUES(1, "Dias", "Aziz", 87777752535, "azizdias@mail.ru", "Citizen", "diasaziz00", '14-03-24',NULL
    );
    INSERT INTO Users
    VALUES(2, "Almas", "Kokenov", 87712541444, "kokenovalmas@mail.ru", "Akim", "kokenalmas00", '14-03-24',NULL
    );
    """
    cursor.executescript(query)
    db.commit()
    
    query = """
    INSERT INTO Users
    VALUES(4, "Abzal", "Yegemberdiyev", +77272020205, "yegemberdiyevabzal@mail.ru", "Akim", "abzalyegemberdi00", '13-03-2024',NULL
    );
    INSERT INTO Akims
    VALUES(2, "Abzal", +77272020205, "yegemberdiyevabzal@mail.ru", "Auezov", "Akim"
    );
    INSERT INTO Civic_Engagement_History
    VALUES(2, 2, "Issue", 4, "In Process", '13-03-2024'
    );
    INSERT INTO District
    VALUES(2, "Auezov"
    );
    INSERT INTO Issues
    VALUES(2, "Turned off light","There is a turned off light",'In process', "Road issue", 1, 1, "Auezov", "13-03-2024 14:00:00", Null
    );
    INSERT INTO Location
    VALUES(2, "Almaty", "Auezov", "Zhetisu-2", 50, 2
    );
    INSERT INTO PhotoReport
    VALUES(2, Null, "We fixed the light", '14-03-2024', 2, 2
    );
    INSERT INTO Rating
    VALUES(2, "4.5", '14-03-2024',Null, 2 
    );
    """
    cursor.executescript(query)
    db.commit()
    
    query = """
    INSERT INTO Users
    VALUES(3, "Aidar", "Zhakibayev", +77272020202, "zhakibayevaidar@mail.ru", "Akim", "aidarzhakibai00", '13-03-2024',NULL
    );
    INSERT INTO Akims
    VALUES(1, "Aidar", +77272020202, "zhakibayevaidar@mail.ru", "Almaly", "Akim"
    );
    INSERT INTO Civic_Engagement_History
    VALUES(1, 1, "Isuue", 4, "In Process", '13-03-2024'
    );
    INSERT INTO District
    VALUES(1, "Almaly"
    );
    INSERT INTO Issues
    VALUES(1, "Pothole on the road","There is a hole in the road with an area of 1 sq.m. ",'In process', "Road issue", 1, 1, "Almaly", "13-03-2024 12:00:00", Null
    );
    INSERT INTO Location
    VALUES(1, "Almaty", "Almaly", "Tole Bi", 159, 1
    );
    INSERT INTO PhotoReport
    VALUES(1, Null, "We fixed the hole", '14-03-2024', 1, 1
    );
    INSERT INTO Rating
    VALUES(1, "4", '14-03-2024',Null, 1 
    );"""
    cursor.executescript(query)
    db.commit()
    
    # Delete row
    # query = """ delete from Users where user_id=2 """
    # cursor.execute(query)
    # db.commit()
    
    # Drop table
    # query = "Drop table Users"
    # cursor.execute(query)
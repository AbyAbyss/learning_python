import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")

#create_table()  after creating table leave it..no need to run it each time..there will be errors

def enter_data():
    #make sure u create table first
    c.execute("INSERT INTO example VALUES('Python', 2.7, 'Beginner')")
    c.execute("INSERT INTO example VALUES('Python', 3.3, 'Intermediate')")
    c.execute("INSERT INTO example VALUES('Python', 3.6, 'Expert')")
    conn.commit()

#enter_data()   can use

def enter_dynamic_data():
    lang = input("What language? ")
    version = input("version? ")
    skill = input("What skill level? ")
    
    c.execute("INSERT INTO example (Language, Version, Skill) VALUES (?, ?, ?)", (lang, version, skill))
    
    conn.commit()




def read_from_database():
    sql = "SELECT * FROM example"
    #sql = "SELECT * FROM example LIMIT 2"
    #sql = "UPDATE example SET Skill = 'Expert' WHERE Skill = 'expert'"
    #for update/delet no need of "for"
    #c.execute(sql)
    #conn.commit() #MUST WRITE THIS TO SAVE THE UPDATE
    #sql = "SELECT * FROM example WHERE Skill == 'Beginner'"
    
    #what_skill = input("What skill level are we looking for? ")
    #what_language = input("What language?: ")
    #sql = "SELECT * FROM example WHERE Skill = ? AND Language = ?"
    #sql = "SELECT * FROM example" #testing UPDATE

    for row in c.execute(sql):  # for row in c.execute(sql,[(what_skill), (what_language)]):
        print(row)
        #print(row[0])
    print(20*"#")

#for update
    sql = "UPDATE example SET Skill = 'Expert' WHERE Skill = 'Beginner'"
    c.execute(sql)
    conn.commit();






#for deleting
    sql = "DELETE FROM example WHERE Skill = 'Intermediate'"
    c.execute(sql)
    conn.commit() #will save the CHANGES
    sql = "SELECT * FROM example"
    for row in c.execute(sql):  
        print(row)

    



#enter_dynamic_data()

read_from_database()
conn.close()


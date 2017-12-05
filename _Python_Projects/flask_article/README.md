# Python_Flask_APP
Article App build with flask...

Step 1: Create Database "article_app" in MySQL
			code:
				CREATE DATABASE article_app;
				USE article_app;

Step 2: Create two tables, "users" and "articles"

			
			    CREATE TABLE users (id INT(11) AUTO_IMCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100), username VARCHAR(30), password VARCHAR(100), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
			    DESCRIBE users;
				
			  
			    CREATE TABLE articles (id INT(11) AUTO_IMCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(100), body TEXT, create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
			    DESCRIBE articles;
				
Step 3: Run the app.py file
			code:
				$ python app.py
				
				
NOTE: make sure to change your MySQL username and password in app.py
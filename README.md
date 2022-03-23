# Book_Journal_Project-Using-Flask-
Web based Book Journaling - TAKS

Login Page
- Login with email and password (if user already exists) - DONE
- Authenticate the user login - DONE

Sign up
- Sign up new users with email, username, password, confirm password - DONE
- Check if the user already exist - DONE
- Check and confirm password - DONE
- Hash the password - DONE
- Set length/limit to each field or throw an error - DONE

Home
- Display only home and logout options after login was successful - DONE
- List the menus - List of Books read, currently reading list, Wishlist, summary section (results of analysis or status of what has been read so far)  - DONE
- Display the username once logged in - DONE
- Display last logged in timestamp 

Read
- Option to add books (book title, author name, rating) - DONE
- Set conditions - if book already exists, title & author name should not be empty - DONE
- condition / Check on already existing book - case sensitive, string search, etc
- Display the added books in table format - DONE
- Add option to update and delete records or individual books - DONE
- Add a serial number or number each rows - DONE
- Update the row number automatically when records are deleted - DONE
- Add start date and end date for book - for later analysis
- Add scroll bar for the table
- Add review column for books (review should be optional - column accepts null value)
- Add Genre column (get the info from goodreads based on book title) 
- change the way of adding books to the list - type in the book title and get other information from goodreads website
- Display rating as stars(pic or symbol)
- Add option to indicate - listened in Audiobooks or physically read
- Set a reading goal (yearly/ monthly )
- Add option to select multiple rows or select all and perform an action (delete)

Currently Reading
- Add books (get the info from goodreads website based on book title)
- option to Move books from Wishlist
- When to the list, use current date as starting date (for reading)
- ‘Finished’ button - to add end-date and move the book to read list
- Add rating 
- Add review(optional)
- Add ‘DNF’ button

Wishlist
- Add, delete, update books
- Option to move books to currently reading list
- Add ‘priority’ or ‘wish to read next’ option - automatically move to currently reading
- Option to look for new releases each month and add to the Wishlist based on conditions (genera, authors popularity, recommendation based on other readers)

Summary / Report
- Perform analysis and display the results in the form of dynamic dashboards
- No of books read (period = weekly, monthly)
- Group by books on rating, genre, author
- Series finished
- Comparison - audiobooks vs physical books
- How long to read, popularity of books vs number of reviews from other readers, 
- Based on analysis influence the Wishlist in future (automatically choose or recommend books based on analysis)
- Analysis - whether to improve reading time

- Trigger a email or message, if no activity for certain period
- Deploy the flask application on a server


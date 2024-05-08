# BOOK MANAGEMENT SYSTEM (DJANGO REST API's)

This project is a Django REST Framework API for managing books, authors, reading lists, and more. It allows you to create, retrieve, update, and delete book-related data using RESTful APIs.

## Setup

### Activate Virtual Environment

#### Linux

```
python3 -m venv env 
source env/bin/activate
```

#### Windows

```
python -m venv env 
env\Scripts\activate
```

### Install Dependencies

```
pip install -r requirements.txt
```

### Run Migrations

```
python manage.py makemigrations 
python manage.py migrate
```

### Start Development Server

```
python manage.py runserver
```

## API Documentation

### Accounts

#### POST /apiauth/register/

THIS END POINT USE FOR CREATION OF A USER ACCOUNT

```
curl --location 'localhost:8000/apiauth/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"test",
    "username":"test",
    "email":"test@gmail.com",
    "password":"password1@"
}'
```

#### POST /apiauth/token/

THIS END POINT USE TO GENERATE JWT ACCESS TOKEN

```
curl --location 'localhost:8000/apiauth/token/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"test",
    "email":"test@gmail.com",
    "password":"password1@"
}'
```

IN CONTINUATION TTO THIS I ALSO HAVE CREATED A REFRESH TOKEN END POINT.

VISIT JWT WEBSITE FOR MORE INFORMATION HOW WE CAN USE IT AND MAKE EFFECIENT USE OF IT IN FRONT END INTEGRATION, THE END POINT OF REFRESH TOKEN IS :-

#### POST /apiauth/token/refresh

#### POST /apiauth/login/

THIS END POINT CAN BE USED TO SHOW A LOGIN OF AN USER

TO USE THIS END POINT WE NEED TO PUT THE JWT TOKEN OF A USER AS A BEARER TOKEN IN HEADED AS A AUTHENTICATION PURPOSE

```
curl --location 'localhost:8000/apiauth/login/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MTU3NjE0LCJpYXQiOjE3MTQxNTU4MTQsImp0aSI6IjBlYmU1M2YyODg1MTQ1MGNiNzYzZDA2ZmNjNWEzZGY5IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJrYXVzaGlrZG9sdWk0IiwiZW1haWwiOiJrYXVzaGlrZG9sdWk0QGdtYWlsLmNvbSJ9.KdZt1541u7lv5EQcbJBrSpMn8AfSfJF8bde2C5f9Su4' \
--data-raw '{
    "email":"kaushikdolui4@gmail.com",
    "username":"kaushikdolui4",
    "password":"password1@"
}'
```

#### GET /apiauth/userjwt

THIS END POINT CAN BE USE TO GET THE DETAILS OF A USER USING JWT TOKEN

```
curl --location 'localhost:8000/apiauth/userjwt/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MTU3NjE0LCJpYXQiOjE3MTQxNTU4MTQsImp0aSI6IjBlYmU1M2YyODg1MTQ1MGNiNzYzZDA2ZmNjNWEzZGY5IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJrYXVzaGlrZG9sdWk0IiwiZW1haWwiOiJrYXVzaGlrZG9sdWk0QGdtYWlsLmNvbSJ9.KdZt1541u7lv5EQcbJBrSpMn8AfSfJF8bde2C5f9Su4'
```

#### POST /apiauth/logout/

THIS END POINT CAN BE USE TO LOGOUT OF AN USER

```
curl --location --request POST 'localhost:8000/apiauth/logout/' \
--data ''
```

#### GET /apiauth/accounts/

RETRIEVE THE LIST OF ALL USERS

```
curl --location 'localhost:8000/apiauth/accounts/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjI5NTg0LCJpYXQiOjE3MTQyMjc3ODQsImp0aSI6ImIzMWVhZTRkNjY3NTRhYjViYjIwNjhkNzZjMGIwZGZjIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSJ9.8Fk4yWXhoeU0922XlzJ-7fiIU2g-idX9TNsSi4P8fmk' \
--data ''
```

#### GET /apiauth/account/[int:id](int:id)/

THIS END POINT GIVES A DETAIL INFO ABOUT THE USER BASED ON THE ID

```
curl --location 'localhost:8000/apiauth/account/1/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MTU3NjE0LCJpYXQiOjE3MTQxNTU4MTQsImp0aSI6IjBlYmU1M2YyODg1MTQ1MGNiNzYzZDA2ZmNjNWEzZGY5IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJrYXVzaGlrZG9sdWk0IiwiZW1haWwiOiJrYXVzaGlrZG9sdWk0QGdtYWlsLmNvbSJ9.KdZt1541u7lv5EQcbJBrSpMn8AfSfJF8bde2C5f9Su4'
```

#### PUT /apiauth/account/[int:id](int:id)/update/

THIS END POINT USE FOR UPDATE OF USER DATA BASED ON THE ID

```
curl --location --request PUT 'localhost:8000/apiauth/account/1/update/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "kaushik",
    "username": "kaushik_dolui",
    "email": "kaushikdolui4@gmail.com",
    "password": "password1@"
}'
```

#### DELETE /apiauth/account/[int:id](int:id)/delete/

THIS END POINT USE FOR DELETION  OF USER DATA BASED ON THE ID

### Authors

#### POST /books/authors/create/

THIS END POINT USE FOR CREATION OF AN AUTHOR

```
curl --location 'localhost:8000/books/author/create/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjM0MjM4LCJpYXQiOjE3MTQyMzI0MzgsImp0aSI6ImFhMjc0NjNmYTk2MzQxZDFhYmE0NTFhMjk1NzVkZmQ0IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSJ9.XYwXW2BZ7Ep2u3uaHyOMhSXM6KhkjQ9Vjqt64wqbt-Y' \
--data '{
    "name":"kaushik"
}'
```

#### POST /books/author/update/[int:id](int:id)/

THIS END POINT IS USE TO UPDATE AN EXISTING AUTHOR

```
curl --location --request PUT 'localhost:8000/books/author/update/1/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjM0MjM4LCJpYXQiOjE3MTQyMzI0MzgsImp0aSI6ImFhMjc0NjNmYTk2MzQxZDFhYmE0NTFhMjk1NzVkZmQ0IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSJ9.XYwXW2BZ7Ep2u3uaHyOMhSXM6KhkjQ9Vjqt64wqbt-Y' \
--data '{
    "name":"kaushik dolui"
}'
```

#### DELETE /books/author/delete/[int:id](int:id)/

THIS END POINT IS USE TO DELETE AN AUTHOR

```
curl --location --request DELETE 'localhost:8000/books/author/delete/1/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjM0MjM4LCJpYXQiOjE3MTQyMzI0MzgsImp0aSI6ImFhMjc0NjNmYTk2MzQxZDFhYmE0NTFhMjk1NzVkZmQ0IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSJ9.XYwXW2BZ7Ep2u3uaHyOMhSXM6KhkjQ9Vjqt64wqbt-Y' \
--data ''
```

### Books

#### GET /books/booklist/

Retrieve a list of all books.

```
curl --location 'localhost:8000/books/booklist/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjM0MjM4LCJpYXQiOjE3MTQyMzI0MzgsImp0aSI6ImFhMjc0NjNmYTk2MzQxZDFhYmE0NTFhMjk1NzVkZmQ0IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSJ9.XYwXW2BZ7Ep2u3uaHyOMhSXM6KhkjQ9Vjqt64wqbt-Y'
```

#### POST /books/create/

Create a new book.

```
curl --location 'localhost:8000/books/create/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjM0MjM4LCJpYXQiOjE3MTQyMzI0MzgsImp0aSI6ImFhMjc0NjNmYTk2MzQxZDFhYmE0NTFhMjk1NzVkZmQ0IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSJ9.XYwXW2BZ7Ep2u3uaHyOMhSXM6KhkjQ9Vjqt64wqbt-Y' \
--form 'title="testing book"' \
--form 'authors="2"' \
--form 'genre="Dystopian"' \
--form 'publication_date="1949-06-08"' \
--form 'description="\"A dystopian social science fiction novel by George Orwell.\""' \
--form 'book_file=@"/home/panda/Downloads/kaushik_dolui_resume.pdf"'
```

#### GET /books/booklist/[int:id](int:id)/

Retrieve details of a specific book.

```
curl --location 'localhost:8000/books/booklist/2/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjMyMDc1LCJpYXQiOjE3MTQyMzAyNzUsImp0aSI6ImFkYmNkY2Y1ZTgwNTRhZmFiMjUyNGJmNjMwNWE0ZDdjIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSJ9.plmPplhIGG-Bh_ukDMSa9Dbh5AiYQufBtl8JZkL9f-g'
```

#### PUT /books/update/[int:id](int:id)/

Update an existing book.

```
curl --location --request PUT 'localhost:8000/books/update/1/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjM2MzEzLCJpYXQiOjE3MTQyMzQ1MTMsImp0aSI6IjBkNzRlNDE0OTUxNTQ4MmQ4ZmVjZDU1ZmZkNTc2ZTMxIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSJ9.XI_XBDRCHqZBeII_PkQdxalmAy3EpIB2i3utCF87mSw' \
--form 'title="testing book"' \
--form 'authors="2"' \
--form 'genre="Dystopian"' \
--form 'publication_date="1949-06-08"' \
--form 'description="A dystopian social science fiction novel by George Orwell."' \
--form 'book_file=@"/home/panda/Downloads/kaushik_dolui_resume.pdf"'
```

#### DELETE /books/delete/[int:id](int:id)/

Delete a book.

```
curl --location --request DELETE 'localhost:8000/books/delete/1/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjMyMDc1LCJpYXQiOjE3MTQyMzAyNzUsImp0aSI6ImFkYmNkY2Y1ZTgwNTRhZmFiMjUyNGJmNjMwNWE0ZDdjIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSJ9.plmPplhIGG-Bh_ukDMSa9Dbh5AiYQufBtl8JZkL9f-g' \
--data ''
```

### Reading Lists

#### POST /books/reading-lists/

Create a new reading list.

```
curl --location 'localhost:8000/books/reading-lists/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjM2MzEzLCJpYXQiOjE3MTQyMzQ1MTMsImp0aSI6IjBkNzRlNDE0OTUxNTQ4MmQ4ZmVjZDU1ZmZkNTc2ZTMxIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSJ9.XI_XBDRCHqZBeII_PkQdxalmAy3EpIB2i3utCF87mSw' \
--data '{
    "name": "My Reading List",
    "books": [1,2,3,4]
}'
```

#### GET /books/reading-lists/[int:id](int:id)/

Retrieve details of a specific reading list.

```
curl --location 'localhost:8000/books/reading-lists/3/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjM4NjE5LCJpYXQiOjE3MTQyMzY4MTksImp0aSI6IjM5ZTk2OGYzMWVkNDRiNThhYTFmN2I2YzU1ODNkMGUzIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSJ9._COJqBT7BXb-W94MGGkdrXEmPK5U9H7BaHbmRJeffSk' \
--data ''
```

#### PUT /books/reading-lists/[int:id](int:id)/

Update an existing reading list.

```
curl --location --request PUT 'localhost:8000/books/reading-lists/3/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjM4NjE5LCJpYXQiOjE3MTQyMzY4MTksImp0aSI6IjM5ZTk2OGYzMWVkNDRiNThhYTFmN2I2YzU1ODNkMGUzIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSJ9._COJqBT7BXb-W94MGGkdrXEmPK5U9H7BaHbmRJeffSk' \
--data '{
    "name": "My Reading List",
    "books": [4,3,2,1]
}'
```

#### DELETE /books/reading-lists/[int:id](int:id)/

Delete a reading list.

```
curl --location --request DELETE 'localhost:8000/books/reading-lists/2/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjM2MzEzLCJpYXQiOjE3MTQyMzQ1MTMsImp0aSI6IjBkNzRlNDE0OTUxNTQ4MmQ4ZmVjZDU1ZmZkNTc2ZTMxIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSJ9.XI_XBDRCHqZBeII_PkQdxalmAy3EpIB2i3utCF87mSw' \
--data ''
```

## Additional Features

* User authentication and authorization using JWT
* File uploads for book files
* Media file config
* Documentation of API'S

Feel free to explore the codebase

## Contact info

#### Email - [kaushikdolui4@gmail.com](kaushikdolui4@gmail.com "Email id")

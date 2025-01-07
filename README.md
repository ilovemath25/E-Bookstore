| Name       | Student ID  |
|------------|-------------|
| 楊君威    | 111590059   |
| 陳軒元    | 111590058   |
| 鄭秀心    | 111590060   |
| 黃音慈    | 110830009   |
| 楊建璋    | 111590057   |
| 李其灝    | 111590062   |


**Set up database**

-> Install PostgreSQL and Pg Admin 4

-> Set up user and port number

-> Create database

-> Right click the database and select `Query Tool`

-> Execute SQL statements in files `DB_table.sql` and `DB_testdata.sql`

**Set up environment**

->Run in terminal `pip install -r requirements.txt`

**Adjust "run.py"**

-> change user, password, db, and port according created server

-> Run in terminal `py run.py`

-> open the local generated link in browser

File structure :
```
├───ebookstore_flask
|   ├── models
|   |   ├── __init__.py
|   |   ├── credit_card.py
|   |   ├── discount.py
|   |   ├── item_line.py
|   |   ├── member.py
|   |   ├── order.py
|   |   ├── product.py
|   |   ├── review.py
|   |   ├── seasoning.py
|   |   ├── shipping.py
|   |   ├── shoppingCart_item.py
|   |   └── special_event.py
|   ├── routes
|   |   └── ... .py
|   ├── static
|   |   ├── script
|   |   |   └── ... .js
|   |   ├── style
|   |   |   ├── nunito
|   |   |   |   └── ... .ttf
|   |   |   └── ... .css
|   ├── templates
|   |   ├── admin
|   |   |   └── ... .html
|   |   ├── login
|   |   |   └── ... .html
|   |   ├── staff
|   |   |   └── ... .html
|   |   ├── user
|   |   |   └── ... .html
|   ├── utils
|   |   ├── credit_card.py
|   |   ├── role.py
|   |   ├── search.py
|   |   ├── session.py
|   |   └── sessions.json
|   └── __init__.py
.gitignore
binlist.csv
DB_table.sql
DB_testdata.sql
README.md
run.py
```

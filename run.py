from ebookstore_flask import create_app
POSTGRES = {
   'user':'postgres',
   'password':'haloinibv',
   'db':'e-bookstore',
   'host':'localhost',
   'port':'5432',
}
app = create_app(POSTGRES)
if __name__=='__main__':app.run(host='0.0.0.0', debug=True, port=5001)

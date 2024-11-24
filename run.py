from ebookstore_flask import create_app
POSTGRES = {
   'user':'postgres',
   'password':'ilovemath25',
   'db':'ebookstore',
   'host':'localhost',
   'port':'5432',
}
app = create_app(POSTGRES)
if __name__=='__main__': app.run(debug=True, port=5000)
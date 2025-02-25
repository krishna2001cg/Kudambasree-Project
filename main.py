from flask import Flask
#from public import public
from admin import admin





app=Flask(__name__)
app.secret_key="hello"

#mail=Mail(app)
#app.config['MAIL_SERVER']='smtp.gmail.com'
#app.config['MAIL_PORT'] = 587
#app.config['MAIL_USERNAME'] = 'projectsriss2020@gmail.com'
#app.config['MAIL_PASSWORD'] = 'messageforall'
#app.config['MAIL_USE_TLS'] = False
#app.config['MAIL_USE_SSL'] = True

#app.register_blueprint(public)
app.register_blueprint(admin,url_prefix="/admin")
#app.register_blueprint(bank,url_prefix="/bank")
#app.register_blueprint(employee,url_prefix="/employee")
#app.register_blueprint(customer,url_prefix="/customer")


app.run(debug=True,port=5180)
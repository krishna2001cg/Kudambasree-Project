from flask import *
from database import *

public=Blueprint('public',__name__)


@public.route('/')
def home():
	return render_template("home.html")

@public.route('/login',methods=['get','post'])
def login():
	if 'login' in request.form:
		username=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']
			usertype=res[0]['usertype']
			if usertype=="admin":
				return redirect(url_for('admin.adminhome'))
			elif usertype=="bank":
				q="select * from bank where login_id='%s'"%(session['lid'])
				res=select(q)
				session['bid']=res[0]['bank_id']
				session['bankname']=res[0]['bankname']
				return redirect(url_for('bank.bankhome'))
			elif usertype=="employee":
				q="select *,bank.login_id as bid,CONCAT(`firstname`,' ',`lastname`) AS empname from employee inner join bank using(bank_id) where employee.login_id='%s'"%(session['lid'])
				res=select(q)
				session['eid']=res[0]['employee_id']
				session['bbid']=res[0]['bank_id']
				session['bids']=res[0]['bid']
				session['empname']=res[0]['empname']

				return redirect(url_for('employee.employeehome'))

			elif usertype=="customer":
				q="select *,CONCAT(`firstname`,' ',`lastname`) AS cname from customer where login_id='%s'"%(session['lid'])
				res=select(q)
				session['cid']=res[0]['customer_id']
				session['cname']=res[0]['cname']
				return redirect(url_for('customer.customerhome'))
		else:
			flash("invalid username and password")
	return render_template("login.html")


@public.route('/customerregister',methods=['get','post'])
def customerregister():
	if 'register' in request.form:
		# securitykey=request.form['securitykey']
		firstname=request.form['firstname']
		lastname=request.form['lastname']
		housename=request.form['housename']
		place=request.form['place']
		pincode=request.form['pincode']
		phone=request.form['phone']
		email=request.form['email']
		username=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		if res:
			flash("username and password already exists")
		else:
			q="insert into login values(null,'%s','%s','customer')"%(username,password)
			lid=insert(q)
			q="insert into customer values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,firstname,lastname,housename,place,pincode,phone,email)
			insert(q)
			return redirect(url_for('public.login'))
	return render_template("customerregister.html")
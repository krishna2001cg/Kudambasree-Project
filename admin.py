from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
	return render_template("adminhome.html")

@admin.route('/adminmanagebank',methods=['get','post'])
def adminmanagebank():
	data={}
	q="select * from bank"
	res=select(q)
	data['bank']=res

	if 'submit' in request.form:
		bankname=request.form['bankname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		username=request.form['username']
		password=request.form['password']
		q="insert into login values(null,'%s','%s','bank')"%(username,password)
		lid=insert(q)
		q="insert into bank values(null,'%s','%s','%s','%s','%s')"%(lid,bankname,place,phone,email)
		insert(q)
		return redirect(url_for('admin.adminmanagebank'))

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from login where login_id='%s'"%(id)
		delete(q)
		q="delete from bank where login_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.adminmanagebank'))

	if action=="update":
		q="select * from bank where login_id='%s'"%(id)
		res=select(q)
		data['banks']=res
	if 'update' in request.form:
		bankname=request.form['bankname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		q="update bank set bankname='%s',place='%s',phone='%s',email='%s' where login_id='%s'"%(bankname,place,phone,email,id)
		update(q)
		return redirect(url_for('admin.adminmanagebank'))

	return render_template("adminmanagebank.html",data=data)


@admin.route('/adminviewaccountandcustomers')
def adminviewaccountandcustomers():
	data={}
	q="SELECT *,`customer`.`place`AS customerplace,`customer`.`phone` AS customerphone,`bank`.`place`AS bankplace,`bank`.`phone`AS bankphone,`customer`.`email` AS customeremail,`bank`.`email` AS bankemail FROM account INNER JOIN customer USING(customer_id) INNER JOIN bank USING(bank_id)"
	res=select(q)
	data['accounts']=res
	return render_template("adminviewaccountandcustomers.html",data=data)

@admin.route('/adminviewloandetails')
def adminviewloandetails():
	data={}
	q="select * from loans inner join bank using(bank_id)"
	res=select(q)
	data['loans']=res
	return render_template("adminviewloandetails.html",data=data)


@admin.route('/adminviewaccounts')
def adminviewaccounts():
	data={}
	q="SELECT *,`customer`.`place`AS customerplace,`customer`.`phone` AS customerphone,`bank`.`place`AS bankplace,`bank`.`phone`AS bankphone,`customer`.`email` AS customeremail,`bank`.`email` AS bankemail FROM account INNER JOIN customer USING(customer_id) INNER JOIN bank USING(bank_id)"
	res=select(q)
	data['account']=res
	return render_template("adminviewaccounts.html",data=data)


@admin.route('/adminviewloanrequest')
def adminviewloanrequest():
	data={}
	q="SELECT *,`customer`.`place`AS customerplace,`customer`.`phone` AS customerphone,`bank`.`place`AS bankplace,`bank`.`phone`AS bankphone,`customer`.`email` AS customeremail,`bank`.`email` AS bankemail FROM `loanrequest` INNER JOIN `customer` USING(customer_id) INNER JOIN `loans` USING(loan_id) inner join bank using(bank_id)"
	res=select(q)
	data['request']=res
	return render_template("adminviewloanrequest.html",data=data)

@admin.route('/adminviewcomplaint')
def adminviewcomplaint():
	data={}
	q="select * from complaint inner join customer using(customer_id)"
	res=select(q)
	data['complaint']=res
	return render_template("adminviewcomplaint.html",data=data)


@admin.route('/adminsendreply',methods=['get','post'])
def adminsendreply():
	cid=request.args['cid']
	if 'send' in request.form:
		reply=request.form['reply']
		q="update complaint set reply='%s' where complaint_id='%s'"%(reply,cid)
		update(q)
		return redirect(url_for('admin.adminviewcomplaint'))
	return render_template("adminsendreply.html")




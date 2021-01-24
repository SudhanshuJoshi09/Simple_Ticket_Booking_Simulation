from flask import render_template, request, redirect, url_for
from app.models import Ticket
from app import app, db
from random import randint

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/store',methods=['POST', 'GET'])
def store():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        from1 = request.form['from1']
        to1 = request.form['to1']
        date = request.form['date']
        type1 = request.form['type1']
        count = request.form['count']
        class1 = request.form['class1']
        email = request.form['email']
        tel = request.form['tel']
        payment = request.form.getlist('payment')
        payment = payment[0]
        l = [fname, lname, from1, to1, date, type1, count, class1, email, tel, payment]

        pnr = randint(1000000000,10000000000)
        pnr_list = []
        for ele in Ticket.query.all():
            pnr_list.append(ele.pnr)
        while pnr in pnr_list:
            pnr = randint(1000000000,10000000000)

        try:
            try:
                db.session.add(Ticket(pnr=pnr, fname=fname, lname=lname, from1=from1, to1=to1, date=date, 
                                        type1=type1, count=count, class1=class1, email=email, 
                                        tel=tel, payment=payment))
                db.session.commit()
                return render_template('index.html',response = 'Ticked Booked Sucessfully')
            except:
                db.create_all()
                db.session.add(Ticket(pnr=pnr, fname=fname, lname=lname, from1=from1, to1=to1, date=date, 
                                        type1=type1, count=count, class1=class1, email=email, 
                                        tel=tel, payment=payment))
                db.session.commit()
                return render_template('index.html',response = 'Ticked Booked Sucessfully')
        except:
            return render_template('index.html',response = 'Something Went Wrong')
    elif request.method == 'GET':
        return render_template('index.html',response = '')


@app.route('/display',methods=['GET'])
def display():
    if request.method =='GET':
        resp = []
        for ele in Ticket.query.all():
            r = {}
            r['pnr'] = ele.pnr
            r['fname'] = ele.fname
            r['lname'] = ele.lname
            r['from1'] = ele.from1
            r['to1'] = ele.to1
            r['date'] = ele.date
            r['type'] = ele.type1
            r['count'] = ele.count
            r['class1'] = ele.class1
            r['email'] = ele.email
            resp.append(r)
        return render_template('display.html', resp=resp)


@app.route('/search',methods=['GET', 'POST'])
def search_pnr():
    if request.method == 'GET':
        return render_template('search.html')
    elif request.method == 'POST':
        pnr = request.form['pnr']
        if len(pnr) == 10:
            return redirect(url_for('ticket_result', pnr=pnr))
        else:
            return render_template('search.html', response='Enter a proper PNR Number')


@app.route("/result")
def ticket_result():
    pnr_no = request.args.get('pnr')
    pnr_no = int(pnr_no)
    resp = []
    for ele in Ticket.query.all():
        if ele.pnr == pnr_no:
            r = {}
            r['pnr'] = ele.pnr
            r['fname'] = ele.fname
            r['lname'] = ele.lname
            r['from1'] = ele.from1
            r['to1'] = ele.to1
            r['date'] = ele.date
            r['type'] = ele.type1
            r['count'] = ele.count
            r['class1'] = ele.class1
            r['email'] = ele.email
            resp.append(r)

    if not resp:
        return "Ticket not found"
    return render_template('display.html', resp=resp)
from asyncio.windows_events import NULL
from calendar import weekheader
from flask import Flask, request, json
from flask_mysqldb import MySQL


app = Flask(__name__)

#MySQL Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'a2censo'
mysql= MySQL(app)


@app.route ('/list_campanign', methods=['GET'])
def list_campanign():
    print('inicio lista')
    try:
        amount = request.form['amount']
    except:
        amount = None
    try:
        requested_Amount = request.form['requested_Amount']
    except:
        requested_Amount = None
    try:
        order = request.form['order']
    except:
        ordert = None
    cur = mysql.connection.cursor()
    query = 'SELECT * FROM campaign'
    select = ''
    where = ''
    if amount is not None:
        select +=  'amount'
        where += 'amount = '+str(amount)
    if requested_Amount is not None:
        select +=  ',requested_Amount'
        where += ' and requested_Amount = '+str(requested_Amount)
    if order is not None:
        if amount is not None or requested_Amount is not None:
            query += ' order by '+select+' '+ order
    print(query)
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
    )
    return response


@app.route('/add_campanign', methods=['POST'])
def add_campanign():
    print('iniciar')
    if request.method =='POST':
        name = request.form['name']
        amount = request.form['amount']
        requested_Amount = request.form ['requested_Amount']
        admin_Rate = request.form ['admin_Rate']
        cur = mysql.connection.cursor()
        query = "INSERT INTO campaign (name, amount, requested_Amount) VALUES ('%s', %s, %s)" % ( name, amount, requested_Amount )
        print(query)
        cur.execute(query)
        mysql.connection.commit()
        response = app.response_class(
            response=json.dumps({'msn':'creado'}),
            status=200,
            mimetype='application/json'
        )
        return response


if __name__ == '__main__':
    app.run(port = 5000, debug = True)
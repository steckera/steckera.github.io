import datetime, gspread, json
from oauth2client.service_account import ServiceAccountCredentials
from json import JSONEncoder, JSONDecoder
from flask import Flask, render_template, redirect, url_for, request, Response

# create the application object
app = Flask(__name__)

#Homepage

@app.route('/')
def welcome():
    return render_template('Homepage.html')  # render a template

#login to webpage

#route for handling the login page logic
@app.route("/login", methods=['GET', 'POST'])

def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('DisplayAllRows'))
    return render_template('login.html', error=error)

#Show inventory

@app.route("/index", methods=['GET','POST'])

def DisplayAllRows():
     
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
     
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("Inventory").sheet1

    #Deleting row using row number
    #sheet.delete_row(1)

    # Update cell by cell
    #Sheet.update_cell(1, 1, "SomeTextHere")

    #Pull data from row, column, or cell
    '''Sheet.row_values(1)
    Sheet.col_values(1)
    Sheet.cell(1, 1).value'''

    '''# Get row count
    count = sheet.row_count
    print(count)'''

    # Extract and print all of the values
    '''list_of_hashes = sheet.get_all_records()
    print(list_of_hashes)'''

    # Extract and print the values as a list
    list_of_values = sheet.get_all_values()
    jsonString = JSONEncoder(ensure_ascii=True).encode(
        list_of_values
        )

    return render_template('index.html', data = jsonString)

@app.route('/receiver', methods = ['POST'])
# Insert row
def NewRow():
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
     
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("Inventory").sheet1
    #read json + reply
    data = request.get_json()
    print(data)
    #newDic = JSONDecoder().decode(data)
    #print (newDic)
    
    '''arr = request.get_json()
    data = json.loads(arr)

    for element in data:
        print (element)'''
    '''result = ''
    for item in data:
        #loop over every row
        result += str(item) + '\n'
    print(result)'''
    #set up info to add to a new row
    # Getting current datetime
    now = datetime.datetime.now()
    isbn = data['isbn']
    title = data['title']
    author = data['author']
    pubDate = data['pubDate']
    genre = data['genre']

    #get current row count and future row count
    count = sheet.row_count
    rowNum = count + 1

    #prepare for lift off
    row = ["",str(now),isbn,title,author,pubDate,genre]
    sheet.insert_row(row, rowNum)
    
    
    return render_template('index.html')

    #old option
    '''jsdata = request.form['javascript_data']
    print(jsdata)
    
    return json.loads(jsdata)[0]
    if request.method == 'POST':
        # Getting current datetime
        now = datetime.datetime.now()
        asd = request.json
        print(asd)
        session['data'] = asd
        if 'data' in session:
            return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
        string = request.args.get(data)
        print(string)'''
'''
        isbn = request.form('isbn')
        title = request.form('title')
        author = request.form('author')
        pub = request.form('pubDate')
        genre = request.form('genre')
        console.log(now, title, author)
        #jsonString = JSONDecoder().decode(data)
        row = ["",str(now),isbn,title,author,pub,genre]
        count = sheet.row_count
        RowNum = count+1
        sheet.insert_row(row, RowNum)
        console.log(row)'''


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run()

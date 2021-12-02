from flask import Flask,jsonify,request

app=Flask(__name__)

data=[
    {
        "Contact": "9658329348",
        "Name": "Carolina Marin",
        "done": False,
        "id": 1
    },
    {   
        "Contact":"9654732834",
        "Name":"Nozomi Okuhara",
        "done":False,
        "id":2
    },
    {
        "Contact":"9323329436",
        "Name":"Sapisree Tearattanachai",
        "done":False,
        "id":3
    },
    {
        "Contact":"7657434567",
        "Name":"Lee Chong Wei",
        "done":False,
        "id":4
    }

]

@app.route('/add-data' ,methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide the data'
        },400)
    contact={
        'id':data[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'done':False
    }
    data.append(contact)
    return jsonify({
        'status':'success',
        'message':'task added successfully'
    })
if(__name__=='__main__'):
    app.run(debug=True)

from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.train 
def insert():
    try:
        Id =input(' Enter traincsv Passenger Id: ')
        Name =input('Enter Name: ')
        Age =input('Enter age: ')
        Fare =input('Enter Fare: ')
        Sex =input('Enter Sex: ')
        Ticket =input('Enter Ticket: ')
        db.traincsv.insert_one(
        {
        "PassengerId": Id,
        "Name":Name,
        "Age":Age,
        "Fare":Fare,
        "Sex":Sex,
        "Ticket":Ticket,
        })
        print("\nInserted data successfully\n")
    except Exception as e:
        print(str(e))

def read():
    try:
        TrainCol =db.traincsv.find()
        print("All Data From Train \n")
        for Train in TrainCol:
            print(Train)

    except Exception as e:
        print(str(e))

def update():
    try:
        name = input("Enter the Name to Update: ")
        age = input("Enter the Age to Update: ")
        db.traincsv.update_one({"Name": name},
        {"$set": {"Age": age} }
        )
        print("Record has been Updated")
    except Exception as e:
        print(str(e))

def delete():
    try:
        value = input("\n Enter the Name to Delete: ")
        db.traincsv.delete_one({"Name":value})
        print("\n DELETION SUCCESSFUL \n")
    except Exception as e:
        print(str(e))
        
#insert()
#read()
#update()
#delete()
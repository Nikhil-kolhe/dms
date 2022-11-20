import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
mydb=client["College"]
mycol=mydb["Students"]
while True:
    id1=int(input("Enter Student id: "))
    name1=input("Enter Student name: ")
    age1=int(input("Enter Student age: "))
    
    data={'_id':id1,'name':name1,'age':age1}
    mycol.insert_one(data)

    x=int(input("1->Enter More\n2->Exit\nEnter choice:"))
    if x==2:
        break
    

for data in mycol.find({}):
    print(data)
    print()


print("find Specific field ,using specific key and value:")
for data in mycol.find({'age':20}):
   print(data)
   print()


#Update /Edit Specific field ,using specific key ,method and values and update_one()

mycol.update_one(
     {'name':'Sam'},
     {
         "$set":{
             'age':21
       }
     }
)

print("Updated the record ")
print()


#Delete / remove Specific field ,using specific key ,method and values and update_one()
mycol.delete_one({'name':'Jeevan'})
print("Deleted the record :Jeevan")
print()



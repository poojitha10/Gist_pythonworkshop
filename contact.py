contact={}
def add_contact(name,ph_no):
    if(name in contact.keys()):
        print(name,"contact already exit---!!!")
    else:
        contact[name]=ph_no
        print("contact added/saved successfully---!!!")
def display_contact():
    i=0
    if(i<len(contact)):
        for name,phone in contact.items():
            print(i+1,".name=",name,".phonenumber=",phone)
            i=i+1
def delete_contact(name):
    if(name in contact.keys()):
        contact.pop(name)
        print(name,"deleted successfully....!!!")
    else:
        print(name,"does not exits in contact list...!!!")
def update_contact(name,ph_no):
    if name in contact.keys():
        contact[name]=ph_no
        print(" ")
    else:
        print("contact not exits....!!!!")
def search_contact(name):
    if(name in contact.keys()):
        print("name=",name,"phonenumber=",contact[name])
    else:
        print(name,"don't exits...!!!")
            
                    
current_staff = {"name" : "Sameer" , "role" : "Salesman"}
def manager_only(func):
    def wrapper(*args,**kwargs):
        if current_staff["role"] != "manager":
            print (f'Denied {current_staff["name"]} "is not a manager" ')

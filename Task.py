import json 
import User


class Tasks:
    def __init__(self,ID,Description,Status):
        self.ID = ID
        self.Description = Description
        self.Status = Status 
    

class Task_list:
    def __init__(self):
        self.TaskList = []

    def addTask(self,task):
        self.TaskList.append(task)

    def ViewTask(self):
        for item in self.TaskList:
            print(item)
    

data = {}

def LoadData(data):
    try:
        with open("Tasks.json", "r") as jsonfile:
            data = json.load(jsonfile)
    except FileNotFoundError:
        print("The file was not found")
    
    return data

def WriteData(data):
    with open("Tasks.json", "w") as jsonfile:
        json.dump(data,jsonfile,indent= 4)


data = LoadData(data)


user = User.Users("Khawar",0,"Novice",1)

userdata = {
    "username" : user.username,
    "xp": user.xp,
    "rank": user.rank
}

data["User"] = userdata
print(data["User"], data["Tasks"])
WriteData(data)

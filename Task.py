import json 

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
    


def LoadData(data):
    with open("Tasks.json", "r") as jsonfile:
        data["Tasks"] = json.load(jsonfile)
    print(data["Tasks"]) 

def WriteData(data):
    with open("Tasks.json", "w") as jsonfile:
        json.dump(data,jsonfile,indent= 4)




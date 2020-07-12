from helperMethods import *
employeeAttendance = None

class EmpNode:
    def __init__(self, EId):
        self.EmpId = EId
        self.attCtr = 1
        self.left = None
        self.right = None

def _recordSwipeRec(eNode, EId):
        if eNode is None:
            eNode = EmpNode(EId)
        else:
            if eNode.EmpId == EId:
                eNode.attCtr = eNode.attCtr + 1
            elif eNode.EmpId > EId:
                if eNode.left is None:
                    eNode.left = EmpNode(EId)
                else:
                    _recordSwipeRec(eNode.left, EId)
            else:
                if eNode.right is None:
                    eNode.right =  EmpNode(EId)
                else:
                    _recordSwipeRec(eNode.right, EId)

def _getSwipeRec(eNode):
    print("Total number of employees recorded today: " + str(findTotalEmployeesToday(employeeAttendance)))

def _onPremisesRec(eNode):
    numOfEmployeesOnPrem = findOnPrem(eNode)
    if numOfEmployeesOnPrem > 0:
        print( str(numOfEmployeesOnPrem) + " employees still on premises")
    else:
        print("No employees present on premises.")




def _checkEmpRec(eNode, EId):
    attCtr = search(eNode, EId)
    if attCtr is None:
        print("Employee id "+str(EId)+" did not swipe today")
    elif attCtr % 2 == 0:
        print("Employee id "+str(EId)+" swiped "+str(attCtr)+" times today and is currently outside office")
    else:
        print("Employee id "+str(EId)+" swiped "+str(attCtr)+" times today and is currently in office")


def _frequentVisitorRec(eNode, freq):
    findEmployeesGreaterThanFreq(eNode, freq)
    if(len(listOfEmployees) > 0):
        print("Employees that swiped more than "+str(freq)+" number of times today are:")
        for emp in listOfEmployees:
            print (str(emp.EmpId) + ", " + str(emp.attCtr))
    else:
        print("No employee swiped more than " +str(freq)+ " times today")
    clearList()

def _printRangePresent(eNode, StartId, EndId):
    findEmployeesInRange(eNode, StartId, EndId)
    if(len(listOfEmployees) > 0):
        print("Range "+str(StartId)+ " to " +str(EndId))
        print("Employee swipe:")
        for emp in listOfEmployees:
            print (str(emp.EmpId) + ", " + str(emp.attCtr) + ", " + ("in" if emp.attCtr%2 != 0 else "out"))
    else:
        print("No employee in range "+str(StartId)+ " to " +str(EndId))
    clearList()

def employeeEntry():
    global employeeAttendance
    f=open("inputPS5.txt", "r") 
    Lines = f.readlines() 
    count = 1
    for line in Lines: 
        empId = int(line.strip())
        if count == 1:
            employeeAttendance = EmpNode(empId)
        else:
            _recordSwipeRec(employeeAttendance, empId)
        count = count + 1

def prompts():
    
    global employeeAttendance
    
    f=open("promptsPS5.txt", "r") 
    Lines = f.readlines()
    for line in Lines: 
        # print(line)
        if line.find("onPremises") != -1:
            _getSwipeRec(employeeAttendance)
            _onPremisesRec(employeeAttendance)
        elif line.find("checkEmp") != -1:
            empId = int(line.split(":")[1].strip())
            _checkEmpRec(employeeAttendance, empId)
        elif line.find("freqVisit") != -1:
            freq = int(line.split(":")[1].strip())
            _frequentVisitorRec(employeeAttendance, freq)
        elif line.find("range") != -1:
            startId = int(line.split(":")[1].strip())
            endId = int(line.split(":")[2].strip())
            _printRangePresent(employeeAttendance, startId , endId)
            


employeeEntry()
prompts()

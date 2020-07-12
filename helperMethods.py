listOfEmployees = []

def findTotalEmployeesToday(eNode):
    if eNode is None:
        return 0
    return 1 + findTotalEmployeesToday(eNode.left) + findTotalEmployeesToday(eNode.right)

def findOnPrem(eNode):
    if eNode is None:
        return 0
    return (eNode.attCtr % 2) + findOnPrem(eNode.left) + findOnPrem(eNode.right)

def findEmployeesInRange(eNode, StartId, EndId):
    if eNode != None:
        findEmployeesInRange(eNode.left, StartId, EndId)
        if eNode.EmpId > EndId:
            # We donot need to check more since for InOrderTraversal, since employeeIds will be greater now
            return
        elif eNode.EmpId >= StartId:
            listOfEmployees.append(eNode)
        findEmployeesInRange(eNode.right, StartId, EndId)

def findEmployeesGreaterThanFreq(eNode, freq):
    if eNode != None:
        findEmployeesGreaterThanFreq(eNode.left, freq)
        if eNode.attCtr >= freq:
            listOfEmployees.append(eNode)
        findEmployeesGreaterThanFreq(eNode.right, freq)

def search(eNode, empId):
        if eNode.EmpId == empId:
            return eNode.attCtr
        if eNode.left is not None and eNode.EmpId > empId:
            temp =  search(eNode.left, empId)
            if temp is not None:
                return temp
        if eNode.right is not None and eNode.EmpId <= empId:
            temp =  search(eNode.right, empId)
            return temp
        return None

def clearList():
    listOfEmployees[:] = []

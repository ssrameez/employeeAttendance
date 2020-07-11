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

def findTotalEmployeesToday(eNode):
    if eNode is None:
        return 0
    return 1 + findTotalEmployeesToday(eNode.left) + findTotalEmployeesToday(eNode.right)

def _onPremisesRec(eNode):
    numOfEmployeesOnPrem = findOnPrem(eNode)
    if numOfEmployeesOnPrem > 0:
        print( str(numOfEmployeesOnPrem) + " employees still on premises")
    else:
        print("No employees present on premises.")
    
def findOnPrem(eNode):
    if eNode is None:
        return 0
    return (eNode.attCtr % 2) + findOnPrem(eNode.left) + findOnPrem(eNode.right)

def _printTree(tree):
    if tree != None:
        _printTree(tree.left)
        print(tree.EmpId, tree.attCtr)
        _printTree(tree.right)


# def _getSwipeRec(self, eNode):

# def _onPremisesRec(self, eNode, eId):

# def _checkEmpRec(self, eNode, EId):

# def _frequentVisitorRec(self, eNode):

# def printRangePresent(self, StartId, EndId):


employeeAttendance = EmpNode(21)
_recordSwipeRec(employeeAttendance, 23)
_recordSwipeRec(employeeAttendance, 22)
_recordSwipeRec(employeeAttendance, 41)
_recordSwipeRec(employeeAttendance, 21)

_printTree(employeeAttendance)
_getSwipeRec(employeeAttendance)
_onPremisesRec(employeeAttendance)


# _printTree(employeeAttendance)



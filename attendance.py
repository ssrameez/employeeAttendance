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
    if eNode is None:
        return 0
    return 1 + _getSwipeRec(eNode.left) + _getSwipeRec(eNode.right)

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
_recordSwipeRec(employeeAttendance, 22)
print("Total number of employees recorded today: " + str(_getSwipeRec(employeeAttendance)))

# _printTree(employeeAttendance)



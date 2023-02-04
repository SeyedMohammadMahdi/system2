from elevator import Elevator
from GUI import MyWindow
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5 import QtTest

app = QApplication(sys.argv)
win = MyWindow()
win.show()
def updateElavator(position1, position2, position3, info1, info2, info3):
    win.printInfo(info1, info2, info3)
    win.elevatorPosition(position1, position2, position3)


# request = [[position, destination, time]]
request = [[0, 9, 0], [0, 9, 0], [4, 9, 3], [3, 9, 2], [7, 9, 5], [0, 9, 0]]
elevator1 = Elevator(1)
elevator2 = Elevator(2)
elevator3 = Elevator(3)
newReqList = []
for req in request:
    if req[2] == 0:
        elevator1.addExternalRequest(req[0], req[1])
    else:
        newReqList.append(req)

request = newReqList


# elevator.remainedFloors = 0

while elevator1.internalRequestDown or elevator1.internalRequestUp or elevator1.externalRequest or request or elevator1.requestExistFlag or \
    elevator2.internalRequestDown or elevator2.internalRequestUp or elevator2.externalRequest or elevator2.requestExistFlag or \
    elevator3.internalRequestDown or elevator3.internalRequestUp or elevator3.externalRequest or elevator3.requestExistFlag:

    elevator1.moveToDest()
    elevator2.moveToDest()
    elevator3.moveToDest()


    updateElavator(elevator1.floor, elevator2.floor, elevator3.floor, elevator1.info, elevator2.info, elevator3.info)
    QtTest.QTest.qWait(500)

    newReqList = []
    flag = False
    for req in request:
        req[2] -= 1
        if elevator1.currentCapacity < elevator1.maxCapacity:
            if req[2] <= 0:
                elevator1.addExternalRequest(req[0], req[1])
                # request.remove(req)
            else:
                flag = False
        elif elevator2.currentCapacity < elevator2.maxCapacity:
            if req[2] <= 0:
                flag = True
                elevator2.addExternalRequest(req[0], req[1])
                # request.remove(req)
            else:
                flag = False
        elif elevator3.currentCapacity < elevator3.maxCapacity:
            if req[2] <= 0:
                flag = True
                elevator3.addExternalRequest(req[0], req[1])
                # request.remove(req)
            else:
                flag = False
        if not flag:
            newReqList.append(req)
    request = newReqList



sys.exit(app.exec_())



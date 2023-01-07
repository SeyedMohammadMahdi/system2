# request = [[position, destination, time]]
from elevator2 import Elevator

request = [[0, 9, 0], [0, 9, 0], [4, 9, 3], [3, 9, 2], [7, 9, 5], [0, 9, 0]]
elevator = Elevator()
newReqList = []
for req in request:
    if req[2] == 0:
        elevator.addExternalRequest(req[0], req[1])
        # print("new person in the elevator request: ", req[1])
        # request.remove(req)
    else:
        newReqList.append(req)

request = newReqList


# elevator.remainedFloors = 0

while elevator.internalRequestDown or elevator.internalRequestUp or elevator.externalRequest or request or elevator.requestExistFlag:
    elevator.moveToDest()
    for req in request:
        req[2] -= 1
        if req[2] <= 0 and elevator.floor == req[0]:
            elevator.addExternalRequest(req[0], req[1])
            request.remove(req)



# request = [[position, destination, time]]
from elevator import Elevator

request = [[0, 9, 0], [5, 0, 0], [8, 2, 3], [3, 15, 2], [5, 12, 8], [2, 12, 5]]
elevator = Elevator()

for req in request:
    if req[2] == 0 and elevator.floor == req[0]:
        elevator.addInternalRequest(req[1])
        request.remove(req)

# elevator.remainedFloors = 0

while elevator.internalRequestDown or elevator.internalRequestUp or elevator.externalRequest or elevator.agingQueue or request:
    elevator.moveToDestination()
    for req in request:
        req[2] -= 1
        if req[2] <= 0 and elevator.floor == req[0]:
            elevator.addInternalRequest(req[1])
            request.remove(req)



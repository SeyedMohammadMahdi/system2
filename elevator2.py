class Elevator:
    def __init__(self, id):
        self.id = id
        # following lists store lists with size 2 in the format of [destination, age]
        self.internalRequestUp = []
        self.internalRequestDown = []
        self.movedInternalRequestUp = []
        self.movedInternalRequestDown = []
        self.externalRequest = []
        self.movedExternal = []
        self.agedRequest = []
        # stores an age that the requests with higher ages will be added to agedRequest list
        self.maxAged = 5
        # the floor variable stores current floor
        self.floor = 0
        # MAXFLOORS stores maximum number of floors
        self.MAXFLOORS = 15
        # direction stores the direction of elevator. 1, means up and -1 means down
        self.direction = 1
        # remainedToDest stores the remaining number of floor to serve the current request
        self.remainedToDest = 0
        # stores current request that is being served
        self.move = [0, 0]
        # if there is a request being served
        self.requestExistFlag = False
        self.maxCapacity = 2
        self.currentCapacity = 0
        self.firstTime = True


    def moveToDest(self):

        if self.remainedToDest == 0 and not self.firstTime:
            print(f"request {self.move[0]} served by {self.id}")
            self.firstTime = False
        # adds externalRequests to internalRequests
        self.moveFromexternalToInternal()

        # checks if any other requests destination is in this floor
        newInternalUp = []
        for req in self.movedInternalRequestUp:
            if req[0] == self.floor:
                # self.internalRequestUp.remove(req)
                print(f" \n ************************************************************ request {req[0]} served by {self.id} \n")
            else:
                newInternalUp.append(req)

        self.movedInternalRequestUp = newInternalUp
        # checks if any other requests destination is in this floor
        newInternalDown = []
        for req in self.movedInternalRequestDown:
            if req[0] == self.floor:
                # self.internalRequestDown.remove(req)
                print(f" \n ************************************************************ request {req[0]} served by {self.id} \n")
            else:
                newInternalDown.append(req)

        self.movedInternalRequestDown = newInternalDown
        newAgedReq = []
        for req in self.agedRequest:
            if req[0] == self.floor:
                # self.agedRequest.remove(req)
                print(f" \n ************************************************************ request {req[0]} served by {self.id} \n")
            else:
                newAgedReq.append(req)

        self.agedRequest = newAgedReq

        if self.remainedToDest == 0:
            self.requestExistFlag = False
            # change direction if any of internalRequest lists is empty or we are in floor 0 or MAXFLOORS
            if ((not self.internalRequestUp) and self.direction == 1) \
                    or ((not self.internalRequestDown) and self.direction == -1) or (self.floor == 0 and self.direction == -1) or (self.floor == self.MAXFLOORS and self.direction == 1):
                self.direction *= -1
            # if there is any aged request in agedRequest it will be served first
            if self.agedRequest:
                self.move = self.agedRequest.pop(0)
                self.remainedToDest = abs(self.floor - self.move[0])
                self.requestExistFlag = True
                if self.floor - self.move[0] > 0:
                    self.direction = -1
                else:
                    self.direction = 1
            # if direction is up and internalRequestUp is none empty serve a request
            elif self.internalRequestUp and self.direction == 1:
                self.move = self.internalRequestUp.pop(0)
                self.movedInternalRequestUp.append(self.move)
                self.remainedToDest = abs(self.floor - self.move[0])
                self.requestExistFlag = True
            # if direction is down and internalRequestDown is none empty serve a request
            elif self.internalRequestDown and self.direction == -1:
                self.move = self.internalRequestDown.pop(0)
                self.movedInternalRequestDown.append(self.move)
                self.remainedToDest = abs(self.floor - self.move[0])
                self.requestExistFlag = True
            elif self.externalRequest:
                self.move = self.externalRequest.pop(0)
                self.movedExternal.append(self.move)
                self.remainedToDest = abs(self.floor - self.move[0])
                self.direction = 1 if (self.floor - self.move[0]) < 0 else -1
                self.requestExistFlag = True

            if self.requestExistFlag:
                print(f"-->new destination<-- by {self.id} : ", self.move[0])




        # print(self.agedRequest)

        self.update()
        # if direction is to down, direction value is -1.
        # if direction in to up, direction value is 1
        if self.requestExistFlag:
            self.floor += self.direction
        # checks if value of floor is not negative or higher than maximum number of floors
        if self.floor > self.MAXFLOORS \
                or self.floor < 0:
            self.floor -= self.direction
        # if the elevator hasn't reached to destination
        # remainedToDest will be decremented
        if self.remainedToDest > 0:
            self.remainedToDest -= 1

        # print(self.floor, self.remainedToDest)
        if self.requestExistFlag:
            print(f" elevator {self.id} at floor: ", self.floor)

        self.currentCapacity = len(self.internalRequestUp) + len(self.internalRequestDown) + len(self.externalRequest) + len(self.agedRequest)

    def addInternalRequest(self, destination):
        # if the destination of request is in higher floor
        # it will be added to internalRequestUp
        # otherwise it will be added to internalRequestDown
        if destination - self.floor > 0:
            i = 0
            while i < len(self.internalRequestUp) and self.internalRequestUp[i][0] < destination:
                i += 1
            self.internalRequestUp.insert(i, [destination, 0])
        else:
            i = 0
            while i < len(self.internalRequestDown) and self.internalRequestDown[i][0] > destination:
                i += 1
            self.internalRequestDown.insert(i, [destination, 0])

    def addExternalRequest(self, position, destination):
        self.externalRequest.append([position, destination])

    def moveFromexternalToInternal(self):
        newExterReqList = []
        for exReq in self.movedExternal:
            if exReq[0] == self.floor:
                self.addInternalRequest(exReq[1])
                print("__new person in the elevator requests: ", exReq[1])
                # self.externalRequest.remove(exReq)
            else:
                newExterReqList.append(exReq)

        self.movedExternal = newExterReqList

    def update(self):
        # updating ages for each request that is in the reverse direction of elevator
        # and checks if a request is aged then adds it to agedRequests
        if self.direction == -1:
            for req in self.internalRequestUp:
                req[1] += 1
                if req[1] > self.maxAged:
                    self.agedRequest.append(req)
                    self.internalRequestUp.remove(req)
        elif self.direction == 1:
            for req in self.internalRequestDown:
                req[1] += 1
                if req[1] > self.maxAged:
                    self.agedRequest.append(req)
                    self.internalRequestDown.remove(req)

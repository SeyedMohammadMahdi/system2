class Elevator:
    def __init__(self):
        # following lists store lists with size 2 in the format of [destination, age]
        self.internalRequestUp = []
        self.internalRequestDown = []
        self.externalRequest = []
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

    def moveToDest(self):
        move = [self.floor, 0]
        # adds externalRequests to internalRequests
        self.moveFromexternalToInternal()

        # checks if any other requests destination is in this floor
        for req in self.internalRequestUp:
            if req[0] == self.floor:
                self.internalRequestUp.remove(req)
        # checks if any other requests destination is in this floor
        for req in self.internalRequestDown:
            if req[0] == self.floor:
                self.internalRequestDown.remove(req)


        if self.remainedToDest == 0:
            # change direction if any of internalRequest lists is empty or we are in floor 0 or MAXFLOORS
            if ((not self.internalRequestUp) and self.direction == 1) \
                    or ((
                        not self.internalRequestDown) and self.direction == -1) or self.floor == 0 or self.floor == self.MAXFLOORS:
                self.direction *= -1
            # if there is any aged request in agedRequest it will be served first
            if self.agedRequest:
                move = self.agedRequest.pop(0)
                self.remainedToDest = abs(self.floor - move[0])
                if self.floor - move[0] > 0:
                    self.direction = -1
                else:
                    self.direction = 1
            # if direction is up and internalRequestUp is none empty serve a request
            elif self.internalRequestUp and self.direction == 1:
                move = self.internalRequestUp.pop(0)
                self.remainedToDest = abs(self.floor - move[0])
            # if direction is down and internalRequestDown is none empty serve a request
            elif self.internalRequestDown and self.direction == -1:
                move = self.internalRequestDown.pop(0)
                self.remainedToDest = abs(self.floor - move[0])
            elif self.externalRequest:
                move = self.externalRequest.pop(0)
                self.remainedToDest = abs(self.floor - move[0])
                self.direction = 1 if (self.floor - move[0]) < 0 else -1

        print(self.floor, self.remainedToDest)
        # print(self.agedRequest)

        self.update()
        # if direction is to down, direction value is -1.
        # if direction in to up, direction value is 1
        self.floor += self.direction
        # checks if value of floor is not negative or higher than maximum number of floors
        if self.floor > self.MAXFLOORS \
                or self.floor < 0:
            self.floor -= self.direction
        # if the elevator hasn't reached to destination
        # remainedToDest will be decremented
        if self.remainedToDest > 0:
            self.remainedToDest -= 1



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
        for exReq in self.externalRequest:
            if exReq[0] == self.floor:
                self.addInternalRequest(exReq[1])
                self.externalRequest.remove(exReq)

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

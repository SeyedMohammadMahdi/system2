class Elevator:
    def __init__(self):
        self.internalRequestUp = []
        self.internalRequestDown = []
        self.externalRequest = []
        # above lists store lists with size 2 in the format of [destination, age]
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
        if self.remainedToDest == 0:

            # change direction if any of internalRequest lists is empty or we are in floor 0 or MAXFLOORS
            if ((not self.internalRequestUp) and self.direction == 1) \
                    or ((
                        not self.internalRequestDown) and self.direction == -1) or self.floor == 0 or self.floor == self.MAXFLOORS:
                self.direction *= -1
            # if direction is up and internalRequestUp is none empty serve a request
            if self.internalRequestUp and self.direction == 1:
                move = self.internalRequestUp.pop(0)
                self.remainedToDest = abs(self.floor - move[0])
            # if direction is down and internalRequestDown is none empty serve a request
            elif self.internalRequestDown and self.direction == -1:
                move = self.internalRequestDown.pop(0)
                self.remainedToDest = abs(self.floor - move[0])

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

        print(self.floor, self.remainedToDest)

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

    def addEternalRequest(self, position, destination):
        self.externalRequest.append([position, destination])

    def moveFromexternalToInternal(self):
        pass

    def update(self):
        # updating ages for each request that is in the reverse direction of elevator
        if self.direction == -1:
            for req in self.internalRequestUp:
                req[1] += 1
        elif self.direction == 1:
            for req in self.internalRequestDown:
                req[1] += 1

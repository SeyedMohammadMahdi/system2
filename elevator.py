class elvator:
    def __init__(self):
        self.internalRequestUp = []
        self.internalRequestDown = []
        self.externalRequest = []
        self.agingQueue = []
        self.floor = 0
        self.agedValue = 5
        self.direction = 1
        self.agingCoefficient = 0.5
        self.distanceCoefficient = 0.5
        self.agedMove = 0
        self.maxAgedMove = 4
        # after exiting agingQueue
        self.flag = False

    def update(self):
        remainingTime = []
        agingRemainingTime = []
        #
        # for req in self.internalRequestUp:
        #     req[1] += 1
        #     remainingTime.append(self.floor - req[0])
        #
        # if len(self.agingQueue) == 0:
        #     for i in range(len(remainingTime)):
        #         for j in range(i):
        #             if (remainingTime[j] > remainingTime[j + 1]):
        #                 remainingTime[j], remainingTime[j + 1] = remainingTime[j + 1], remainingTime[j]
        #                 self.internalRequestUp[j], self.internalRequestUp[j + 1] = self.internalRequestUp[j + 1], self.internalRequestUp[j]
        #
        # remainingTime.clear()
        # for req in self.internalRequestDown:
        #     req[1] += 1
        #     remainingTime.append(self.floor - req[0])
        #
        # if len(self.agingQueue) == 0:
        #     for i in range(len(remainingTime)):
        #         for j in range(i):
        #             if (remainingTime[j] > remainingTime[j + 1]):
        #                 remainingTime[j], remainingTime[j + 1] = remainingTime[j + 1], remainingTime[j]
        #                 self.internalRequestDown[j], self.internalRequestDown[j + 1] = self.internalRequestDown[j + 1], \
        #                 self.internalRequestDown[j]

        for i in range(len(self.internalRequestUp) - 1, 0):
            if self.internalRequestUp[i][1] >= self.agedValue:
                # internalRequest.insert(0, internalRequest.pop(i))
                self.agingQueue.append(self.internalRequestUp.pop(i))

        for i in range(len(self.internalRequestDown) - 1, 0):
            if self.internalRequestDown[i][1] >= self.agedValue:
                # internalRequest.insert(0, internalRequest.pop(i))
                self.agingQueue.append(self.internalRequestDown.pop(i))

        for aged in self.agingQueue:
            aged[1] += 1
            self.agingRamainingTime.append(
                self.distanceCoefficient * abs(self.floor - aged[0]) + self.agingCoefficient * abs(aged[1]))

        if len(self.agingQueue) > 0:
            for i in range(len(agingRemainingTime)):
                for j in range(i):
                    if agingRemainingTime[j] < agingRemainingTime[j + 1]:
                        agingRemainingTime[j], agingRemainingTime[j + 1] = agingRemainingTime[j + 1], \
                                                                           agingRemainingTime[j]
                        self.agingQueue[j], self.agingQueue[j + 1] = self.agingQueue[j + 1], self.agingQueue[j]

        if (self.flag and len(self.agingQueue) == 0):
            if self.floor > self.internalRequestUp[0][0]:
                while self.floor > self.internalRequestUp[0][0]:
                    self.internalRequestDown.append(self.internalRequestUp.pop(0))
            else:
                while self.floor < self.internalRequestDown[len(self.internalRequestDown) - 1][0]:
                    self.internalRequestUp.insert(0, self.internalRequestDown.pop(len(self.internalRequestDown) - 1))
            self.flag = False

    def moveToDestination(self):
        move = [self.floor, 0]
        if len(self.agingQueue) == 0 and (len(self.internalRequestUp) != 0 or len(self.internalRequestDown) != 0):
            if (len(self.internalRequestUp) == 0 and self.direction == 1) or (
                    len(self.internalRequestDown) == 0 and self.direction == 0):
                self.direction = 1 - self.direction
            if self.direction == 1:
                move = self.internalRequestUp.pop(0)
            else:
                move = self.internalRequestDown.pop(len(self.internalRequestDown) - 1)

            self.agedMove += 1
        elif len(self.agingQueue) != 0:
            self.flag = True
            move = self.agingQueue.pop(0)

        # it needs to be completed
        elif len(self.externalRequest) != 0:
            print()

        if self.agedMove > self.maxAgedMove:
            self.agedMove = 0
            self.direction = 1 - self.direction

        print("reached floor " + move[0])

    def addInternalRequest(self, destination):
        if self.floor - destination > 0:
            i = 0
            while self.internalRequestUp[i][0] < destination:
                i += 1
            self.internalRequestUp.insert(i, [destination, 0])
        else:
            i = 0
            while self.internalRequestDown[i][0] < destination:
                i += 1
            self.internalRequestDown.append([destination, 0])

    def addExternalRequest(self, destination):
        self.externalRequest.append(destination)
        pass

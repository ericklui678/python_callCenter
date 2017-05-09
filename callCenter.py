from itertools import count

class Call(object):
    _ids = count(0)     # start count at 1
    def __init__(self, name, number, time, reason):
        self.id = self._ids.next()  # increment id for every call instance
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    def displayInfo(self):
        print "ID:", self.id
        print "Caller Name:", self.name
        print "Number:", self.number
        print "Time:", self.time
        print "Reason:", self.reason
        print
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queueSize = 0
    def addCall(self, callObj):
        self.calls.append(callObj)
        self.queueSize += 1
        print "Call ID #" +str(callObj.id), "was added to the queue"
        print
        return self
    def info(self):
        print "Queue Length:", self.queueSize
        for i in range(self.queueSize):
            print self.calls[i].name, self.calls[i].number, self.calls[i].time
            # print self.calls[i].displayInfo()
        print
        return self
    def remove(self):
        self.calls.pop(0)
        self.queueSize -= 1
        return self
    def removeByNum(self, num):
        for i in range(self.queueSize):
            if self.calls[i].number == num:
                self.calls.pop(i)
                self.queueSize -= 1
                print "Number #" + str(num), "was removed from queue"
                break
        return self
    # uses bubbleSort, can be modified later for efficiency
    def sort(self):
        sorted = False
        while not sorted:
            swapCount = 0
            for i in range(self.queueSize - 1):
                if self.calls[i].time > self.calls[i+1].time:
                    self.calls[i], self.calls[i+1] = self.calls[i+1], self.calls[i]
                    swapCount += 1
            if swapCount == 0:
                sorted = True
        return self

call1 = Call("Bob", 2342342345, 1700, "complaint")
call2 = Call("Jeff", 3453453456, 110, "daily update")
call3 = Call("Kevin", 1231231234, 1200, "security concerns")

main = CallCenter()
main.addCall(call1).addCall(call2).addCall(call3).info()

main.sort().info()
main.removeByNum(2342342345).info()

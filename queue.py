class Queue:

    def __init__(self):
        self.contents = []

    def isEmpty(self):
        return self.contents == []

    def enqueue(self, item):
        self.contents.insert(0, item)

    def dequeue(self):
        return self.items.pop()

def main():
    testQueue = Queue()
    testQueue.enqueue(1)
    testQueue.enqueue(4)
    testQueue.enqueue(7)
    print(testQueue)

if __name__ == "__main__":
    main()
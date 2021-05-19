'''
Cracking the coding interview
Chapter 3 - Stacks and Queues
Stacks and Queues: Stack of Plates
----------------------------------------
Question: Imagine a literal stack of plates. If the stack gets too high, it might topple. There-fore, in real life, we would likely
start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. 
SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.
Push() and SetOfStacks.Pop() should behave identically to a single stack (that is pop() should return the same value as it would if there were just a 
single stack
Example: 5 is stack limit 
input: 
output: 
Constraits or Questions you need to ask:
Solution notes:
'''
class Stack:
    def __init__(self, size):
        #Using a list for the stack
        self.stacks = []
        if size < 1:
            raise NameError("A stack is greater than one")
        else:
            self.size = size

    def push(self, data):
        if self.stacks == []:
            self.stacks.append([data])
        else:
            if len(self.stacks[-1]) >= self.size:
                self.stacks.append([data])
            else:
                self.stacks[-1].append(data)
     
    def pop(self):
        if self.stacks == []:
            raise NameError("Can't pop an empty stack")
        else:
            poppedData = self.stacks[-1][-1]
            if len(self.stacks[-1]) == 1:
                self.stacks[-1].pop()
            else: 
                self.stacks[-1][-1]
            return poppedData







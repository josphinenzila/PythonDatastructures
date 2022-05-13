""" Queues and stacks """

#A palindrome is a word, phrase, number or other sequence which reads 
#the same backwards or forward. can you dertemine if a given string s, is a palindrome

from collections import deque


class Solution:
    def __init__(self):
        self.queue = deque()
        self.stack = list()

    def pushCharacter(self, character):
        self.stack.append(character)

    def enqueueCharacter(self, character):
        self.queue.append(character)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.popleft()


# read the string s
s = input("Enter the string: ")
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
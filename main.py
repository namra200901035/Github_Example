from collections import deque


class Brackets_Check():

    Open_List = ["[", "{", "("]
    Close_List = ["]", "}", ")"]

    def Check(self, myString):
        self.stack = deque()
        for a in myString:

            if a in self.Open_List:

                self.stack.append(a)

            elif a in self.Close_List:

                pos = self.Close_List.index(a)

                if ((len(self.stack) > 0) and (self.Open_List[pos] == self.stack[len(self.stack) - 1])):

                    self.stack.pop()

                else:
                    return "Unbalanced"
                if len(self.stack) == 0:
                    return "Balanced"
                else:
                    return "Unbalanced"


object = Brackets_Check()

string = "{[]{()}}"
print(object.Check(string))

string = "[{}{})(]"
print(object.Check(string))
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        return self.find(eval(s))
    
    def find(self, s) -> NestedInteger:
        if type(s) == type(1):
            return NestedInteger(s)
        
        n = NestedInteger()

        for x in s:
            n.add(self.find(x))
        return n
        
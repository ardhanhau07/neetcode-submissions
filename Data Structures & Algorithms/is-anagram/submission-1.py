class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elif sorted(s) == sorted(t):
            return True
        else:
            return False

def main():
    print(isAnagram("racecar", "carrace"))
    print(isAnagram("jar", "jam"))
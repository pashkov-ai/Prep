# class Solution:
#     def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
#         sarr = sorted(arr)
#         diff = sarr[1] - sarr[0]
#         for i, e in enumerate(sarr[1:], start=1):
#             if sarr[i] - sarr[i-1] != diff:
#                 return False
#         return True

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        emax = max(arr)
        emin = min(arr)
        if (emax - emin) % (len(arr) - 1) != 0:
            return False
        d = (emax - emin) / (len(arr) - 1)
        if d == 0:
            return True
        elem_set = set()
        for i, e in enumerate(arr):
            if (e - emin) % d != 0:
                return False # not divisable
            if e in elem_set:
                return False # duplicate
            elem_set.add(e)
        return True
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        gvmap = {}
        monostack = []
        for e in nums2:
            while monostack and monostack[-1] < e:
                gvmap[monostack.pop()] = e
            monostack.append(e)
        ans = [gvmap.get(e, -1) for e in nums1]
        return ans
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        setnums = set (nums)
        if len(setnums) < len(nums):
            return True
        else:
            return False
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
        version1 = [int(n) for n in version1]
        version2 = [int(n) for n in version2]
        i, j = 0, 0

        while i < len(version1) and j < len(version2):
            if version1[i] > version2[j]:
                return 1
            elif version1[i] < version2[j]:
                return -1
            else:
                i += 1
                j += 1

        if i < len(version1):
            while i < len(version1):
                if version1[i] != 0:
                    return 1
                else:
                    i += 1
            return 0
        elif j < len(version2):
            while j < len(version2):
                if version2[j] != 0:
                    return -1
                else:
                    j += 1
            return 0
        else:
            return 0

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        sorted = []
        i = 0
        j = 0
        while ((i<len(nums1)) and (j<len(nums2))):
            if (nums1[i] < nums2[j]):
                sorted.append(nums1[i])
                i+=1
            else:
                sorted.append(nums2[j])
                j+=1
        sorted = sorted + nums1[i:] + nums2[j:]
        if (len(sorted)%2 == 0):
            return(float(sorted[(len(sorted)/2)-1]+sorted[(len(sorted)/2)])/2)
        else:
            return(sorted[((len(sorted))/2)])
#note if using integers, / does rounded down integer division and does decimal division for floats
        

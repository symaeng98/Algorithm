class Solution(object):
    def merge(self, nums1, m, nums2, n):
        n1p, n2p = m-1, n-1
        now = n+m-1
        while n2p != -1:
            if n1p == -1 or nums1[n1p] < nums2[n2p]:
                nums1[now] = nums2[n2p]
                n2p -= 1
                now -= 1
            else:
                nums1[now] = nums1[n1p]
                n1p -= 1
                now -= 1
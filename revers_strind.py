class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1

        while start < end:
            #swap
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
        
            # arr[s], arr[e] = arr[e], arr[s]

            start = start + 1
            end = end - 1      
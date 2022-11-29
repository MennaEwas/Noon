#question: https://www.geeksforgeeks.org/place-k-elements-such-that-minimum-distance-is-maximized/

class solution:
    def maxmin(self, n, k, x): #5, 3, [1,2 ,4 ,8 , 9]
        #sort
        x.sort()
        mn_space = 0
        mx_space = x[n-1] - x[0]

        def possible(k, x, middle): # middle = 6 [1, 2,4, 8, 9]
            count = k - 1  #2
            current = x[0] #1
            current_change = x[n-2]
            for e in x:
                if middle <= e - current:
                    count -= 1
                    current = e

            return count <= 0


        while mn_space + 1 < mx_space:
            middle_index = (mx_space + mn_space) // 2
            if possible(k, x, middle_index):
                mn_space = middle_index
            else:
                mx_space = middle_index

        if possible(k, x, mx_space):
            return mx_space
        elif possible(k, x, mn_space):
            return mn_space
        else: return -1

sol = solution()
final = sol.maxmin(5, 3, [1,2,4,8,9])
print(final)






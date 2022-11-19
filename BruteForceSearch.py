from problem import knapsack, split_data



def BruteForceSearch(W, w, v, n):

    if n == 0 or W == 0:
        return 0
 
    if (w[n-1] > W):
        return BruteForceSearch(W, w, v, n-1)
    else:
        return max(v[n-1] + BruteForceSearch(W-w[n-1], w, v, n-1), BruteForceSearch(W, w, v, n-1))
    

    
 
 
#Driver Code
v = [85, 100, 120]
w = [10, 20, 30]
W = 50
n = len(v)
print (BruteForceSearch(W, w, v, n))
 
# This code is contributed by Nikhil Kumar Singh

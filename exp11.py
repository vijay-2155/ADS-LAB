# 0/1 Knapsack using Backtracking

def knapsack_backtrack(wt, val, n, W, i=0, curr_w=0, curr_v=0, best=[0]):
    # If weight exceeds capacity, stop exploring
    if curr_w > W:
        return
    # Update best value found so far
    best[0] = max(best[0], curr_v)
    
    # If all items checked, return
    if i == n:
        return
    
    # Include current item
    knapsack_backtrack(wt, val, n, W, i + 1, curr_w + wt[i], curr_v + val[i], best)
    # Exclude current item
    knapsack_backtrack(wt, val, n, W, i + 1, curr_w, curr_v, best)
    
    return best[0]

# Example input
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

max_value = knapsack_backtrack(wt, val, n, W)
print("Maximum Profit:", max_value)

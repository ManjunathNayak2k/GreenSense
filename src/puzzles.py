
def maxProfit(price, start, end):
    if (end <= start):
        return 0
    
    # Create a memoization table to store previously calculated profits
    memo = [[-1] * (end+1) for _ in range(start+1)]
    
    def helper(price, start, end, memo):
        if (end <= start):
            return 0
        
        # If the profit has already been calculated, return it from the memoization table
        if memo[start][end] != -1:
            return memo[start][end]
        
        # Initialise the profit
        profit = 0
        
        # The day at which the stock must be bought
        for i in range(start, end, 1):
            
            # The day at which the stock must be sold
            for j in range(i+1, end+1):
                
                # If buying the stock at ith day and selling it at jth day is profitable
                if (price[j] > price[i]):
                    
                    # Update the current profit
                    curr_profit = price[j] - price[i] + helper(price, start, i - 1, memo) + helper(price, j + 1, end, memo)
                    
                    # Update the maximum profit so far
                    profit = max(profit, curr_profit)
        
        # Store the calculated profit in the memoization table
        memo[start][end] = profit
        
        return profit
    
    return helper(price, start, end, memo)


def longestCommonSubsequence_brute(text1, text2):
    if not text1 or not text2:
        return 0
    
    # Create a memoization table to store previously calculated LCS lengths
    memo = [[-1] * (len(text2)+1) for _ in range(len(text1)+1)]
    
    def helper(text1, text2, memo):
        if not text1 or not text2:
            return 0
        
        # If the LCS length has already been calculated, return it from the memoization table
        if memo[len(text1)][len(text2)] != -1:
            return memo[len(text1)][len(text2)]
        
        if text1[-1] == text2[-1]:
            # If the last characters of both texts are the same, increment the LCS length by 1
            lcs_length = 1 + helper(text1[:-1], text2[:-1], memo)
        else:
            # If the last characters of both texts are different, find the maximum LCS length by excluding one character from either text
            lcs_length = max(helper(text1[:-1], text2, memo), helper(text1, text2[:-1], memo))
        
        # Store the calculated LCS length in the memoization table
        memo[len(text1)][len(text2)] = lcs_length
        
        return lcs_length
    
    return helper(text1, text2, memo)

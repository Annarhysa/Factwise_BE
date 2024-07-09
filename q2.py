'''
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
 
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
 
Your score is the sum of the points of the cards you have taken.
 
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
 
Example 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
 
Example 2:
Input: cardPoints = [2,2,2], k = 2
Output: 4
 
Example 3:
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55

'''

def maxScore(cardPoints, k):
    n = len(cardPoints)
    total_sum = sum(cardPoints)
    
    # If k is equal to the number of card points, return the total sum
    if k == n:
        return total_sum
    
    # Find the sum of the window of size n-k
    window_size = n - k
    current_window_sum = sum(cardPoints[:window_size])
    min_window_sum = current_window_sum
    
    for i in range(window_size, n):
        current_window_sum += cardPoints[i] - cardPoints[i - window_size]
        min_window_sum = min(min_window_sum, current_window_sum)
    
    # The result is the total sum minus the minimum window sum
    return total_sum - min_window_sum

# Take input from the user
cardPoints = list(map(int, input("Enter the card points separated by spaces: ").split()))
k = int(input("Enter the number of cards to take (k): "))

# Calculate and print the maximum score
print(maxScore(cardPoints, k))
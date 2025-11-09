# Simple Minimax Algorithm with Alpha-Beta Pruning

def minimax(depth, index, isMax, values, alpha, beta):
    # Base case: return leaf node value
    if depth == 3:
        return values[index]

    if isMax:
        best = float('-inf')
        for i in range(2):
            val = minimax(depth + 1, index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:  # Beta cut-off
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth + 1, index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:  # Alpha cut-off
                break
        return best

# Main Program
values = list(map(int, input("Enter 8 leaf node values separated by spaces: ").split()))
result = minimax(0, 0, True, values, float('-inf'), float('inf'))
print("The optimal value is:", result)

# Enter 8 leaf node values separated by spaces: 3 5 6 9 1 2 0 -1

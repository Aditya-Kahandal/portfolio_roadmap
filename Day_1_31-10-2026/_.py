## Smallest difference between alert ids

'''
You’re given a list of alert IDs in the order they arrived. Find two different positions containing the same ID whose distance is smallest.

Return (alert_id, first_index, second_index), using zero-based indices. If there’s a tie for the smallest distance, choose the pair with the smaller second_index; if still tied, choose the smaller first_index. If no ID repeats, return (-1, -1, -1).

Examples
- [4, 9, 4, 2, 9, 4] → (4, 0, 2)
- [1, 2, 1, 2] → (1, 0, 2) — both pairs are distance 2, so choose the smaller second index.
- [5, 1, 2] → (-1, -1, -1)
Constraints: The list may be empty and can contain up to 100,000 integers, including negative values.
'''

def smallest_diff_alert(arr):
    if len(arr) <=1:
        return (-1,-1,-1)
    seen_indices = {}
    smallest_diff = float('inf')
    first = -1
    second = -1
    alert_id = -1

    for i, element in enumerate(arr):
        if element in seen_indices:
            if smallest_diff > i - seen_indices[element]:
                smallest_diff = i - seen_indices[element]
                alert_id = element
                first = seen_indices[element]
                second = i
            seen_indices[element] = i
        else:
            seen_indices[element] = i
    
    return (alert_id, first, second)


arr = [8,8]

print(smallest_diff_alert(arr))
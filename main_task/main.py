import heapq

def cable_connection_expenses(list_of_cables):
    total_expenses = 0
    if len(list_of_cables) <= 1:
        return total_expenses
    else:
        heap = list_of_cables.copy()
        heapq.heapify(heap)
        while len(heap) > 1:
            connection = heapq.heappop(heap) + heapq.heappop(heap)
            heapq.heappush(heap, connection)
            total_expenses += connection
    return total_expenses

list_of_cables = [3,12,2,5,8,16,1,14,4,7,6,8,9,11]

print(f'Сумарні витрати на зєднання кабелю: {cable_connection_expenses(list_of_cables)}')
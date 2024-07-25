import heapq

def merge_k_lists(lists):
    min_heap = []
    
    # Ініціалізуємо купу першими елементами з кожного списку
    for i, lst in enumerate(lists):
        if lst:  # перевірка на порожній список
            heapq.heappush(min_heap, (lst[0], i, 0))  # (значення, індекс списку, індекс елемента)
    
    result = []
    
    while min_heap:
        value, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(value)
        
        # Якщо список ще має елементи, додаємо наступний елемент до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_value, list_idx, element_idx + 1))
    
    return result

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)

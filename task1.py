import heapq

def min_cost_to_connect_cables(cables):
    # Створюємо купу з довжин кабелів
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки в купі більше одного кабелю
    while len(cables) > 1:
        # Виймаємо два найменших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Вартість з'єднання двох кабелів
        cost = first + second
        total_cost += cost
        
        # Додаємо новий об'єднаний кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6, 9, 12]
print(f"Мінімальні витрати на з'єднання кабелів: {min_cost_to_connect_cables(cables)}")

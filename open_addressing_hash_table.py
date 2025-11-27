import math

# 1. НАЛАШТУВАННЯ
UKR_ALPHABET = {
    'а': 1, 'б': 2, 'в': 3, 'г': 4, 'ґ': 5, 'д': 6, 'е': 7, 'є': 8, 'ж': 9, 'з': 10,
    'и': 11, 'і': 12, 'ї': 13, 'й': 14, 'к': 15, 'л': 16, 'м': 17, 'н': 18, 'о': 19,
    'п': 20, 'р': 21, 'с': 22, 'т': 23, 'у': 24, 'ф': 25, 'х': 26, 'ц': 27, 'ч': 28,
    'ш': 29, 'щ': 30, 'ь': 31, 'ю': 32, 'я': 33
}
TEXT = "Щоб рибу їсти треба в воду лізти"
A_CONST = (math.sqrt(5) - 1) / 2  # Золотий перетин (~0.618)

def get_key(word):
    """Обчислює суму позицій літер (ключ K)"""
    return sum(UKR_ALPHABET.get(c, 0) for c in word.lower())

# 2. ХЕШ-ФУНКЦІЇ
def h_div(k, m):
    return k % m

def h_mult(k, m):
    return math.floor(m * ((k * A_CONST) % 1))

# 3. КЛАС: ВІДКРИТЕ ХЕШУВАННЯ (ЛАНЦЮЖКИ)
class ChainingHash:
    def __init__(self, size, method):
        self.size = size
        self.method = method
        # Таблиця складається зі списків
        self.table = [[] for _ in range(size)]

    def _hash(self, k):
        if self.method == 'div':
            return h_div(k, self.size)
        else: # method == 'mult'
            return h_mult(k, self.size)

    def insert(self, word):
        k = get_key(word)
        idx = self._hash(k)
        # Додаємо слово в кінець ланцюжка
        self.table[idx].append((word, k))

    def display_and_analyze(self):
        print(f"\n--- [Ланцюжки] Метод: {self.method.upper()}, Розмір M={self.size} ---")
        
        total_cmp = 0
        max_cmp = 0
        max_word = ""

        # Візуалізація та підрахунок
        for i, chain in enumerate(self.table):
            display_str = str(chain) if chain else "---"
            print(f"[{i:02d}]: {display_str}")
            
            # Аналіз порівнянь у цьому ланцюжку
            for pos, (word, k) in enumerate(chain):
                # 1-й елемент = 1 порівняння, 2-й = 2 порівняння...
                current_cmp = pos + 1
                total_cmp += current_cmp
                
                if current_cmp > max_cmp:
                    max_cmp = current_cmp
                    max_word = word

        # Вивід статистики
        count_words = sum(len(chain) for chain in self.table)
        avg_cmp = total_cmp / count_words if count_words > 0 else 0
        print(f">> Статистика:")
        print(f"   Середня кількість порівнянь: {avg_cmp:.2f}")
        print(f"   Максимум порівнянь: {max_cmp} (на слові '{max_word}')")

# 4. ЗАПУСК
words = [w.strip(".,") for w in TEXT.split()]
print(f"Слова варіанту: {words}")

# Створення таблиць
chain_div = ChainingHash(size=13, method='div')   # Метод ділення
chain_mult = ChainingHash(size=16, method='mult') # Метод множення

# Заповнення
for w in words:
    chain_div.insert(w)
    chain_mult.insert(w)

# Результати
chain_div.display_and_analyze()
chain_mult.display_and_analyze()

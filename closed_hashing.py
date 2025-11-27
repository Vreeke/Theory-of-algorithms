import math

# 1. НАЛАШТУВАННЯ ===
UKR_ALPHABET = {
    'а': 1, 'б': 2, 'в': 3, 'г': 4, 'ґ': 5, 'д': 6, 'е': 7, 'є': 8, 'ж': 9, 'з': 10,
    'и': 11, 'і': 12, 'ї': 13, 'й': 14, 'к': 15, 'л': 16, 'м': 17, 'н': 18, 'о': 19,
    'п': 20, 'р': 21, 'с': 22, 'т': 23, 'у': 24, 'ф': 25, 'х': 26, 'ц': 27, 'ч': 28,
    'ш': 29, 'щ': 30, 'ь': 31, 'ю': 32, 'я': 33
}
TEXT = "Щоб рибу їсти треба в воду лізти"
A_CONST = (math.sqrt(5) - 1) / 2

def get_key(word):
    return sum(UKR_ALPHABET.get(c, 0) for c in word.lower())

# 2. ХЕШ-ФУНКЦІЇ
def h_div(k, m):
    return k % m

def h_mult(k, m):
    return math.floor(m * ((k * A_CONST) % 1))

# 3. КЛАС: ЗАКРИТЕ ХЕШУВАННЯ (ВІДКРИТА АДРЕСАЦІЯ)
class OpenAddressingHash:
    def __init__(self, size, method):
        self.size = size
        self.method = method
        # Таблиця зберігає просто значення або None
        self.table = [None] * size
        # Словник для збереження кількості порівнянь кожного слова
        self.stats = {}

    def _hash(self, k):
        if self.method == 'div':
            return h_div(k, self.size)
        else:
            return h_mult(k, self.size)

    def insert(self, word):
        k = get_key(word)
        start_idx = self._hash(k)
        
        # Лінійне дослідження
        for i in range(self.size):
            idx = (start_idx + i) % self.size
            
            # Якщо комірка пуста -> вставляємо
            if self.table[idx] is None:
                self.table[idx] = (word, k)
                # Кількість спроб = i + 1 (0 зсув = 1 спроба)
                self.stats[word] = i + 1
                return
            
            # Якщо комірка зайнята -> йдемо на наступну ітерацію (i збільшується)
        
        print(f"ПОМИЛКА: Таблиця переповнена, не можу вставити '{word}'")

    def display_and_analyze(self):
        print(f"\n--- [Відкр. Адресація] Метод: {self.method.upper()}, Розмір M={self.size} ---")
        
        # Візуалізація таблиці
        for i, val in enumerate(self.table):
            display_val = f"{val[0]} (k={val[1]})" if val else "---"
            print(f"[{i:02d}]: {display_val}")

        # Статистика
        if not self.stats:
            print("Таблиця порожня.")
            return

        avg_cmp = sum(self.stats.values()) / len(self.stats)
        max_cmp = max(self.stats.values())
        # Знаходимо слово(а) з максимальною кількістю порівнянь
        max_words = [w for w, c in self.stats.items() if c == max_cmp]
        
        print(f">> Статистика:")
        print(f"   Середня кількість порівнянь: {avg_cmp:.2f}")
        print(f"   Максимум порівнянь: {max_cmp} (слова: {max_words})")

# 4. ЗАПУСК
words = [w.strip(".,") for w in TEXT.split()]
print(f"Слова варіанту: {words}")

# Створення таблиць
oa_div = OpenAddressingHash(size=13, method='div')
oa_mult = OpenAddressingHash(size=16, method='mult')

# Заповнення
for w in words:
    oa_div.insert(w)
    oa_mult.insert(w)

# Результати
oa_div.display_and_analyze()
oa_mult.display_and_analyze()

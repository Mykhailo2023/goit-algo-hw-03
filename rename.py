from pathlib import Path

original_path = Path("example.txt")

# Створює новий об'єкт Path з іншим ім'ям файлу
new_path = original_path.with_name("report222.txt")
original_path.rename(new_path)

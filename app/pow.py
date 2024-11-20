import hashlib
import os
import random

def generate_task(difficulty=3):
    """
    Генерирует задачу для PoW.
    :param difficulty: Количество начальных нулей в хэше.
    :return: Словарь с задачей.
    """
    # Генерация целевого значения с заданным количеством нулей в хэше
    target = "0" * difficulty
    random_string = os.urandom(16).hex()  # Генерация случайной строки
    return {"random_string": random_string, "target": target}

def verify_solution(task, solution):
    """
    Проверяет решение задачи.
    :param task: Словарь с random_string и target.
    :param solution: Решение, представленное участником.
    :return: True, если решение верное, иначе False.
    """
    combined = task["random_string"] + solution
    hash_value = hashlib.sha256(combined.encode()).hexdigest()
    return hash_value.startswith(task["target"])

def generate_challenge(difficulty=3):
    """
    Генерирует сложность задачи для мини-приложения.
    :param difficulty: Уровень сложности (по умолчанию 3).
    :return: Задача для майнинга.
    """
    task = generate_task(difficulty)
    challenge = {"random_string": task["random_string"], "target": task["target"]}
    return challenge

def check_solution(challenge, solution):
    """
    Проверяет решение, предложенное пользователем.
    :param challenge: Задача, с которой пользователь работает.
    :param solution: Решение пользователя.
    :return: Сообщение о правильности решения.
    """
    if verify_solution(challenge, solution):
        return {"status": "success", "message": "Correct solution! You've mined the block!"}
    else:
        return {"status": "failure", "message": "Incorrect solution. Try again."}

def adjust_difficulty(block_number):
    """
    Регулировка сложности майнинга после каждых 10 блоков.
    :param block_number: Номер текущего блока.
    :return: Новый уровень сложности.
    """
    # Увеличиваем сложность каждые 10 блоков
    base_difficulty = 3
    difficulty_increment = 1
    difficulty = base_difficulty + (block_number // 10) * difficulty_increment
    return difficulty

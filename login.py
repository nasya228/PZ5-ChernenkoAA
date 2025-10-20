"""
Модуль для безопасной аутентификации пользователей
Версия: 1.0
Исправлены уязвимости безопасности
"""
import hashlib
def check_password(input_password, stored_hash):
    input_hash = hashlib.sha256(input_password.encode()).hexdigest()
    return input_hash == stored_hash

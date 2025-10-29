def get_mask_card_number(card_number: str) -> str:
    """Функция проверяет размер номера банковской карты на корректность и затем маскирует ее в формате
    XXXX XX** **** XXXX"""
    if card_number is None:
        raise ValueError("Номер карты не может быть None")
    if (len(card_number)) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате **XXXX.

    Args:
        account_number (str): Номер счета в виде строки.

    Returns:
        str: Замаскированный номер счета в формате '**XXXX'.

    Example:
        >>> get_mask_account('1234567890')
        '**7890'
        >>> get_mask_account('73654108430135874305')
        '**4305'
    """
    # Убираем все возможные пробелы из входной строки
    cleaned_number = account_number.replace(" ", "")

    # Проверяем, что номер состоит из цифр и имеет достаточную длину
    if len(cleaned_number) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    if not cleaned_number.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")

    # Берем последние 4 цифры и добавляем две звездочки
    return f"**{cleaned_number[-4:]}"


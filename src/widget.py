
def mask_account_card(card_number: str) -> str:
    """Маскирует номер карты в формате XXXX XX ** XXXX."""
    cleaned = card_number.replace(" ", "")
    if len(cleaned) != 16 or not cleaned.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")

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


    if len(cleaned_number) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    if not cleaned_number.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")

    # Берем последние 4 цифры и добавляем две звездочки
    return f"**{cleaned_number[-4:]}"

    return f"{cleaned[:4]} {cleaned[4:6]} ** *** {cleaned[-4:]}"




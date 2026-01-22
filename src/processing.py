def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция которая возвращает новый список словарей в соответствии с аргументом state (по умолчанию - EXECUTED)"""
    new_list_dict = []

    for sta in list_dict:
        if sta.get("state") == state:
            new_list_dict.append(sta)

    return new_list_dict


def sort_by_date(dict_list, descending=True):
    """
    Сортирует список словарей по дате.

    Args:
        dict_list: список словарей, каждый из которых содержит ключ 'date'
        descending: порядок сортировки (True - по убыванию, False - по возрастанию)

    Returns:
        новый отсортированный список словарей
    """
    if not dict_list:
        return []

    # Проверяем, что все словари содержат ключ 'date'
    for item in dict_list:
        if 'date' not in item:
            raise ValueError("Все словари должны содержать ключ 'date'")

    # Сортируем список, преобразуя строку даты в объект datetime для корректного сравнения
    sorted_list = sorted(
        dict_list,
        key=lambda x: datetime.fromisoformat(x['date']) if isinstance(x['date'], str) else x['date'],
        reverse=descending
    )

    return sorted_list
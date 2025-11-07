from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info):
    """
    обрабатывает информацию как о картах, так и о счетах и возвращает строку с замаскированным номером """
    papse = card_info.split()
    namber = papse[-1]
    if papse[0]=="Счет":
        return " Счет " + get_mask_account(namber)
    return ' '.join(papse[:-1]) +" "+ get_mask_card_number(namber)



def get_date(date_str: str) -> str:
    """
    Принимает строку в формате '2024-03-11T02:26:18.671407'
    и возвращает строку в формате 'ДД.ММ.ГГГГ' (например '11.03.2024').
    """
    # Парсим строку в объект datetime
    dt = datetime.fromisoformat(date_str)

    # Возвращаем в нужном формате
    return dt.strftime("%d.%m.%Y")
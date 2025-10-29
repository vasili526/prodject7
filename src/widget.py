from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info):
    """
    обрабатывает информацию как о картах, так и о счетах и возвращает строку с замаскированным номером """
    papse = card_info.split()
    namber = papse[-1]
    if papse[0]=="Счет":
        return " Счет " + get_mask_account(namber)
    return ' '.join(papse[:-1]) +" "+ get_mask_card_number(namber)


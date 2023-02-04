from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiac_dictionary = {
    'leo': 'Знак задиака лев',
    'scorpio': 'Знак задиака Скорпион'
}


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dictionary.get(sign_zodiac, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"not - {sign_zodiac}")


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dictionary)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Неправильный порядковый номер знака задиака - {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,)) #через Кортеж можно добавить
    # redirect_url = reverse('horoscope-name', args=[name_zodiac]) тоже можно добавить в виде списки
    return HttpResponseRedirect(redirect_url)
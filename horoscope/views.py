from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


zodiac_dictionary = {
    'leo': 'Знак задиака лев',
    'aries': 'Знак задиака aries',
    'scorpio': 'Знак задиака Скорпион',
    'vodoley': 'Знак задиака Водолей',
    'sagittarius': 'Знак задиака sagittarius',
    'taurus': 'Знак задиака taurus',
    'virgo': 'Знак задиака virgo',
    'capricorn': 'Знак задиака capricorn',
    'gemini': 'Знак задиака gemini',
    'libra': 'Знак задиака libra',
    'aquarius': 'Знак задиака aquarius',
    'cancer': 'Знак задиака cancer',
    'pisces': 'Знак задиака pisces',
}

types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}


def index(request):
    zodiacs = list(zodiac_dictionary)
    """
    <ol>
        <li>leo</li>
        <li>scorpio</li>
        <li>vodoley</li>
        ...
    </ol>
    """
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse("horoscope-name", args=[sign])
        li_elements += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)


# def get_info_about_sign_zodiac(request, sign_zodiac: str):
#     description = zodiac_dictionary.get(sign_zodiac, None)
#     if description:
#         return HttpResponse(f'<h2>{description}</h2>')
#     else:
#         return HttpResponseNotFound(f"not - {sign_zodiac}")


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    response = render_to_string('horoscope/info_zodiac.html')
    return HttpResponse(response)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dictionary)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Неправильный порядковый номер знака задиака - {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))  # через Кортеж можно добавить
    # redirect_url = reverse('horoscope-name', args=[name_zodiac]) тоже можно добавить в виде списки
    return HttpResponseRedirect(redirect_url)

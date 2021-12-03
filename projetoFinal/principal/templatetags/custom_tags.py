from django import template
from math import ceil

register = template.Library()

@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()

    dict_[field] = value

    return dict_.urlencode()

@register.simple_tag
def convertToStar(nota):
    nota = int(ceil(nota)) if nota is not None else 0
    if nota == 5:
        return '★★★★★'
    elif nota == 4:
        return '★★★★☆'
    elif nota == 3:
        return '★★★☆☆'
    elif nota == 2:
        return '★★☆☆☆'
    elif nota == 1:
        return '★☆☆☆☆'
    else:
        return 'Sem avaliações'

@register.simple_tag
def convertToText(nota):
    nota = int(ceil(nota)) if nota is not None else 0
    if nota == 5:
        return 'muito positivas'
    elif nota == 4:
        return 'muito positivas'
    elif nota == 3:
        return 'positivas'
    elif nota == 2:
        return 'neutras'
    elif nota == 1:
        return 'ruins'
    else:
        return 'Sem avaliações'
from django import template
from ..models import Marks

register = template.Library()

@register.simple_tag(takes_context=True)
def mark_active(context,result):
    if Marks.objects.filter(mark_user=context['user'], url=result['url']):
        return 'markactive'
    else:
        return ''


@register.simple_tag(takes_context=True)
def mark_8(context):
    marks = Marks.objects.filter(mark_user=context['user'])
    return marks.order_by('-id')[:9]



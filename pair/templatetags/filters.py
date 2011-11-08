from django import template
register = template.Library()

@register.filter
def pair_with(programmer_0,programmer_1):
    if programmer_0==programmer_1:
        return 'delete_programmer('+str(programmer_0.id)+')'
    return 'do_pair('+str(programmer_0.id)+","+str(programmer_1.id)+')'

@register.filter
def pair_time_with(programmer0,programmer1):
    if programmer0==programmer1:
        return 'delete'
    return str(programmer0.pair_time_with(programmer1))
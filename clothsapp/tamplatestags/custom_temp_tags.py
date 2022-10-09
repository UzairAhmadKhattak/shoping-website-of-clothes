from django import template

registor = template.Library()

def zipp(value,arg):

    return zip(value,arg)

registor.simple_tag('zipp',zipp)
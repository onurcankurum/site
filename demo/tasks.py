from celery import shared_task



@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_widgets():
    return Widget.objects.count()


@shared_task
def rename_widget(widget_id, name):
    from core.models import Item
    from datetime import datetime as dt
    w = Item.objects.get(title='Aaa')
    w.price = dt.now().second
    w.save()
from django.core.management import BaseCommand
from django.db import connections


class Command(BaseCommand):
    def handle(self, *args, **options):
        with connections['old'].cursor() as cursor:
            cursor.execute("SELECT * FROM core_order WHERE complete=1")
            orders = cursor.fetchall()

        for order in orders:
            cursor.execute("SELECT * FROM core_orderitem WHERE order_id = '" + str(order[0]) + "'")
            order_items = cursor.fetchall()

            print(order_items)

            #Order.objects.create(
            #    id = order_item.id,
            #    code=order.code,
            #    user_id=order.user_id,
            #    total=sum(item.ambassador_revenue for item in order_items)
            #)
           


from django.core.management import BaseCommand
from core.models import Order, OrderItem


class Command(BaseCommand):
    def handle(self, *args, **options):
        orders = Order.objects.using('old').all()

        for order in orders:
            Order.objects.create(
                id = order_item.id,
                code=order.code,
                transaction_id=order.transaction_id,
                ambassador_email=order.ambassador_email,
                first_name=order.first_name(),
                last_name=order.last_name(),
                email=order.email(),
                address=order.address(),
                country=order.country(),
                city=order.city(),
                zip=order.zip()
            )
           

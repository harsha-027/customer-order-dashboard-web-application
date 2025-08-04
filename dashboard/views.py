from django.http import HttpResponse
import csv
import os
from django.conf import settings
from dateutil import parser
from .models import User, Order


# ----------------------------
# Load Users CSV into User model
# ----------------------------
def load_users_csv(request):
    csv_file_path = os.path.join(settings.BASE_DIR, 'users.csv')

    users = []
    with open(csv_file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(User(
                id=row['id'],
                first_name=row['first_name'],
                last_name=row['last_name'],
                email=row['email'],
                age=int(row['age']),
                gender=row['gender'],
                state=row['state'],
                street_address=row['street_address'],
                postal_code=row['postal_code'],
                city=row['city'],
                country=row['country'],
                latitude=float(row['latitude']),
                longitude=float(row['longitude']),
                traffic_source=row['traffic_source'],
                created_at=parser.parse(row['created_at'])
            ))
    User.objects.bulk_create(users, ignore_conflicts=True)
    return HttpResponse("✅ Users CSV data loaded successfully!")


# ----------------------------
# Load Orders CSV into Order model
# ----------------------------
def load_orders_csv(request):
    csv_file_path = os.path.join(settings.BASE_DIR, 'orders.csv')

    orders = []
    with open(csv_file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            orders.append(Order(
                order_id=row['order_id'],
                user_id=int(row['user_id']),
                status=row['status'],
                gender=row['gender'],
                created_at=parser.parse(row['created_at']),
                returned_at=parser.parse(row['returned_at']) if row['returned_at'] else None,
                shipped_at=parser.parse(row['shipped_at']) if row['shipped_at'] else None,
                delivered_at=parser.parse(row['delivered_at']) if row['delivered_at'] else None,
                num_of_item=int(row['num_of_item'])
            ))
    Order.objects.bulk_create(orders, ignore_conflicts=True)
    return HttpResponse("✅ Orders CSV data loaded successfully!")

# permissions.py
from django.contrib.auth.models import Permission

ADD_EDIT_PRODUCT_PERMISSION = Permission.objects.get_or_create(
    codename='add_edit_product',
    name='Can Add/Edit Product',
    content_type=ContentType.objects.get_for_model(Product)  # Замените на реальный content_type
)[0]

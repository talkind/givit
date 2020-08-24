from django.db import models

# Create your models here.

class ItemRequest:
    id: int
    item :str
    city :str
    special_req: str
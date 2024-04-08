from django.contrib import admin
from core.models import (
    User,
    TokenUser
)

admin.site.register(User)
admin.site.register(TokenUser)

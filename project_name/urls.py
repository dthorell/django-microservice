# from django.contrib import admin   # Uncomment if using admin
# from django.urls import path   # Uncomment if using admin
from rest_framework import routers

# Import your viewsets

router = routers.DefaultRouter()
# Register your ViewSets

urlpatterns = [
    # path("admin/", admin.site.urls),  # Uncomment if using admin
]

urlpatterns += router.urls

from rest_framework import routers
from items import api_views as items_views


router = routers.DefaultRouter()
router.register(r'friends', items_views.FriendViewset)
router.register(r'belongings', items_views.BelongingViewset)
router.register(r'borrowings', items_views.BorrowedViewSet)
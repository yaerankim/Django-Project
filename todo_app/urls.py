from django.urls import include, path
from . import views

# 2) extra-patterns를 사용하여 URLconf에서의 중복 제거하는 방식
extra_patterns = [
    path('add/', views.ItemCreate.as_view(), name="item-add"),
    path('<int:pk>/', views.ItemUpdate.as_view(), name="item-update"),
    path('<int:pk>/delete/', views.ItemDelete.as_view(), name="item-delete"),
]

urlpatterns = [
	path("", views.ListListView.as_view(), name="index"),
    path("list/<int:list_id>/", views.ItemListView.as_view(), name="list"),
    # CRUD patterns for ToDoLists
    path("list/add/", views.ListCreate.as_view(), name="list-add"),
    path(
        "list/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete"
    ),
    # CRUD patterns for ToDoItems
    # 1) 하나의 URL pattern을 사용하는 방식
    # path(
    #     "list/<int:list_id>/item/add/",
    #     views.ItemCreate.as_view(),
    #     name="item-add",
    # ),
    # path(
    #     "list/<int:list_id>/item/<int:pk>/",
    #     views.ItemUpdate.as_view(),
    #     name="item-update",
    # ),
    # path(
    #     "list/<int:list_id>/item/<int:pk>/delete/",
    #     views.ItemDelete.as_view(),
    #     name="item-delete",
    # ),
    ##############################################################
    # 2) extra-patterns를 사용하여 URLconf에서의 중복 제거하는 방식
    path('list/<int:list_id>/item/', include(extra_patterns)),
]
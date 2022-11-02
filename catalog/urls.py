from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("signup_complete/", views.signup_complete, name="signup-complete"),
    path(
        "global_put_comparison/",
        views.global_put_comparison,
        name="global-put-comparison",
    ),
    path("tickers/", views.StockTickerListView.as_view(), name="tickers"),
    path(
        "tickers/<int:pk>", views.StockTickerDetailView.as_view(), name="ticker-detail"
    ),
    path("tickers/create/", views.StockTickerCreate.as_view(), name="ticker-create"),
    path(
        "tickers/<int:pk>/update/",
        views.StockTickerUpdate.as_view(),
        name="ticker-update",
    ),
    path(
        "tickers/<int:pk>/delete/",
        views.StockTickerDelete.as_view(),
        name="ticker-delete",
    ),
    path("my_active_wheels/", views.my_active_wheels, name="my-active-wheels"),
    path("my_completed_wheels/", views.my_completed_wheels, name="my-completed-wheels"),
    path("all_active_wheels/", views.all_active_wheels, name="all-active-wheels"),
    path(
        "all_completed_wheels/", views.all_completed_wheels, name="all-completed-wheels"
    ),
    path(
        "todays_active_wheels/", views.todays_active_wheels, name="todays-active-wheels"
    ),
    path("wheels/<int:pk>", views.OptionWheelDetailView.as_view(), name="wheel-detail"),
    path(
        "wheels/<int:wheel_id>/purchase/<int:pk>",
        views.OptionPurchaseDetailView.as_view(),
        name="purchase-detail-view",
    ),
    path(
        "wheels/<int:wheel_id>/purchase/create/",
        views.OptionPurchaseCreate.as_view(),
        name="purchase-create",
    ),
    path(
        "wheels/<int:wheel_id>/purchase/<int:pk>/update/",
        views.OptionPurchaseUpdate.as_view(),
        name="purchase-update",
    ),
    path(
        "wheels/<int:wheel_id>/purchase/<int:pk>/delete/",
        views.OptionPurchaseDelete.as_view(),
        name="purchase-delete",
    ),
    path("wheels/<int:pk>/complete/", views.complete_wheel, name="wheel-complete"),
    path(
        "wheels/<int:pk>/reactivate/", views.reactivate_wheel, name="wheel-reactivate"
    ),
    path("wheels/create/", views.OptionWheelCreate.as_view(), name="wheel-create"),
    path(
        "wheels/<int:pk>/update/",
        views.OptionWheelUpdate.as_view(),
        name="wheel-update",
    ),
    path(
        "wheels/<int:pk>/delete/",
        views.OptionWheelDelete.as_view(),
        name="wheel-delete",
    ),
    path("my_total_profit/", views.my_total_profit, name="my-total-profit"),
    path("users/", views.UserListView.as_view(), name="users"),
    path("user/<int:pk>/total_profit", views.total_profit, name="user-total-profit"),
    path("user/<int:pk>/active_wheels", views.active_wheels, name="user-active-wheels"),
    path(
        "user/<int:pk>/completed_wheels",
        views.completed_wheels,
        name="user-completed-wheels",
    ),
    path("my_accounts/", views.MyAccountsListView.as_view(), name="my-accounts"),
    path("accounts/<int:pk>", views.AccountDetailView.as_view(), name="account-detail"),
    path("accounts/create/", views.AccountCreate.as_view(), name="account-create"),
    path(
        "accounts/<int:pk>/update/",
        views.AccountUpdate.as_view(),
        name="account-update",
    ),
    path(
        "accounts/<int:pk>/delete/",
        views.AccountDelete.as_view(),
        name="account-delete",
    ),
]

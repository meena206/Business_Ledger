from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("",views.landing_page,name="landing"),

    path("register/", views.register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="ledger/login.html"), name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("customers/", views.customer_list, name="customer_list"),
    path("customers/add/", views.customer_add, name="customer_add"),
    path("customers/<int:customer_id>/", views.customer_detail, name="customer_detail"),
    path("customers/<int:customer_id>/edit/", views.customer_edit, name="customer_edit"),
    path("customers/<int:customer_id>/delete/", views.customer_delete, name="customer_delete"),
    path("customers/<int:customer_id>/transaction/add/", views.transaction_add, name="transaction_add"),

    path("ledger/", views.ledger_history, name="ledger_history"),
    path("reports/", views.reports, name="reports"),
]
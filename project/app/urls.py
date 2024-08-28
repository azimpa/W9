from django.urls import path
from app import views

urlpatterns = [
    path("", views.sign_up, name="signup"),
    path("index", views.index, name="index"),
    path("signup", views.sign_up, name="signup"),
    path("login", views.log_In, name="login"),
    path("logout", views.log_out, name="logout"),
    path("adm", views.adm, name="adm"),
    path("insert", views.insertData, name="insertData"),
    path("update/<id>", views.updateData, name="updateData"),
    path("delete/<id>", views.deleteData, name="deleteData"),
]

from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name='home'), #it says that any url with empty path send it to index function in views.py and name it home
    path("contact/", views.contact, name="contact"),
    path("login/",views.loginUser,name="login"),
    path("logout/",views.logoutUser,name="logout"),
    path("register/",views.registerUser,name="register"),
    path("notes/",views.NoteList.as_view(),name="note_list"),
    path('notes/view/<int:pk>', views.NoteView.as_view(), name='note_view'),
    path('notes/new/', views.NoteCreate.as_view(), name='note_new'),
    path('notes/edit/<int:pk>', views.NoteUpdate.as_view(), name='note_edit'),
    path('notes/delete/<int:pk>', views.NoteDelete.as_view(), name='note_delete'),
]
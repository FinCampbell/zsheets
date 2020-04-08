from django.urls import path

from timesheet.views import BasicView, LoginView, RegisterView

urlpatterns = [
  path("", LoginView.as_view(), name="login"),
  path("register/", RegisterView.as_view(), name="register"),
  path("<pk>/", BasicView.as_view(), name="employee"),
]
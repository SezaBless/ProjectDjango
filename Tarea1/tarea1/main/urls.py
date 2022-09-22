from django.urls import path
from . import views


app_name = "main"
#se elimina los path de portfolio view y portfolio 
#se agrega para el login y se agrega para la creacion de blog 
#se usa el mismo de contact para los comentarios
urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),

	path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.TestimonialAddInfo.as_view(), name="contact"),
#	path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
#	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
	path('blogaddinfo/', views.BlogAddInfo.as_view(), name = "blogaddinfo"),
	]

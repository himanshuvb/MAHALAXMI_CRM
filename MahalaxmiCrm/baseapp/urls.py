from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path
#from Mahalaxmi_CRM.MahalaxmiCrm.baseapp.views import booking_salesPerson
from baseapp import views
from django.conf.urls.static import static
from phonenumber_field.modelfields import PhoneNumberField
urlpatterns = [ path("user_login/",views.user_login,name="user_login"),
               path("dashboard/",views.dashboard,name="dashboard"),
               path("supports/",views.supports,name="supports"),
               path ("", views.home , name="home" ),
               path("add_client/",views.add_client , name="add_client" ),
               path("list_clients/", views.list_clients, name="list_clients"),
               path("client/<int:client_id>", views.delete_client, name="delete_client"),
               path("add_agent/", views.add_agent, name="add_agent"),
               path("list_agents/", views.list_agents, name="list_agents"),
               path("add_project/", views.add_project, name="add_project"),
               path("view_project/", views.view_project, name= "view_project"),
               path("add_properties/", views.add_properties, name="add_properties"),
               path("list_properties/", views.list_properties, name="list_properties"),
               path("all_leads/", views.all_leads, name="all_leads"),
               path("fresh_leads/", views.fresh_leads, name="fresh_leads"),
               path("old_followups/", views.old_followups, name="old_followups"),
               path("todays_followups/", views.todays_followups, name="todays_followups"),
               path("upcoming_followups/", views.upcoming_followups, name="upcoming_followups"),
               path("add_new_leads/", views.add_new_leads, name="add_new_leads"),
               path("add_user/", views.add_user, name="add_user"),
               path("history/", views.history, name="history"),
               path("password/",views.password, name="password"),
               path("masters_add_source/", views.masters_add_source, name="masters_add_source"),
               path("masters_add_amenities/", views.masters_add_amenities, name="masters_add_amenities"),
               path("masters_add_property_type", views.masters_add_property_type, name="masters_add_property_type"),
               path("add_payment/", views.add_payment, name="add_payment"),
               path("view_payment/", views.view_payment, name="view_payment"),
               path("add_agreement/",views.add_agreement, name="add_agreement"),
               path("view_agreement/", views.view_agreement, name="view_agreement"),
               path("navbar_admin/", views.navbar_admin, name = "navbar_admin"),
               path("navbar_telecaller/", views.navbar_telecaller, name="navbar_telecaller"),
               path("navbar_salesPerson/", views.navbar_salesPerson, name="navbar_salesPerson"),
               #SalesPerson
               path("sales_login/", views.sales_login, name="sales_login"),
               path("dashboard_salesPerson/", views.dashboard_salesPerson, name= "dashboard_salesPerson"),
               path("booking_salesPerson/", views.booking_salesPerson, name="booking_salesPerson"),
               path("delete_salesperson/<int:add_salesperson_id>/delete/", views.delete_salesperson, name="delete_salesperson"),
               path("TotalBookings_salesPerson/", views.TotalBookings_salesPerson, name="TotalBookings_salesPerson"),
               path("TodaysVisit_salesPerson/", views.TodaysVisit_salesPerson, name="TodaysVisit_salesPerson"),
               #SalesPerson--FollowUps
               path('FollowUps_salesPerson/', views.FollowUps_salesPerson , name = "followUps_salesPerson"),
               path("OldFollowUps_salesPerson/", views.OldFollowUps_salesPerson, name="OldFollowUps_salesPerson"),
               path("TodaysFollowUps_salesPerson/", views.TodaysFollowUps_salesPerson, name="TodaysFollowUps_salesPerson"),
               path("UpComingFollowUps_salesPerson/", views.UpComingFollowUps_salesPerson, name= "UpcomingFollowUps_salesPerson"),
               #Telecaller
               path("telecaller_login/", views.telecaller_login , name="telecaller_login"),
               path("dashboard_telecaller/", views.dashboard_telecaller, name="dashboard_telecaller"),
               path("BookingList_telecaller/", views.BookingList_telecaller, name="BookingList_telecaller"),
               path("newLead_telecaller/", views.NewLead_telecaller , name="NewLead_telecaller"),
               path("delete_telecaller/<int:add_telecaller_id>/delete/", views.delete_telecaller, name="delete_telecaller"),
               path("listLead_telecaller/", views.ListLead_telecaller, name="ListLead_telecaller"),
               path("TotalBookings_telecaller/", views.TotalBookings_telecaller, name="TotalBookings_telecaller"),
               #VisitList
               path("addVisit/" , views.addVisit , name="addVisit"),
               path("visitList_telecaller/", views.VisitList_telecaller, name="VisitList_telecaller"),
               path('deadLead_telecaller/', views.deadLead_telecaller, name="deadLead_telecaller"),
               #Telecaller--FollowUps
               
               path("OldFollowUps_telecaller/", views.OldFollowUps_telecaller , name="OldFollowUps_telecaller"),
               path("TodaysFollowUps_telecaller/", views.TodaysFollowUps_telecaller, name="TodaysFollowUps_telecaller"),
               path("UpcomingFollowUps_telecaller/", views.UpComingFollowUps_telecaller, name="UpcomingFollowUps_telecaller"),
               path("addFollowUps/", views.addFollowUps , name="addFollowUps"),
               path("followups_telecaller/", views.followUps_telecaller , name = "followups_telecaller"),
               #Admin
               path("dashboard_admin", views.dashboard_admin , name="dashboard_admin"),
               path("add_telecaller/", views.add_telecaller, name="add_telecaller"),
               path("list_telecaller/", views.list_telecaller, name="list_telecaller"),
               path("add_salesperson/", views.add_salesperson, name="add_salesperson"),
               path("list_salesperson/", views.list_salesperson, name="list_salesperson"),
               path("employee_review/", views.employee_review, name="employee_review"),
               path("confirmed_bookings/", views.confirmed_bookings, name="confirmed_bookings"),
               path("ongoing_sites/", views.ongoing_sites, name="ongoing_sites"),
               path("add_sites/", views.add_sites, name = "add_sites")]
urlpatterns += static(settings.STATIC_URL)

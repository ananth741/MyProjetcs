from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from .models import Events, Menus, MenuList, Message
from django.urls import reverse
from datetime import date
from django import forms

# Create your views here.


def index(request):
    return render(request, "demo/UserLogin.html")


def user_login(request):
    user_name = request.POST["username"]
    pasw = request.POST["psw"]
    user = authenticate(request, username=user_name, password=pasw)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "demo/UserLogin.html", {"message": "Invalid Credentials"})


def user_logout(request):
    logout(request)
    return render(request, "demo/UserLogin.html", {"message": "Logged Out."})


def home(request):
    if not request.user.is_authenticated:
        return render(request, "demo/UserLogin.html", {"message": None})
    return render(request, "demo/home.html")


def newevent(request):
    if not request.user.is_authenticated:
        return render(request, "demo/UserLogin.html", {"message": None})
    context = {
        "Menus": Menus.objects.all()
    }
    return render(request, "demo/EventRegistration.html", context)


def eventdetails(request, event_id):
    if not request.user.is_authenticated:
        return render(request, "demo/UserLogin.html", {"message": None})
    try:
        event = Events.objects.get(pk=event_id)
    except Events.DoesNotExist:
        raise Http404("Event Doesn't exist.")
    context = {
        "event": event
    }
    return render(request, "demo/EventDetails.html", context)


def eventslist(request):
    if not request.user.is_authenticated:
        return render(request, "demo/UserLogin.html", {"message": None})
    context = {
        "events": Events.objects.all()
    }
    return render(request, "demo/EventsList.html", context)


def navigator(request):
    if not request.user.is_authenticated:
        return render(request, "demo/UserLogin.html", {"message": None})
    return render(request, "demo/Navigation bar.html")


def contact(request):
    if not request.user.is_authenticated:
        return render(request, "demo/UserLogin.html", {"message": None})
    return render(request, "demo/contact.html")


def newmenu(request):
    if not request.user.is_authenticated:
        return render(request, "demo/UserLogin.html", {"message": None})
    context = {
        "starters": MenuList.objects.all().filter(Category="Starters"),
        "main_menus": MenuList.objects.all().filter(Category="Main Menu"),
        "desserts": MenuList.objects.all().filter(Category="Desserts"),
    }
    return render(request, "demo/NewMenu.html",context)


def menudetails(request, menu_id):
    if not request.user.is_authenticated:
        return render(request, "demo/UserLogin.html", {"message": None})
    try:
        menu = Menus.objects.get(pk=menu_id)
    except Events.DoesNotExist:
        raise Http404("menu Doesn't exist.")
    context = {
        "menu": menu
    }
    return render(request, "demo/MenuDetails.html", context)


def menulist(request):
    if not request.user.is_authenticated:
        return render(request, "demo/UserLogin.html", {"message": None})
    context = {
        "menus": Menus.objects.all()
    }
    return render(request, "demo/MenuList.html", context)


def messages(request):
    if not request.user.is_authenticated:
        return render(request, "demo/UserLogin.html", {"message": None})
    context = {
        "msgs": Message.objects.all()
    }
    return render(request, "demo/Messages.html", context)


def book_event(request):
    if not request.user.is_authenticated:
        return render(request, "demo/UserLogin.html", {"message": None})
    f_name = request.POST["fname"]
    l_name = request.POST["lname"]
    email = request.POST["email"]
    e_phone = request.POST["ephone"]
    e_location = request.POST["elocation"]
    e_city = request.POST["ecity"]
    e_Occasion = request.POST["Occasion"]
    e_style = request.POST["style"]
    e_date = request.POST["edate"]
    e_menu = request.POST["Menu"]
    curr_date = date.today()
    e_choice = ""

    if 'ebreakfast' in request.POST:
        e_choice = e_choice + " " + "Breakfast"

    if 'elunch' in request.POST:
        e_choice = e_choice + " " + "Lunch"

    if 'edinner' in request.POST:
        e_choice = e_choice + " " + "Dinner"

    event = Events(First_Name=f_name, Last_Name=l_name, Email=email, Phone=e_phone, Location=e_location,
                   City=e_city, Occation=e_Occasion, Event_Style=e_style, Event_Date=e_date,
                   Event_Choice=e_choice, Menu_Id=e_menu, Created_date=curr_date)
    event.save()
    context = {
        "event": event
    }

    return render(request, "demo/EventDetails.html", context)


def ifnull(val1, val2):
    if val1 is None:
        return val2
    return val2


def book_menu(request):
    if not request.user.is_authenticated:
        return render(request, "demo/UserLogin.html", {"message": None})
    m_name = request.POST["menuname"]
    m_category = request.POST["m_category"]
    m_type = request.POST["m_type"]
    m_time = request.POST["m_time"]
    m_veg_non_veg = request.POST["m_veg"]
    m_date = date.today()
    m_starters = ""
    m_main_menu = ""
    m_dessert = ""

    for key, value in request.POST.items():
        if value == "on":
            item = MenuList.objects.get(pk=key)
            if item.Category == "Starters":
                m_starters = m_starters + item.Name + " "

            if item.Category == "Main Menu":
                m_main_menu = m_main_menu + item.Name + " "

            if item.Category == "Desserts":
                m_dessert = m_dessert + item.Name + " "

    menu = Menus(Menu_Name=m_name, Category=m_category, Type=m_type, Time=m_time, Veg_Nonveg=m_veg_non_veg, Starters=m_starters, Main_Menu=m_main_menu, Dessert=m_dessert, Created_date= m_date)
    menu.save()
    context = {
        "menu": menu
    }
    return render(request, "demo/menudetails.html", context)


def message_in(request):
    if not request.user.is_authenticated:
        return render(request, "demo/UserLogin.html", {"message": None})
    m_date = date.today()
    m_name = request.POST["Name"]
    m_email = request.POST["Email"]
    m_msg_text = request.POST["Message"]
    m_user_id = request.user

    if "Like" in request.POST:
        m_liked = True
    else:
        m_liked = False
    print(m_date, m_name, m_email, m_msg_text, m_user_id)

    msg = Message(Date=m_date, Name=m_name, Email=m_email, Liked=m_liked, Msg_text=m_msg_text, User_id=m_user_id)
    msg.save()
    return HttpResponseRedirect(reverse("home"))





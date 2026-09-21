from PresentationLaye.Main_view import MainView
from BusinessLayer.user_busines_logic import UserBusinesLogic


user_business = UserBusinesLogic()


MainView(user_business)
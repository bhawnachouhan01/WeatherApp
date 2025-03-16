#use tkinker to make graphics
from tkinter import *
from tkinter import ttk
#make an api call (current weather data)
import requests

#crating a fuction to get data
def data_get():
    city = city_name.get()

    #get data from api requests call
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=bb3808839c6dae4bd443865888b584a3").json()
    #transfer  data in weather ,description , temp, pressure , wind speed from get_data
    w_lable1.config(text=data["weather"][0]["main"])
    wd_lable1.config(text=data["weather"][0]["description"])
    temp_lable1.config(text=str(int(data["main"]["temp"]-273.15)))
    pr_lable1.config(text=data["main"]["pressure"])
    wind_lable1.config(text=data["wind"]["speed"])

#creating a window
win = Tk()
win.title("Bhawna Chouhan")
win.config(bg = "cyan")
win.geometry("500x640")

name_lable = Label(win,text="My Weather App", font=("Time New Roman",30,"bold"))
name_lable.place(x=25, y=50, height=50, width=450)

##creating combo box variable 
city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="My Weather App",values=list_name, font=("Time And Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)


##creating weather ,  decription , temp , pressure box
##weather
w_lable = Label(win,text="Weather Climate", font=("Time New Roman",17))
w_lable.place(x=25, y=260, height=50, width=210)
## weather output box
w_lable1 = Label(win,text="", font=("Time New Roman",17))
w_lable1.place(x=250, y=260, height=50, width=210)


##weather description
wd_lable = Label(win,text="Description", font=("Time New Roman",17))
wd_lable.place(x=25, y=330, height=50, width=210)
##weather description output box
wd_lable1 = Label(win,text="", font=("Time New Roman",17))
wd_lable1.place(x=250, y=330, height=50, width=210)


##Weather temperature
temp_lable = Label(win,text="Temperature ", font=("Time New Roman",17))
temp_lable.place(x=25, y=400, height=50, width=210)
##weather temperature output box
temp_lable1 = Label(win,text=" ", font=("Time New Roman",17))
temp_lable1.place(x=250, y=400, height=50, width=210)


##Pressure
pr_lable = Label(win,text="Pressure", font=("Time New Roman",17))
pr_lable.place(x=25, y=470, height=50, width=210)
##pressure output box
pr_lable1 = Label(win,text="", font=("Time New Roman",17))
pr_lable1.place(x=250, y=470, height=50, width=210)


## wind speed
wind_lable = Label(win,text="Wind speed",font=("Time New Roman",17))
wind_lable.place(x=25,y=540, height=50, width=210)
## wind speed output box
wind_lable1 = Label(win, text="", font=("Time And Roman",17))
wind_lable1.place(x=250 , y=540, height=50, width=210)


##creating a Done button
done_button = Button(win,text="Done", font=("Time And Roman",20,"bold"),command=data_get)
done_button.place(y=190, height=50, width=100, x=200)

win.mainloop()



from tkinter import *
import requests
from pprint import pprint

def show():
    api_address = "http://api.openweathermap.org/data/2.5/weather?units=metric&appid=62e494ce9c2b59c2b686b2afa9b8e244&q="
    city=str(entry_1.get())
    url = api_address + city
    json_data = requests.get(url).json()
    # pprint(json_data)
    # print("------------------------------------------------------")
    temp = json_data['main']['temp']
    temp_max = json_data['main']['temp_max']
    temp_min = json_data['main']['temp_min']
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind_speed = json_data['wind']['speed']
    wind_direction = json_data['wind']['deg']
    cloudiness = json_data['clouds']['all']
    lon = json_data['coord']['lon']
    lat = json_data['coord']['lat']

    label_temp.config(text="{} degree celcius".format(temp))
    label_maxtemp.config(text="{} degree celcius".format(temp_max))
    label_mintemp.config(text="{} degree celcius".format(temp_min))
    label_pressure.config(text="{} hPa".format(pressure))
    label_humidity.config(text="{} %".format(humidity))
    label_WindSpeed.config(text="{} m/s".format(wind_speed))
    label_WindDirection.config(text="{} degrees".format(wind_direction))
    label_Cloudiness.config(text="{} %".format(cloudiness))
    label_Longitude.config(text="{} ".format(lon))
    label_Latitude.config(text="{} ".format(lat))
def Location():
    x=entry_2.get()
    y=entry_3.get()
    api_address=("http://api.openweathermap.org/data/2.5/weather?units=metric&appid=62e494ce9c2b59c2b686b2afa9b8e244&lon={}&lat={}").format(x,y)
    # longitude = str(entry_2.get())
    # latitude = str(entry_3.get())

    url = api_address

    json_data = requests.get(url).json()
    # pprint(json_data)

    lon=json_data['coord']['lon']
    lat=json_data['coord']['lat']

    temp = json_data['main']['temp']
    temp_max = json_data['main']['temp_max']
    temp_min = json_data['main']['temp_min']
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind_speed = json_data['wind']['speed']
    wind_direction = json_data['wind']['deg']
    cloudiness = json_data['clouds']['all']

    label_temp.config(text="{} degree celcius".format(temp))
    label_maxtemp.config(text="{} degree celcius".format(temp_max))
    label_mintemp.config(text="{} degree celcius".format(temp_min))
    label_pressure.config(text="{} hPa".format(pressure))
    label_humidity.config(text="{} %".format(humidity))
    label_WindSpeed.config(text="{} m/s".format(wind_speed))
    label_WindDirection.config(text="{} degrees".format(wind_direction))
    label_Cloudiness.config(text="{} %".format(cloudiness))
    label_Longitude.config(text="{} ".format(lon))
    label_Latitude.config(text="{} ".format(lat))

root = Tk()

root.title("Weather")


background_image = PhotoImage(file="Background.png")
background_label = Label(root, image=background_image)
background_label.place(x = 0,y = 0,relwidth = 1, relheight = 1)

root.iconbitmap('download_HTw_icon.ico')

root.geometry('2000x1000')


New_Background = Label(root, bg="#FFE162", width=115, height=50)
New_Background.place(x=200, y=20)




Welcome=Label(root,text="Weather App",font=("Arial Black",50), bg="#FFE162") 
Welcome.place(x=500,y=20)

City = Label(root,text = "Enter City Name:-  ",font=("Arial",20),bg="white",fg="black")
City.place(x=500,y=150)

entry_1 = Entry(root,width=30)
print(entry_1.get())
entry_1.place(x=800,y=150,height=35)

Longitude = Label(root,text = "Enter Longitude..:  ",font=("Arial",20),bg="white",fg="black")
Longitude.place(x=500,y=200)

entry_2 = Entry(root,width=30)
print(entry_2.get())
entry_2.place(x=800,y=200,height=35)

Latitude = Label(root,text = "Enter Latitude.....:  ",font=("Arial",20),bg="white",fg="black")
Latitude.place(x=500,y=250)

entry_3 = Entry(root,width=30)
print(entry_3.get())
entry_3.place(x=800,y=250,height=35)


# Button
b1 = Button(root, text = "Show Weather",fg="black", bg = "firebrick3", command=show,width=19,height=1,font=("Helvetica",10))
b1.place(x=1000,y=150)


b2= Button(root, text= "Show Lan & Lat",fg="black", bg= "firebrick3",command=Location,width=19, height=1, font=("Helvetica",10))
b2.place(x=1000,y=250)


l1=Label(root,width=30,height=2,text="Temperature",font=("Arial",10),bg="white",fg="black")
l1.place(x=500,y=300)

l2=Label(root,width=30,height=2,text="Maximum Temperature",font=("Arial",10),bg="white",fg="black")
l2.place(x=500,y=350)

l3=Label(root,width=30,height=2,text="Minimum Temperature",font=("Arial",10),bg="white",fg="black")
l3.place(x=500,y=400)

l4=Label(root,width=30,height=2,text="Pressure",font=("Arial",10),bg="white",fg="black")
l4.place(x=500,y=450)

l5=Label(root,width=30,height=2,text="Humidity",font=("Arial",10),bg="white",fg="black")
l5.place(x=500,y=500)

l6=Label(root,width=30,height=2,text="Wind Speed",font=("Arial",10),bg="white",fg="black")
l6.place(x=500,y=550)

l7=Label(root,width=30,height=2,text="Wind Direction",font=("Arial",10),bg="white",fg="black")
l7.place(x=500,y=600)

l8=Label(root,width=30,height=2,text="Cloudiness",font=("Arial",10),bg="white",fg="black")
l8.place(x=500,y=650)

l10=Label(root,width=30,height=2,text="Longitude",font=("Arial",10),bg="white",fg="black")
l10.place(x=500,y=700)

l11=Label(root,width=30,height=2,text="Latitude",font=("Arial",10),bg="white",fg="black")
l11.place(x=500,y=750)

label_temp=Label(root,width=25)
label_temp.place(x=800,y=300)

label_maxtemp=Label(root,width=25)
label_maxtemp.place(x=800,y=350)

label_mintemp=Label(root,width=25)
label_mintemp.place(x=800,y=400)

label_pressure=Label(root,width=25)
label_pressure.place(x=800,y=450)

label_humidity=Label(root,width=25)
label_humidity.place(x=800,y=500)

label_WindSpeed=Label(root,width=25)
label_WindSpeed.place(x=800,y=550)

label_WindDirection=Label(root,width=25)
label_WindDirection.place(x=800,y=600)

label_Cloudiness=Label(root,width=25)
label_Cloudiness.place(x=800,y=650)

label_Longitude=Label(root,width=25)
label_Longitude.place(x=800,y=700)

label_Latitude=Label(root,width=25)
label_Latitude.place(x=800,y=750)

root.mainloop()

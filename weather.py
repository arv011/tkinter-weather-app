import tkinter as tk
import requests
from tkinter import ttk
from tkinter import font,messagebox


def weather_response(weather):
    try:
        name = weather['name']
        country = weather['sys']['country']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nCountry: %s \nConditions: %s \nTemperature (°F): %s' % (name,country, desc, temp)
    except:
        if entry.get()=='':
            messagebox.showwarning('invalid field','please fill the field')
        else:
            final_str = 'problem! cannot retrive the data'
    return final_str


def get_weather(city):
    weather_key= '61ee9339d9dfce23e98fb66ae8637bed'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'celcius'}
    response=requests.get(url,params=params)
    weather_current=response.json()
    # print(weather_current)
    label['text'] = weather_response(weather_current)
    


win =tk.Tk()
win.title('Worldwide Weather')
# win.geometry('500x600')
canvas = tk.Canvas(win,height=500,width=600)
canvas.pack()
background_image = tk.PhotoImage(file = "pic.png")
background_label = tk.Label(win,image=background_image)
background_label.place(relwidth=1, relheight=1)
# background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(win, bg='#FCFF33', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40,command=lambda : get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(win, bg='#FCFF33', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)


win.mainloop()


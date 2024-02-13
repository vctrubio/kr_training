import os
import requests
import json
import datetime

from tkinter import Tk, Label, Button, Text, Scrollbar, Frame
from PIL import Image, ImageTk


'''
Find the streamlit version online 

https://kreative-weatherman.streamlit.app/
git repo https://github.com/vctrubio/weatherman_streamlit

> I stored the data in a json file - because we are only allowed one call per day
> requirements> pip install pillow 
> logo.png is can't be upload... see full project in the git repo


'''


def pretty_date_now():
    date_now = datetime.datetime.now()
    if date_now.strftime("%m-%d") == "02-14":
        return "It's Valentine's Day, what are you doing here?"
    return date_now.strftime("%H O'clock, @ %M mins, in year %Y, of %B-%d")

def get_request(address='London'):
    key = 'C2REQFLYJ8L2B9TKC595H7TTZ'

    tmp_date = str(datetime.date.today()) + '.json'
    tmp_dir = '/json_data/'
    tmp_file = str(os.path.dirname(os.path.abspath(__file__))) + tmp_dir + tmp_date

    try:
        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{address}/last30days?unitGroup=us&key={key}'
        response = requests.get(url)
        data = response.json()
        with open(tmp_file, 'w') as file:
            json.dump(data, file)
            print('get_json_call, succesfull; ', response.status_code)
    except:
        print('no data to show, probably already made an api call. check again mañana; ',
              response.status_code)
    return tmp_file

def tkinter():
    TK_BTN_CONFIG = {'padx': 5, 'pady': 5}
    DATA_KEYS = ['tempmax', 'tempmin', 'tempmax', 'precip', 'windspeed', 'windgust', 'winddir', 'pressure', 'cloudcover', 'visibility', 'sunrise', 'sunset']

    def extraction(data_file):
        print('extracting data from: ', data_file)
        with open(data_file, 'r') as file:
            data = json.load(file)

        if (data):
            print('Succesfull extraction of data')
            return data
        else:
            print('No data to show')
            return

    def show_weather(data, weather_type):
        text.delete('1.0', 'end')
        text.insert('1.0', '\n'.join(f"On: {day['datetime']}: {day[weather_type]} < {weather_type}" for day in data))


    #Weather confif
    weather_data = extraction(get_request(address='London'))
    label = weather_data.get('resolvedAddress', 'Unkown')
    itr_days = weather_data['days']
    title = f'Weather in {label} for the last 30 days'

    #TKJ CONFIG
    tk = Tk()
    tk.title(title)
    tk.geometry('1000x800')

    #SET DIV 1
    logo_frame = Frame(tk, padx=10, pady=10)
    logo_frame.grid(row=0, column=0)
    
    image = Image.open("logo.png")
    image = image.resize((100, 100))
    photo = ImageTk.PhotoImage(image)
    logo_label = Label(logo_frame, image=photo, width=100, height=100)
    logo_label.pack()

    
    #SET DIV 2
    button_frame = Frame(tk, padx=10, pady=10)
    button_frame.grid(row=0, column=1)

    for index, item in enumerate(DATA_KEYS):
        row = index // 4  
        column = index % 4 
        Button(button_frame, text=f"Show {item}", command=lambda item=item: show_weather(itr_days, item)).grid(row=row, column=column, **TK_BTN_CONFIG)

    text_frame = Frame(tk)
    text_frame.grid(row=1, column=0, columnspan=2, sticky='nsew')

    text = Text(text_frame, wrap='word', width=100, height=34)
    text.pack(padx=10, pady=10)

    #SET DIV 3
    bottom_frame = Label(tk, text=pretty_date_now(), fg='yellow')
    bottom_frame.grid(row=2, column=0, columnspan=2, pady=25) 

    tk.mainloop()
    return itr_days

i = tkinter()
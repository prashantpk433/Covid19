# dash for layout
import io
import pandas as pd
import numpy as np
from random import random
from bs4 import BeautifulSoup
import requests
from tkinter import*
import tkinter as tk
from tkinter.messagebox import showerror,showinfo




def get_corona_data():
    url = "https://www.worldometers.info/coronavirus/"
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text
    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    gdp_table = soup.find("table", id="main_table_countries_today")
    gdp_table_data = gdp_table.tbody.find_all("tr")

    # Getting all countries names
    dicts = {}
    for i in range(len(gdp_table_data)):
        try:
            key = (gdp_table_data[i].find_all('a', href=True)[0].string)
        except:
            key = (gdp_table_data[i].find_all('td')[0].string)

        value = [j.string for j in gdp_table_data[i].find_all('td')]
        dicts[key] = value
    live_data = pd.DataFrame(dicts).drop(0).T.iloc[:, :12]
    live_data.columns = ["Total Cases", "New Cases", "Total Deaths", "New Deaths", "Total Recovered", "Active",
                         "Serious Critical",
                         "Tot Cases/1M pop","Deaths/1M pop","Total Tests","Tests/1M pop","Population"]
    live_data.index.name = 'Country'

    ### your file is saved here
    live_data.iloc[:, :12].to_csv("data.csv")

def download():
    get_corona_data()
    showinfo("Message","Successfully Downloaded")




root=tk.Tk()
root.geometry('400x330')
root.title("Corona Data Downloader")
root.iconbitmap("icon.ico")
root.config(background='White')
f = ("poppins", 25, 'bold')
button=Button(root ,text="Download Now",border=3,bg="black",fg="white",font=f,command=download).pack(expand=TRUE)


root.mainloop()



import tkinter as tk
from tkinter import ttk
from nomdelarue import nom
import geopy
from geopy.geocoders import Nominatim
geocoders=Nominatim(user_agent='http')

def callbackFunc():
    rue=nom((float(latitudeString.get()),float(longitudeString.get())))
    resultString.set("À "+str(rue[0])+', '+str(rue[1])+', '+str(rue[2]) )
     
app = tk.Tk() 
app.geometry('200x100')

labelLatitude = tk.Label(app,text = "Latitude")
labelLatitude.grid(column=0, row=0, sticky=tk.W)
labelLongitude = tk.Label(app,text = "Longitude")
labelLongitude.grid(column=0, row=1, sticky=tk.W)

latitudeString = tk.StringVar()
longitudeString = tk.StringVar()
entryLatitude = tk.Entry(app, width=20, textvariable=latitudeString)
entryLongitude = tk.Entry(app, width=20, textvariable=longitudeString)

entryLatitude.grid(column=1, row=0, padx=10)
entryLongitude.grid(column=1, row=1, padx=10)


resultButton = tk.Button(app, text = 'Localiser',command=callbackFunc)

resultButton.grid(column=0, row=2, pady=10, sticky=tk.W)

resultString=tk.StringVar()
resultLabel = tk.Label(app, textvariable=resultString)
resultLabel.grid(column=1, row=2, padx=10, sticky=tk.W)

app.mainloop()
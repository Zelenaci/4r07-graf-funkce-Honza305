#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:00:39 2019
@author: mah35070
"""

import tkinter as tk
from tkinter import LabelFrame, Radiobutton, Label, IntVar, Entry, Message, Button, messagebox, StringVar
import pylab as lab
from tkinter import filedialog


class Application(tk.Tk):
    name = 'Graf'

    def __init__(self):
        super().__init__(className=self.name)
        
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        
        self.lblffce = LabelFrame(self, text="Graf matematické funkce", padx=5, pady=5)
        self.lblffce.grid(column = 1, row = 1)
        
        self.lblfce = Label(self.lblffce)
        self.lblfce.grid(row= 1, column = 1)
        
        self.v = IntVar()
        
        self.radsin = Radiobutton(self.lblfce, text="sin" , variable=self.v, value=0)
        self.radsin.grid(column=1, row=1)
        
        self.radlog = Radiobutton(self.lblfce, text="log" , variable=self.v, value=1)
        self.radlog.grid(column=1, row=2)
        
        self.radexp = Radiobutton(self.lblfce, text="exp" , variable=self.v, value=2)
        self.radexp.grid(column=1, row=3)
        
        self.lblodd = Label(self.lblffce)
        self.lblodd.grid(row=1, column = 2)
        
        self.msgo = Message(self.lblodd, text = "Od")
        self.msgo.grid(row = 1 , column = 1)
        
        self.Sod= StringVar()
        
        self.ode= Entry(self.lblodd, textvariable=self.Sod, width=10)
        self.ode.grid(row=1,column=2)
        
        self.msgd = Message(self.lblodd, text=u"Do:")
        self.msgd.grid(row=2, column=1)
        
        self.Sdo= StringVar()
        
        self.doe=Entry(self.lblodd, textvariable=self.Sdo,width=10)
        self.doe.grid(row=2,column=2)
        
        self.ugraf= Button(self,text=u"Vytvoř graf", width=7, height=4, command=self.vytvorgraf)
        self.ugraf.grid(row=1,column=2)
        
        self.genztext=LabelFrame(self,text=u"Generuj z text", padx=25)
        self.genztext.grid(row=2,column=1)
        
        self.asv=StringVar()
        self.asv.set("")
        
        self.centr= Entry(self.genztext, textvariable=self.asv)
        self.centr.grid(row=1,column=1)
        
        self.vs=Button(self.genztext,text=u"Vyber soubor", command=self.vybrsoubor)
        self.vs.grid(row=2,column=1)
        
        self.vgb=Button(self,text=u"Vytvořit graf", width=7, height=4, command=self.vytvorgrsoubor)
        self.vgb.grid(row=2,column=2)
        
        self.oylblf=LabelFrame(self,text=u"Popisy os", padx=40)
        self.oylblf.grid(row=3,column=1)
        
        self.oxmess = Message(self.oylblf, text=u"Osa X:")
        self.oxmess.grid(row=1, column=1)
        
        self.ox=StringVar()
        
        self.oxentr=Entry(self.oylblf, textvariable=self.osx,width=10)
        self.oxentr.grid(row=1,column=2)
        
        self.oymess = Message(self.oylblf, text=u"Osa Y:")
        self.oymess.grid(row=2, column=1)
        
        self.oy=StringVar()
        
        self.oyentr=Entry(self.oylblf, textvariable=self.osy,width=10)
        self.oyentr.grid(row=2,column=2)
        
def vybrsoubor(self):
    cesta= filedialog.askopenfilename(title='Vyber soubor')    
    if cesta != '':
        self.a.set(cesta)

def vytvorgraf(self):
    try:
        od=float(self.sod.get())
        do=float(self.sdo.get())
        x=lab.linspace(od, do, 500)
        if self.v.get() == 1:
            y=lab.sin(x)
        elif self.v.get() == 2:
            y=lab.log10(x)
        elif self.v.get() == 3:
            y=lab.exp(x)
        lab.figure()
        lab.plot(x,y)
        lab.xlabel(self.osx.get())
        lab.ylabel(self.osy.get())
        lab.grid(True)
        lab.show()
    except:
        messagebox.showerror(title='Chybné meze', message='Meze osy X\njako reálná čísla')        
            
def vytvorgrsoubor(self):
        try:
            cesta = self.a.get()
            f = open(cesta,'r')
            x=[]
            y=[]
            while 1:
                radek=f.readline()
                if radek=='':
                    break
                cisla=radek.split()
                x.append( float(cisla[0]) )
                y.append( float(cisla[1]) )
            f.close()
            lab.figure()
            lab.plot(x,y)
            lab.xlabel(self.osx.get())
            lab.ylabel(self.osy.get())
            lab.grid(True)
            lab.show()
        except:
            messagebox.showerror(title='Chybný formát', message='Graf se nepodařilo vytvořit,\n zkontrolujte fomát souboru.')
        
app = Application()
app.mainloop()

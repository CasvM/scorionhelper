# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 09:50:15 2017

@author: cwvanmierlo
"""

#TODO: make the GUI and tools threaded

from tkinter import Tk;
from tkinter import Toplevel;
from tkinter.ttk import Style, Progressbar;

from tkinter import Frame;
from tkinter import Button;
from tkinter import Text;
from tkinter import Label;
from tkinter import StringVar;
from tkinter import IntVar;
from tkinter import Entry;
from tkinter import Radiobutton;
from tkinter import Checkbutton;

from tkinter import NORMAL;
from tkinter import DISABLED;
from tkinter import END;
from tkinter import HORIZONTAL;
from tkinter import LEFT;

from tkinter import font;
from tkinter.filedialog import askopenfile;
from tkinter.messagebox import showerror;

from Tools import getGroups;
from Tools import splitGroups;
from Tools import createScorionGroups;
from Tools import errorChecker;

import os;
import sys;

#variables
framewidth = 400;
topBarHeight = 24;
frameheight = 400 + topBarHeight;
title = "Scorion Tool";
fgColor = "#f2f2f2";
fg2Color = "#0f0f0f"
hyperlinkColor = "#68a3ff";
errorColor = "#ff3030";
topBarColor = "#192231";
bgColor = "#494E6B";
bg2Color = "#5D6387";
bg3Color = "#727aa8";
codeBGColor = "#393d56"
codeBG2Color = "#2d3042"
buttonColor = "#985E6D";
buttonPressedColor = "#A36474";
buttonHoverColor = "#AB6879";
disabledButtonColor = "#cccccc";



nextprevButtonWidth = 100;
nextprevButtonHeight = 24;
nextprevButtonPaddingX = 16
nextprevButtonPaddingY = 16 + topBarHeight;

#TODO: formatting, clear var names, documentation, updated manual

global tb;
tb = "Unknown error";

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path);

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs);
    def show(self):
        self.lift();

class Page1(Page):
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs);

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs);

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs);

class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs);

class Page5(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs);

class Page6(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs);
       
class Page7(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs); 
       
class Page8(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs);

class Page9(Page):
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs);

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs);
        
        self.toForeGround
        ################### init, main config ######################
        container = Frame(self, bg=bgColor);
        container.pack(side="top", fill="both", expand=True);       
        
        
        self.ft1 = font.Font(family='Arial', size=11);     
        self.ft2 = font.Font(family='MS Gothic', size=10);
        self.ft3 = font.Font(family='Arial', size=9);
        self.ft4 = font.Font(family='Arial', size=10);
        self.ft5 = font.Font(family='Arial', size=14);
        self.ft6 = font.Font(family="Courier", size = 9);
        
        self.p1 = Page1(container, bg=container["background"]);
        self.p2 = Page2(container, bg=container["background"]);
        self.p3 = Page3(container, bg=container["background"]);
        self.p4 = Page4(container, bg=container["background"]);
        self.p5 = Page5(container, bg=container["background"]);
        self.p6 = Page6(container, bg=container["background"]);
        self.p7 = Page7(container, bg=container["background"]);
        self.p8 = Page8(container, bg=container["background"]);
        self.p9 = Page9(container, bg=container["background"]);
        
        topBar = Frame(container, bg=topBarColor, width=container.winfo_width() * framewidth, height=topBarHeight);
        topBar.place(x=0, y=0);
        
        self.p1.place(in_=container, x=0, y= topBar["height"], relwidth=1, relheight=1);
        self.p2.place(in_=container, x=0, y= topBar["height"], relwidth=1, relheight=1);
        self.p3.place(in_=container, x=0, y= topBar["height"], relwidth=1, relheight=1);
        self.p4.place(in_=container, x=0, y= topBar["height"], relwidth=1, relheight=1);
        self.p5.place(in_=container, x=0, y= topBar["height"], relwidth=1, relheight=1);
        self.p6.place(in_=container, x=0, y= topBar["height"], relwidth=1, relheight=1);      
        self.p7.place(in_=container, x=0, y= topBar["height"], relwidth=1, relheight=1);
        self.p8.place(in_=container, x=0, y= topBar["height"], relwidth=1, relheight=1);
        self.p9.place(in_=container, x=0, y= topBar["height"], relwidth=1, relheight=1);
        
        close= Button(topBar, text=u"\u2715", command= lambda: self.close(), bg=topBar["background"], bd=0, font = self.ft2, fg=fgColor, activebackground="#940000");
        close.place(x = topBar["width"] - topBar["height"], y = 0, width = topBar["height"], height= topBar["height"]);
        
        minim = Button(topBar, text="_", command= lambda: self.toicon(), bg=topBar["background"], bd=0, font=self.ft2, fg=fgColor, activebackground="#364969");
        minim.place(x = topBar["width"] - 2 * topBar["height"], y = 0, width = topBar["height"], height= topBar["height"]);
        
        label = Label(topBar, text=title, font=self.ft3, bg=topBar["background"], fg=fgColor);
        label.place(x = 5, y = 0, height= topBar["height"]);
        
        #event handlers so the window can be moved
        topBar.bind("<ButtonPress-1>", self.StartMove);
        topBar.bind("<ButtonRelease-1>", self.StopMove);
        topBar.bind("<B1-Motion>", self.OnMotion);
        
        label.bind("<ButtonPress-1>", self.StartMove);
        label.bind("<ButtonRelease-1>", self.StopMove);
        label.bind("<B1-Motion>", self.OnMotion);
        
        close.bind("<Enter>", self.closeEnterBG);
        close.bind("<Leave>", self.topBarButtonNormalBG);
        
        minim.bind("<Enter>", self.minimEnterBG);
        minim.bind("<Leave>", self.topBarButtonNormalBG);
        
        self.master.bind("<Unmap>", self.toiconify);
        self.master.bind("<Map>", self.todeiconify);
        
        ##################### page 1, intro ############################
        
        T1 = Text(self.p1, height = 8, width = 31, font=self.ft5, bg=bgColor, fg=fgColor, bd=0);
        T1.place(x=10, y=10);
        
        HelpButton = Label(self.p1, text = "help", background=bgColor, fg = hyperlinkColor, font = self.ft5, cursor="hand2");
        HelpButton.place(x=8, y=53);
        
        underlineFont = font.Font(HelpButton, HelpButton.cget("font"));
        underlineFont.configure(underline = True);
        
        HelpButton.configure(font=underlineFont);
        HelpButton.bind("<Button-1>", lambda x: self.clickHelp())
        
        T2 = Text(self.p1, height = 8, width = 31, font=self.ft5, bg=bgColor, fg=fgColor, bd=0);
        T2.place(x=53, y=55);
        
        
        T1.insert(END, "Welcome to the ELS Scorion tool. Click next to select what tool to use, or press\n");
        T2.insert(END, "to learn more about the tool.");
        
        T1.configure(state=DISABLED);
        T2.configure(state=DISABLED);
        
        nextButtonP1 = Button(self.p1, text = "Next", command=self.p2.lift, background=buttonColor, foreground=fgColor, bd=0, font=self.ft1, activebackground=buttonPressedColor, activeforeground=fgColor);
        nextButtonP1.place(x = framewidth - nextprevButtonWidth - nextprevButtonPaddingX, y = frameheight - nextprevButtonHeight - nextprevButtonPaddingY, width = nextprevButtonWidth, height = nextprevButtonHeight);
        nextButtonP1.bind("<Enter>", self.buttonEnterBG);
        nextButtonP1.bind("<Leave>", self.buttonNormalBG);

        ################## page 2, task picker #########################
        instrLabel = Label(self.p2, text = "Choose what tool to use", bg=self.p2["background"], fg=fgColor, font=self.ft5);
        instrLabel.place(x= 30, y = 10);
        buildGroupsButton = Button(self.p2, text = "Build Scorion groups", command=self.p3.lift, background=buttonColor, foreground=fgColor, bd=0, font=self.ft5, activebackground=buttonPressedColor, activeforeground=fgColor);
        buildGroupsButton.place(x = 75, y = 48, width = 250, height = 2*nextprevButtonHeight);
        
        buildGroupsButton.bind("<Enter>", self.buttonEnterBG);
        buildGroupsButton.bind("<Leave>", self.buttonNormalBG);
        
        splitGroupsButton = Button(self.p2, text = "Split Scorion file", command=self.p4.lift, background=buttonColor, foreground=fgColor, bd=0, font=self.ft5, activebackground=buttonPressedColor, activeforeground=fgColor);
        splitGroupsButton.place(x = 75, y = 120, width = 250, height = 2*nextprevButtonHeight);
        
        splitGroupsButton.bind("<Enter>", self.buttonEnterBG);
        splitGroupsButton.bind("<Leave>", self.buttonNormalBG);
        
        onlyFileButton = Button(self.p2, text = "Only create Scorion file", command=self.p5.lift, background=buttonColor, foreground=fgColor, bd=0, font=self.ft5, activebackground=buttonPressedColor, activeforeground=fgColor);
        onlyFileButton.place(x = 75, y = 192, width = 250, height = 2*nextprevButtonHeight);
        
        onlyFileButton.bind("<Enter>", self.buttonEnterBG);
        onlyFileButton.bind("<Leave>", self.buttonNormalBG);
        
        possibleErrorButton = Button(self.p2, text = "Find errors in file", command=self.p8.lift, background=buttonColor, foreground=fgColor, bd=0, font=self.ft5, activebackground=buttonPressedColor, activeforeground=fgColor);
        possibleErrorButton.place(x = 75, y = 264, width = 250, height = 2*nextprevButtonHeight);
        
        possibleErrorButton.bind("<Enter>", self.buttonEnterBG);
        possibleErrorButton.bind("<Leave>", self.buttonNormalBG);
        
        previousButtonP2 = Button(self.p2, text = "Back", command=self.p1.lift, background=buttonColor, foreground=fgColor, bd=0, font=self.ft1, activebackground=buttonPressedColor, activeforeground=fgColor);
        previousButtonP2.place(x = nextprevButtonPaddingX, y = frameheight - nextprevButtonHeight - nextprevButtonPaddingY, width = nextprevButtonWidth, height = nextprevButtonHeight);
        
        previousButtonP2.bind("<Enter>", self.buttonEnterBG);
        previousButtonP2.bind("<Leave>", self.buttonNormalBG);
        
        
        ################## page 3, group builder ######################## 
        previousButtonP3 = Button(self.p3, text = "Back", command=self.p2.lift, background=buttonColor, foreground=fgColor, bd=0, font=self.ft1, activebackground=buttonPressedColor, activeforeground=fgColor);
        previousButtonP3.place(x = nextprevButtonPaddingX, y = frameheight - nextprevButtonHeight - nextprevButtonPaddingY, width = nextprevButtonWidth, height = nextprevButtonHeight);
        
        previousButtonP3.bind("<Enter>", self.buttonEnterBG);
        previousButtonP3.bind("<Leave>", self.buttonNormalBG);
        
        courseIdWrap = Frame(self.p3, bg= self.p3["background"]);
        courseIdWrap.place(x = 10, y = 10, width = framewidth - 20, height = topBarHeight)
        
        self.courseVar = StringVar();
        self.courseVar.trace("w", lambda name, index, mode, courseVar=self.courseVar: self.firecallback());
        
        courseIdLabel = Label(courseIdWrap, text = "Course Id:", bg=self.p3["background"], fg=fgColor, font=self.ft4);
        courseIdLabel.place(x= 0, y = 0, height = topBarHeight);
        
        courseId = Entry(courseIdWrap, width= 45, bg=bg2Color, textvariable=self.courseVar,fg=fgColor, borderwidth = 0, font=self.ft4, insertbackground=fgColor, insertofftime= 500, insertontime= 500);
        courseId.place(x = 65, y = 0, height=topBarHeight);
        
        
        fileWrap = Frame(self.p3, bg =self.p3["background"]);
        fileWrap.place(x = 10, y = 44, width = framewidth - 20, height = topBarHeight);
        
        
        fileLabel = Label(fileWrap, text = "File:", bg=self.p3["background"], fg=fgColor, font=self.ft4);
        fileLabel.place(x= 30, y = 0, height = topBarHeight);
        
        self.fileVar = StringVar();
        self.fileVar.trace("w", lambda name, index, mode, fileVar=self.fileVar: self.firecallback());

        self.fileName = Entry(fileWrap, width= 36, textvariable=self.fileVar,bg=bg2Color, fg=fgColor, borderwidth = 0, font=self.ft4, insertbackground=fgColor, insertofftime= 500, insertontime= 500);
        self.fileName.place(x = 65, y = 0, height= topBarHeight);


        #TODO: drag files into the text field
        self.browse = Button(fileWrap, text="Browse", command=self.load_file, background=buttonColor, foreground=fgColor, bd=0, font=self.ft4, activebackground=buttonPressedColor, activeforeground=fgColor, anchor="center");
        self.browse.place(x=326, y=0, height = topBarHeight, width=60);
        
        self.browse.bind("<Enter>", self.buttonEnterBG);
        self.browse.bind("<Leave>", self.buttonNormalBG);        
        
        
        seperatorWrap = Frame(self.p3, bg = self.p3["background"]);
        seperatorWrap.place(x=10, y = 106, height = 2*topBarHeight + 2, width = framewidth - 20);
        
        optionLabel = Label(seperatorWrap, text="What seperator is used in the file?", bg=self.p3["background"], fg=fgColor, font=self.ft4);
        optionLabel.place(x = 0, y = 0, height = topBarHeight);
      
        optionList = [("Comma ( , )", ","),("Semicolon ( ; )", ";")];
        
        self.sepVar = StringVar();
        self.sepVar.set(optionList[0][1]);
        
        commaButton = Radiobutton(seperatorWrap, text=optionList[0][0], variable = self.sepVar, value=optionList[0][1], anchor="w", padx=5, bg=bg2Color, fg=fgColor, activebackground=bg2Color, activeforeground=fgColor, selectcolor=bg2Color);
        semiColonButton = Radiobutton(seperatorWrap, text=optionList[1][0], variable = self.sepVar, value=optionList[1][1], anchor="w", padx=5, bg=bg2Color, fg=fgColor, activebackground=bg2Color, activeforeground=fgColor, selectcolor=bg2Color);
        
        commaButton.place(x=260, y=0, height=topBarHeight, width = 120);
        semiColonButton.place(x=260, y = topBarHeight + 2, width = 120);
        
        
        optionLabel = Label(self.p3, text="Do you already have a Scorion File?");
        
        scorionCheckWrap = Frame(self.p3, bg = self.p3["background"]);
        scorionCheckWrap.place(x=10, y = 194, height=topBarHeight, width = framewidth - 20);
        
        self.checkVar = IntVar();
        
        scorionCheck = Checkbutton(scorionCheckWrap, text="Create a Scorion file?", var = self.checkVar, font=self.ft4, fg=fgColor, bg=bg2Color, bd=0, highlightthickness = 0, selectcolor=bg2Color, activeforeground=fgColor, activebackground= bg2Color);
        scorionCheck.select();        
        scorionCheck.place(x=210, y=0, height=topBarHeight, width = 170);
        
        
        self.goButton = Button(self.p3, text = "Run", command=self.combineFuncs, state=DISABLED,background=disabledButtonColor, foreground=fgColor, bd=0, font=self.ft1, activebackground=disabledButtonColor, activeforeground=fgColor, disabledforeground=fg2Color);
        self.goButton.place(x = framewidth - nextprevButtonWidth - nextprevButtonPaddingX, y = frameheight - nextprevButtonHeight - nextprevButtonPaddingY, width = nextprevButtonWidth, height = nextprevButtonHeight);
    
        
        ################### page 4, split groups page ########################
        previousButtonP4 = Button(self.p4, text = "Back", command=self.p2.lift, background=buttonColor, foreground=fgColor, bd=0, font=self.ft1, activebackground=buttonPressedColor, activeforeground=fgColor);
        previousButtonP4.place(x = nextprevButtonPaddingX, y = frameheight - nextprevButtonHeight - nextprevButtonPaddingY, width = nextprevButtonWidth, height = nextprevButtonHeight);
        
        previousButtonP4.bind("<Enter>", self.buttonEnterBG);
        previousButtonP4.bind("<Leave>", self.buttonNormalBG);
        
        scorFileWrap = Frame(self.p4, bg =self.p4["background"]);
        scorFileWrap.place(x = 10, y = 10, width = framewidth - 20, height = topBarHeight);
        
        
        fileLabel = Label(scorFileWrap, text = "Scorion File:", bg=self.p4["background"], fg=fgColor, font=self.ft4);
        fileLabel.place(x= 0, y = 0, height = topBarHeight);
        
        self.scorFileVar = StringVar();
        self.scorFileVar.trace("w", lambda name, index, mode, scorFileVar=self.scorFileVar: self.firecallback1());

        self.scorFileName = Entry(scorFileWrap, width= 34, textvariable=self.scorFileVar,bg=bg2Color, fg=fgColor, borderwidth = 0, font=self.ft4, insertbackground=fgColor, insertofftime= 500, insertontime= 500);
        self.scorFileName.place(x = 79, y = 0, height= topBarHeight);

        self.browse1 = Button(scorFileWrap, text="Browse", command=self.load_file1, background=buttonColor, foreground=fgColor, bd=0, font=self.ft4, activebackground=buttonPressedColor, activeforeground=fgColor, anchor="center");
        self.browse1.place(x=326, y=0, height = topBarHeight, width=60);
        
        self.browse1.bind("<Enter>", self.buttonEnterBG);
        self.browse1.bind("<Leave>", self.buttonNormalBG);
        
        errFileWrap = Frame(self.p4, bg =self.p4["background"]);
        errFileWrap.place(x = 10, y = 44, width = framewidth - 20, height = topBarHeight);
        
        
        errLabel = Label(errFileWrap, text = "Error File:", bg=self.p4["background"], fg=fgColor, font=self.ft4);
        errLabel.place(x= 0, y = 0, height = topBarHeight);
        
        self.errFileVar = StringVar();
        self.errFileVar.trace("w", lambda name, index, mode, errFileVar=self.errFileVar: self.firecallback1());

        self.errFileName = Entry(errFileWrap, width= 36, textvariable=self.errFileVar,bg=bg2Color, fg=fgColor, borderwidth = 0, font=self.ft4, insertbackground=fgColor, insertofftime= 500, insertontime= 500);
        self.errFileName.place(x = 65, y = 0, height= topBarHeight);

        self.browse2 = Button(errFileWrap, text="Browse", command=self.load_file2, background=buttonColor, foreground=fgColor, bd=0, font=self.ft4, activebackground=buttonPressedColor, activeforeground=fgColor, anchor="center");
        self.browse2.place(x=326, y=0, height = topBarHeight, width=60);
        
        self.browse2.bind("<Enter>", self.buttonEnterBG);
        self.browse2.bind("<Leave>", self.buttonNormalBG);
        
        self.goButtonP4 = Button(self.p4, text = "Run", command=self.combineFuncs2, state=DISABLED,background=disabledButtonColor, foreground=fgColor, bd=0, font=self.ft1, activebackground=disabledButtonColor, activeforeground=fgColor, disabledforeground=fg2Color);
        self.goButtonP4.place(x = framewidth - nextprevButtonWidth - nextprevButtonPaddingX, y = frameheight - nextprevButtonHeight - nextprevButtonPaddingY, width = nextprevButtonWidth, height = nextprevButtonHeight);
        
        ################### page 5, only create groups page ##################
        previousButtonP5 = Button(self.p5, text = "Back", command=self.p2.lift, background=buttonColor, foreground=fgColor, bd=0, font=self.ft1, activebackground=buttonPressedColor, activeforeground=fgColor);
        previousButtonP5.place(x = nextprevButtonPaddingX, y = frameheight - nextprevButtonHeight - nextprevButtonPaddingY, width = nextprevButtonWidth, height = nextprevButtonHeight);
        
        previousButtonP5.bind("<Enter>", self.buttonEnterBG);
        previousButtonP5.bind("<Leave>", self.buttonNormalBG);
        
        courseIdWrap2 = Frame(self.p5, bg= self.p5["background"]);
        courseIdWrap2.place(x = 10, y = 10, width = framewidth - 20, height = topBarHeight)
        
        self.courseVar2 = StringVar();
        self.courseVar2.trace("w", lambda name, index, mode, courseVar2=self.courseVar2: self.firecallback2());
        
        courseIdLabel2 = Label(courseIdWrap2, text = "Course Id:", bg=self.p5["background"], fg=fgColor, font=self.ft4);
        courseIdLabel2.place(x= 0, y = 0, height = topBarHeight);
        
        courseId2 = Entry(courseIdWrap2, width= 45, bg=bg2Color, textvariable=self.courseVar2,fg=fgColor, borderwidth = 0, font=self.ft4, insertbackground=fgColor, insertofftime= 500, insertontime= 500);
        courseId2.place(x = 65, y = 0, height=topBarHeight);
        
        
        fileWrap2 = Frame(self.p5, bg =self.p5["background"]);
        fileWrap2.place(x = 10, y = 44, width = framewidth - 20, height = topBarHeight);
        
        
        fileLabel2 = Label(fileWrap2, text = "File:", bg=self.p5["background"], fg=fgColor, font=self.ft4);
        fileLabel2.place(x= 30, y = 0, height = topBarHeight);
        
        self.fileVar2 = StringVar();
        self.fileVar2.trace("w", lambda name, index, mode, fileVar2=self.fileVar2: self.firecallback2());

        self.fileName2 = Entry(fileWrap2, width= 36, textvariable=self.fileVar2,bg=bg2Color, fg=fgColor, borderwidth = 0, font=self.ft4, insertbackground=fgColor, insertofftime= 500, insertontime= 500);
        self.fileName2.place(x = 65, y = 0, height= topBarHeight);

        self.browse3 = Button(fileWrap2, text="Browse", command=self.load_file3, background=buttonColor, foreground=fgColor, bd=0, font=self.ft4, activebackground=buttonPressedColor, activeforeground=fgColor, anchor="center");
        self.browse3.place(x=326, y=0, height = topBarHeight, width=60);
        
        self.browse3.bind("<Enter>", self.buttonEnterBG);
        self.browse3.bind("<Leave>", self.buttonNormalBG);        
        
        
        seperatorWrap2 = Frame(self.p5, bg = self.p5["background"]);
        seperatorWrap2.place(x=10, y = 106, height = 2*topBarHeight + 2, width = framewidth - 20);
        
        optionLabel2 = Label(seperatorWrap2, text="What seperator is used in the file?", bg=self.p5["background"], fg=fgColor, font=self.ft4);
        optionLabel2.place(x = 0, y = 0, height = topBarHeight);
      
        optionList2 = [("Comma ( , )", ","),("Semicolon ( ; )", ";")];
        
        self.sepVar2 = StringVar();
        self.sepVar2.set(optionList2[0][1]);
        
        commaButton2 = Radiobutton(seperatorWrap2, text=optionList2[0][0], variable = self.sepVar2, value=optionList2[0][1], anchor="w", padx=5, bg=bg2Color, fg=fgColor, activebackground=bg2Color, activeforeground=fgColor, selectcolor=bg2Color);
        semiColonButton2 = Radiobutton(seperatorWrap2, text=optionList2[1][0], variable = self.sepVar2, value=optionList2[1][1], anchor="w", padx=5, bg=bg2Color, fg=fgColor, activebackground=bg2Color, activeforeground=fgColor, selectcolor=bg2Color);
    
        commaButton2.place(x=260, y=0, height=topBarHeight, width = 120);
        semiColonButton2.place(x=260, y = topBarHeight + 2, width = 120);
        
        self.goButtonP5 = Button(self.p5, text = "Run", command=self.combineFuncs3, state=DISABLED,background=disabledButtonColor, foreground=fgColor, bd=0, font=self.ft1, activebackground=disabledButtonColor, activeforeground=fgColor, disabledforeground=fg2Color);
        self.goButtonP5.place(x = framewidth - nextprevButtonWidth - nextprevButtonPaddingX, y = frameheight - nextprevButtonHeight - nextprevButtonPaddingY, width = nextprevButtonWidth, height = nextprevButtonHeight);
        
        
        ################### page 6, progress page ###########################
        self.cancelButton = Button(self.p6, text = "cancel", command=lambda:sys.exit(), background=buttonColor, foreground=fgColor, bd=0, font=self.ft1, activebackground=buttonPressedColor, activeforeground=fgColor);
        self.cancelButton.place(x = nextprevButtonPaddingX, y = frameheight - nextprevButtonHeight - nextprevButtonPaddingY, width = nextprevButtonWidth, height = nextprevButtonHeight);
        
        self.cancelButton.bind("<Enter>", self.buttonEnterBG);
        self.cancelButton.bind("<Leave>", self.buttonNormalBG);
        
        self.progressLabel = Label(self.p6, text = "Working, this might take a couple of minutes...", bg=self.p6["background"], fg=fgColor, font=self.ft1)        
        self.progressLabel.place(x=10, y=36);
        
        
        #TODO: make the progressbar actually progress to the things that are done
        style = Style();    
        style.theme_use('alt')
        style.configure("els.Horizontal.TProgressbar", background=fgColor);        
        
        self.progress = Progressbar(self.p6, orient=HORIZONTAL, length = framewidth - 20, mode="indeterminate", style="els.Horizontal.TProgressbar", maximum=40);  
        self.progress.place(x=10, y=10);
        self.progress.start(17);
        
        self.closeP6 = Button(self.p6, text = "Close", command=self.close, background=buttonColor, foreground=fgColor, bd=0, font=self.ft1, activebackground=buttonPressedColor, activeforeground=fgColor);    
        
        
        ################### page 7, error page ###########################
        #TODO: implement full stacktrace instead of only 2
        #TODO: or: make a log file of the stacktrace that can be "downloaded" when clicked
        #TODO: error page is not working correctly anymore; errors are being cut off
        self.errorLabel = Label(self.p7, text = "Something went wrong, try again or contact Cas", bg=self.p7["background"], fg=errorColor, font=self.ft1);
        self.errorLabel.place(x=36, y=10);

        self.errorInfoLabel = Label(self.p7, text = "Error Info:", bg=self.p7["background"], fg=fgColor, font=self.ft1);
        self.errorInfoLabel.place(x=36, y=50);

        self.stackTraceStringVar1 = StringVar();
        self.stackTraceStringVar2 = StringVar();
        
        self.stackTraceLabel1 = Label(self.p7, textvariable = self.stackTraceStringVar1, bg=self.p7["background"], fg=errorColor, font=self.ft1, wraplength = 350, justify=LEFT);
        self.stackTraceLabel2 = Label(self.p7, textvariable = self.stackTraceStringVar2, bg=self.p7["background"], fg=errorColor, font=self.ft1, wraplength = 350, justify=LEFT);
        
        self.stackTraceStringVar1.set(self.getStackTrace()[0]);
        self.stackTraceStringVar2.set(self.getStackTrace()[1]);
        
        self.stackTraceLabel1.place(x=36, y=70);
        self.stackTraceLabel2.place(x=36, y=110);
        
        self.backToMenu = Button(self.p7, text = "Back to menu", command=self.backtomenu, background=buttonColor, foreground=fgColor, bd=0, font=self.ft1, activebackground=buttonPressedColor, activeforeground=fgColor);
        self.backToMenu.place(x = nextprevButtonPaddingX, y = frameheight - nextprevButtonHeight - nextprevButtonPaddingY, width = nextprevButtonWidth, height = nextprevButtonHeight);
        self.backToMenu.bind("<Enter>", self.buttonEnterBG);
        self.backToMenu.bind("<Leave>", self.buttonNormalBG);

        self.closeP7 = Button(self.p7, text = "Close", command=self.close, background=buttonColor, foreground=fgColor, bd=0, font=self.ft1, activebackground=buttonPressedColor, activeforeground=fgColor);
        self.closeP7.place(x = framewidth - nextprevButtonWidth - nextprevButtonPaddingX, y = frameheight - nextprevButtonHeight - nextprevButtonPaddingY, width = nextprevButtonWidth, height = nextprevButtonHeight);
        self.closeP7.bind("<Enter>", self.buttonEnterBG);
        self.closeP7.bind("<Leave>", self.buttonNormalBG);
        
        
        ################### page 8, find error page ###########################
        previousButtonP8 = Button(self.p8, text = "Back", command=self.p2.lift, background=buttonColor, foreground=fgColor, bd=0, font=self.ft1, activebackground=buttonPressedColor, activeforeground=fgColor);
        previousButtonP8.place(x = nextprevButtonPaddingX, y = frameheight - nextprevButtonHeight - nextprevButtonPaddingY, width = nextprevButtonWidth, height = nextprevButtonHeight);
        
        previousButtonP8.bind("<Enter>", self.buttonEnterBG);
        previousButtonP8.bind("<Leave>", self.buttonNormalBG);
        
        checkErrFileWrap = Frame(self.p8, bg =self.p8["background"]);
        checkErrFileWrap.place(x = 10, y = 10, width = framewidth - 20, height = 3*topBarHeight);
        
        
        checkErrLabel = Label(checkErrFileWrap, text = "File to check for Errors:", bg=self.p4["background"], fg=fgColor, font=self.ft4);
        checkErrLabel.place(x= 0, y = 0, height = topBarHeight);
        
        self.checkErrFileVar = StringVar();
        self.checkErrFileVar.trace("w", lambda name, index, mode, checkErrFileVar=self.checkErrFileVar: self.firecallback3());

        self.checkErrFileName = Entry(checkErrFileWrap, width= 45, textvariable=self.checkErrFileVar,bg=bg2Color, fg=fgColor, borderwidth = 0, font=self.ft4, insertbackground=fgColor, insertofftime= 500, insertontime= 500);
        self.checkErrFileName.place(x = 2, y = 25, height= topBarHeight);

        self.browse4 = Button(checkErrFileWrap, text="Browse", command=self.load_file4, background=buttonColor, foreground=fgColor, bd=0, font=self.ft4, activebackground=buttonPressedColor, activeforeground=fgColor, anchor="center");
        self.browse4.place(x=326, y=25, height = topBarHeight, width=60);
        
        self.browse4.bind("<Enter>", self.buttonEnterBG);
        self.browse4.bind("<Leave>", self.buttonNormalBG);
        
        self.goButtonP8 = Button(self.p8, text = "Run", command=self.p9.lift, state=DISABLED,background=disabledButtonColor, foreground=fgColor, bd=0, font=self.ft1, activebackground=disabledButtonColor, activeforeground=fgColor, disabledforeground=fg2Color);
        self.goButtonP8.place(x = framewidth - nextprevButtonWidth - nextprevButtonPaddingX, y = frameheight - nextprevButtonHeight - nextprevButtonPaddingY, width = nextprevButtonWidth, height = nextprevButtonHeight);
        
        ################### page 9, find error results ###########################
        previousButtonP9 = Button(self.p9, text = "Back", command=self.p8.lift, background=buttonColor, foreground=fgColor, bd=0, font=self.ft1, activebackground=buttonPressedColor, activeforeground=fgColor);
        previousButtonP9.place(x = nextprevButtonPaddingX, y = frameheight - nextprevButtonHeight - nextprevButtonPaddingY, width = nextprevButtonWidth, height = nextprevButtonHeight);
        
        previousButtonP9.bind("<Enter>", self.buttonEnterBG);
        previousButtonP9.bind("<Leave>", self.buttonNormalBG);
        
              
        #testing
        self.checkErrFileName.delete(0, END);
        self.checkErrFileName.insert(0, r"M:\ud\os\ssc\imos\bbsup\@ new folder_Surfdrive\7. Scorion\Vakmappen 171804\46597-171804\group_import_no_TAs.txt");
        
        self.errors = errorChecker(self.checkErrFileVar.get());
        self.croppedErrors = self.errors[0:7]
        
        if (len(self.errors) > 0):
            Label(self.p9, text = "Found %d possible errors, on the following lines:" %len(self.errors), fg = fgColor, bg = bgColor, font = self.ft1).place(x=16, y=12);


            openFile = Button(self.p9, text = "Open file", command=lambda: self.clickOpenFile(), background=buttonColor, foreground=fgColor, bd=0, font=self.ft1, activebackground=buttonPressedColor, activeforeground=fgColor);
            openFile.place(x = framewidth - nextprevButtonWidth - nextprevButtonPaddingX, y = frameheight - nextprevButtonHeight - nextprevButtonPaddingY, width = nextprevButtonWidth, height = nextprevButtonHeight);
        
            openFile.bind("<Enter>", self.buttonEnterBG);
            openFile.bind("<Leave>", self.buttonNormalBG);            
            
            self.drawErrors();
            
        else:
             Label(self.p9, text = "Found no errors", fg = fgColor, bg = bgColor, font = self.ft5).place(x=10, y=10);    
                
                
        ################### finally, show page 1 to start ################
        self.p1.show();
        
       
        
    ################### window event handlers ##########################
    def StartMove(self, event):
        self.master.x = event.x;
        self.master.y = event.y;

    def StopMove(self, event):
        self.master.x = None;
        self.master.y = None;

    def OnMotion(self, event):
        deltax = event.x - self.master.x;
        deltay = event.y - self.master.y;
        x = self.master.winfo_x() + deltax;
        y = self.master.winfo_y() + deltay;
        self.master.geometry("+%s+%s" % (x, y));
    
    def toForeGround(self):
        self.master.lift();
    
    def toicon(self):
        self.master.update_idletasks();
        self.master.overrideredirect(False);
        self.master.iconify();
    
    def toiconify(self, event):
        self.master.overrideredirect(False);
        
    def todeiconify(self, event):
        self.master.overrideredirect(True);
        
    def closeEnterBG(self, event):
        event.widget.config(bg="#C40000");
    
    def minimEnterBG(self, event):
        event.widget.config(bg="#455D85")
    
    def topBarButtonNormalBG(self, event):
        event.widget.config(bg=topBarColor);

    def buttonEnterBG(self, event):
        event.widget.config(bg=buttonHoverColor);
    
    def buttonNormalBG(self, event):
        event.widget.config(bg=buttonColor);
        
    def buttonEnterDisabledBG(self, event):
        event.widget.config(bg=disabledButtonColor);
    
    def buttonNormalDisabledBG(self, event):
        event.widget.config(bg=disabledButtonColor);
        
    def close(self):
        self.progress.stop();
        self.progress.destroy();
        self.master.quit();
        
    
    ################### other functions ##############################
    def clickHelp(self):
        location = "manual.docx";
        os.system("start " + location);
    
    def clickOpenFile(self):
        import subprocess;
        
        location = self.checkErrFileName.get();
        program = resource_path("Notepad++\\notepad++.exe")
        
        subprocess.call([program, location]);
        
    def showNextErrors(self):
        startNumber = self.errors.index(self.croppedErrors[0]);
        self.croppedErrors = self.errors[startNumber + 7:startNumber + 14];
        self.drawErrors();
    
    def showPrevErrors(self):
        startNumber = self.errors.index(self.croppedErrors[0])
        self.croppedErrors = self.errors[startNumber - 7:startNumber];
        self.drawErrors();
        
    def drawErrors(self):        
        if (len(self.errors) > 7):
                startNumber = self.errors.index(self.croppedErrors[0]);
                
                self.nextErrors = Button(self.p9, text = ">", command=lambda: self.showNextErrors(), background=buttonColor, foreground=fgColor, bd=0, font=self.ft5, activebackground=buttonPressedColor, activeforeground=fgColor);
                self.prevErrors = Button(self.p9, text = "<", command=lambda: self.showPrevErrors(), background=buttonColor, foreground=fgColor, bd=0, font=self.ft5, activebackground=buttonPressedColor, activeforeground=fgColor);
                
                if not (startNumber >= (len(self.errors) - 7)):
                    self.nextErrors.place(x = framewidth - nextprevButtonWidth - nextprevButtonPaddingX + nextprevButtonWidth/2 + 2, y = frameheight - nextprevButtonHeight - 2 * nextprevButtonPaddingY, width = nextprevButtonWidth/2 - 2, height = nextprevButtonHeight);
                else:
                    print("should hide");
                    self.hideNextButton();
                    
                if (startNumber > 0):
                    self.prevErrors.place(x = framewidth - nextprevButtonWidth - nextprevButtonPaddingX, y = frameheight - nextprevButtonHeight - 2 * nextprevButtonPaddingY, width = nextprevButtonWidth/2 - 2, height = nextprevButtonHeight);
                else:
                    self.prevErrors.lower();
        cropRange = 22;
        
        ErrorWrap = Frame(self.p9, bg = codeBGColor);
        ErrorWrap.place(x = 56, y = 40, width = framewidth - 72, height = frameheight - topBarHeight - 124)
        
        LineWrap = Frame(self.p9, bg = codeBG2Color);
        LineWrap.place(x=16, y = 40, width = 40, height = frameheight - topBarHeight - 124);
        
        for i in range(len(self.croppedErrors)):
            formattedLine = str((int(self.croppedErrors[i].getLineOccurence()) + 1))
            for k in range(3 - len(formattedLine)):
                formattedLine = "0" + formattedLine;
                
            Label(LineWrap, text = formattedLine, bg = codeBG2Color, font = self.ft6, fg = fgColor).place(x = 6, y = 4+40*i)
        
        for i in range(len(self.croppedErrors)):
            sourceLine = self.croppedErrors[i].getSourceLine();
            if (len(sourceLine) - self.croppedErrors[i].getColOccurence()) > cropRange:
                cropped = sourceLine[max(self.croppedErrors[i].getColOccurence() - cropRange, 0):max(self.croppedErrors[i].getColOccurence() + cropRange, 2 * cropRange)]
                    
                Label(ErrorWrap, text="^", fg = errorColor, bg = codeBGColor).place(x = min(round(7.05 * cropRange), round(7.1*self.croppedErrors[i].getColOccurence())), y = 20 + 40*i)
                
                Label(ErrorWrap, text=cropped, fg = fgColor, bg = codeBGColor, font = self.ft6).place(x = 2, y = 5+40*i)
            else:
                EOLOccurence = len(sourceLine) - self.croppedErrors[i].getColOccurence() - 1;
                cropped = sourceLine[self.croppedErrors[i].getColOccurence() - (2 * cropRange - EOLOccurence):]
                Label(ErrorWrap, text=cropped, fg = fgColor, bg = codeBGColor, font = self.ft6).place(x = 2, y = 5+40*i)
                Label(ErrorWrap, text="^", fg = errorColor, bg = codeBGColor).place(x = round(7.05*((2*cropRange) - EOLOccurence)), y = 20 + 40*i)        
    
    def hideNextButton(self):
        self.nextErrors.place_forget();
    
    def firecallback(self):
        if len(self.courseVar.get()) == 0 or len(self.fileVar.get()) == 0:
            self.goButton.config(state=DISABLED,background=disabledButtonColor, activebackground=disabledButtonColor);
            self.goButton.bind("<Enter>", self.buttonEnterDisabledBG);
            self.goButton.bind("<Leave>", self.buttonNormalDisabledBG);
        else:
            self.goButton.config(state=NORMAL,background=buttonColor, activebackground=buttonPressedColor);
            self.goButton.bind("<Enter>", self.buttonEnterBG);
            self.goButton.bind("<Leave>", self.buttonNormalBG);
    
    def firecallback1(self):
        if len(self.scorFileVar.get()) == 0 or len(self.errFileVar.get()) == 0:
            self.goButtonP4.config(state=DISABLED,background=disabledButtonColor, activebackground=disabledButtonColor);
            self.goButtonP4.bind("<Enter>", self.buttonEnterDisabledBG);
            self.goButtonP4.bind("<Leave>", self.buttonNormalDisabledBG);
        else:
            self.goButtonP4.config(state=NORMAL,background=buttonColor, activebackground=buttonPressedColor);
            self.goButtonP4.bind("<Enter>", self.buttonEnterBG);
            self.goButtonP4.bind("<Leave>", self.buttonNormalBG);
    
    def firecallback2(self):
        if len(self.courseVar2.get()) == 0 or len(self.fileVar2.get()) == 0:
            self.goButtonP5.config(state=DISABLED,background=disabledButtonColor, activebackground=disabledButtonColor);
            self.goButtonP5.bind("<Enter>", self.buttonEnterDisabledBG);
            self.goButtonP5.bind("<Leave>", self.buttonNormalDisabledBG);
        else:
            self.goButtonP5.config(state=NORMAL,background=buttonColor, activebackground=buttonPressedColor);
            self.goButtonP5.bind("<Enter>", self.buttonEnterBG);
            self.goButtonP5.bind("<Leave>", self.buttonNormalBG);
    
    def firecallback3(self):
        if len(self.checkErrFileVar.get()) == 0:
            self.goButtonP8.config(state=DISABLED,background=disabledButtonColor, activebackground=disabledButtonColor);
            self.goButtonP8.bind("<Enter>", self.buttonEnterDisabledBG);
            self.goButtonP8.bind("<Leave>", self.buttonNormalDisabledBG);
        else:
            self.goButtonP8.config(state=NORMAL,background=buttonColor, activebackground=buttonPressedColor);
            self.goButtonP8.bind("<Enter>", self.buttonEnterBG);
            self.goButtonP8.bind("<Leave>", self.buttonNormalBG);

    
    def combineFuncs(self):
        self.p6.lift();
        try:
            self.createGroups();
        except Exception as e:
            self.fireErrorPage(e);
        return
        
    def combineFuncs2(self):
        self.p6.lift();
        try:
            self.split();
        except Exception as e:
            self.fireErrorPage(e);
        return
    
    def combineFuncs3(self):
        self.p6.lift();
        try:
            self.createFile();
        except Exception as e:         
            self.fireErrorPage(e);
        return
        
    def fireErrorPage(self, e):
        import traceback;

        global tb;

        tb = traceback.format_exc();

        traceback.print_exc();
        
        self.stackTraceStringVar1.set(self.getStackTrace()[0]);
        self.stackTraceStringVar2.set(self.getStackTrace()[1]);
        self.p7.lift();
    
    def getStackTrace(self):
        if len(tb.split("\n")) == 1:
            return [tb, ""];
        elif len(tb.split("\n")) < 4:
            return [tb.split("\n")[-2].lstrip(), ""];
        return [tb.split("\n")[-2].lstrip(), tb.split("\n")[-4].lstrip()];
    
    def load_file(self):
        self.browse.config(state=DISABLED,background=disabledButtonColor, activebackground=disabledButtonColor);
        self.browse.bind("<Enter>", self.buttonEnterDisabledBG);
        self.browse.bind("<Leave>", self.buttonNormalDisabledBG);
        
        fname = askopenfile(filetypes=(("CSV files", "*.csv"),
                                           ("Text files", "*.txt"),
                                           ("All files", "*.*") ));
        if fname:
            try:
                self.fileName.delete(0, END);
                self.fileName.insert(0, fname.name);
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname);
                
        self.browse.config(state=NORMAL,background=buttonColor, activebackground=buttonPressedColor);
        self.browse.bind("<Enter>", self.buttonEnterBG);
        self.browse.bind("<Leave>", self.buttonNormalBG);
        return
            
    def load_file1(self):
        self.browse1.config(state=DISABLED,background=disabledButtonColor, activebackground=disabledButtonColor);
        self.browse1.bind("<Enter>", self.buttonEnterDisabledBG);
        self.browse1.bind("<Leave>", self.buttonNormalDisabledBG);
        
        fname = askopenfile(filetypes=(("CSV files", "*.csv"),
                                           ("Text files", "*.txt"),
                                           ("All files", "*.*") ));
        if fname:
            try:
                self.scorFileName.delete(0, END);
                self.scorFileName.insert(0, fname.name);
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname);
                
        self.browse1.config(state=NORMAL,background=buttonColor, activebackground=buttonPressedColor);
        self.browse1.bind("<Enter>", self.buttonEnterBG);
        self.browse1.bind("<Leave>", self.buttonNormalBG);
        return

    def load_file2(self):
        self.browse2.config(state=DISABLED,background=disabledButtonColor, activebackground=disabledButtonColor);
        self.browse2.bind("<Enter>", self.buttonEnterDisabledBG);
        self.browse2.bind("<Leave>", self.buttonNormalDisabledBG);
        
        fname = askopenfile(filetypes=(("CSV files", "*.csv"),
                                           ("Text files", "*.txt"),
                                           ("All files", "*.*") ));
        if fname:
            try:
                self.errFileName.delete(0, END);
                self.errFileName.insert(0, fname.name);
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname);
        
        self.browse2.config(state=NORMAL,background=buttonColor, activebackground=buttonPressedColor);
        self.browse2.bind("<Enter>", self.buttonEnterBG);
        self.browse2.bind("<Leave>", self.buttonNormalBG);
        return
            
    def load_file3(self):
        self.browse3.config(state=DISABLED,background=disabledButtonColor, activebackground=disabledButtonColor);
        self.browse3.bind("<Enter>", self.buttonEnterDisabledBG);
        self.browse3.bind("<Leave>", self.buttonNormalDisabledBG);
        
        fname = askopenfile(filetypes=(("CSV files", "*.csv"),
                                           ("Text files", "*.txt"),
                                           ("All files", "*.*") ));
        if fname:
            try:
                self.fileName2.delete(0, END);
                self.fileName2.insert(0, fname.name);
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname);
        
        self.browse3.config(state=NORMAL,background=buttonColor, activebackground=buttonPressedColor);
        self.browse3.bind("<Enter>", self.buttonEnterBG);
        self.browse3.bind("<Leave>", self.buttonNormalBG);
        return    

    def load_file4(self):
        self.browse4.config(state=DISABLED,background=disabledButtonColor, activebackground=disabledButtonColor);
        self.browse4.bind("<Enter>", self.buttonEnterDisabledBG);
        self.browse4.bind("<Leave>", self.buttonNormalDisabledBG);
        
        fname = askopenfile(filetypes=(("CSV files", "*.csv"),
                                           ("Text files", "*.txt"),
                                           ("All files", "*.*") ));
        if fname:
            try:
                self.checkErrFileName.delete(0, END);
                self.checkErrFileName.insert(0, fname.name);
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname);
        
        self.browse4.config(state=NORMAL,background=buttonColor, activebackground=buttonPressedColor);
        self.browse4.bind("<Enter>", self.buttonEnterBG);
        self.browse4.bind("<Leave>", self.buttonNormalBG);
        return  
            
    def createGroups(self):
        course_id = self.courseVar.get();
        fileName = self.fileVar.get();
        seperator = self.sepVar.get();
    
        write = self.checkVar.get() == 1;
        
        groups = getGroups(course_id, fileName, seperator, write);
        
        driver = createScorionGroups(groups, course_id);
        #throws windowserror
        driver.quit();
        
        self.finish();
    
    def createFile(self):
        course_id = self.courseVar2.get();
        fileName = self.fileVar2.get();
        seperator = self.sepVar2.get();
        
        getGroups(course_id, fileName, seperator, True);
        self.finish();
        
    def split(self):
        scorFile = self.scorFileName.get();
        errFile = self.errFileName.get();
        splitGroups(scorFile, errFile);
        
        self.finish();
        
    def finish(self):
        self.progress["mode"] = 'determinate';
        self.progress.update_idletasks();
        self.progress.stop();

        self.progressLabel["text"] = "Finished!";
        self.cancelButton["text"] = "Back to menu";
        
        self.closeP6.place(x = framewidth - nextprevButtonWidth - nextprevButtonPaddingX, y = frameheight - nextprevButtonHeight - nextprevButtonPaddingY, width = nextprevButtonWidth, height = nextprevButtonHeight);
        self.closeP6.bind("<Enter>", self.buttonEnterBG);
        self.closeP6.bind("<Leave>", self.buttonNormalBG)
        self.cancelButton.config(command=self.backtomenu);
    
    def backtomenu(self):
        self.scorFileVar.set("");
        self.errFileVar.set("");
        self.courseVar.set("");
        self.courseVar2.set("");
        self.fileVar.set("");
        self.fileVar2.set("");
        self.sepVar.set(",");
        self.sepVar2.set(",");
        self.p2.lift();
        self.cancelButton.config(text = "cancel", command=exit);
        self.closeP6.place_forget();
        self.progressLabel["text"] = "Working, this might take a couple of minutes...";
        self.progress["mode"] = 'indeterminate';
        
if __name__ == "__main__":
    root = Tk();
    root.withdraw();
    
    screen_width = root.winfo_screenwidth();
    screen_height = root.winfo_screenheight();

    # calculate position x and y coordinates
    x = (screen_width/2) - (framewidth/2);
    y = (screen_height/2) - (frameheight/2);
    
    window = Toplevel(root);
    window.geometry("%dx%d+%d+%d" %(framewidth, frameheight, x, y));
    window.resizable(False, False);
    
    window.iconbitmap(resource_path("elslogo.ico"));    
    
    main = MainView(window);
    main.pack(side="top", fill="both", expand=True);
    
    window.attributes("-topmost", 1);
    
    window.mainloop();
    
    root.destroy();
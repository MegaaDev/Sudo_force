import customtkinter
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import os
from PIL import Image
from main import final, chat_with_gpt
from listen import Listen


message = []


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CLI Done Right")
        self.geometry("800x800")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        photo = customtkinter.CTkImage(Image.open(
            r"mic.png"))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(
            self.navigation_frame, text="CLI Done Right", compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Cmd made easy",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="ChatBot",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(
            row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        def button_click_event():
            global var
            global message
            var = self.entry_frame_1.get()

            data = final(var)
            if (data):
                message.append((data[0]+"\n"+data[1]))
            if ("clear" in var):
                self.entry_frame_1.select_clear()
                self.entry_frame_1 = customtkinter.CTkEntry(self.home_frame,
                                                            placeholder_text="Hey, Type your command here",
                                                            width=500,
                                                            height=40,
                                                            border_width=2,
                                                            corner_radius=10)
                self.entry_frame_1.grid(
                    row=1, column=0, ipadx=5, padx=10, pady=10,)
                self.textbox = customtkinter.CTkTextbox(
                    self.home_frame, width=700, height=600, border_width=2, corner_radius=10)
                self.textbox.grid(
                    row=2, column=0, sticky="w", padx=10, pady=20)
                return

            self.textbox = customtkinter.CTkTextbox(
                self.home_frame, width=700, height=600, border_width=2, corner_radius=10)
            self.textbox.grid(row=2, column=0, sticky="w", padx=10, pady=20)
            for i in message:
                self.textbox.insert("0.0", f"{i}\n")
            self.entry_frame_1.select_clear()
            self.entry_frame_1 = customtkinter.CTkEntry(self.home_frame,
                                                        placeholder_text="Hey, Type your command here",
                                                        width=500,
                                                        height=40,
                                                        border_width=2,
                                                        corner_radius=10)
            self.entry_frame_1.grid(
                row=1, column=0, ipadx=5, padx=10, pady=10,)

        def voice_recog_event():
            global var
            global message
            self.textbox = customtkinter.CTkTextbox(
                self.home_frame, width=700, height=800, border_width=2, corner_radius=10)
            self.textbox.grid(row=2, column=0, sticky="w", padx=10, pady=10)
            self.textbox.insert("0.0", f"Listening....\n")
            var = Listen()
            data = final(var)

            if ("clear" in var):
                self.entry_frame_1.select_clear()
                self.entry_frame_1 = customtkinter.CTkEntry(self.home_frame,
                                                            placeholder_text="Hey, Type your command here",
                                                            width=500,
                                                            height=40,
                                                            border_width=2,
                                                            corner_radius=10)
                self.entry_frame_1.grid(
                    row=1, column=0, ipadx=5, padx=10, pady=10,)
                self.textbox = customtkinter.CTkTextbox(
                    self.home_frame, width=700, height=800, border_width=2, corner_radius=10)
                self.textbox.grid(
                    row=2, column=0, sticky="w", padx=10, pady=10)
                return
            if (data):
                message.append((data[0]+"\n"+data[1]))
            self.textbox = customtkinter.CTkTextbox(
                self.home_frame, width=700, height=800, border_width=2, corner_radius=10)
            self.textbox.grid(row=2, column=0, sticky="w", padx=10, pady=10)
            for i in message:
                self.textbox.insert("0.0", f"{i}\n")
            self.entry_frame_1.select_clear()
            self.entry_frame_1 = customtkinter.CTkEntry(self.home_frame,
                                                        placeholder_text="Hey, Type your command here",
                                                        width=500,
                                                        height=40,
                                                        border_width=2,
                                                        corner_radius=10)
            self.entry_frame_1.grid(
                row=1, column=0, ipadx=5, padx=10, pady=10,)

        # self.entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Execute", compound="right", width=75, height=40, border_width=2,
                                                           corner_radius=10, command=button_click_event)

        # self.home_frame.bind("<Return>", button_click_event)

        self.home_frame_button_1 = customtkinter.CTkButton(
            self.home_frame, text="")
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.entry_frame_1 = customtkinter.CTkEntry(self.home_frame,
                                                    placeholder_text="Hey, Type your command here",
                                                    width=500,
                                                    height=40,
                                                    border_width=2,
                                                    corner_radius=10)
        self.entry_frame_1.grid(row=1, column=0, ipadx=5, padx=10, pady=10,)
        # self.entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.voice_recog = customtkinter.CTkButton(self.home_frame, text=None, text_color="black", compound="right", width=40, height=40, border_width=2,
                                                   corner_radius=300, command=voice_recog_event, fg_color="gray70", hover_color="gray30", image=photo)
        # self.entry_frame_1.bind("<Return>", button_click_event)
        self.voice_recog.grid(
            row=1, column=1, padx=5, pady=5)

        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Execute", compound="right", width=75, height=40, border_width=2,
                                                           corner_radius=10, command=button_click_event)
        # self.entry_frame_1.bind("<Return>", button_click_event)
        self.home_frame_button_2.grid(
            row=1, column=2, ipadx=5, padx=10, pady=10)

        def gptClick():
            data = chat_with_gpt(self.entry_frame_2.get())
            # data = final(var)
            self.textbox2 = customtkinter.CTkTextbox(
                self.second_frame, width=500, height=800, border_width=2, corner_radius=10)
            self.textbox2.grid(row=2, column=0, sticky="w", padx=10, pady=10)
            self.textbox2.insert("0.0", f"{data}\n")
            self.entry_frame_2.select_clear()
            self.entry_frame_2 = customtkinter.CTkEntry(self.second_frame,
                                                        placeholder_text="Hey, what do you like to talk about",
                                                        width=500,
                                                        height=40,
                                                        border_width=2,
                                                        corner_radius=10)
            self.entry_frame_2.grid(
                row=1, column=0, ipadx=5, padx=10, pady=10,)
            self.second_frame_button_2 = customtkinter.CTkButton(self.second_frame, text="Execute", compound="right", width=75, height=40, border_width=2,
                                                                 corner_radius=10, command=gptClick)
            self.second_frame_button_2.grid(
                row=1, column=2, ipadx=5, padx=10, pady=10)

        self.second_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        # self.second_frame.bind("<Return>", button_click_event)

        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Execute", compound="right", width=75, height=40, border_width=2,
                                                           corner_radius=10, command=button_click_event)

        # self.home_frame.bind("<Return>", button_click_event)

        self.second_frame_button_1 = customtkinter.CTkButton(
            self.second_frame, text="")
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.entry_frame_2 = customtkinter.CTkEntry(self.second_frame,
                                                    placeholder_text="Hey, What wpuld you like to talk about?",
                                                    width=412,
                                                    height=40,
                                                    border_width=2,
                                                    corner_radius=10)
        self.entry_frame_2.grid(row=1, column=0, ipadx=5, padx=10, pady=10,)
        # self.entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.voice_recog_2 = customtkinter.CTkButton(self.second_frame, text=None, text_color="black", compound="right", width=40, height=40, border_width=2,
                                                     corner_radius=300, command=voice_recog_event, fg_color="gray70", hover_color="gray30", image=photo)
        # self.entry_frame_1.bind("<Return>", button_click_event)
        self.voice_recog_2.grid(
            row=1, column=1, padx=5, pady=5)

        self.home_frame_button_2 = customtkinter.CTkButton(self.second_frame, text="Execute", compound="right", width=75, height=40, border_width=2,
                                                           corner_radius=10, command=gptClick)
        # self.entry_frame_1.bind("<Return>", button_click_event)
        self.home_frame_button_2.grid(
            row=1, column=2, ipadx=5, padx=10, pady=10)

        # create third frame
        self.third_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(
            fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        # self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()

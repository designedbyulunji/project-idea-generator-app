from openai import OpenAI
import customtkinter as ctk

# PROGRAM CALL BACKS
def generate_func():
  prompt = "Hello GPT, would you please generate 5 coding project ideas. "
  language_choice = programming_language_dropdown.get()
  prompt += "The programming language to be used is " + language_choice + ". "
  difficulty = project_difficulty.get()
  prompt += "The project difficulty level should be " + difficulty + ". "

  if project_features_check_box_one.get() == True and project_features_check_box_two.get() == True:
    prompt += "The project should also include a Database and API(s)" + ". "
  
  elif project_features_check_box_one.get() == True and project_features_check_box_two.get() == False:
    prompt += "The project should include a Database" + ". "

  elif project_features_check_box_one.get() == False and project_features_check_box_one.get() == True:
    prompt += "The project should include API(s)"
  else:
    prompt += "The project should not include a Database or API(s)"

  
  client = OpenAI(
    api_key=""
  )
  chat_completion = client.chat.completions.create(
  messages=[
    {"role":"user",
    "content": prompt}
  ],
  model="gpt-3.5-turbo"
  )
  gpt_response = chat_completion.choices[0].message.content
  
  response_box.insert("0.0", gpt_response)


# PROGRAM ROOT WINDOW
root_window = ctk.CTk()

# DEFAULT PROGRAM SETUP
root_window._set_appearance_mode("Sytem")
root_window.geometry("720x620")
root_window.title("AI Project Idea Generator")

# USER INTERFACE SETUP
title = ctk.CTkLabel(root_window, text="AI Project Idea Generator",
                     font= ctk.CTkFont("AcmeFont", size=25))
title.pack(fill="x", pady=(20, 20))

# MAIN FRAME
main_frame = ctk.CTkFrame(root_window)
main_frame.pack(pady=(10, 10))

# LANGUAGE SELECTION FRAME
programming_language_frame = ctk.CTkFrame(master=main_frame)
programming_language_frame.pack(padx=120, pady=(20, 20), fill="both")

# LANGUAGE FRAME LABEL
programming_language_label = ctk.CTkLabel(master=programming_language_frame,
                                          text="Programming Language",
                                          font=ctk.CTkFont("Roboto", size=20, weight="bold"),
                                          padx=20, pady=10)
programming_language_label.pack()

# LANGUAGE DROPDOWN SELECTION COMBOBOX
programming_language_dropdown = ctk.CTkComboBox(master=programming_language_frame, 
                                                values=["Python", "JavaScript", "C#", "Java"])
programming_language_dropdown.pack(padx=20, pady=(0, 10))

# PROJECT DIFFICULTY SELECTION FRAME
project_difficulty_frame = ctk.CTkFrame(master=main_frame)
project_difficulty_frame.pack(padx=120, pady=(0,10), fill="both")

# PROJECT DIFICULTY FRAME LABEL
project_difficulty_label = ctk.CTkLabel(master=project_difficulty_frame,
                                          text="Project Difficulty",
                                          font=ctk.CTkFont("Roboto", size=20, weight="bold"),
                                          padx=50, pady=10)
project_difficulty_label.pack()

# PROJECT DIFFICULTY RADIO BUTTONS
project_difficulty = ctk.StringVar(value="Easy")

project_difficulty_radio_button_1 = ctk.CTkRadioButton(master=project_difficulty_frame,
                                                     text="Easy", variable=project_difficulty,
                                                     value="Easy")
project_difficulty_radio_button_1.pack(side="left", padx = 20, pady = (20, 20))

project_difficulty_radio_button_2 = ctk.CTkRadioButton(master=project_difficulty_frame,
                                                     text="Medium", variable=project_difficulty,
                                                     value="Medium")
project_difficulty_radio_button_2.pack(side="left", pady = (20, 20))

project_difficulty_radio_button_3 = ctk.CTkRadioButton(master=project_difficulty_frame,
                                                     text="Hard", variable=project_difficulty,
                                                     value="Hard")
project_difficulty_radio_button_3.pack(side="left", padx = 20, pady =(20, 20))

# PROJECT FATURES FRAME
project_features_frame = ctk.CTkFrame(master=main_frame)
project_features_frame.pack(padx=120, pady=(0,10), fill="both")

# PROJECT FEATURES FRAME LABEL
project_features_label = ctk.CTkLabel(master=project_features_frame, 
                                      text="Project Features",
                                      font=ctk.CTkFont("Roboto", size=20, weight="bold"),
                                      padx=50, pady=10)
project_features_label.pack()

# PROJECT FEATURES CHECK BOXES
project_features_check_box_one = ctk.CTkCheckBox(master=project_features_frame, 
                                               text="Database")
project_features_check_box_one.pack(side="left", padx = 20, pady =(20, 20))

project_features_check_box_two = ctk.CTkCheckBox(master=project_features_frame, 
                                               text="API")
project_features_check_box_two.pack(side="right", padx = 20, pady =(20, 20))

# GENERATE BUTTON
generate_button = ctk.CTkButton(master=main_frame, text="Generate", 
                                font=ctk.CTkFont("Roboto", size=20, weight="bold"), command=generate_func)
generate_button.pack(fill="both", padx=120)

# RESPONSE DISPLAY SCREEN
response_box = ctk.CTkTextbox(master=main_frame)
response_box.pack(fill="both",  padx = 20, pady =(20, 20))

# RUN PROGRAM
root_window.mainloop()

# Poor Richard
# 18thCentury
# AcmeFont
# Times New Roman
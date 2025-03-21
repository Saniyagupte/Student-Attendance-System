import tkinter as tk
import cv2
from PIL import Image, ImageTk
import utils

class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")

        self.login_button_main_window = utils.get_button(self.main_window, 'login', 'green', self.login)
        self.login_button_main_window.place(x=750, y=300)

        self.register_new_user_button_main_window = utils.get_button(
            self.main_window, 'register new user', 'gray', self.register_new_user, fg='black'
        )
        self.register_new_user_button_main_window.place(x=750, y=400)

        self.webcam_label = utils.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

        self.add_webcam(self.webcam_label)

    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)  # Default camera index

        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Failed to grab frame")
            self._label.after(20, self.process_webcam)
            return

        self.most_recent_capture_arr = frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)

        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)

        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(20, self.process_webcam)  # Pass function reference correctly

    def start(self):
        self.main_window.mainloop()

    def login(self):
        pass

    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)  # Corrected
        self.register_new_user_window.geometry("1200x520+350+100")  # Set size for new window

        self.accept_button_register_new_user_window = utils.get_button(self.register_new_user_window, 'Accept', 'green', self.accept_register_new_user)
        self.accept_button_register_new_user_window.place(x=750, y=300)

        self.try_again_button_register_new_user_window = utils.get_button(self.register_new_user_window, 'Try Again', 'red', self.accept_register_new_user)
        self.try_again_button_register_new_user_window.place(x=750, y=400)

        self.capture_label = utils.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)

        self.add_img_to_label(self.capture_label)

    def accept_register_new_user(self):
        pass

    def add_img_to_label(self , label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)

        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_new_user_capture = self.most_recent_capture_arr.copy()

if __name__ == "__main__":
    app = App()
    app.start()

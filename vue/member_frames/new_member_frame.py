from tkinter import *
from tkinter import messagebox

from exceptions import Error
from vue.member_frames.new_person_frame import NewPersonFrame


class NewMemberFrame(NewPersonFrame):

    def __init__(self, person_controller, master=None):
        super().__init__(person_controller, master)

    def create_widgets(self):
        super().create_widgets()
       

    def valid(self):

        data = super().get_data()
        data['medical_certificate'] = bool(True)

        try:
            member_data = self._person_controller.create_member(data)
            messagebox.showinfo("Success",
                                "Member %s %s created !" % (member_data['firstname'], member_data['lastname']))

        except Error as e:
            messagebox.showerror("Error", str(e))
            return

        self.show_menu()

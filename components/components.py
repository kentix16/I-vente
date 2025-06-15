from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivymd.theming import ThemeManager
from kivymd.uix.pickers import MDDockedDatePicker, MDTimePickerDialVertical, MDTimePickerDialHorizontal, \
    MDModalDatePicker
from typing import Literal

Builder.load_file("components.kv")


ORIENTATION = Literal["portrait", "landscape"]
time_picker_horizontal: MDTimePickerDialHorizontal = ObjectProperty(
    allownone=True
)
time_picker_vertical: MDTimePickerDialHorizontal = ObjectProperty(
    allownone=True
)

date_picker_horizontal: MDModalDatePicker = ObjectProperty(
    allownone=True
)
date_picker_vertical: MDModalDatePicker = ObjectProperty(
    allownone=True
)

def check_orientation(
        self, instance: ThemeManager, orientation: ORIENTATION
):
    if orientation == "portrait" and self.time_picker_horizontal:
        self.time_picker_horizontal.dismiss()
        hour = str(self.time_picker_horizontal.time.hour)
        minute = str(self.time_picker_horizontal.time.minute)
        Clock.schedule_once(
            lambda x: self.open_time_picker_vertical(hour, minute),
            0.1,
        )
    elif orientation == "landscape" and self.time_picker_vertical:
        self.time_picker_vertical.dismiss()
        hour = str(self.time_picker_vertical.time.hour)
        minute = str(self.time_picker_vertical.time.minute)
        Clock.schedule_once(
            lambda x: self.open_time_picker_horizontal(hour, minute),
            0.1,
        )
    if orientation == "portrait" and self.date_picker_horizontal:
        self.date_picker_horizontal.dismiss()
        day = str(self.date_picker_horizontal.date.minute)
        minute = str(self.date_picker_horizontal.date.minute)
        Clock.schedule_once(
            lambda x: self.open_date_picker_vertical(hour, minute),
            0.1,
        )
    elif orientation == "landscape" and self.date_picker_vertical:
        self.date_picker_vertical.dismiss()
        hour = str(self.date_picker_vertical.date.hour)
        minute = str(self.date_picker_vertical.date.minute)
        Clock.schedule_once(
            lambda x: self.open_date_picker_horizontal(hour, minute),
            0.1,
        )

def open_time_picker_horizontal(self, hour, minute):
    self.time_picker_vertical = None
    self.time_picker_horizontal = MDTimePickerDialHorizontal(
        hour=hour, minute=minute
    )
    self.time_picker_horizontal.open()

def open_time_picker_vertical(self, hour, minute):
    self.time_picker_horizontal = None
    self.time_picker_vertical = MDTimePickerDialVertical(
        hour=hour, minute=minute
    )
    self.time_picker_vertical.open()

def show_date_picker(self):

    date_dialog = MDDockedDatePicker()
    # You have to control the position of the date picker dialog yourself.
    date_dialog.pos = [
        self.ids.date_button.center_x - date_dialog.width / 2,
        self.ids.date_button.y - (date_dialog.height + dp(32)),
    ]
    date_dialog.bind(on_ok=self.on_ok_date)
    date_dialog.open()

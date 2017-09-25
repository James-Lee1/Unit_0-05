# Created by: James Lee
# Created on: Sep 2017
# Created for: ICS3U
# This program does basic math

import ui

def perimeter_touch_up_inside(sender):
    # displays the answer to equation 1
    view['perimeter_label'].text = str((5+3)*2)+"cm"
    
def area_touch_up_inside(sender):
    # displays the answer to equation 2
    view['area_label'].text = str(3*5)+"cm^2"

view = ui.load_view()
view.present('full_screen')

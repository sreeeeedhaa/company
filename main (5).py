from kivymd.app import MDApp
from kivy.lang import Builder


class Arul_Tyres(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        return Builder.load_string(
            '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:

        title: 'Arul & Co., Tyres ✆=7010809652'
        md_bg_color: .2, .2, .2, 1
        specific_text_color: 1, 1, 1, 1

    MDBottomNavigation:
        panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Bike'  
            icon: 'bikeicon.png'
            Image:
                id: imageview
                source: 'bikes.png'
            
            

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Car'
            icon: 'caricon.png'
            Image:
                id: imageview
                source: 'cars.png'
            
            

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Truck'
            icon: 'truckicon.png'
            Image:
                id: imageview
                source: 'trucks.png'
            
        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'JK products'
            icon: 'jktyres.png'
            Image:
                id: imageview
                source: 'sensor.png'    
'''
        )


Arul_Tyres().run()

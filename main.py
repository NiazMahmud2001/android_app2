from kivymd.app import MDApp
from kivy_garden.mapview import MapView, MapMarker
import requests
import geocoder
# res = requests.get("https://ipinfo.io/")
# print(res.text)

myInfo = geocoder.ip("me")
myAddr = myInfo.latlng
print(myInfo)
print(myAddr)


class MapViewApp(MDApp):
    def build(self):
        mapview = MapView(zoom=100, lat=myAddr[0], lon=myAddr[1])
        mapview.add_widget(MapMarker(lat=myAddr[0], lon=myAddr[1], source="map_marker.png"))
        return mapview

if __name__ =="__main__":
    MapViewApp().run()

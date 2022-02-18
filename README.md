# Twitter_API
Lab 2(2). Map with twitter friends locations 

# Second task (navigatio)
module json_navigation gives for users a convinient tool to navigate json files in two directions.

Usage of the script: 
:go [key/index]  - go to the value on key/index\
:gb - go back on 1 level
:gb / - go back to the root
:gb [number]  - go back on [number] > 0 levels
:print all - print all values from the root with their path from the root
:print - print all values from current location with their path from the root
:quit - stop running program
:h - print USAGE information
:crp - print current position from root

Examples:







![image](https://user-images.githubusercontent.com/91615606/154764706-dae28c8c-1cf2-4260-b85d-f9c6b55e2564.png)
![image](https://user-images.githubusercontent.com/91615606/154764905-35628368-b406-4600-a637-c11aa96ec3a9.png)
![image](https://user-images.githubusercontent.com/91615606/154765047-37523de1-7a3c-4042-91bd-40add7931cba.png)

# Third Task (Map)
Main module is web_app.py .  It runs server with app that can draw a map with locations of folowing people on Twitter.

#Home page looks minimalistsc:

![image](https://user-images.githubusercontent.com/91615606/154765469-13a4768f-44f5-4e6a-a613-02172c015035.png)







#Here you can print Twitter user nickname and number of following people to find.
![image](https://user-images.githubusercontent.com/91615606/154765908-83dd31c8-46fd-4e69-a7e1-d02b10c196e7.png)
![image](https://user-images.githubusercontent.com/91615606/154765965-33e9e896-136c-4d52-b032-58211fdc6737.png)


It was creating with using flask modul to run app. For data information was used Twitter API. Also, It was used folium and geopy modules to create map.

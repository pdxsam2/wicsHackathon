# import folium package
import folium
import random
import time

num_to_issue = {1:'G', 2:'T', 3:'P'}

def add_rand_issue(mapitems):
    lat = random.uniform(45.50, 45.545)
    lon = random.uniform(237.300, 237.500)
    category = num_to_issue[random.randrange(1, 4)]
    severity = random.randrange(1, 6)
    mapitems.append([category, lat, lon, severity])


def rand_change(mapitems):
    for item in mapitems:
        item[3] += random.randrange(-1,2) #update intensity
    for i, issue in enumerate(mapitems):
        print(issue[3])
        if issue[3] == 8 or issue[3] == 0:
            mapitems.remove(issue)
    for i in range(2):
        add_rand_issue(mapitems)
    return


def update(mapitems, my_map):
    my_map = folium.Map(location=[45.5199226, (360 - 122.6390)],
                         zoom_start=13)
    rand_change(mapitems)
    for item in mapitems:
        days = random.randrange(0,30)
        popup_msg = str(days) + " days old"
        folium.CircleMarker(location=[ item[1], item[2]],
                            radius=(3 * item[3]), fill=True, color=color_value[item[0]], popup=popup_msg).add_to(my_map)
    my_map.save("C:\\Users\\LDING\\Desktop\\map11.html")

    return

with open ("citySample.txt", 'r') as myfile:
    lines = myfile.readlines()

# Map method of folium return Map object

# Here we pass coordinates of Gfg
# and starting Zoom level = 12
my_map1 = folium.Map(location=[45.5011226, (360-122.6793)],
                     zoom_start=13)
color_value = {"G":"Red", "T":"Yellow", "P":"Blue"}
issues = []

for line in lines:
    a, b, c, d = line.split(',')
    folium.CircleMarker(location=[float(b), float(c)],
                        radius= (3*float(d)), fill=True, color=color_value[a], popup=' FRI ').add_to(my_map1)
    issues.append([a,float(b),float(c),int(d)])


# save method of Map object will create a map
my_map1.save("C:\\Users\\LDING\\Desktop\\map11.html")

for i in range(100):
    update(issues, my_map1)
    time.sleep(4)

# # import gmplot package
# import gmplot
#
# # GoogleMapPlotter return Map object
# # Pass the center latitude and
# # center longitude
#
# gmap1 = gmplot.GoogleMapPlotter(45.5155,
#                                 (360-122.6793), 13)
# gmap1.apikey = "AIzaSyBQcWnkgflLwUJNv5ycpPUyNGrNF0MBAcs"
# # Pass the absolute path
# gmap1.draw("C:\\Users\\LDING\\Desktop\\map11.html")
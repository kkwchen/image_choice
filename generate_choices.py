import os
from collections import defaultdict
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("directory", help='the location of the folder of images')
args = parser.parse_args()
directory = args.directory


image_types = ('.jpg', '.png')
image_files = []

for file in os.listdir(directory):
    if file.endswith(image_types):
        image_files.append(file)

sort_list = sorted(image_files, key=len)

start = True
layer = 2
layer_code = defaultdict(list)

for i in range(0,len(sort_list)):
    item = sort_list[i]
    strip_name = sort_list[i][:-4]
    html_name = strip_name[:-1]

    # print('file ', item,' html ', html_name, ' link to next ', strip_name, '')

    if len(strip_name) == layer:            
        layer_code[html_name].append(  '<a href=\"'+str(strip_name)+'.html\"> <img class=\"logo\" border=\"0\" src=\"'+str(directory)+'\\'
                                                + str(item)+'\"style=\"width: 250px;height: 250px;\"> </a>')

    else:
        layer += 1
        layer_code[html_name].append(  '<a href=\"'+str(strip_name)+'.html\"> <img class=\"logo\" border=\"0\" src=\"'+str(directory)+'\\'
                                                + str(item)+'\"style=\"width: 250px;height: 250px;\"> </a>')

start = True

for key in layer_code:

    layer_file = key

    if start:
        layer_file = 0
        start = False

    with open(str(layer_file)+'.html', "w") as text_file: 

        print('<html> <head> <link rel=\"stylesheet\" type=\"text/css\" href=\"choice.css\"> </head>'+
                '<body> <div id=\"center\"> ',file=text_file)

        for snippet in layer_code[key]:
            print(snippet,file=text_file)

        print('</div> <div id=\"button\"> <a href=\"0.html\"> <p>home</p> </a> <p style=\"color:white\";>secretbuffertext</p> </div>' +
                '</body> </html>',file=text_file)
# image_choice
generator script 


Please ensure that both input and output directories exist before running.

This script will not create new directories if they do not exist.


run with argument -h for help

python generate_choices.py -h

run with source output filetypes width height

for example, display images at width x height (800 x 400)

python generate_choices.py images save ".png" 800 400

or

python generate_choices.py "C:/user/images" "C:/user/output/html" (".png",".jpg",".bmp") 800 400

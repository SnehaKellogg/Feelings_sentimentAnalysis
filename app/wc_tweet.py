import numpy as np
import csv
import random
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from palettable.colorbrewer.qualitative import Dark2_8 ##, Greens_9, Reds_9

def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(Dark2_8.colors[random.randint(0,7)])

## For Green or Red palette -- import and replace
# return tuple(Reds_9.colors[random.randint(2,8)])
# return tuple(Greens_9.colors[random.randint(2,8)])

## For grey color palette
# def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
#     return "hsl(0, 0%%, %d%%)" % random.randint(10, 50)

csv_path = "/static/css/cnn_facebook_statuses.csv"
fa_path = "/static/images/"
# font_path = ".ttf"

icon = "twitter"

message = ''
with open(csv_path, 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		message += " " + row['link_name'] #change this 
		 		
# http://stackoverflow.com/questions/7911451/pil-convert-png-or-gif-with-transparency-to-jpg-without
icon_path = fa_path + "%s.png" % icon
icon = Image.open(icon_path)
mask = Image.new("RGB", icon.size, (255,255,255))
mask.paste(icon,icon)
mask = np.array(mask)

wc = WordCloud(background_color="white", max_words=2000, mask=mask,
               max_font_size=300, random_state=42) #font_path=font_path,
               
# generate word cloud
wc.generate_from_text(message)
wc.recolor(color_func=color_func, random_state=3)
wc.to_file("tweet_wordcloud.png")

#Credits: https://github.com/minimaxir/stylistic-word-clouds/blob/master/wordcloud_cnn.py
#https://minimaxir.com/2016/05/wordclouds/

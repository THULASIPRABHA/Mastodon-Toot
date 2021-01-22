import potd 
import posttoot
from datetime import date



imgdata=potd.fetch_potd(cur_date=date.today())
imgsrc=imgdata['image_src']
pageurl=imgdata['image_page_url']
potd.saveimg(imgsrc)

posttoot.post("picoftheday.jpg",pageurl)
#import modules
import arcpy

#set environment
aprx = arcpy.mp.ArcGISProject("CURRENT")

#specify layout
lyt = aprx.listLayouts("PolkGrdWater")[0]

#list layout text elements
eleList = lyt.listElements("TEXT_ELEMENT")

#loop through list and find all text elements with "Polk County" title
for ele in eleList:
    if ele.text == "Polk County":
        ele.text = "Polk County, OR"

#refresh the active view
aprx.save()
del aprx

print ("Script completed")
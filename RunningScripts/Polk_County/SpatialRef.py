#import modules
import arcpy

#set workspace
arcpy.env.workspace = r"D:\ArcGISData\ArcProLessons\EsriTraining\PythEveryone\RunningScripts\Polk_County\OregonPolk.gdb"

#set up a describe object for each fc in geodatabase
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    desc = arcpy.Describe(fc)
    print (desc.spatialReference.name)

print ("Script completed")


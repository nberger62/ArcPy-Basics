# Set up variables
import arcpy
streams = r"D:\ArcGISData\ArcProLessons\EsriTraining\PythEveryone\HandleErrors\SanDiego.gdb\SD_Stream"
buffDists = [100, 500, 1000]

# Loop through the different buffer distances and create buffers
# using each buffer distance
for buff in buffDists:
    print(str(buff) + " is processing")
    arcpy.Buffer_analysis(streams, streams + str(buff), buff)

# Write a print statement so user knows when script is complete
print("Script is complete")

#Lee Allen
#format comes from this post: http://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
#Use in MXD to calculate areas in polygon layer
#Runs on selected features in MXD if any features are selected.
#LayerName ex: "Parcels"
#FieldName ex: "Acres field, must contain numbers

# for use outside MXD, specify full path using varialble
#LayerName=r"\\server\folder\name.gdb\Parcels"

def calcacres(LayerName,FieldName):
    featurecursor = arcpy.da.SearchCursor(LayerName,FieldName)
    total = 0
    try:
        for row in featurecursor:
            acres = float(row[0])
            total = acres + total
    except:
        print "Field Contains Non-numerical text"

    sqmiles = total*0.0015625
    acres = total
    #print "Total Acres of all rows:","{0:.2f}".format(total)
    print "Total Acres:","{0:.2f}".format(acres)
    print "Total Sq Miles:","{0:.2f}".format(sqmiles)


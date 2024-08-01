with open(file_name,'a', ) as f:
    for key in data.keys():
            f.write("%s, %s\n" % (key, data1[key]))
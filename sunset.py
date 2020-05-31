data = [None, None,None,None]
def get_sun_data():
    import ephem as sun
    import datetime
    sun.Observer().date = 99999999999999
    sun.Observer().lat = sun.city('Moscow').lat 
    sun.Observer().long= sun.city('Moscow').long 
    
    sun.Observer().date = datetime.date.today()
    
    data[0] = sun.localtime(sun.Observer().next_rising(sun.Sun())).ctime()
#    data[1] = sun.localtime(sun.Observer().next_setting(sun.Sun())).ctime()
    
#    sun.Observer().date = datetime.datetime.today() + datetime.timedelta(days=1)
#    data[2] = sun.localtime(sun.Observer().next_rising(sun.Sun())).ctime()
#    data[3] = sun.localtime(sun.Observer().next_setting(sun.Sun())).ctime()
    return data
a = get_sun_data()
for x in a:
    print (x)

def get_sun_data():
    rise_t = [ None,None]
    set_t = [ None,None]
    data = [ None,None]
    import ephem, datetime
    
    moscow = ephem.city('Moscow')
    obs = ephem.Observer()
    obs.lat = moscow.lat #'55.7522222'
    obs.long= moscow.long #'37.6155556'
    
    sun = ephem.Sun()
    
    obs.date = datetime.date.today()
    
    rise_time = obs.next_rising(sun)
    set_time = obs.next_setting(sun)
    
    rise_t[0] = ephem.localtime(rise_time).ctime()
    set_t[0] = ephem.localtime(set_time).ctime()
    
    obs.date = datetime.date.today() + datetime.timedelta(days=1)
    
    rise_time = obs.next_rising(sun)
    set_time = obs.next_setting(sun)
    
    rise_t[1]= ephem.localtime(rise_time).ctime()
    set_t[1] = ephem.localtime(set_time).ctime()
   
    data[0] = rise_t
    data[1] = set_t
    return data

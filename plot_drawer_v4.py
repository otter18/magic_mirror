def plot_get():
        #%%
        import weather_get
        data = weather_get.forecast()
        #%%
        import pandas as pd
        t=pd.DataFrame()
        a=1

        for i in range(0,8):          #data['list']:
            
            t.loc[a,'date']=pd.to_datetime( data['list'][i]['dt'], unit='s')
            t.loc[a,'temp']=int(data['list'][i]['main']['temp'])
            t.loc[a,'humidity']=data['list'][i]['main']['humidity']
            t.loc[a,'pressure']=float(data['list'][i]['main']['pressure']/1.3332)
            t.loc[a,'conditions']=data['list'][i]['weather'][0]['description']

          
            a+=1
        t.set_index('date', inplace =True)    
        print(t)
        
        #%%
        import matplotlib.pyplot as plt
        
        
        plt.rcParams.update({
            "lines.color": "black",
            "patch.edgecolor": "black",
            "text.color": "white",
            "axes.facecolor": "black",
            "axes.edgecolor": "black",
            "axes.labelcolor": "black",
            "xtick.color": "white",
            "ytick.color": "gray",
            "grid.color": "#4d4d4d",
            "figure.facecolor": "black",
            "figure.edgecolor": "black",
            "savefig.facecolor": "black",
            "savefig.edgecolor": "black",
             'xtick.labelsize':'x-large'})
        fig, ax = plt.subplots(figsize=(9, 3), dpi=100)
        import datetime
        ax.plot(t.index, t.temp, '-', dash_joinstyle = "round",  color='white'  ) 
#        ax.fill_between(t.index, t.temp, facecolor = 'darkblue', alpha=.5)
        ax.tick_params(axis='x')
        ax.set_xticklabels([], minor = True)
#        ax.grid()
#        ax2 = ax.twinx()
#        ax2.set_ylabel('Humidity, %', color = 'white')
#        ax2.plot(t.index, t.pressure,'o-', color='white' ) 
#        ax2.tick_params(axis='x')
#        ax2.grid()
#        ax2.title.set_text('Hudimidity(%)')
#        ax2.fill_between(t.index, t.pressure, facecolor = 'lightblue', alpha=0.5)
#        plt.axvline(x="23:59:59", color = "gray")
        

        from matplotlib.dates import DateFormatter, HourLocator
        ax.xaxis.set_major_formatter(DateFormatter('%H'))
        ax.xaxis.set_minor_locator(HourLocator())
        
        import matplotlib.ticker as ticker
        ax.yaxis.set_major_locator(ticker.MultipleLocator(5.00))
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(1.00))
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%d °С"))
        ax.axes.get_yaxis().set_visible(False)
#        ax2.yaxis.set_major_locator(ticker.MultipleLocator(1.00))
#        ax2.yaxis.set_minor_locator(ticker.MultipleLocator(.25))
#        ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter("%d mm"))

        image = { 'ясно' : [plt.imread('image/icon set/forecast/ясно.png'), plt.imread('image/icon set/forecast/ясно1.png')], 
                  'облачно' : [plt.imread('image/icon set/forecast/облачно.png'),plt.imread('image/icon set/forecast/облачно.png')],
                  'слегка облачно' : [plt.imread('image/icon set/forecast/слегка облачно.png'),plt.imread('image/icon set/forecast/слегка облачно1.png')],
                  'легкий дождь' : [plt.imread('image/icon set/forecast/легкий дождь.png'),plt.imread('image/icon set/forecast/легкий дождь.png')],
                  'пасмурно' : [plt.imread('image/icon set/forecast/пасмурно.png'),plt.imread('image/icon set/forecast/пасмурно.png')],
                  '1' : plt.imread('image/icon set/forecast/закат.png'),
                  '0' : plt.imread('image/icon set/forecast/рассвет.png'),
                  'bg' : plt.imread('image/icon set/bg3.png')}
        
        
#        ax.text(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),((t.temp[0]+t.temp[1])/2)-3 ,"^Now" , color = "Lime")
        ax.figure.figimage(image["bg"], 0, 45, alpha=.5, zorder=1)
        import matplotlib.lines as lines
        midnight_line = [("23:59:59", t.temp[str(datetime.date.today() + datetime.timedelta(days=1))+"  00:00:00"]), ("23:59:59",min(t.temp)-9)]
        (midnight_line_x, midnight_line_y) = zip(*midnight_line)
        ax.add_line(lines.Line2D(midnight_line_x, midnight_line_y, linewidth=2, color='white'))

        ax.text(str(datetime.date.today() + datetime.timedelta(days=1))+"  00:00:00", min(t.temp)-8.6,  
                (datetime.date.today() + datetime.timedelta(days=1)).strftime(" %a"), fontsize = 12, color = "white")
        
        ax.text(str(datetime.date.today() + datetime.timedelta(days=1))+"  00:00:00", min(t.temp)-8.6,  
                datetime.date.today().strftime('%a '),
                color = "white",
                fontsize = 12,
                horizontalalignment='right')
        import sunset_v2
        sun = sunset_v2.get_sun_data()
        from matplotlib.offsetbox import  OffsetImage, AnnotationBbox
#        
       
            
        for i in range (0,8):
#           
            ax.text(t.index[i], t.temp[i]+4, str(int(t.temp[i]))+"°С",fontsize=15, color = "white",
                    horizontalalignment='center', verticalalignment='center')
#            ax2.text(t.index[i], t.pressure[i]+.25, str(int(t.pressure[i]))+"mm", color = "white")
            
            
            for x in range (0,2):
                    if t.index[i] < datetime.datetime.strptime(sun[0], '%a %b %d %H:%M:%S %Y') and  t.index[i]>datetime.datetime.strptime(sun[1], '%a %b %d %H:%M:%S %Y'):
                        try:
                                imagebox = OffsetImage(image[t.conditions[i]][1])
                        except:
                                imagebox = OffsetImage(image["ясно"][1])
                    else:
                        try:
                                    imagebox = OffsetImage(image[t.conditions[i]][0])
                        except:
                                    imagebox = OffsetImage(image["ясно"][0])


            imagebox.image.axes = ax
            ab = AnnotationBbox(imagebox,  (t.index[i], t.temp[i]), xycoords='data', frameon=False)
            
             
            ax.add_artist(ab)
            
            
        
        ax.axis(ymin = min(t.temp)-9, ymax = max(t.temp)+4)
        ax.axis(xmin = min(t.index)-datetime.timedelta(hours=1), xmax = max(t.index)+datetime.timedelta(hours=1))
#        ax2.axis(ymin = min(t.pressure)-5, ymax = max(t.pressure)+1)
        
#        ax.set_title("Temperature and humidity", fontsize=20)
        fig.tight_layout()
        plt.savefig('image/forecast_plot.png', dpi=100)
#        plt.show()
        plt.close()
        #%%
        
        
        import weather_get
        from PIL import Image, ImageDraw, ImageFont
        
        now = weather_get.current_weather()
        plot = Image.new("RGBA", (900, 1600))
        im = Image.new("RGBA", (900, 1300))
        draw = ImageDraw.Draw(im)
        
        try:
            if str(now['weather'][0]['description']) == "слегка облачно" or str(now['weather'][0]['description']) == "ясно":
                
                if datetime.datetime.today() < datetime.datetime.strptime(sun[0], '%a %b %d %H:%M:%S %Y') and  datetime.datetime.today() >datetime.datetime.strptime(sun[1], '%a %b %d %H:%M:%S %Y'):
                    image1 = Image.open("image/icon set/"+str(now['weather'][0]['description'])+"1.png").resize((200,200), resample=0)
                else:
                    image1 = Image.open("image/icon set/"+str(now['weather'][0]['description'])+".png").resize((200,200), resample=0)
            else:
                    image1 = Image.open("image/icon set/"+str(now['weather'][0]['description'])+".png").resize((200,200), resample=0)
        except:
            image1 = Image.open("image/icon set/none.png").resize((200,200), resample=0)
            
        temp_icon = Image.open("image/icon set/temp_icon.png").resize(( 80, 80), resample=0)
       
        plot_im = Image.open("image/forecast_plot.png")
        sun_icon = [Image.open("image/icon set/forecast/рассвет.png"),Image.open("image/icon set/forecast/закат.png")]
#        draw.line((0,0,0,30), fill="gray", width=2) 
        #now = weather_get.current_weather()
        #forecast = weather_get.forecast()
        
        
        im.paste(image1, (0,0), mask=image1)   
        draw.text((190,55), str(int(now['main']['temp'])) ,
                  font = ImageFont.truetype("arial.ttf", 110), 
                  fill="white")
        
        im.paste(temp_icon, (320,40), mask=temp_icon)
        draw.text((320,400), "", font = ImageFont.truetype("arial.ttf", 100), fill="white")
        
        
            
        im.paste(sun_icon[0], (77,1190), mask=sun_icon[0])
        im.paste(sun_icon[1], (762,1190), mask=sun_icon[1])
        
        draw.text((77,1260),str(datetime.datetime.strptime(sun[0], '%a %b %d %H:%M:%S %Y').strftime("%H:%M")),
                  font = ImageFont.truetype("arial.ttf", 22), 
                  fill="white")
        draw.text((762,1260),str(datetime.datetime.strptime(sun[1], '%a %b %d %H:%M:%S %Y').strftime("%H:%M")),
                  font = ImageFont.truetype("arial.ttf", 22), 
                  fill="white")
         
        
        
        icon = Image.open("image/icon set/visibility.png").resize(( 60, 60), resample=0)    
        im.paste(icon, (351,1190), mask=icon)
        draw.text((341,1260), str(now['visibility']/1000)+" km",
                  font = ImageFont.truetype("arial.ttf", 22), 
                  fill="white")
            
        icon = Image.open("image/icon set/forecast/ветренно.png").resize(( 70, 60), resample=0)    
        im.paste(icon, (498,1190), mask=icon)
        draw.text((488,1260), str(int(now['wind']['speed']*3.6))+" km/h",
                  font = ImageFont.truetype("arial.ttf", 22), 
                  fill="white")
        
        icon = Image.open("image/icon set/pressure.png").resize(( 60, 60), resample=0)    
        im.paste(icon, (625,1190), mask=icon)
        draw.text((615,1260), str(int(now['main']['pressure']/1.3332))+" mm",
                  font = ImageFont.truetype("arial.ttf", 22),
                  fill="white")
        
        icon = Image.open("image/icon set/humidity.png").resize(( 60, 60), resample=0)    
        im.paste(icon, (214,1190), mask=icon)
        draw.text((224,1260), str(int(now['main']['humidity']))+" %",
                  font = ImageFont.truetype("arial.ttf", 22), 
                  fill="white")
         
         
        plot.paste(im, (0,0))
        
        plot.paste(plot_im, (0,1300))
        
        
        
        
        
        plot.show()
        plot.save("image/weather.png")
        
        
        
        
        
plot_get()
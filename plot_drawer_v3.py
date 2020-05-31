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
            "savefig.edgecolor": "black"})
        fig, ax = plt.subplots(figsize=(9, 4), dpi=100)

        ax.plot(t.index, t.temp, 'o-',  color='white'  ) 
        ax.fill_between(t.index, t.temp, facecolor = 'blue', alpha=0.1)
        ax.tick_params(axis='x')
        ax.set_xticklabels([], minor = True)
#        ax.grid()
        ax2 = ax.twinx()
#        ax2.set_ylabel('Humidity, %', color = 'white')
        ax2.plot(t.index, t.pressure,'o-', color='white' ) 
        ax2.tick_params(axis='x')
#        ax2.grid()
#        ax2.title.set_text('Hudimidity(%)')
        ax2.fill_between(t.index, t.pressure, facecolor = 'lightblue', alpha=0.5)
        plt.axvline(x="23:59:59", color = "gray")


        from matplotlib.dates import DateFormatter, HourLocator
        ax.xaxis.set_major_formatter(DateFormatter('%H h'))
        ax.xaxis.set_minor_locator(HourLocator())
        
        import matplotlib.ticker as ticker
        ax.yaxis.set_major_locator(ticker.MultipleLocator(5.00))
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(1.00))
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%d °С"))
        
        ax2.yaxis.set_major_locator(ticker.MultipleLocator(1.00))
        ax2.yaxis.set_minor_locator(ticker.MultipleLocator(.25))
        ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter("%d mm"))

        image = { 'ясно' : plt.imread('image/icon set/forecast/ясно.png'), 
                  'облачно' : plt.imread('image/icon set/forecast/облачно.png'),
                  'слегка облачно' : plt.imread('image/icon set/forecast/слегка облачно.png'),
                  'легкий дождь' : plt.imread('image/icon set/forecast/легкий дождь.png'),
                  'пасмурно' : plt.imread('image/icon set/forecast/пасмурно.png')}
        plt.imshow(image["ясно"])
        import datetime
        ax.text(datetime.datetime.today().strftime("'%Y-%m-%d %H:%M:%S"),((t.temp[0]+t.temp[1])/2)-3 ,"^Now" , color = "Lime")
        for i in range (0,8):
            ax.figure.figimage(image[t.conditions[i]], 70+(i*95), 60, alpha=1, zorder=1)
            ax.text(t.index[i], t.temp[i]+1, str(int(t.temp[i]))+"°С", color = "white")
            ax2.text(t.index[i], t.pressure[i]+.25, str(int(t.pressure[i]))+"mm", color = "white")
            
            
        ax.axis(ymin = min(t.temp)-7, ymax = max(t.temp)+10)
        ax2.axis(ymin = min(t.pressure)-5, ymax = max(t.pressure)+1)
        
#        ax.set_title("Temperature and humidity", fontsize=20)
        fig.tight_layout()
        plt.savefig('image/forecast_plot.png', dpi=100)
#        plt.show()
        plt.close()
        #%%
        
        
        import weather_get
        from PIL import Image, ImageDraw, ImageFont
        
        now = weather_get.current_weather()
        plot = Image.new("RGBA", (900, 600))
        im = Image.new("RGBA", (900, 200))
        draw = ImageDraw.Draw(im)
        image = Image.open("image/icon set/"+str(now['weather'][0]['description'])+".png").resize((200,200), resample=0)
        temp_icon = Image.open("image/icon set/temp_icon.png").resize(( 70, 70), resample=0)
        plot_im = Image.open("image/forecast_plot.png")
#        draw.line((0,0,0,30), fill="gray", width=2) 
        #now = weather_get.current_weather()
        #forecast = weather_get.forecast()
        
        im.paste(image, (0,0), mask=image)
        draw.text((200,55), str(int(now['main']['temp'])) , font = ImageFont.truetype("arial.ttf", 85), fill="white")
        im.paste(temp_icon, (300,40), mask=temp_icon)
        draw.text((320,400), "", font = ImageFont.truetype("arial.ttf", 85), fill="white")
        
        
        plot.paste(im, (0,0))
        
        plot.paste(plot_im, (0,200))
        
        plot.show()
        plot.save("image/weather.png")
        
        
        
        
        
plot_get()
from django.shortcuts import render
import pandas as pd
import datetime

# Create your views here.
def index(request):
    return render(request,'predict.html')

def predict(request):
    date = request.POST['date']
    time = request.POST['time']
    sa = float(request.POST['sa'])
    ct = int(request.POST['ct'])
    dp = int(request.POST['dp'])
    sza =float(request.POST['sza'])
    p = float(request.POST['p'])
    wd = float(request.POST['wd'])
    ws = float(request.POST['ws'])
    rh = float(request.POST['rh'])
    t = float(request.POST['t'])
    pw = float(request.POST['pw'])
        # Unpickle model
    model = pd.read_pickle(r"decidion_model.pickle")
        # Make prediction
    
    hour = time.split(':')[0]
    minute = time.split(':')[1]
    month = date.split('-')[1]
    year = date.split('-')[0]
    day = date.split('-')[2]
    hm = hour+'.'+minute
    list=[[year,day,hm,sa,ct,dp,sza,month,p,wd,ws,rh,t,pw]]
    
    result = model.predict(list)
    data={'Year':year,'Month':month,'Day':day,'HourMinute':hm,'SurfaceAlbedo':sa,'CloudType':ct,'DewPoint':dp,'Solar':sza,'Pressure':p,'winddirection':wd,'windspeed':ws,'Humidity':rh,'temp':t,'Precipitation':pw

    ,'GHI':result[0]}

    classification = result[0]
    return render(request,'predict.html',{'prediction':classification})


from django.shortcuts import render

import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
	"X-RapidAPI-Key": "91ea35d90fmsh2775fe5bb0c399ap168040jsn2bf1be1e7987",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()



def helloworld(request):
    mylist=[]
    numofresults=int(response['results'])
    for x in range(0,numofresults):
        mylist.append(response['response'][x]['country'])

    if request.method=="POST":
        selectedcountry = request.POST['selectedcountry']
        
       
        for x in range(0,numofresults):
            if selectedcountry==response['response'][x]['country']:
                new=response['response'][x]['cases']['new']
                active=response['response'][x]['cases']['active']
                critical=response['response'][x]['cases']['critical']
                recovered=response['response'][x]['cases']['recovered']
                total=response['response'][x]['cases']['total']
                deaths=int(total)-int(active)-int(recovered)

        context={'selectedcountry' : selectedcountry,'mylist' : mylist,'new' : new,'active' : active,'critical' : critical,'recovered' : recovered,'deaths' : deaths,'total' : total}
        return render(request,'webpage.html',context)

    numofresults=int(response['results'])
   
    context={'mylist' :mylist}
    return render(request,'webpage.html',context)

    

 
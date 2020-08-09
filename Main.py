import yaml  
from tkinter import *

def readjson(path):
    with open (path) as f:
        data=yaml.safe_load(f)
        return data

    
def pop_show10():
    toplevel1=Toplevel(bg="#585D3C")
    data_pop=readjson("node_modules\country-json\src\country-by-population.json")
    for i in range(243):
        for j in range(242):
            if(int(data_pop[i]["population"])<int(data_pop[j]["population"])):
                kova=data_pop[j]
                data_pop[j]=data_pop[i]
                data_pop[i]=kova
                
    for a in range(11):
        Label(toplevel1,bg="#585D3C",text=str(a+1)+"  "+data_pop[242-a]["country"]+"     "+data_pop[242-a]["population"]).pack()

def top10area():
    top=Toplevel(bg="#585D3C")
    top.title("Top 10 Surface Area")
    listem=readjson("node_modules\country-json\src\country-by-surface-area.json")
    for i in range (239):
        for j in range(239):#bubble catch
            if(int(listem[i]["area"])<int(listem[j]["area"])):
                tmp=listem[j]
                listem[j]=listem[i]
                listem[i]=tmp
    for  k in range(11):
        Label(top,bg="#585D3C",text=str(k+1)+". Country "+listem[238-k]["country"]+"   Area = "+str(listem[238-k]["area"])).pack()

def textOlustur():
    
    verim=readjson('node_modules\country-json\src\country-by-name.json')

    for i in range(241):
        listNodes.insert(END, str(verim[i]["country"]))

def go (event):
    
    i_secimim=listNodes.curselection()
    


    verim=readjson('node_modules\country-json\src\country-by-name.json')
    for i in i_secimim:
        top=Toplevel(bg="#585D3C") 
        #canvas =Canvas(root,width=800,height=600)

        #image1 = ImageTk.PhotoImage(Image.open("node_modules\\country-json\\src\\askerpostali.jpg"))
        #canvas.create_image(0,0,anchor=NW,image=image1).pack()
        top.title(str(verim[i]["country"]))  
      
        
        temp="" 




        verim2=readjson("node_modules\country-json\src\country-by-capital-city.json")
        temp="" 
        for j in range(242):

            if(verim2[j].get("country")==str(verim[i]["country"]) ):
                temp+=str(verim2[j]["city"])+"  "
                label=Label(top,text="Capital city = "+ temp,bg="#585D3C")
                label.grid(column=0,row=0)
        


        
        temp=""
        verim2=readjson("node_modules\country-json\src\country-by-languages.json")
        
        for j in range(994):

            if(verim2[j].get("country")==str(verim[i]["country"]) ):

                temp+=verim2[j]["language"]+"  "

        label=Label(top,text="Language = "+ temp,bg="#585D3C")
        label.grid(column=0,row=1)
 

        verim2=readjson("node_modules\country-json\src\country-by-abbreviation.json")
        temp=""
        for j in range(246):

            if(verim2[j].get("country")==str(verim[i]["country"]) ):

                temp+=verim2[j]["abbreviation"]+"  "
        
        label=Label(top,text="Abbreviation = "+str(temp),bg="#585D3C")
        label.grid(column=2 ,row=4)

        verim2=readjson("node_modules\country-json\src\country-by-region-in-world.json")
        for j in range(243):
            if(verim2[j].get("country")==(str(verim[i]["country"]))):
                label=Label(top,text="Location ="+str(verim2[j]["location"]),bg="#585D3C")
                label.grid(column=0,row=3,padx=50,pady=20)

        
        verim2=readjson("node_modules\country-json\src\country-by-government-type.json")
        for j in range(243):
             if(verim2[j].get("country")==(str(verim[i]["country"]))):
                 label=Label(top,text="Goverment Type ="+str(verim2[j]["government"]),bg="#585D3C")
                 label.grid(column=0,row=4,padx=50,pady=20)



        verim2=readjson("node_modules\country-json\src\country-by-surface-area.json")
        for j in range(239):
             if(verim2[j].get("country")==(str(verim[i]["country"]))):
                 label=Label(top,text="Area ="+str(verim2[j]["area"])+"  square kilometers",bg="#585D3C")
                 label.grid(column=1,row=0,padx=50,pady=20)
        
        verim2=readjson("node_modules\country-json\src\country-by-population.json")
        for j in range(243):
             if(verim2[j].get("country")==(str(verim[i]["country"]))):
                 label=Label(top,text="Population ="+str(verim2[j]["population"])+ " people",bg="#585D3C")
                 label.grid(column=1,row=1,padx=50,pady=20)


        verim2=readjson("node_modules\country-json\src\country-by-population-density.json")
        for j in range(243):
             if(verim2[j].get("country")==(str(verim[i]["country"]))):
                 label=Label(top,text="Population density ="+str(verim2[j]["density"])+" per sq. mi.",bg="#585D3C")
                 label.grid(column=1,row=2,padx=50,pady=20)



        verim2=readjson("node_modules\country-json\src\country-by-independence-date.json")
        for j in range(243):
             if(verim2[j].get("country")==(str(verim[i]["country"]))):
                 label=Label(top,text="Independence ="+str(verim2[j]["independence"]),bg="#585D3C")
                 label.grid(column=1,row=3,padx=50,pady=20)

        verim2=readjson("node_modules\country-json\src\country-by-currency-name.json")
        for j in range(243):
             if(verim2[j].get("country")==(str(verim[i]["country"]))):
                 label=Label(top,text="Currency Name ="+str(verim2[j]["currency_name"]),bg="#585D3C")
                 label.grid(column=1,row=4,padx=50,pady=20)


        verim2=readjson("node_modules\country-json\src\country-by-domain-tld.json")
        for j in range(243):
             if(verim2[j].get("country")==(str(verim[i]["country"]))):
                 label=Label(top,text="Top Level Domain="+str(verim2[j]["tld"]),bg="#585D3C")
                 label.grid(column=2,row=0,padx=50,pady=20)
                    
        verim2=readjson("node_modules\country-json\src\country-by-calling-code.json")
        for j in range(243):
             if(verim2[j].get("country")==(str(verim[i]["country"]))):
                 label=Label(top,text="Calling Code="+str(verim2[j]["calling_code"]),bg="#585D3C")
                 label.grid(column=2,row=1,padx=50,pady=20)

        verim2=readjson("node_modules\country-json\src\country-by-religion.json")
        for j in range(240):
             if(verim2[j].get("country")==(str(verim[i]["country"]))):
                 label=Label(top,text="Religion="+str(verim2[j]["religion"]),bg="#585D3C")
                 label.grid(column=2,row=2,padx=50,pady=20)

        verim2=readjson("node_modules\country-json\src\country-by-yearly-average-temperature.json")
        for j in range(243):
             if(verim2[j].get("country")==(str(verim[i]["country"]))):
                 label=Label(top,text="Yearly Average Temperature ="+str(verim2[j]["temperature"]),bg="#585D3C")
                 label.grid(column=2,row=3,padx=50,pady=20)

        verim2=readjson("node_modules\country-json\src\country-by-life-expectancy.json")
        for j in range(243):
             if(verim2[j].get("country")==(str(verim[i]["country"]))):
                 label=Label(top,text="Life Expectancy="+str(verim2[j]["expectancy"]),bg="#585D3C")
                 label.grid(column=3,row=3,padx=50,pady=20)
        verim2=readjson("node_modules\country-json\src\country-by-avg-male-height.json")
        for j in range(243):
             if(verim2[j].get("country")==(str(verim[i]["country"]))):
                 label=Label(top,text="Average Male Height="+str(verim2[j]["height"]),bg="#585D3C")
                 label.grid(column=3,row=4,padx=50,pady=20)
        verim2=readjson("node_modules\country-json\src\country-by-geo-coordinates.json")
        temp=""
        for j in range(242):
            if(verim2[j].get("country")==str(verim[i]["country"])):
                temp+="North :"+ str(verim2[j]["north"])+"  "+"\n"
                temp+="South :"+ str(verim2[j]["south"])+"  "+"\n"
                temp+="West :" +str(verim2[j]["west"])+"  "+"\n"
                temp+="East :" +str(verim2[j]["east"])+"  "+"\n"
        
        label=Label(top,text=temp,bg="#585D3C")
        label.grid(column=0,row=2)



def ara_func():
    verim=readjson('node_modules\country-json\src\country-by-name.json')
    kontrol=True
    for i in range(241):
        if( str(str.upper( mystring.get()))[0]==verim[i]["country"][0] and kontrol==True):#listeyi tara
            kontrol=False
            listNodes.yview(i)
            break

root=Tk()
root.configure(bg="#585D3C")
root.title("General Information About Countries")


show_population_b=Button(root,text="Top 10 Population",command=pop_show10,fg="#000000",bg="#585D3C").pack(side="top")
show_area=Button(root,text="Area",command=top10area,bg="#585D3C").pack(side="top")


frame = Frame(root)
frame.pack(side= LEFT)

mystring =StringVar(root)
e1 = Entry(root,textvariable = mystring,width=30,fg="blue",bd=3,selectbackground='violet').pack()
butooon= Button(root,text="Search",command=ara_func).pack(side="top")


listNodes = Listbox(frame, width=20, height=20, font=("Helvetica", 12))



scrollbar = Scrollbar(frame, orient="vertical")
scrollbar.config(command=listNodes.yview)
scrollbar.pack(side="left", fill="y")



textOlustur()


listNodes.bind('<Double-1>', go) 
listNodes.pack(side="left", fill="y")







root.mainloop()
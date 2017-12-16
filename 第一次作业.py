dic={"张三":{"年龄":18,"联系方式":111},"李四":{"年龄":29,"联系方式":222}}
while True :

    InputMes=input("输入信息").strip()
    if InputMes == "delete":
        DelMEs=input("输入需要删除的用户名").strip()
        if DelMEs in dic:
            del dic[DelMEs]
            print ("修改后的数据库为",dic)
        else:
            print ("用户不存在")
    elif InputMes == "update":
        UpdateMes=input("输入需要更新的用户信息，格式为:用户名:年龄:联系方式").strip()
        UserName=UpdateMes.split(':')[0]
        if UserName in dic :
            dic[UserName]["年龄"]=UpdateMes.split(':')[1]
            dic[UserName]["联系方式"]=UpdateMes.split(':')[2]
            print(dic)
        else:
            print ("用户不存在")
    elif InputMes == "find":
        FindMes=input("输入需要查找的用户名").strip()
        if FindMes in dic :
            print(dic[FindMes])
        else :
            print ("用户不存在")
    elif InputMes == "list":
        print([i for i in dic.keys()])
        print([i for i in dic.values()])
    elif InputMes == "exit":
        print("程序结束")
        break
    else :
        print("请输入有效的关键字")
        print("有效的关键字为:delete,update,find,list,exit")
        

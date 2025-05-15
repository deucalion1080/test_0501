#BMI 偵測體質版本 + elif 
#ipynb =>測試與學習用
try:
    height:float = float(input("請輸入您的身高(要120~220公分之間):"))
    if height <120 or height >220 :
        raise Exception(f"您輸入的身高是:{height} 超出範圍!請重新輸入")
    weight:float = float(input("請輸入您的體重(要30~200公斤之間):"))
    if weight <30 or weight >200 :
        raise Exception(f"您輸入的體重是:{weight} 超出範圍!請重新輸入")
    BMI = weight/(height/100)**2
    
except ValueError:       
     print("輸入值錯誤!請重新輸入!")    
except Exception as error:
    print(error)
else:   
    print(f"您的身高是:{height}公分")
    print(f"您的體重是:{weight}公斤")
    print(f"您的BMI結果是:{BMI:.2f}")
    if BMI < 18.5 :
        print("體重過輕!")
    elif BMI < 24 :
        print("體重正常!")
    elif BMI < 27 :
        print("體重過重!")
    elif BMI < 30 :
        print("體重輕度肥胖!")
    elif BMI < 35 :
        print("體重中度肥胖!")
    else :
        print("體重重度肥胖!")
print("BMI偵測結束!")

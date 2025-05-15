#BMI 偵測體質版本 + elif 
#ipynb =>測試與學習用
def caculate_bmi(height:float,weight:float):
    if height <120 or height >220 :
        raise Exception(f"您輸入的身高是:{height} 超出範圍!請重新輸入")
    if weight <30 or weight >200 :
        raise Exception(f"您輸入的體重是:{weight} 超出範圍!請重新輸入")
    
    BMI_caculate = weight/(height/100)**2    
    return BMI_caculate 
def get_state(BMI:float)->str:
    if BMI < 18.5 :
        message = "體重過輕!"
    elif BMI < 24 :
        message = "體重正常!"
    elif BMI < 27 :
        message = "體重過重!"
    elif BMI < 30 :
        message = "體重輕度肥胖!"
    elif BMI < 35 :
        message = "體重中度肥胖!"
    else :
        message = "體重重度肥胖!"
     
def main():
    try:
        height:float = float(input("請輸入您的身高(要120~220公分之間):"))        
        weight:float = float(input("請輸入您的體重(要30~200公斤之間):"))        
        BMI = caculate_bmi(height,weight)
    
    except ValueError:       
            print("輸入值錯誤!請重新輸入!")    
    except Exception as error:
            print(error)
    else:   
        print(f"您的身高是:{height}公分")
        print(f"您的體重是:{weight}公斤")
        print(f"您的BMI結果是:{BMI:.2f}")
        print(get_state(BMI))
        
    print("BMI偵測結束!") 
if __name__ == "__main__":
    main()
    


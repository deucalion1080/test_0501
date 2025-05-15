#BMI 偵測體質版本 + elif 
#ipynb =>測試與學習用
#import les06_tools
from les06_tools import caculate_bmi,get_state

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
    


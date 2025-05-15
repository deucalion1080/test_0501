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
    return message
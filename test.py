down_line = float(input("삼각형의 밑변의 길이를 입력하세요."))
height = float(input("삼각형의 높이를 입력하세요"))
scale = down_line * height * 0.5
print("삼각형의 넓이는" +str(scale)+ '입니다')


f_temp = int(input("화씨온도를 입력하세요"))
c_temp = (f_temp - 32)/1.8
print('화씨' +str(f_temp)+ '도는 섭씨' +str(c_temp)+ '도입니다')


mass = int(input("물체의 질량을 입력하세요"))
speed = int(input("물체의 속도를 입력하세요"))
kinetic_e = mass * speed * speed * 0.5
print("이 물체의 운동에너지 값은" +str(kinetic_e)+ "입니다")


birth_year = int(input("출생연도를 입력하세요"))
n = birth_year % 12
if n == 0:
    print("원숭이띠")
if n == 1:
    print("닭띠")
if n == 2:
    print("개띠")
if n == 3:
    print("돼지띠")
if n == 4:
    print("쥐띠")
if n == 5:
    print("소띠")
if n == 6:
    print("호랑이띠")
if n == 7:
    print("토끼띠")
if n == 8:
    print("용띠")
if n == 9:
    print("뱀띠")
if n == 10:
    print("말띠")
if n == 11:
    print("양띠")


print("이차방정식 ax^2+bx+c=0이 있다. 다음 질문에 성실히 답하면 근을 알려주겠다.")
aa = float(input("a의 값을 입력하시오"))
bb = float(input("b의 값을 입력하시오"))
cc = float(input("c의 값을 입력하시오"))
if ((bb)**2 - 4* aa *cc >= 0):
    if ((bb)**2 - 4* aa*cc > 0):
        solution_1 = (-bb + ((bb) **2 - 4* aa* cc) ** (0.5)) / (2*aa)
        solution_2 = (-bb - ((bb) ** 2 - 4 * aa * cc) ** (0.5)) / (2*aa)
        print('이차방정식의 근은' +str(solution_1)+ '와' +str(solution_2)+ '입니다')
    else:
        solution_1 = -bb / (2*aa)
        print('이차방정식의 근은' +str(solution_1)+ '입니다')
else:
    print("해당 방정식은 실근을 갖지 않습니다")
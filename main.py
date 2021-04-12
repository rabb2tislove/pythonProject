print("이차방정식 ax^2+bx+c=0이 있다. 다음 질문에 성실히 답하면 근을 알려주겠다.")
aa = float(input("a의 값을 입력하시오"))
bb = float(input("b의 값을 입력하시오"))
cc = float(input("c의 값을 입력하시오"))
if ((bb)**2 - 4* aa *cc >= 0):
    if ((bb)**2 - 4* aa*cc > 0):
        solution_1 = (-bb + ((bb)**2 - 4* aa* cc) ** (0.5)) / (2*aa)
        solution_2 = (-bb - ((bb) ** 2 - 4 * aa * cc) ** (0.5)) / (2*aa)
        print('이차방정식의 근은' +str(solution_1)+ '와' +str(solution_2)+ '입니다')
    else:
        solution_1 = -bb / (2*aa)
        print('이차방정식의 근은' +str(solution_1)+ '입니다')
else:
    print("해당 방정식은 실근을 갖지 않습니다")
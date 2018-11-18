def answer():
    P = [1,2,3,4,5,6,7,8,9]
    E = [1,2,3,4,5,6,7,8,9]

    for number_P in P:
        P__P = number_P*1001
        PP = number_P*11
        for number_E in E:
            _EE_ = number_E*110
            if P__P+_EE_ == PP**number_E:
                print(P__P+_EE_,"= ("+str(PP)+")^"+str(number_E))

if __name__ == "__main__":
    print(answer())

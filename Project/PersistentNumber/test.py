

num = int(input("Please give me an integer (negative to quit): "))

while num >0:
    m_num = num
    a_num = num
    
    m_count = 0
    
    print("Multiplicative loop")
    while m_num//10>0:
        m_count+=1
        prod = 1
        while m_num>0:
            prod *= m_num%10
            m_num=m_num//10
        print("product:",prod)
        m_num = prod
    #print(m_count)
    print()
    a_count = 0
    print("Additive loop")
    while a_num//10>0:
        a_count+=1
        total = 0
        while a_num>0:
            total += a_num%10
            a_num=a_num//10
        print("sum:",total)
        a_num = total
    #print(a_count)
    
    print()
    print("For the interger:",num)
    print("\tAdditive persistence:",a_count,", Additive root:",a_num)
    print("\tMultiplicative persistence:",m_count,", Multiplicative root:",m_num)
    
    num = int(input("Please give me an integer (negative to quit): "))
else:
    print("Thank you for playing!")

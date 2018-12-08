



calc = [1,2,3, "*", "+", 2, "-"]

st = []

for i in calc:
    if type (i) == int:
        st.append(i)
        continue

    if i == "Z":
        print("Zuzuzu!!!")
        continue
    
    if i == "*":
        a = st.pop()
        b = st.pop()
        c = a*b
        st.append(c)
        

    if i == "+":
        if len(st) < 2:
            print("sorry, invalid operator ", i)
            continue
        
        a = st.pop()
        b = st.pop()
        c = a+b
        st.append(c)  
    
    if i == "-":
        a = st.pop()
        b = st.pop()
        c = b-a
        st.append(c)
        
    if i == "/":
        a = st.pop()
        b = st.pop()
        c = b/a
        st.append(c)  




    
print(st)

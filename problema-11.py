a = {'A', 'B', 'C', 'D'}
b='A'
c='B'
d='C'
e='C'
print("submultimi cu 1 element: ", ({b}),({c}),({d}),({e}))
print("submultimi cu 2 elemente: ",({b,c}),({c,d}),({d,e}),({e,b}),({b,d}))
print("submultimi cu 3 elemente: ",({b,c,d}),({c,d,e}),({d,e,b}),({b,e,c}))
print("submultimi cu 4 elemente: ",({b,c,d,e}))
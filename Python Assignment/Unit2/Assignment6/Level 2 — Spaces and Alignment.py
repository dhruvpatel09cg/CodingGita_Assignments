# Q13
# N = int(input("N:"))
# for u in range(1,N+1):
#     for v in range(1,N-u+1):
#         print(" ",end="")
#     for w in range(1,u+1):
#         print("*",end="")
#     print()

# Q14
# N = int(input("N:"))
# for x in range(1,N+1):
#     for z in range(1,x):
#         print(" ",end="")
#     for y in range(N-x+1,0,-1):
#         print("*",end="")
#     print()

# Q15
# N = int(input("N:"))
# for u in range(1,N+1):
#     for v in range(1,N-u+1):
#         print(" ",end="")
#     for w in range(1,2*u):
#         print("*",end="")
#     print()

# Q16
# N = int(input("N:"))
# for x in range(1,N+1):
#     for z in range(1,x):
#         print(" ",end="")
#     for y in range((N-x)*2+1,0,-1):
#         print("*",end="")
#     print()

# Q17
# N = int(input("N:"))
# for u in range(1,N+1):
#     for v in range(1,N-u+1):
#         print(" ",end="")
#     for w in range(1,2*u):
#         print("*",end="")
#     print()
# for u in range(N+1,2*N):
#     for z in range(N,u):
#         print(" ",end="")
#     for y in range((2*N-u)*2,1,-1):
#         print("*",end="")
#     print()

# Q18
# N = int(input("N:"))
# for x in range(1,N+1):
#     for z in range(N-x,0,-1):
#         print(" ",end="")
#     for y in range(N):
#         print("*",end="")
#     print()

# Q19
# N = int(input("N:"))
# for a in range(1,N+1):
#     for b in range (1,a+1):
#         print(b, end="")
#     for c in range(1,2*N-2*a+1):
#         print(" ",end="")
#     for d in range(a,0,-1):
#         print(d,end="")
#     print()

# Q20
# N = int(input("N:"))
# for e in range(1,N+1):
#     for g in range(1,N-e+1):
#         print(" ",end="")
#     for f in range(1,e+1):
#         print(f,end=" ")
#     print()

# Q21
# N = int(input("N:"))
# for h in range(1,N+1):
#     for i in range(1,N-h+1):
#         print(" ",end="")
#     for j in range(1,h+1):
#         print(j,end="")
#     for k in range(1,h):
#         print(h-k,end="")
#     print()

# Q22
# N = int(input("N:"))
# for l in range(1,N+1):
#     for m in range(1,N-l+1):
#         print(" ",end="")
#     for n in range(1,l+1):
#         print(chr(64+n),end="")
#     for o in range(1,l):
#         print(chr(64+l-o),end="")
#     print()

# Q23
# N = int(input("N:"))
# for p in range(1,N+1):
#     for q in range(1,p+1):
#         print(chr(64+N+q-p),end=" ")
#     print()
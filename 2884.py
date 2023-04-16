H,M = map(int,input().split())
if M >= 45 and M < 60:
    print(H, (M-45))
elif H != 0 and M < 45:
    print(H-1, M+60-45)
elif H == 0 and M < 45:
    print(23, M+60-45)
n = int(input("enter number:"))
kha = n // 100
ba = n % 100
khb = ba // 10
bb = ba % 10
sadgan = bb * 100
dahgan = khb * 10
yekan = kha
sum = sadgan + dahgan + yekan
print(sum)
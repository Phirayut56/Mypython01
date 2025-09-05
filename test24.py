# คำสั่ง break, continue
# break ใน Loop ทำงานเมื่อใดจบ Looop ทันที
# continue ใน Loop ทำงานเมื่อใดจบ Loop แต่ รอบนั้นทันที แล้วให้ไปรอบต่อไปได้เลย

for aa in range(5) :
    if aa == 2 :
        break
    print(aa, 'hi ...')

print('+++++++++++++++++++++++++++++++++++')
for aa in range(5) :
    if aa == 2 :
        continue
    print(aa, 'hi...')
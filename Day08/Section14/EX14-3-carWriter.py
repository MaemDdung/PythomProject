



import csv
'''
# 찻번째 방법
with open('차량관리.csv', 'w', encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([1, "08러1234", "2020-10-12,14:10"])
    csv_maker.writerow([2, "07러3215", "2020-10-12,14:20"])
    csv_maker.writerow([3, "06러5315", "2020-10-12,14:30"])
    csv_maker.writerow([4, "05러1588", "2020-10-12,14:40"])
print('차량 관리.csv 파일이 생성되었습니다.')
'''
'''
# 두번째 방법 한줄띄어주는거 없에기
with open('차량관리.csv', 'w', newline='', encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([1, "08러1234", "2020-10-12,14:10"])
    csv_maker.writerow([2, "07러3215", "2020-10-12,14:20"])
    csv_maker.writerow([3, "06러5315", "2020-10-12,14:30"])
    csv_maker.writerow([4, "05러1588", "2020-10-12,14:40"])
print('차량 관리.csv 파일이 생성되었습니다.')
'''
# 3번째 방법 따옴표 없에기
with open('차량관리.csv', 'w', newline='', encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter=',', quotechar=' ') #quotechar='"'가 디폴트다
    csv_maker.writerow([1, "08러1234", "2020-10-12,14:10"])
    csv_maker.writerow([2, "07러3215", "2020-10-12,14:20"])
    csv_maker.writerow([3, "06러5315", "2020-10-12,14:30"])
    csv_maker.writerow([4, "05러1588", "2020-10-12,14:40"])
print('차량 관리.csv 파일이 생성되었습니다.')



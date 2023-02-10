class HourError(Exception):
    def __int__(self):
        super().__init__('올바른 시간이 압닙니다.')
try:
    hour = int(input('시간을 입력해 주세요 >>>'))
    if hour < 0 or hour>23:
        raise HourError

except HourError as e:
    print(e)
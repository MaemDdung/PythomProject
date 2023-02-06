'''
object

클래스
    객체를 만드는 설계도  
    붕어빵 틀, 와플 기계
    객체화(인스턴스화) - 메모리에 올리는 것
    
객체(object)
    현실 세계 존재하는 물리적, 추상적 식별할 수 있는 모든것
    예) 학생, 주문, 배송, 대한민국국민
    
객체 구성
    
    속성값 - 변수
    기능 - 메소드(함수)
    
'''


class Computer:
    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print('CPU = {}'.format(self.cpu))
        print('RAM = {}'.format(self.ram))
        print('VGA = {}'.format(self.vga))
        print('SSD = {}'.format(self.ssd))


desktop = Computer()
desktop.set_spec('i7','18GB','RTX3060', '512GB')
desktop.hardware_info()
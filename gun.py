from machine import Pin, PWM
import time

# gpio 設定
pir = Pin(16, Pin.IN, Pin.PULL_DOWN)
led = Pin(25, Pin.OUT)

SERVO_PIN = 0
PWM_FREQ = 50

def pulse_width(val, freq=PWM_FREQ, resol=65535):
    pulse = freq * val * 1e-6 * resol
    return int(pulse)

servo = PWM(Pin(SERVO_PIN))
servo.freq(PWM_FREQ)

unko=0
print("prepare")
led.value(1)
time.sleep(3)

while True:
    if pir.value() == 0:
        led.value(0)
        duty = pulse_width(1500)
        servo.duty_u16(duty)
        time.sleep(1)
        print("disappear")

    else:
        led.value(1)
        duty = pulse_width(2000)
        servo.duty_u16(duty)
        print("appear")
        unko=unko+1
        print(unko)
        time.sleep(0.1)



import RPi.GPIO as GPIO
import time

triggerPin = 17
echoPin = 27
pinPiezo = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin, GPIO.OUT)    # 출력
GPIO.setup(echoPin, GPIO.IN)        # 입력
GPIO.setup(pinPiezo, GPIO.OUT)

Buzz = GPIO.PWM(pinPiezo, 440)      # 부저센서 초기화

try:
   while True:
      #구형파 발생
      GPIO.output(triggerPin, GPIO.LOW)  
      time.sleep(0.00001) 
      GPIO.output(triggerPin, GPIO.HIGH)

      #시간측정
      while GPIO.input(echoPin) == 0:  # 펄스 발생
         start = time.time()
      while GPIO.input(echoPin) == 1:  # 펄스 돌아옴
         stop = time.time()

      rtTotime = stop - start                   # 리턴 투 타임 = (end시간 - start시간)

      distance = rtTotime * (34000 / 2 )
      print("distance : %.2f cm" %distance)     # 거리 출력
      time.sleep(0.2)  

      if(distance <= 40 and distance > 25):     # 26 ~ 40 cm 일때
         Buzz.start(50)
         Buzz.ChangeFrequency(523)
         time.sleep(0.3)
         Buzz.stop()
         time.sleep(0.3)
      elif(distance <= 25 and distance > 10):   # 25 ~ 11 cm 일때
         Buzz.start(50)
         Buzz.ChangeFrequency(523)
         time.sleep(0.15)
         Buzz.stop()
         time.sleep(0.1)
      elif(distance <= 10):                     # 10cm 이하일때
         Buzz.start(99)
         Buzz.ChangeFrequency(523) 
         time.sleep(0.05)
         Buzz.stop()
         time.sleep(0.05)
      else:                                     # 그 외(겁나 멀때)
         Buzz.stop()
         time.sleep(0.5)

except KeyboardInterrupt:
   GPIO.cleanup()

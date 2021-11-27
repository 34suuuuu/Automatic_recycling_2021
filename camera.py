import picamera as pic
import time

camera = pic.PiCamera()
#camera.brightness = 58 밝기 (0~100) 
#camera.sharpness = 10 
#camera.contrast = 10 명암대비

camera.start_preview()
time.sleep(5)
camera.rotation = 180
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()


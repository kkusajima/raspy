#169.254.189.221

# -*- coding: utf-8 -*-
import time
import wiringpi as pi


motor1_pin = 23
motor2_pin = 24
SW_PIN = 4
SW2_PIN = 10

pi.wiringPiSetupGpio()
pi.pinMode( SW_PIN, pi.INPUT )
pi.pinMode( motor1_pin, pi.OUTPUT)
pi.pinMode( motor2_pin, pi.OUTPUT)

pi.softPwmCreate( motor1_pin, 0, 100)
pi.softPwmCreate( motor2_pin, 0, 100)

pi.softPwmWrite( motor1_pin, 0 )
pi.softPwmWrite( motor2_pin, 0 )

max_speed = 30
max2_speed = max_speed - 1

def go_up():

    print("go_start")
    pi.softPwmWrite( motor1_pin, 0 )
    pi.softPwmWrite( motor2_pin, 0 )
    time.sleep(1)

    speed = 0
    while ( speed <= max_speed):
        
        if ( pi.digitalRead( SW2_PIN ) == pi.HIGH ):
            print("go")
            pi.softPwmWrite( motor1_pin, speed )
            pi.softPwmWrite( motor2_pin, 0 )
            time.sleep(0.3)
            speed = speed + 1
        else:
            print("stop")
            pi.softPwmWrite( motor1_pin, 0 )
            pi.softPwmWrite( motor2_pin, 0 )
            time.sleep(5)
            break

        if speed == max_speed:
            print('max_go')
            if ( pi.digitalRead( SW2_PIN ) == pi.HIGH ):
                print("go_keep")
                pi.softPwmWrite( motor1_pin, max_speed )
                pi.softPwmWrite( motor2_pin, 0 )
                speed = max2_speed
                time.sleep(0.3)
            else:
                print("stop")
                pi.softPwmWrite( motor1_pin, 0 )
                pi.softPwmWrite( motor2_pin, 0 )
                time.sleep(5)
                break

def go_back():

    print("back_start")
    pi.softPwmWrite( motor1_pin, 0 )
    pi.softPwmWrite( motor2_pin, 0 )
    time.sleep(1)

    speed = 0
    while ( speed <= max_speed):

        if ( pi.digitalRead( SW2_PIN ) == pi.HIGH ):
            print("back")
            pi.softPwmWrite( motor1_pin, 0 )
            pi.softPwmWrite( motor2_pin, speed )
            time.sleep(0.3)
            speed = speed + 1
            
        else:
            print("stop")
            pi.softPwmWrite( motor1_pin, 0 )
            pi.softPwmWrite( motor2_pin, 0 )
            time.sleep(5)
            break

        if speed == max_speed:
            print('max_back')
            if ( pi.digitalRead( SW2_PIN ) == pi.HIGH ):
                print("back_keep")
                pi.softPwmWrite( motor1_pin, 0 )
                pi.softPwmWrite( motor2_pin, max_speed )
                speed = max2_speed
                time.sleep(0.3)
            else:
                print("stop")
                pi.softPwmWrite( motor1_pin, 0 )
                pi.softPwmWrite( motor2_pin, 0 )
                time.sleep(5)
                break

def main():

    pi.softPwmWrite( motor1_pin, 0 )
    pi.softPwmWrite( motor2_pin, 0 )

    while True:
        print("start")
        time.sleep(3)
        if ( pi.digitalRead( SW_PIN ) == pi.HIGH ):
            print("main_go")
            time.sleep(3)
            go_up()
        else:
            print("main_back")
            time.sleep(3)
            go_back()

main()




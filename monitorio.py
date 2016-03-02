#!/usr/bin/env python
from time import sleep, time
from subprocess import check_call

DRIVE = 'sda'
STATS_PATH = '/proc/diskstats'
LED_PATH = '/sys/class/leds/a3g_led/color'


def activate_led():
    print('activate')
    with open(LED_PATH, 'w') as led:
        led.write('green')


def deactivate_led():
    print('deactivate')
    with open(LED_PATH, 'w') as led:
        led.write('blue')


def sleep_drive():
    print('sleep')
    check_call('hdparm -y /dev/{}'.format(DRIVE).split())


def monitor_disk():
    prev_val = 0
    led_active = False
    drive_active = True
    last_active_time = time()

    while (True):
        for line in open(STATS_PATH, 'r').readlines():
            if '{} '.format(DRIVE) in line:
                val = int(line.split()[12])

                if val > prev_val:
                    last_active_time = time()
                    drive_active = True
                    if not led_active:
                        activate_led()
                        led_active = True
                    prev_val = val

                elif drive_active and time() - last_active_time > 900:  # 15 mins
                    deactivate_led()
                    led_active = False
                    sleep_drive()
                    drive_active = False

        sleep(1)


if __name__ == '__main__':
    monitor_disk()

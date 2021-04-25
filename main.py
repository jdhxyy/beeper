"""
Copyright 2021-2021 The jdh99 Authors. All rights reserved.
室外温度显示
Authors: jdh99 <jdh821@163.com>
"""

import tziot
import time
import ssd1306py as lcd
import machine
import font
import dcompy
import lagan
import utime

# 本节点地址和密码
IA =
PWD =

# 目标节点地址
DST_IA =

# WIFI账号密码
WIFI_SSID =
WIFI_PWD =

# 服务号
# 读取时间
RID_GET_TIME = 1

# 读取温度
RID_GET_TEMP = 1

# 本机提供的服务
# 按键
RID_KEY = 1

# 通信管道
pipe = 0

# 对方发送过来的信息
rx_text = ''

# 灯
red_led = None
blue_led = None
# 蜂鸣器
beep = None
# 按键
key = list()

# 上次按键时间
last_push_time = 0

# 是否接收到新消息
is_rx_msg = False

# 日期
date_text = ''
# 温度
outdoor_temp = 0


def main():
    global pipe

    lagan.set_filter_level(lagan.LEVEL_OFF)
    dcompy.set_filter_level(lagan.LEVEL_OFF)

    # 初始化设备
    init_device()
    # 初始化OLED屏
    init_oled()
    # 连接wifi
    connect_wifi()

    pipe = tziot.bind_pipe_net(IA, PWD, '0.0.0.0', 12025)
    # 注册按键服务
    tziot.register(RID_KEY, service_key)
    tziot.run(app)


def init_device():
    global red_led, blue_led, beep
    red_led = machine.Pin(25, machine.Pin.OUT)
    red_led.value(1)
    blue_led = machine.Pin(26, machine.Pin.OUT)
    blue_led.value(1)
    beep = machine.Pin(27, machine.Pin.OUT, machine.Pin.PULL_DOWN)
    beep.value(0)

    key.append(machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP))
    key.append(machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP))
    key.append(machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP))
    key.append(machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP))
    key.append(machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP))
    key.append(machine.Pin(33, machine.Pin.IN, machine.Pin.PULL_UP))


def init_oled():
    lcd.init_i2c(22, 21, 128, 64)
    lcd.set_font(font.font16, 16)
    lcd.set_font(font.font32, 32)
    lcd.text_cn('系统启动中', 0, 25, 16)
    lcd.text('...', 80, 25, 16)
    lcd.show()


def connect_wifi():
    ok = tziot.connect_wifi(WIFI_SSID, WIFI_PWD)
    if ok is False:
        print('connect wifi failed')
        lcd.clear()
        lcd.text_cn('连接', 0, 25, 16)
        lcd.text('wifi', 32, 25, 16)
        lcd.text_cn('失败', 64, 25, 16)
        lcd.show()
        machine.reset()
    print('connect wifi success')
    lcd.clear()
    lcd.text_cn('连接', 0, 25, 16)
    lcd.text('wifi', 32, 25, 16)
    lcd.text_cn('成功', 64, 25, 16)
    lcd.show()


def service_key(pipe: int, src_ia: int, req: bytearray) -> (bytearray, int):
    """按键服务"""
    global rx_text, red_led, beep, is_rx_msg
    if len(req) != 1:
        return None, 0

    is_rx_msg = True

    if req[0] == 0:
        rx_text = '出来玩'
    elif req[0] == 1:
        rx_text = '好的'
    elif req[0] == 2:
        rx_text = '不好'
    elif req[0] == 3:
        rx_text = '到我家写作业'
    elif req[0] == 4:
        rx_text = '呼叫'
    print('rx msg', rx_text)
    return None, 0


def app():
    """业务程序.每分钟获取ntp时间"""
    global pipe, red_led, blue_led, beep, is_rx_msg, rx_text, date_text, outdoor_temp

    # 连接物联网
    fail_num = 0
    while True:
        if fail_num >= 10:
            print('connect too many.reset!')
            machine.reset()

        if not tziot.is_conn():
            fail_num += 1
            time.sleep(10)
            continue
        break
    print('connect ok')

    # 周期业务
    fail_num = 0
    run_time = 0
    last_get_time = 0
    while True:
        if fail_num >= 10:
            print('fail too many.reset!')
            machine.reset()

        if is_rx_msg:
            is_rx_msg = False
            # 亮灯,蜂鸣器鸣叫
            red_led.value(0)
            beep.value(1)
            time.sleep(0.5)
            beep.value(0)
            time.sleep(0.5)
            beep.value(1)
            time.sleep(0.5)
            beep.value(0)
            # 显示文字
            lcd.clear()
            lcd.text(date_text, 0, 0, 8)
            lcd.text_cn(rx_text, 0, 32, 16)
            lcd.show()
        beep.value(0)

        t = utime.time()
        if t - last_get_time > 60 and rx_text == '':
            last_get_time = t
            # 获取ntp网络时间
            resp, err = tziot.call(pipe, 0x2141000000000004, RID_GET_TIME, 5000, bytearray())
            if err != 0:
                fail_num += 1
                continue
            date_text = tziot.bytearray_to_str(resp)

            lcd.clear()
            lcd.text(date_text, 0, 0, 8)

            # 获取南京室外温度
            resp, err = tziot.call(pipe, 0x2141000000010001, RID_GET_TEMP, 5000, bytearray())
            if err != 0 or len(resp) != 2:
                fail_num += 1
                continue
            fail_num = 0
            outdoor_temp = (resp[0] << 8) + resp[1]
            if outdoor_temp >= 0x8000:
                outdoor_temp = 0x10000 - outdoor_temp
            outdoor_temp = outdoor_temp / 10
            lcd.text('%.1f' % outdoor_temp, 30, 20, 32)
            lcd.show()
            red_led.value(1)
            blue_led.value(1)

        # 检测按键是否按下
        detect_key()
        time.sleep(1)

        # 每半小时定时复位
        run_time += 1
        if run_time >= 3600:
            print('reset system!')
            machine.reset()


def detect_key():
    global key, rx_text, red_led, blue_led, last_push_time, date_text, outdoor_temp

    # 2s之内重复按键无效
    t = utime.time()
    if t - last_push_time <= 2:
        return
    last_push_time = t

    value = -1
    for i in range(6):
        if key[i].value() == 0:
            value = i
            break
    if value == -1:
        return
    print('key push:', value)
    # 5号按键是确认键
    if value == 5:
        rx_text = ''
        red_led.value(1)
        blue_led.value(1)
        beep.value(0)

        lcd.clear()
        lcd.text(date_text, 0, 0, 8)
        lcd.text('%.1f' % outdoor_temp, 30, 20, 32)
        lcd.show()
        return

    red_led.value(1)
    blue_led.value(0)
    beep.value(0)
    rx_text = ''
    lcd.clear()
    lcd.text_cn('发送中', 0, 25, 16)
    lcd.text('...', 48, 25, 16)
    lcd.show()

    resp, err = tziot.call(pipe, DST_IA, RID_KEY, 5000, bytearray([value]))
    blue_led.value(1)

    lcd.clear()
    if err != 0:
        lcd.text_cn('发送失败', 0, 25, 16)
    else:
        lcd.text_cn('发送成功', 0, 25, 16)
    lcd.show()


if __name__ == '__main__':
    main()

"""
Copyright 2021-2021 The jdh99 Authors. All rights reserved.
中文字库
Authors: jdh99 <jdh821@163.com>
"""

font16 = {
    0xe69cba:
        [0x10, 0x11, 0x11, 0x11, 0xFD, 0x11, 0x31, 0x39, 0x55, 0x55, 0x91, 0x11, 0x11, 0x12, 0x12, 0x14,
         0x00, 0xF0, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x12, 0x12, 0x12, 0x0E, 0x00],  # 机,0
    0xe587ba:
        [0x01, 0x01, 0x21, 0x21, 0x21, 0x21, 0x3F, 0x01, 0x01, 0x01, 0x41, 0x41, 0x41, 0x41, 0x7F, 0x00,
         0x00, 0x00, 0x08, 0x08, 0x08, 0x08, 0xF8, 0x08, 0x00, 0x00, 0x04, 0x04, 0x04, 0x04, 0xFC, 0x04],  # 出,0
    0xe69da5:
        [0x01, 0x01, 0x01, 0x7F, 0x01, 0x11, 0x09, 0x09, 0xFF, 0x03, 0x05, 0x09, 0x31, 0xC1, 0x01, 0x01,
         0x00, 0x00, 0x00, 0xFC, 0x00, 0x10, 0x10, 0x20, 0xFE, 0x80, 0x40, 0x20, 0x18, 0x06, 0x00, 0x00],  # 来,1
    0xe78ea9:
        [0x00, 0x00, 0xFD, 0x10, 0x10, 0x10, 0x13, 0x7C, 0x10, 0x10, 0x10, 0x10, 0x1D, 0xE1, 0x42, 0x04,
         0x00, 0x00, 0xFC, 0x00, 0x00, 0x00, 0xFE, 0x90, 0x90, 0x90, 0x90, 0x90, 0x12, 0x12, 0x0E, 0x00],  # 玩,2
    0xe588b0:
        [0x00, 0xFF, 0x08, 0x10, 0x22, 0x41, 0xFF, 0x08, 0x08, 0x08, 0x7F, 0x08, 0x08, 0x0F, 0xF8, 0x40,
         0x04, 0x84, 0x04, 0x24, 0x24, 0x24, 0xA4, 0xA4, 0x24, 0x24, 0x24, 0x24, 0x04, 0x84, 0x14, 0x08],  # 到,3
    0xe68891:
        [0x04, 0x0E, 0x78, 0x08, 0x08, 0xFF, 0x08, 0x08, 0x0A, 0x0C, 0x18, 0x68, 0x08, 0x08, 0x2B, 0x10,
         0x40, 0x50, 0x48, 0x48, 0x40, 0xFE, 0x40, 0x44, 0x44, 0x48, 0x30, 0x22, 0x52, 0x8A, 0x06, 0x02],  # 我,4
    0xe5aeb6:
        [0x02, 0x01, 0x7F, 0x40, 0x80, 0x7F, 0x02, 0x0D, 0x71, 0x02, 0x0C, 0x71, 0x06, 0x18, 0xE2, 0x01,
         0x00, 0x00, 0xFE, 0x02, 0x04, 0xFC, 0x00, 0x08, 0x90, 0xA0, 0xC0, 0xA0, 0x98, 0x86, 0x80, 0x00],  # 家,5
    0xe58699:
        [0x00, 0x7F, 0x40, 0x90, 0x10, 0x1F, 0x10, 0x20, 0x3F, 0x00, 0x00, 0xFF, 0x00, 0x00, 0x00, 0x00,
         0x00, 0xFE, 0x02, 0x04, 0x00, 0xF8, 0x00, 0x00, 0xF8, 0x08, 0x08, 0xC8, 0x08, 0x08, 0x50, 0x20],  # 写,6
    0xe4bd9c:
        [0x09, 0x09, 0x09, 0x11, 0x12, 0x32, 0x34, 0x50, 0x90, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10,
         0x00, 0x00, 0x00, 0xFE, 0x80, 0x80, 0x80, 0xF8, 0x80, 0x80, 0x80, 0xFC, 0x80, 0x80, 0x80, 0x80],  # 作,7
    0xe4b89a:
        [0x04, 0x04, 0x04, 0x04, 0x44, 0x24, 0x24, 0x14, 0x14, 0x14, 0x04, 0x04, 0x04, 0x04, 0xFF, 0x00,
         0x40, 0x40, 0x40, 0x40, 0x44, 0x44, 0x48, 0x48, 0x50, 0x60, 0x40, 0x40, 0x40, 0x40, 0xFE, 0x00],  # 业,8
    0xe5a5bd:
        [0x10, 0x10, 0x10, 0x10, 0xFC, 0x24, 0x24, 0x25, 0x24, 0x48, 0x28, 0x10, 0x28, 0x44, 0x84, 0x00,
         0x00, 0xFC, 0x04, 0x08, 0x10, 0x20, 0x20, 0xFE, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0xA0, 0x40],  # 好,9
    0xe79a84:
        [0x10, 0x10, 0x20, 0x7E, 0x42, 0x42, 0x43, 0x42, 0x7E, 0x42, 0x42, 0x42, 0x42, 0x7E, 0x42, 0x00,
         0x40, 0x40, 0x40, 0x7C, 0x84, 0x84, 0x04, 0x44, 0x24, 0x24, 0x04, 0x04, 0x04, 0x04, 0x28, 0x10],  # 的,10
    0xe4b88d:
        [0x00, 0x7F, 0x00, 0x00, 0x01, 0x01, 0x03, 0x05, 0x09, 0x11, 0x21, 0x41, 0x81, 0x01, 0x01, 0x01,
         0x00, 0xFC, 0x80, 0x80, 0x00, 0x00, 0x40, 0x20, 0x10, 0x08, 0x04, 0x04, 0x00, 0x00, 0x00, 0x00],  # 不,11
    0xe591bc:
        [0x00, 0x00, 0x7B, 0x48, 0x49, 0x48, 0x48, 0x48, 0x4B, 0x48, 0x78, 0x48, 0x00, 0x00, 0x00, 0x00,
         0x08, 0x3C, 0xE0, 0x20, 0x24, 0xA4, 0xA8, 0x20, 0xFE, 0x20, 0x20, 0x20, 0x20, 0x20, 0xA0, 0x40],  # 呼,12
    0xe58fab:
        [0x00, 0x00, 0x7C, 0x44, 0x44, 0x44, 0x44, 0x44, 0x44, 0x44, 0x7C, 0x44, 0x00, 0x00, 0x00, 0x00,
         0x04, 0x04, 0x84, 0x84, 0x84, 0x84, 0x84, 0x84, 0x8C, 0xB4, 0xC4, 0x84, 0x04, 0x04, 0x04, 0x04],  # 叫,13
    0xE7B3BB:
        [0x00, 0x3F, 0x04, 0x08, 0x10, 0x3F, 0x01, 0x06, 0x18, 0x7F, 0x01, 0x09, 0x11, 0x21, 0x45, 0x02,
         0xF8, 0x00, 0x00, 0x20, 0x40, 0x80, 0x00, 0x10, 0x08, 0xFC, 0x04, 0x20, 0x10, 0x08, 0x04, 0x00],  # 系,14
    0xE7BB9F:
        [0x10, 0x10, 0x20, 0x23, 0x48, 0xF8, 0x11, 0x23, 0x40, 0xF8, 0x40, 0x00, 0x19, 0xE1, 0x42, 0x04,
         0x40, 0x20, 0x20, 0xFE, 0x40, 0x88, 0x04, 0xFE, 0x92, 0x90, 0x90, 0x90, 0x12, 0x12, 0x0E, 0x00],  # 统,15
    0xE590AF:
        [0x01, 0x00, 0x1F, 0x10, 0x10, 0x10, 0x1F, 0x10, 0x10, 0x10, 0x17, 0x24, 0x24, 0x44, 0x87, 0x04,
         0x00, 0x80, 0xFC, 0x04, 0x04, 0x04, 0xFC, 0x00, 0x00, 0x00, 0xFC, 0x04, 0x04, 0x04, 0xFC, 0x04],  # 启,16
    0xE58AA8:
        [0x00, 0x00, 0x7C, 0x00, 0x01, 0x00, 0xFE, 0x20, 0x20, 0x20, 0x48, 0x44, 0xFD, 0x45, 0x02, 0x04,
         0x40, 0x40, 0x40, 0x40, 0xFC, 0x44, 0x44, 0x44, 0x44, 0x84, 0x84, 0x84, 0x04, 0x04, 0x28, 0x10],  # 动,17
    0xE4B8AD:
        [0x01, 0x01, 0x01, 0x01, 0x3F, 0x21, 0x21, 0x21, 0x21, 0x21, 0x3F, 0x21, 0x01, 0x01, 0x01, 0x01,
         0x00, 0x00, 0x00, 0x00, 0xF8, 0x08, 0x08, 0x08, 0x08, 0x08, 0xF8, 0x08, 0x00, 0x00, 0x00, 0x00],  # 中,18
    0xE8BF9E:
        [0x00, 0x20, 0x17, 0x10, 0x00, 0x01, 0xF3, 0x10, 0x10, 0x10, 0x17, 0x10, 0x10, 0x28, 0x47, 0x00,
         0x40, 0x40, 0xFE, 0x80, 0xA0, 0x20, 0xFC, 0x20, 0x20, 0x20, 0xFE, 0x20, 0x20, 0x20, 0xFE, 0x00],  # 连,19
    0xE68EA5:
        [0x10, 0x10, 0x13, 0x10, 0xFD, 0x10, 0x17, 0x10, 0x18, 0x37, 0xD0, 0x11, 0x10, 0x10, 0x51, 0x26,
         0x80, 0x40, 0xFC, 0x00, 0x08, 0x90, 0xFE, 0x40, 0x40, 0xFE, 0x88, 0x08, 0x90, 0x60, 0x98, 0x04],  # 接,20
    0xE5A4B1:
        [0x01, 0x11, 0x11, 0x11, 0x3F, 0x21, 0x41, 0x01, 0xFF, 0x02, 0x04, 0x04, 0x08, 0x10, 0x20, 0xC0,
         0x00, 0x00, 0x00, 0x00, 0xF8, 0x00, 0x00, 0x00, 0xFE, 0x80, 0x40, 0x40, 0x20, 0x10, 0x08, 0x06],  # 失,21
    0xE8B4A5:
        [0x00, 0x7C, 0x44, 0x54, 0x54, 0x55, 0x56, 0x54, 0x54, 0x54, 0x54, 0x10, 0x28, 0x24, 0x45, 0x82,
         0x40, 0x40, 0x40, 0x80, 0xFE, 0x08, 0x88, 0x88, 0x88, 0x50, 0x50, 0x20, 0x50, 0x88, 0x04, 0x02],  # 败,22
    0xE68890:
        [0x00, 0x00, 0x00, 0x3F, 0x20, 0x20, 0x20, 0x3E, 0x22, 0x22, 0x22, 0x22, 0x2A, 0x44, 0x40, 0x81,
         0x50, 0x48, 0x40, 0xFE, 0x40, 0x40, 0x44, 0x44, 0x44, 0x28, 0x28, 0x12, 0x32, 0x4A, 0x86, 0x02],  # 成,23
    0xE58A9F:
        [0x00, 0x00, 0x00, 0xFE, 0x11, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x1E, 0xF1, 0x41, 0x02, 0x04,
         0x40, 0x40, 0x40, 0x40, 0xFC, 0x44, 0x44, 0x44, 0x44, 0x84, 0x84, 0x84, 0x04, 0x04, 0x28, 0x10],  # 功,24
    0xE58F91:
        [0x01, 0x11, 0x11, 0x22, 0x3F, 0x02, 0x04, 0x07, 0x0A, 0x09, 0x11, 0x10, 0x20, 0x40, 0x03, 0x1C,
         0x00, 0x10, 0x08, 0x00, 0xFC, 0x00, 0x00, 0xF8, 0x08, 0x08, 0x10, 0xA0, 0x40, 0xA0, 0x18, 0x06],  # 发,25
    0xE98081:
        [0x02, 0x21, 0x11, 0x17, 0x00, 0x00, 0xF0, 0x17, 0x10, 0x10, 0x10, 0x11, 0x12, 0x28, 0x47, 0x00,
         0x08, 0x08, 0x10, 0xFC, 0x40, 0x40, 0x40, 0xFE, 0x40, 0xA0, 0x90, 0x08, 0x08, 0x00, 0xFE, 0x00],  # 送,26

}

font32 = {
    0xe69cba:
        [0x00, 0x00, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x3F, 0x01, 0x03, 0x03, 0x03, 0x03,
         0x07, 0x05, 0x0D, 0x09, 0x09, 0x11, 0x11, 0x21, 0x41, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x00,
         0x00, 0x00, 0x00, 0x80, 0x81, 0x81, 0x81, 0x81, 0x81, 0x91, 0xF9, 0x81, 0x81, 0x81, 0x81, 0xF1,
         0x99, 0x99, 0x89, 0x81, 0x81, 0x81, 0x83, 0x83, 0x82, 0x86, 0x84, 0x88, 0x90, 0xA0, 0x00, 0x00,
         0x00, 0x00, 0x00, 0x00, 0x01, 0xFF, 0x81, 0x81, 0x81, 0x81, 0x81, 0x81, 0x81, 0x81, 0x81, 0x81,
         0x81, 0x81, 0x81, 0x81, 0x81, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x00, 0x00, 0x00,
         0x00, 0x00, 0x00, 0x00, 0x00, 0xC0, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80,
         0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x88, 0x88, 0x88, 0x8C, 0xFE, 0xFC, 0x00, 0x00, 0x00],  # 机,0
}

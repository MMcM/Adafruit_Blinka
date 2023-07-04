# SPDX-FileCopyrightText: 2022 mmontol
#
# SPDX-License-Identifier: MIT
"""Pin definitions for the LubanCat zero."""

from adafruit_blinka.microcontroller.rockchip.rk3566 import pin

# lbancat zero board 40-pin  J8 or J7:
# --------------------------
# 3V3 | (1)  (2)  | 5V
# D3  | (3)  (4)  | 5V
# D5  | (5)  (6)  | GND
# D7  | (7)  (8)  | D8
# GND | (9)  (10) | D10
# .......................
# .......................
# D33 | (33) (34) | GND
# D35 | (35) (36) | D36
# D37 | (37) (38) | D38
# GND | (39) (40) | D40
# --------------------------

D3 = pin.GPIO1_A0
D5 = pin.GPIO1_A1
D7 = pin.GPIO1_A2
D8 = pin.GPIO2_C5
D10 = pin.GPIO2_C6
D11 = pin.GPIO1_A3
D12 = pin.GPIO0_C2
D13 = pin.GPIO1_A4
D15 = pin.GPIO1_A5
D16 = pin.GPIO2_C3
D18 = pin.GPIO2_C4
D19 = pin.GPIO4_C3
D21 = pin.GPIO4_C5
D22 = pin.GPIO1_B0
D23 = pin.GPIO4_C2
D24 = pin.GPIO4_C6
D26 = pin.GPIO1_B3
D27 = pin.GPIO3_B4
D28 = pin.GPIO3_B3
D29 = pin.GPIO1_A7
D31 = pin.GPIO1_B0
D32 = pin.GPIO3_B6
D33 = pin.GPIO3_B1
D35 = pin.GPIO3_B2
D36 = pin.GPIO3_A5
D37 = pin.GPIO1_B1
D38 = pin.GPIO3_A6
D40 = pin.GPIO3_A7

# I2C
SDA3 = pin.I2C3_SDA_M0
SCL3 = pin.I2C3_SCL_M0
SDA = SDA3
SCL = SCL3
SCL5 = pin.I2C5_SCL_M0
SDA5 = pin.I2C5_SDA_M0

# UART
TX = pin.UART8_TX_M0
RX = pin.UART8_RX_M0

# SPI
MOSI = pin.SPI3_MOSI_M0
MISO = pin.SPI3_MISO_M0
SCLK = pin.SPI3_CLK_M0
CS0 = pin.SPI3_CS0_M1
CS1 = pin.GPIO1_B3

# PWM

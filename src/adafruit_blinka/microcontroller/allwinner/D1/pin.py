# SPDX-FileCopyrightText: 2022 Aleksandr Saiapin for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""Allwinner D1 pin names"""
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

PB0 = Pin(32)
TWI2_SCL = PB0
PB1 = Pin(33)
TWI2_SDA = PB1
PB2 = Pin(34)
PB3 = Pin(35)
PB4 = Pin(36)
TWI1_SCL = PB4
PB5 = Pin(37)
TWI1_SDA = PB5
PB6 = Pin(38)
PB7 = Pin(39)
PB8 = Pin(40)
UART0_TX = PB8
PB9 = Pin(41)
UART0_RX = PB9
PB10 = Pin(42)
PB11 = Pin(43)
PB12 = Pin(44)
PC0 = Pin(64)
UART2_TX = PC0
PC1 = Pin(65)
UART2_RX = PC1
PC2 = Pin(66)
SPI0_SCLK = PC2
PC3 = Pin(67)
SPI0_CS = PC3
PC4 = Pin(68)
SPI0_MOSI = PC4
PC5 = Pin(69)
SPI0_MISO = PC5
PC6 = Pin(70)
SPI0_WP = PC6
PC7 = Pin(71)
SPI0_HOLD = PC7
PD0 = Pin(96)
PD1 = Pin(97)
PD2 = Pin(98)
PD3 = Pin(99)
PD4 = Pin(100)
PD5 = Pin(101)
PD6 = Pin(102)
PD7 = Pin(103)
PD8 = Pin(104)
PD9 = Pin(105)
PD10 = Pin(106)
PD11 = Pin(107)
SPI1_SCLK = PD11
PD12 = Pin(108)
SPI1_MOSI = PD12
PD13 = Pin(109)
SPI1_MISO = PD13
PD14 = Pin(110)
PD15 = Pin(111)
PD16 = Pin(112)
PD17 = Pin(113)
PD18 = Pin(114)
PD19 = Pin(115)
PD20 = Pin(116)
PD21 = Pin(117)
PD22 = Pin(118)
PE0 = Pin(128)
PE1 = Pin(129)
PE2 = Pin(130)
PE3 = Pin(131)
PE4 = Pin(132)
PE5 = Pin(133)
PE6 = Pin(134)
PE7 = Pin(135)
PE8 = Pin(136)
PE9 = Pin(137)
PE10 = Pin(138)
PE11 = Pin(139)
PE12 = Pin(140)
PE13 = Pin(141)
PE14 = Pin(142)
TWI1_SCL = PE14
PE15 = Pin(143)
TWI1_SDA = PE15
PE16 = Pin(144)
TWI3_SCL = PE16
PE17 = Pin(145)
TWI3_SDA = PE17
PG6 = Pin(198)
UART1_TX = PG6
PG7 = Pin(199)
UART1_RX = PG7
PG8 = Pin(200)
UART1_RTS = PG8
PG9 = Pin(201)
UART1_CTS = PG9
PG10 = Pin(202)
PG11 = Pin(203)
PG12 = Pin(204)
TWI0_SCL = PG12
PG13 = Pin(205)
TWI0_SDA = PG13
PG14 = Pin(206)
PG15 = Pin(207)
PG16 = Pin(208)
PG17 = Pin(209)
PG18 = Pin(210)

i2cPorts = (
    (0, TWI0_SCL, TWI0_SDA),
    (1, TWI1_SCL, TWI1_SDA),
    (2, TWI2_SCL, TWI2_SDA),
    (3, TWI3_SCL, TWI3_SDA),
)
uartPorts = (
    (0, UART0_TX, UART0_RX),
    (1, UART1_TX, UART1_RX),
    (2, UART2_TX, UART2_RX),
)
spiPorts = (
    (0, SPI0_SCLK, SPI0_MOSI, SPI0_MISO),
    (1, SPI1_SCLK, SPI1_MOSI, SPI1_MISO),
)

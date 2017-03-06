#!/bin/bash
#coding: utf8

numero = input("Pon tu número: ")

if numero%2 == 0:
	print "Su número es par"
if numero >= -10 and numero <= 40:
	print "Su número está entre 10 y 40"
if numero < 0:
	print "Su número es negativo"

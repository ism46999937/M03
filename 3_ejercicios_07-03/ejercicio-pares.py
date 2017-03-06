#!/bin/bash
#coding: utf8
numero = input("Pon tu número: ")
if numero < 0: 
	print "Su número es negativo"
if numero%2 == 0:
	print "Su número es par"
if numero%2 != 0:
	print "Su número es impar"


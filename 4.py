# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 23:46:54 2020

@author: user
"""

x=int(input("X軸座標:"))
y=int(input("Y軸座標:"))
ans=x**2+y**2

if x==0 and y==0:
    print("該點位於原點")
elif y==0:
    if x>0:
        print("該點位於右半平面X軸上，離原點距離為根號",ans)
    else:
        print("該點位於左半平面X軸上，離原點距離為根號",ans)
elif x==0:
    if y>0:
        print("該點位於上半平面Y軸上，離原點距離為根號",ans)
    else:
        print("該點位於下半平面Y軸上，離原點距離為根號",ans)
elif x>0:
    if y>0:
        print("該點位於第一象限，離原點距離為根號",ans)
    else:
        print("該點位於第四象限，離原點距離為根號",ans)
else:
    if y>0:
        print("該點位於第二象限，離原點距離為根號",ans)
    else:
        print("該點位於第三象限，離原點距離為根號",ans)
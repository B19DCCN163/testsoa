from lib2to3.pgen2 import driver
from selenium import  webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='C:\\Users\\tranh\\Downloads\\test\\chromedriver.exe',options=options)
time.sleep(3)

# test dang nhap
# 28 
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)

# 29
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"password").send_keys("admin01")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)

# 30 
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)

#31
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("ưeyyedh")
driver.find_element(By.ID,"password").send_keys("ddkkd")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)

#32
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)

#33
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin01")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)

# quan ly mat hang
# dang nhap 
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(1)").click()')
driver.execute_script('document.querySelector("body > div:nth-child(3) > a:nth-child(1)").click()')

#34

driver.find_element(By.ID,"ten").send_keys("Sua")
driver.find_element(By.ID,"gianhap").send_keys("25000")
driver.find_element(By.ID,"giaban").send_keys("30000")
driver.find_element(By.ID,"loai").send_keys("Gia dung")
time.sleep(1)
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1)
#35
driver.refresh()
time.sleep(1)
driver.find_element(By.ID,"ma").send_keys("A02")

driver.find_element(By.ID,"gianhap").send_keys("25000")
driver.find_element(By.ID,"giaban").send_keys("30000")
driver.find_element(By.ID,"loai").send_keys("Gia dung")
time.sleep(1)
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1)
#36
driver.refresh()
time.sleep(1)
driver.find_element(By.ID,"ma").send_keys("A02")
driver.find_element(By.ID,"ten").send_keys("Sua")

driver.find_element(By.ID,"giaban").send_keys("30000")
driver.find_element(By.ID,"loai").send_keys("Gia dung")
time.sleep(1)
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1)
#37
driver.refresh()
time.sleep(1)
driver.find_element(By.ID,"ma").send_keys("A02")
driver.find_element(By.ID,"ten").send_keys("Sua")
driver.find_element(By.ID,"gianhap").send_keys("25000")

driver.find_element(By.ID,"loai").send_keys("Gia dung")
time.sleep(1)
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1)
#38
driver.refresh()
time.sleep(1)
driver.find_element(By.ID,"ma").send_keys("A02")
driver.find_element(By.ID,"ten").send_keys("Sua")
driver.find_element(By.ID,"gianhap").send_keys("25000")
driver.find_element(By.ID,"giaban").send_keys("30000")

time.sleep(1)
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1)

# 39 
driver.refresh()
time.sleep(1)
driver.find_element(By.ID,"ma").send_keys("A01")
driver.find_element(By.ID,"ten").send_keys("Sua")
driver.find_element(By.ID,"gianhap").send_keys("25000")
driver.find_element(By.ID,"giaban").send_keys("30000")
driver.find_element(By.ID,"loai").send_keys("Gia dung")
time.sleep(1)
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1)

#Nhap sai kieu du lieu 
#40
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(1)").click()')
driver.execute_script('document.querySelector("body > div:nth-child(3) > a:nth-child(1)").click()')
driver.refresh()
time.sleep(1)
driver.find_element(By.ID,"ma").send_keys("A06")
driver.find_element(By.ID,"ten").send_keys("@@@@@@@")
driver.find_element(By.ID,"gianhap").send_keys("25000")
driver.find_element(By.ID,"giaban").send_keys("30000")
driver.find_element(By.ID,"loai").send_keys("Gia dung")
time.sleep(1)
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1)  
#42
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(1)").click()')
driver.execute_script('document.querySelector("body > div:nth-child(3) > a:nth-child(1)").click()')
driver.refresh()
time.sleep(1)
driver.find_element(By.ID,"ma").send_keys("A04")
driver.find_element(By.ID,"ten").send_keys("Sua tuoi")
driver.find_element(By.ID,"gianhap").send_keys("0")
driver.find_element(By.ID,"giaban").send_keys("30000")
driver.find_element(By.ID,"loai").send_keys("Gia dung")
time.sleep(1)
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1)    
#43
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(1)").click()')
driver.execute_script('document.querySelector("body > div:nth-child(3) > a:nth-child(1)").click()')
driver.refresh()
time.sleep(1)
driver.find_element(By.ID,"ma").send_keys("A07")
driver.find_element(By.ID,"ten").send_keys("Sua tuoi")
driver.find_element(By.ID,"gianhap").send_keys("-1000")
driver.find_element(By.ID,"giaban").send_keys("30000")
driver.find_element(By.ID,"loai").send_keys("Gia dung")
time.sleep(1)
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1) 
#45
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(1)").click()')
driver.execute_script('document.querySelector("body > div:nth-child(3) > a:nth-child(1)").click()')
driver.refresh()
time.sleep(1)
driver.find_element(By.ID,"ma").send_keys("A08")
driver.find_element(By.ID,"ten").send_keys("Sua tuoi")
driver.find_element(By.ID,"gianhap").send_keys("abc")
driver.find_element(By.ID,"giaban").send_keys("30000")
driver.find_element(By.ID,"loai").send_keys("Gia dung")
time.sleep(1)
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1)  
#46
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(1)").click()')
driver.execute_script('document.querySelector("body > div:nth-child(3) > a:nth-child(1)").click()')
driver.refresh()
time.sleep(1)
driver.find_element(By.ID,"ma").send_keys("A09")
driver.find_element(By.ID,"ten").send_keys("Sua tuoi")
driver.find_element(By.ID,"gianhap").send_keys("283834")
driver.find_element(By.ID,"giaban").send_keys("0")
driver.find_element(By.ID,"loai").send_keys("Gia dung")
time.sleep(1)
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1) 
#47
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(1)").click()')
driver.execute_script('document.querySelector("body > div:nth-child(3) > a:nth-child(1)").click()')
driver.refresh()
time.sleep(1)
driver.find_element(By.ID,"ma").send_keys("A010")
driver.find_element(By.ID,"ten").send_keys("Sua tuoi")
driver.find_element(By.ID,"gianhap").send_keys("1000000")
driver.find_element(By.ID,"giaban").send_keys("30000")
driver.find_element(By.ID,"loai").send_keys("Gia dung")
time.sleep(1)
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1) 
#48
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(1)").click()')
driver.execute_script('document.querySelector("body > div:nth-child(3) > a:nth-child(1)").click()')
driver.refresh()
time.sleep(1)
driver.find_element(By.ID,"ma").send_keys("A011")
driver.find_element(By.ID,"ten").send_keys("Sua tuoi")
driver.find_element(By.ID,"gianhap").send_keys("1000")
driver.find_element(By.ID,"giaban").send_keys("-30000")
driver.find_element(By.ID,"loai").send_keys("Gia dung")
time.sleep(1)
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1) 
#50
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(1)").click()')
driver.execute_script('document.querySelector("body > div:nth-child(3) > a:nth-child(1)").click()')
driver.refresh()
time.sleep(1)
driver.find_element(By.ID,"ma").send_keys("A12")
driver.find_element(By.ID,"ten").send_keys("Sua tuoi")
driver.find_element(By.ID,"gianhap").send_keys("1000")
driver.find_element(By.ID,"giaban").send_keys("acb")
driver.find_element(By.ID,"loai").send_keys("Gia dung")
time.sleep(1)
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1) 

# sua mat hang
#51
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(1)").click()')
driver.execute_script('document.querySelector("#table1 > tbody > tr:nth-child(2) > td:nth-child(6) > a:nth-child(1)").click()')
driver.find_element(By.ID,"ma").clear()
driver.find_element(By.ID,"ma").send_keys("A16")
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1)
#54
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(1)").click()')
driver.execute_script('document.querySelector("#table1 > tbody > tr:nth-child(2) > td:nth-child(6) > a:nth-child(1)").click()')
driver.find_element(By.ID,"gianhap").clear()
driver.find_element(By.ID,"ma").send_keys("-1000")
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1)
#56
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(1)").click()')
driver.execute_script('document.querySelector("#table1 > tbody > tr:nth-child(2) > td:nth-child(6) > a:nth-child(1)").click()')
driver.find_element(By.ID,"gianhap").clear()
driver.find_element(By.ID,"gianhap").send_keys("abc")
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1)
# 58
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(1)").click()')
driver.execute_script('document.querySelector("#table1 > tbody > tr:nth-child(2) > td:nth-child(6) > a:nth-child(1)").click()')
driver.find_element(By.ID,"giaban").clear()
driver.find_element(By.ID,"giaban").send_keys("-1000")
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1)
#59
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(1)").click()')
driver.execute_script('document.querySelector("#table1 > tbody > tr:nth-child(2) > td:nth-child(6) > a:nth-child(1)").click()')
driver.find_element(By.ID,"giaban").clear()
driver.find_element(By.ID,"giaban").send_keys("absdvbd")
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1)
#60
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(1)").click()')
driver.execute_script('document.querySelector("#table1 > tbody > tr:nth-child(2) > td:nth-child(6) > a:nth-child(1)").click()')
driver.find_element(By.ID,"ten").clear()
driver.find_element(By.ID,"ten").send_keys("@@@@@@")
driver.execute_script('document.querySelector("body > main > form > div:nth-child(7) > button").click()')
time.sleep(1)
# nhap hang
#67
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(2)").click()')
driver.execute_script('document.querySelector("#table1 > tbody > tr:nth-child(1) > td:nth-child(6) > a").click()')
driver.find_element(By.ID,"soluong").send_keys("12")
time.sleep(1)
driver.execute_script('document.querySelector("body > div.container > form > button").click()')
time.sleep(1)
#68
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(2)").click()')
driver.execute_script('document.querySelector("#table1 > tbody > tr:nth-child(1) > td:nth-child(6) > a").click()')
driver.find_element(By.ID,"soluong").send_keys("-12")
time.sleep(1)
driver.execute_script('document.querySelector("body > div.container > form > button").click()')
time.sleep(1)
#69
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(2)").click()')
driver.execute_script('document.querySelector("#table1 > tbody > tr:nth-child(1) > td:nth-child(6) > a").click()')
driver.find_element(By.ID,"soluong").send_keys("muoi hai ")
time.sleep(1)
driver.execute_script('document.querySelector("body > div.container > form > button").click()')
time.sleep(1)
#
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(2)").click()')
driver.execute_script('document.querySelector("#table1 > tbody > tr:nth-child(1) > td:nth-child(6) > a").click()')
driver.find_element(By.ID,"soluong").send_keys("10.5")
time.sleep(1)
driver.execute_script('document.querySelector("body > div.container > form > button").click()')
time.sleep(1)
#
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(2)").click()')
driver.execute_script('document.querySelector("#table1 > tbody > tr:nth-child(1) > td:nth-child(6) > a").click()')
driver.find_element(By.ID,"soluong").send_keys("0")
time.sleep(1)
driver.execute_script('document.querySelector("body > div.container > form > button").click()')
time.sleep(1)
# 
driver.get('http://localhost:8080/quanlimathang/')
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin")
time.sleep(0.5)
driver.execute_script('document.querySelector("body > form > button").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > nav > div > a:nth-child(2)").click()')

driver.find_element(By.ID,"soluong").send_keys("12")
time.sleep(1)
driver.execute_script('document.querySelector("body > div.container > form > button").click()')
time.sleep(1)
from selenium import webdriver
import getpass
import time

# codechef credentials for login
username = "nikhilksingh97"
password = getpass.getpass("Password:")

# problem code
problem = 'TEST'

# submission code
code = """
#include <iostream>
 
int main(void) {
char c, d=10;
while(std::cin.get(c) && (c!='2' || d!='4') && std::cout.put(d))
d=c;
} 
"""

# start a browser session
browser = webdriver.Firefox()

# open link in browser
browser.get('https://www.codechef.com')

# login
nameElem = browser.find_element_by_id('edit-name')
nameElem.send_keys(username)

passElem = browser.find_element_by_id('edit-pass')
passElem.send_keys(password)

browser.find_element_by_id('edit-submit').click()

# open submission page
browser.get("https://www.codechef.com/submit/" + problem)

# sleep function to let web components load in case of slow internet connnection
time.sleep(10)

# click on toggle button to open simple text mode
browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()

# submit the code
inputElem = browser.find_element_by_id('edit-program')
inputElem.send_keys(code)

browser.find_element_by_id("edit-submit").click()


'''
Created on Jan 11, 2015

@author: max@theprogrammingclub.com
'''
from selenium import webdriver, common
from os import path
import re
import codecs
import password_handler as p_h

tld = r"https://www.ubcengcore.com"
login = r"/secure/shibboleth.htm"
postings = r"/myAccount/postings.htm"

browser = webdriver.PhantomJS()
browser.delete_all_cookies()

while True:
    try:
        browser.get(tld + login)
        p_h.enter_username_and_password(browser)
        browser.get(tld + postings)
        browser.find_element_by_id("fs5").submit()
        break
    except common.exceptions.NoSuchElementException:
        pass
    
content = browser.page_source

regex = re.compile("postingViewForm[0-9]\d*")
matches = regex.findall(content)

basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "..", "jobs"))

for form_id in matches:
    regex = re.compile("\d+$") 
    numerical_id = regex.findall(form_id)[0]
    numerical_id = numerical_id.encode("ascii")
    
    filename = filepath + '/' + numerical_id + '.html'
    
    if path.isfile(filename) is not True:    
        form = browser.find_element_by_id(form_id)
        form.submit()
        content = browser.page_source
        browser.save_screenshot("last.png")
        
        print "creating " + filename
        f = codecs.open(filename, 'w', "utf-8")
        for line in content:
            f.write(line)
        f.close()
    
        browser.back()

browser.close()
quit()
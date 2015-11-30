import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

profile = webdriver.FirefoxProfile()
profile.add_extension(extension='firebug-2.0.12.xpi')
profile.add_extension(extension='netExport-0.9b7.xpi')

profile.set_preference("browser.cache.disk.enable", False)
domain = "extensions.firebug.";

# Set default Firebug preferences
profile.set_preference(domain + "currentVersion", "2.0.12")
profile.set_preference(domain + "allPagesActivation", "on")
profile.set_preference(domain + "defaultPanelName", "net")
profile.set_preference(domain + "net.enableSites", True)

# Set default NetExport preferences
profile.set_preference(domain + "netexport.alwaysEnableAutoExport", True)
profile.set_preference(domain + "netexport.showPreview", False)
profile.set_preference(domain + "netexport.defaultLogDir", "/Users/Anirudh/Desktop/570/project/output/")

browser = webdriver.Firefox(firefox_profile=profile)
time.sleep(5)
for i in range(10):
	browser.get("10.245.206.250/NDTV/")
	time.sleep(6)
time.sleep(5)
browser.close()


'''
try: 
    #elem = browser.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr/td[3]/a")
    elem = browser.find_element_by_link_text("SEARCH")
    elem.send_keys(Keys.RETURN)

except NoSuchElementException:
    assert 0, "can't find XPATH or Link Name"
'''

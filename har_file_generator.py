import argparse
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def setup_profile(url, logdir):
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
	profile.set_preference(domain + "netexport.defaultFileName", url.split("/")[-2] + "-%Y-%m-%d")
	profile.set_preference(domain + "netexport.showPreview", False)
	profile.set_preference(domain + "netexport.defaultLogDir", logdir)
	
	return profile

def start(url, logdir):
	for i in range(5):
		profile = setup_profile(url, logdir)
		browser = webdriver.Firefox(firefox_profile=profile)
		time.sleep(5)
		browser.get(url)
		time.sleep(5)
		browser.close()
	

def main():
	parser = argparse.ArgumentParser(description="Open webpages and trigger net export ")
	parser.add_argument('--url', help="url to be loaded")
	parser.add_argument('--logdir', help = ".har file log location")
	#parser.add_argument('--threads', type=int, default=10, help="number of threads to use")
	args = parser.parse_args()
	#read_graphs(args.input, args.output, args.k, args.threads)
	start(args.url, args.logdir)

if __name__ == "__main__":
	main()

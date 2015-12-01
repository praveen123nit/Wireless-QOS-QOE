import csv
import os
import argparse

sites = ['NDTV', '9GAG', 'Airbnb', 'BBC', 'eBay', 'ESPN', 'Google', 'Netflix', 'reddit', 'Snapdeal', 'StackOverflow', 'TOI', 'WIRED', 'YouTube']

def run(iters, outfile, host):
	pw_dir = os.path.dirname(os.path.realpath(__file__)) 
	print ("current working directory", pw_dir)
	
	for site in sites:
		os.system('python har_file_generator.py --url http://' + str(host) + '/' + site + '/ --logdir ' + pw_dir + '/output_' + site + '/ ' + '--outfile ' +outfile + ' --iters ' + str(iters))
	
def main():
	parser = argparse.ArgumentParser(description="Open webpages and trigger net export ")
	parser.add_argument('--outfile', help = "output file to write the page load time")
	parser.add_argument('--iters', help = "number of reloads of the page to find avg. page load time")
	parser.add_argument('--host', help = "Wifi hosts IP address")
	args = parser.parse_args()
	try:
		os.remove(args.outfile)
	except:
		a = 1
	with open(args.outfile, 'a+') as csvfile:
		fieldnames = ['Site', 'Iterations', 'Avg Content Load Time', 'Avg On Load Time']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
	run(int(args.iters), args.outfile, args.host)

if __name__ == "__main__":
	main()

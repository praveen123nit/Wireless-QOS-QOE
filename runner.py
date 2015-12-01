#python har_file_generator.py --url http://localhost/NDTV/ --logdir /usr/vishnu/wireless/output
import os
import argparse

sites = ['NDTV', '9GAG', 'Airbnb', 'BBC', 'eBay', 'ESPN', 'Google', 'NDTV', 'Netflix', 'reddit', 'Snapdeal', 'StackOverflow', 'TOI', 'WIRED', 'YouTube']
#sites = ['NDTV', '9GAG', 'Airbnb']

def run(iters, outfile):
	pw_dir = os.path.dirname(os.path.realpath(__file__)) 
	print ("current working directory", pw_dir)
	
	for site in sites:
		os.system('python har_file_generator.py --url http://localhost/' + site + '/ --logdir ' + pw_dir + '/output_' + site + '/ ' + '--outfile ' +outfile + ' --iters ' + str(iters))
	
def main():
	parser = argparse.ArgumentParser(description="Open webpages and trigger net export ")
	parser.add_argument('--outfile', help = "output file to write the page load time")
	parser.add_argument('--iters', help = "number of reloads of the page to find avg. page load time")
	args = parser.parse_args()
	#print args.outfile
	os.remove("data.csv")
	with open('data.csv', 'a+') as csvfile:
		fieldnames = ['Site', 'Iterations', 'Avg Content Load Time', 'Avg On Load Time']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
	run(int(args.iters), args.outfile)

if __name__ == "__main__":
	main()

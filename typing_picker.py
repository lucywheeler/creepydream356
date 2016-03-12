# import the magic random picker
import random, urllib2

# list of things to pick from
url_for_list = "https://raw.githubusercontent.com/lucywheeler/creepydream356/master/typing_options.lst"
raw_typing_options = urllib2.urlopen(url_for_list)
list_of_options = raw_typing_options.read()
real_list = list_of_options.split()

# find a way to pick something
typing_choice = random.choice(real_list)

# a way to tell the user what to do
usage = """Usage:
This is the activity picker program.
It will give you a random typing option.
The source of the options is
%s
""" % (url_for_list)

print usage
print typing_choice

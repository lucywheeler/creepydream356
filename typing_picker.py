# import the magic random picker
import random, urllib2

# list of things to pick from
url_for_list = "https://raw.githubusercontent.com/lucywheeler/creepydream356/master/typing_options.lst"
raw_typing_options = urllib2.urlopen(url_for_list)
list_of_options = raw_typing_options.read()

print "DEBUG - typing options is \n%s" % list_of_options
typing_options = ["Ben", "Lucy", "Jude", "Max", "Mom", "Dad"]

# find a way to pick something
typing_choice = random.choice(typing_options)

# a way to tell the user what to do
print typing_choice

#codewars kata => https://www.codewars.com/kata/514a024011ea4fb54200004b/python

def domain_name(url):
  pass

#tests

#should print "google"
print(domain_name("http://google.com"))
#should print "google"
print(domain_name("http://google.co.jp"))
#should print "123"
print(domain_name("https://123.net"))
#should print "hyphen-site"
print(domain_name("https://hyphen-site.org"))
#should print "codewars"
print(domain_name("http://codewars.com"))
#should print "xakep"
print(domain_name("www.xakep.ru"))
#should print "youtube"
print(domain_name("https://youtube.com"))
#should print "codewars"
print(domain_name("http://www.codewars.com/kata/"))
#should print "icann"
print(domain_name("icann.org"))
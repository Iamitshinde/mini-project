import urllib.request as usrllib

def main(url):
    print("Checking COnnectivity")

    response=usrllib.urlopen(url)
    print("Connected to ",url,"successfully")
    print("The respose code was:",response.getcode())

print("This is site connectivity checker program")
input_url=input("Input the url of the site you want to check:")
main(input_url)
from flask import Flask, render_template, request
import numpy as np
import cv2 as cv
import urllib.request

app = Flask(__name__)

def classify(img_path):
    img2 = cv.imread(img_path,cv.IMREAD_GRAYSCALE)
    logo_images = []
    url = []
    # EBAY - 0
    req = urllib.request.urlopen('https://media-exp1.licdn.com/dms/image/C560BAQFfGj-Xuawo6A/company-logo_200_200/0/1634568184091?e=1648080000&v=beta&t=0l3qi1_3i9Obj8eorfo14Ti0wHlzFWqvi97HyR6mT8I')
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    logo_images.append(cv.imdecode(arr, -1))
    logo_images[0] = cv.cvtColor(logo_images[0], cv.COLOR_BGR2GRAY)
    url.append("ebay.com")

    # THE GUARDIAN - 1
    req = urllib.request.urlopen('https://bankimooncentre.org/wp-content/uploads/2020/06/guardian-logo-square.jpg')
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    logo_images.append(cv.imdecode(arr, -1))
    logo_images[1] = cv.cvtColor(logo_images[1], cv.COLOR_BGR2GRAY)
    url.append("theguardian.com")

    # CNN - 2
    req = urllib.request.urlopen('https://simg.nicepng.com/png/small/908-9086310_awesome-cnn-logo-png-free-transparent-png-logos.png')
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    logo_images.append(cv.imdecode(arr, -1))
    logo_images[2] = cv.cvtColor(logo_images[2], cv.COLOR_BGR2GRAY)
    url.append("cnn.com")

    # SPIEGEL - 3
    req = urllib.request.urlopen('https://www.spiegel.de/public/spon/images/logos/fb_logo_default.jpg')
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    logo_images.append(cv.imdecode(arr, -1))
    logo_images[3] = cv.cvtColor(logo_images[3], cv.COLOR_BGR2GRAY)
    url.append("spiegel.de")

    # BBC - 4
    req = urllib.request.urlopen('https://ichef.bbci.co.uk/images/ic/1920x1080/p09xtmrp.jpg')
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    logo_images.append(cv.imdecode(arr, -1))
    logo_images[4] = cv.cvtColor(logo_images[4], cv.COLOR_BGR2GRAY)
    url.append("bbc.com")

    # AMAZON - 5
    req = urllib.request.urlopen('https://pbs.twimg.com/profile_images/1400483947319115776/bTfxhuOK_400x400.jpg')
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    logo_images.append(cv.imdecode(arr, -1))
    logo_images[5] = cv.cvtColor(logo_images[5], cv.COLOR_BGR2GRAY)
    url.append("amazon.com")

    # NJUSKALO - 6
    req = urllib.request.urlopen('https://www.oldtimeri.hr/media/k2/items/cache/46276ded2fdd3245a9a8536c50ae55dd_XL.jpg')
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    logo_images.append(cv.imdecode(arr, -1))
    logo_images[6] = cv.cvtColor(logo_images[6], cv.COLOR_BGR2GRAY)
    url.append("njuskalo.hr")

    # GOOGLE - 7
    req = urllib.request.urlopen('https://www.pngitem.com/pimgs/m/356-3564611_imagens-do-nome-google-hd-png-download.png')
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    logo_images.append(cv.imdecode(arr, -1))
    logo_images[7] = cv.cvtColor(logo_images[7], cv.COLOR_BGR2GRAY)
    url.append("google.com")

    # GITHUB - 8
    req = urllib.request.urlopen('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTFSIO_dsJJiOX3Sntwxpw6lUIJKI0ueBlRpcQ3q57xVOw4-bCAQ2eX0v_5v2sf5CIiNA&usqp=CAU')
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    logo_images.append(cv.imdecode(arr, -1))
    logo_images[8] = cv.cvtColor(logo_images[8], cv.COLOR_BGR2GRAY)
    url.append("github.com")

    # YOUTUBE - 9
    req = urllib.request.urlopen('https://i2.wp.com/www.dafontfree.io/wp-content/uploads/2021/08/Youtube-Logo-Font.jpg?resize=849%2C395&ssl=1')
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    logo_images.append(cv.imdecode(arr, -1))
    logo_images[9] = cv.cvtColor(logo_images[9], cv.COLOR_BGR2GRAY)
    url.append("youtube.com")

    ind = 0
    max = 0
    max_index = 0

    for i in range(0,10):
        
        sift = cv.SIFT_create()
       
        kp1, des1 = sift.detectAndCompute(logo_images[i],None)
        kp2, des2 = sift.detectAndCompute(img2,None)
       
        bf = cv.BFMatcher()
        matches = bf.knnMatch(des1,des2,k=2)
        good = []

        for m,n in matches:
            if m.distance < 0.5*n.distance:
                good.append([m])

        if i == 0:
            max = len(good)

        if len(good) > max:
            max = len(good)
            max_index = i
        
    
    if max >= 5:
        return url[max_index]

    return "Website is not recognized!"


@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = classify(img_path)

	return render_template("index.html", prediction = p, img_path = img_path)

if __name__ =='__main__':
	#app.debug = True
	app.run(port=3000, debug = False)

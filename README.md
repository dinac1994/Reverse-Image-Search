# Reverse Image Search - Web Screenshot Classification

This repository includes a demo flask app in which you can upload a screenshot (or an image from a phone) of a website and it returns a fully qualified domain name (FQDN, e.g. "cnn.com") of the following websites:

https://www.theguardian.com/international

https://www.spiegel.de/

https://cnn.com

https://www.bbc.com/

https://www.amazon.com/

https://www.ebay.com/

https://www.google.com/

https://www.youtube.com/

## How does this app work?

1. User is asked to upload an image.
2. Click "Submit".
3. After around 10 seconds, app shows the image you've uploaded and the FQDN prediction for the given image.

## Backend Explanation

Classifying a website is done by detecting it's logo on the image. For the training dataset, we include logo pictures for each of the previously given websites. One logo per website which makes it a pretty small training dataset. We are allowed to do this since the logos of each website are consistent and do not change (except Google logo that can appear in infinitely many variants, so this app might not perform the best when Google does not have their usual logo).

The main part in detecting a logo on the image of a website is keypoint detection. Keypoint detectors use corners and edges to find low level features in images.

### Example of keypoints on the logo of Der Spiegel Website

<img width="474" alt="Slika_0" src="https://user-images.githubusercontent.com/92053362/146651995-99e88e20-6ebc-44a1-8d83-2ff826a83774.png">

After indentifying the keypoints, the next step is to get the matcher that matches the keypoints between the logo image and the website screenshot. We do this with k-nearest neighbours comparison, which we ask to provide the top two matches for each keypoint descriptor. We then use Ratio Test to ensure that matches are high quality matches and not false positives.

## Examples

## Der Spiegel logo

Let's look at some examples to get a better idea. Left image is a logo of a certain website. Right image is a screenshot of a website.

![Slika_1](https://user-images.githubusercontent.com/92053362/146652143-4fd85cc7-9961-43d4-99bc-4fb65c76e314.png)



After drawing matching pairs, we get the following image:

![Slika_2](https://user-images.githubusercontent.com/92053362/146652184-1175483b-e7aa-44cc-8ce3-4393db4e8a6a.png)

Conclusion: Since there are many matching pairs, we classify the right website as "Der Spiegel" website.

How about if we made a photo of computer screen using our phone? Let's see how our program works on "weirder" pictures.

![Slika_3](https://user-images.githubusercontent.com/92053362/146652250-91f285cf-d473-4179-bbca-b92f8809e2b4.png)

Again, there are a lot of matching pairs even though the input image of a website is cluttered.

## eBay logo

![Slika_4](https://user-images.githubusercontent.com/92053362/146652272-04c65c72-fec5-4e20-bc6f-994fccb56b30.png)
 
eBay website is properly classified because there are many matching pairs between the ebay logo and the eBay website image.



![Slika_5](https://user-images.githubusercontent.com/92053362/146652299-2b3b0600-e874-4f09-b7cf-00a6bf2205e7.png)

Ebay logo has only 2 matching pairs with the BBC website, which is not enough to classify the BBC website as the eBay website.

## Njuskalo logo

![Slika_6](https://user-images.githubusercontent.com/92053362/146652369-b7b01ccf-46a4-4689-a773-e9c869b9e75f.png)

Njuskalo website is properly classified because there are many matching pairs between the njuskalo logo and the njuskalo website image.



![Slika_7](https://user-images.githubusercontent.com/92053362/146652376-13243c39-47d4-4f5b-9c10-b285b6bbcc31.png)

There are no matching pairs between njuskalo logo and amazon. website

## Amazon logo

![Slika_8](https://user-images.githubusercontent.com/92053362/146652419-870fbcf3-0f30-4730-94c6-a63425d35176.png)

Again, many matching pairs. How about a cluttered picture taken with phone?

![Slika_9](https://user-images.githubusercontent.com/92053362/146652449-261c70b2-c8ef-4f09-85c4-55dd2bacf48d.png)

It works!

## UI of a simple web app

<img width="1427" alt="Slika_10" src="https://user-images.githubusercontent.com/92053362/146652692-66cf1fe0-5bbc-474a-9b3f-b077852feed5.png">








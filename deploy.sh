# 1. Download and install IBM Cloud CLI Tools and the Kubernetes Service Plug-in
curl -sL https://ibm.biz/idt-installer | bash

# 2. Login to IBM Cloud using API Key
ibmcloud login -a https://api.ng.bluemix.net --apikey $CLOUD_API_KEY

# 3. Build the image
echo "Building Docker Image"
docker build -t $IMAGE_NAME .

# 4. Tag the image as latest and with a custom tag
echo "Tagging the image as $IMAGE_NAME:$TRAVIS_BUILD_NUMBER-$TRAVIS_BRANCH" \ and $IMAGE_NAME:latest
docker tag $IMAGE_NAME us.icr.io/$CR_NAMESPACE/$IMAGE_NAME:$TRAVIS_BUILD_NUMBER-$TRAVIS_BRANCH
docker tag $IMAGE_NAME:latest us.icr.io/$CR_NAMESPACE/$IMAGE_NAME:latest

# 5. Login into Cloud CR
ibmcloud cr login
echo "Pushing image to registry"
docker push us.icr.io/$CR_NAMESPACE/$IMAGE_NAME:$TRAVIS_BUILD_NUMBER-$TRAVIS_BRANCH
echo "Image push complete!"
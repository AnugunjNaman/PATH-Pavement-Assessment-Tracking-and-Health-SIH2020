# SIH2020 PATH: Pavement Assessment Tracking and Health (Official Repository)
## Team: Segmentation Fault
## Problem: MK199

#### Link for the inference model 1: [Inception v3 FasterRCNN](https://drive.google.com/file/d/1wDPMs-oruB8TvRZZWYMDSpdBt_ROcPZ1/view?usp=sharing)
#### Link for the inference model 2: [MaskRCNN](https://drive.google.com/file/d/1IN5uENGEF4VmZiG6HfqPU3SWW4dONAcb/view?usp=sharing)

### Step's to Compile the App:
1. Install npm
2. Clone this repository.
3. Inside Meri-Sadak run `npm install expo`
4. Then run npm install .
5. To start the development server, `npm run start` or `expo start -c` (to clear Js cache)
6. Open a new terminal, `cd ./server` and then `npm install .` and then `nodemon app` to start the node server.
7. Open a new terminal and `npm install -g ngrok` then `ngrok http 3000`
8. Copy the http url from ngrok output to the app wherever needed.(in Home.js, Profile.js, RoadDetails.js)
9. Rest of the errors may be due to version, therefore try to debug using web.
10. For flask server, details go to PCI Detector, Flask folder

### Team Members: 
    1. Anugunj Naman
    2. Ashish Goswami (Leader)
    3. Chetan Sinha 
    4. Harshit Dixit
    5. Rutuja Patole
    6. Siddharth Rajawat

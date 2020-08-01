THis repository is a simple docker exercise with following features
   Build arguments
   Environmental Variable
   Docker volume mapping
   Port mapping
   Volume share between dockers

The Exercise is categorised into 3 folders
   registration_container --- Code details for the user registration
   administration_container --- Code details for admin processing app
   dock_volume --- Local folder shared as volume to both the dockers

Following commands were executed

User registration containers

   cd registration_container
   sudo docker build -t userreg:py3 --build-arg requirements=py3_req.txt -f Dockerfile .
   sudo docker run -d -v /home/praveen/workspace/microsvc/dckr_volume_flask/dock_volume:/reg_data -v /home/praveen/workspace/microsvc/dckr_volume_flask/registration_container/user_reg_app:/user_registration --name userregistration  -e FLASKHOSTNAME='0.0.0.0' -e FLASKPORT=4500 -e CODER='By Praveen!' -e REG_FILE=/reg_data/userRegistration.json -p 4500:4500 userreg:py3

Administration containers

   cd administration_container
   sudo docker build -t adminprocessing:py3 --build-arg requirements=admin_req.txt -f Dockerfile .
   sudo docker run -d -v /home/praveen/workspace/microsvc/dckr_volume_flask/dock_volume/:/reg_data -v /home/praveen/workspace/microsvc/dckr_volume_flask/administration_container/adminprocessing_app/:/admin_processing --name adminpy3 -e FLASKHOSTNAME='0.0.0.0' -e FLASKPORT=4500 -e REG_FILE=/reg_data/userRegistration.json -p 4501:4500 adminprocessing:py3

Used curl to test the containers

To register a user
   curl -d "username=arunkc&pwd=test321&fname=arunkumar&lname=chandramouli" -XPOST http://localhost:4500/signup
   curl -d "username=pravsp&pwd=test123&fname=praveen&lname=sp" -XPOST http://localhost:4500/signup

To administer a user
   curl -XGET http://localhost:4501/users
   curl -XGET http://localhost:4501/user/arunkc
   curl -XGET http://localhost:4501/user/pravsp

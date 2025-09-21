# Setup script
# ! WORK IN PROGRESS ! do not run yet!

RED="\033[0;31m"
BLUE="\033[1;34m"
NC="\033[0m"

echo -e "${BLUE}Installing Docker...${NC}"
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose

#echo -e "${BLUE}Setting up MySQL database...${NC}"
#mysql -u root -p -e "CREATE DATABASE sensordata"
#mysql -u root -p sensordata < sensordata.sql
# TODO: Prompt user for new MySQL password
PASS="testpass"

#export DB_HOST=

echo -e "${BLUE}Setting up environment...${NC}"
cp env_sample .env
sed -i 's/MQTT_PUB_USER=/MQTT_PUB_USER=publisher/g' .env
sed -i 's/MQTT_PUB_PASS=/MQTT_PUB_PASS=replace-with-env-pw/g' .env
sed -i 's/MQTT_SUB_USER=/MQTT_SUB_USER=subscriber/g' .env
sed -i 's/MQTT_SUB_PASS=/MQTT_SUB_PASS=replace-with-env-pw/g' .env

#sed -i 's/DB_HOST=/DB_HOST=localhost/g' .envtest
#sed -i 's/DB_NAME=/DB_NAME=sensordata/g' .envtest
#sed -i 's/DB_USER=/DB_USER=dht11/g' .envtest
#sed -i "s/DB_PASS=/DB_PASS="${PASS}"/g" .env

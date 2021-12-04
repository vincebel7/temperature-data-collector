# Setup script
# ! WORK IN PROGRESS ! do not run yet!

RED="\033[0;31m"
BLUE="\033[1;34m"
NC="\033[0m"

echo -e "${BLUE}Setting up MySQL database...${NC}"
#mysql -u root -p -e "CREATE DATABASE sensordata"
#mysql -u root -p sensordata < sensordata.sql


echo -e "${BLUE}Setting up environment...${NC}"
cp env_sample .env # Remember to replace .envtest with .env when ready
#sed -i 's/DB_HOST=/DB_HOST=localhost/g' .envtest
#sed -i 's/DB_NAME=/DB_NAME=sensordata/g' .envtest
#sed -i 's/DB_USER=/DB_USER=dht11/g' .envtest

# TODO: Prompt user for new MySQL password
PASS="testpass"

#sed -i "s/DB_PASS=/DB_PASS="${PASS}"/g" .env
export DB_HOST=

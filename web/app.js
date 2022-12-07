require("dotenv").config()

// Redis
const redis = require('redis');
const redis_client = redis.createClient({
	    host: 'localhost',
	    port: 6379
});

redis_client.on('error', err => {
	console.log('Error ' + err);
});

redis_client.on('ready', () => {
    let response = client.ping()
    console.log("Redis ping result: ", response);
});

// MySQL (TODO)

// Web server
var http = require('http');
var express = require('express');
var app = express();

var server = http.createServer(app);
var io = require('socket.io')(server);


console.log("Listening on 8080");

app.get('/', function (req, res) {
	console.log("New client");
	res.sendFile(__dirname + "/index.html");
});

// Serve CSS, etc
app.use(express.static('public')); 

// On connection
io.on('connection', function (socket) {
        stdout.write("Fetching data...(stdout write)");
	console.log("Fetching data...(console log)")
	async function main() {
	//socket.on('poll-db', function (message) {
        	stdout.write("Fetching data...(stdout write)");
		console.log("Fetching data...(console log)")
		// Redis part
		const result = await redis.rpop("DHT-data")
		stdout.write(result)
		console.log(result)
		//redis_client.rpop(
		//con.query("SELECT * FROM dht11_data ORDER BY date DESC LIMIT 1", (err, result, field)=>{
		//	if (err) throw err;
		//	socket.emit('data-from-server'), {
		//		data: result
		//	});
		//	console.log("Emitted data");
		//});
	}
});

server.listen(8080);

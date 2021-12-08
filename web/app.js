require("dotenv").config()

// MySQL

// Web server
var http = require('http');
var express = require('express');
var app = express();

var server = http.createServer(app);
var io = require('socket.io')(server);


server.listen(8080);
console.log("Listening on 8080");

app.get('/', function (req, res) {
	console.log("New client");
	res.sendFile(__dirname + "/index.html");
});

// Serve CSS, etc
app.use(express.static('public')); 

// On connection

io.on('connection', function (socket) {
	socket.on('poll-db', function (message) {
        	console.log("Fetching data...");
		//con.query("SELECT * FROM dht11_data ORDER BY date DESC LIMIT 1", (err, result, field)=>{
		//	if (err) throw err;
			socket.emit('data-from-server', {
		//		data: result
			});
			console.log("Emitted data");
		//});
	});
});


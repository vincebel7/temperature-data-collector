require("dotenv").config()

// MySQL
var mysql = require('mysql')
const DB_HOST = process.env.DB_HOST;
const DB_USER = process.env.DB_USER;
const DB_PASS = process.env.DB_PASS;
const DB_NAME = process.env.DB_NAME;

var con = mysql.createConnection({
	host: DB_HOST,
	user: DB_USER,
	password: DB_PASS,
	database: DB_NAME
});

con.connect(function(err) {
	if (err) throw err;
	console.log("Connected to MySQL");
});

// Web server
var http = require('http');
var express = require('express');
var app = express();

var server = http.createServer(app);
var io = require('socket.io')(server);


server.listen(8080);

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
		con.query("SELECT * FROM dht11_data ORDER BY date DESC LIMIT 1", (err, result, field)=>{
			if (err) throw err;
			console.log(result);

			socket.emit('data-from-server', {
				data: result
			});
		});
	});
});

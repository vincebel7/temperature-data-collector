require("dotenv").config() 
const http = require('http')
const port = 8080

var express = require('express');
var app = express();
var io = require('socket.io')(http);

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

function get_data(){
	console.log("Fetching data...");

	con.query("SELECT * FROM dht11_data ORDER BY date DESC LIMIT 1", (err, result, field)=>{
		if (err) throw err;
		console.log(result);
	});
}

con.connect(function(err) {
	if (err) throw err;
	console.log("Connected to MySQL");
});


app.get('/', function (req, res) {
	res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket) {
	console.log("connected");
});

var server = app.listen(8080, function () {
	var host = server.address().address
	var port = server.address().port

	console.log("Server is listening on port " + port)

    	//setInterval(get_data,1000)
})

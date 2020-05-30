function getData(callback){
    const spawn = require("child_process").spawn;

    const pythonProcess = spawn('python3', ["../../backend/sensors.py"]);
    var temperature = 'Debugging';

    pythonProcess.stdout.on('data', (data) => {
        mystr = data.toString();
        myjson = JSON.parse(mystr);
        // console.log(myjson);
        // console.log(myjson.temp);
        // console.log(myjson.air_hum); 
        // console.log(myjson.soil_hum); 
        // console.log(myjson.lum);
        temperature = myjson.temp;    
    });
    pythonProcess.on('close', function(code) {
        return callback(temperature);
    });
}
// getData(function(temperature) { document.getElementById("temp").innerHTML += temperature});
getData(function(temperature) { /* alert(temperature)*/ console.log(temperature)});










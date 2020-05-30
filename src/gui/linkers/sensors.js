function getData(){
    const {PythonShell} = require("python-shell");
    const path = require("path");

    let options = {
        scriptPath: path.join(__dirname, '../../backend')
    }

    var data = new PythonShell('sensors.py', options);

    data.on('message', function(message) {

        myjson = JSON.parse(message);
        
        const sensors = document.querySelector('#sensors');

        sensorsTemplate = ` <div id = "temp">
                            Temperatura: ${myjson.temp}
                            </div>
                            <hr/>
                            Humedad del aire: ${myjson.air_hum}
                            <hr/>
                            Humedad de la tierra: ${myjson.soil_hum}
                            <hr/>
                            Luminosidad: ${myjson.lum}
                        `
        sensors.innerHTML += sensorsTemplate;

    })
   
}

getData();










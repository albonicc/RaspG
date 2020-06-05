process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';

function getData(){
    const {PythonShell} = require("python-shell");
    const path = require("path");
    const wia = require('wia')('d_sk_UhWMznloNclQRH3E3M3Nrqqm');

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
        sensors.innerHTML = sensorsTemplate;
        
        wia.events.publish({
        name: 'Temperatura',
        data: myjson.temp
        });
        wia.events.publish({
        name: 'Humedad aire',
        data: myjson.air_hum
        });
        wia.events.publish({
        name: 'Humedad tierra',
        data: myjson.soil_hum
        });
        wia.events.publish({
        name: 'Luminosidad',
        data: myjson.lum
        }); 

    })
   
}

getData();










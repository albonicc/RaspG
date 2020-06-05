const { app, BrowserWindow, Menu } = require('electron');
const url = require('url');
const path = require('path');
const wia = require('wia')('d_sk_1v2Z1lGl28e2fGPlTuRwhnEc');

if(process.env.NODE_ENV !== 'production'){
    require('electron-reload')(__dirname, {
        electron: path.join(__dirname, '../node_modules', '.bin', 'electron')
    });
}

let mainWindow
let newProductWindow

app.on('ready', () => {
   mainWindow = new BrowserWindow({
    webPreferences: {
        nodeIntegration: true
    }
   });
   mainWindow.loadURL(url.format({
       pathname: path.join(__dirname, 'views/index.html'),
       protocol: 'file',
       slashes: true
   }))

   const mainMenu = Menu.buildFromTemplate(templateMenu);
   Menu.setApplicationMenu(mainMenu);

   mainWindow.on('closed', () => {
       app.quit();
   })
});

function createNewProductWindow(){
        newProductWindow =  new BrowserWindow({
        width: 400,
        height: 300,
        title: "RaspG"
    });
        //newProductWindow.setMenu(null);
        newProductWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'views/new_product.html'),
        protocol: 'file',
        slashes: true
    })) 
}

const templateMenu = [
    {
        label: 'File',
        submenu:[
            {
                label: 'New product',
                accelerator:'Ctrl + n',
                accelerator:'Cmd + n',
                click() {
                    createNewProductWindow()
                }
            },
            {
                label: 'Copy',
                role: 'copy'
            },
            {
                label: 'Close',
                accelerator:'Crl + w',
                accelerator:'Cmd + w',
                click() {
                    app.quit();
                }
            }
        ]
    },
    {
        label: 'Edit',
        submenu: [
            {
                label: 'New edit',
                accelerator: "Ctrl + x",
                accelerator: 'Cmd + x'
            }
        ]
    }
];

if(process.platform === 'darwin'){
    templateMenu.unshift({
        label: app.getName()
    })
}

if(process.env.NODE_ENV !== 'production') {
    templateMenu.push({
        label: 'DevTools',
        submenu: [
            {
                label: 'Show/Hide DevTools',
                accelerator: "Ctrl + d",
                click(item, focusedWindow) {
                    focusedWindow.toggleDevTools();
                }
            },
            {
                role: 'reload'
            }
        ]
    })
}

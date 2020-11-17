var Blob = require('blob');
const fetch = require('node-fetch');
var FileReader = require('filereader');
const crypto = require('crypto');

// async function getImage() {
//     var xhr = new XMLHttpRequest();
//     var imageURL = 'http://localhost:8124/img/bubbles.jpg';
//     var response = await fetch(imageURL);
//     console.log(">>>>>>>>>>>>>>>>>>>>>>>BEGIN>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
//     console.log(response)
//     console.log(">>>>>>>>>>>>>>>>>>>>>>>END>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");

//     var ablob = await response.blob();
//     console.log(ablob);
//     console.log(">>>>>>>>>>>>>>>>>>>>>>>END 2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");

//     var reader = new FileReader();
//     console.log(ablob);
//     await reader.readAsDataURL(ablob);
    

//     await new Promise((resolve, reject) => {
//         reader.onloadend = function () {
//             resolve(reader.result)
//             console.log(">>>>>>>>>>>>>>>>>>>>>>>END 3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
//             console.log("STRING LEN = " + reader.result.length);
//         }
//     })
//     // 2. calculate the hash of the blob

//     const myhash = crypto.createHash('sha256') // enables digest
//         .update(reader.result) // create the hash
//         .digest('hex'); // convert to string

//     console.log("myhash = " + myhash);


// }

// getImage();

async function getImage() {
    var imageURL = 'http://localhost:8083/img/bubbles.jpg';
    var response = await fetch(imageURL);
    console.log(">>>>>>>>>>>>>>>>>>>>>>>BEGIN>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
    console.log(response)
    console.log(">>>>>>>>>>>>>>>>>>>>>>>END>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");

    var blob = await response.blob();
    console.log(blob.length());
    console.log(">>>>>>>>>>>>>>>>>>>>>>>END 2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
    var reader = new FileReader();
    await reader.readAsDataURL(blob);
    reader.onloadend = function () {
        console.log(reader.result);
        console.log(">>>>>>>>>>>>>>>>>>>>>>>END 3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
        console.log("STRING LEN = " + reader.result.length);
    };
}
// var imageAsBase64 = fs.readFileSync('./img/bubbles.jpg', 'base64');
// console.log(imageAsBase64);
// console.log("LEN = " + imageAsBase64.length);

getImage();
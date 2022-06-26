const abiDecoder=require('abi-decoder');
const Web3=require('web3');
const Box = require('./build/contracts/Box.json');
abiDecoder.addABI(Box.abi);
const web3 = new Web3('http://18.133.191.37:8545');

const readProof =async (transactionHash) => {
    let transaction= await web3.eth.getTransaction(transactionHash);
    //console.log(transaction);
    let bn=transaction.blockNumber;
    const blockha = await web3.eth.getBlock(bn);
    let unix_timestamp = blockha.timestamp
        var months_arr = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
        console.log('','=================Log time=====================','\n');
    var date = new Date(unix_timestamp * 1000);
        // Year
    var year = date.getFullYear();
        // Month
    var month = months_arr[date.getMonth()];
        // Day
    var day = date.getDate();
        // Hours part from the timestamp
    var hours = date.getHours();
        // Minutes part from the timestamp
    var minutes = "0" + date.getMinutes();
        // Seconds part from the timestamp
    var seconds = "0" + date.getSeconds();
        // Display date time in MM-dd-yyyy h:m:s format
    var convdataTime = month+'-'+day+'-'+year+' '+hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
        console.log('Root timestamp: ', convdataTime);
        console.log('\n','============================================','\n');
    const decodedData= abiDecoder.decodeMethod(transaction.input);
    //console.log(decodedData);
    //console.log(decodedData.params[0].value);
    const fs = require('fs');
    let info = decodedData.params[0].value
    fs.writeFileSync('bcroot.txt', info, (err) => {
                 //check if there is error
                        if (err) throw err;
                });
};

const fs = require('fs');
const input1 = fs.readFileSync('Thash.txt', 'utf8');
//console.log(input1);
//console.log(typeof input1);
readProof(input1.toString(16));
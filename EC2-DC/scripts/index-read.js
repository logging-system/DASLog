// scripts/index-read.js
module.exports = async function main (callback) {
  try {
        // Set up a Truffle contract, representing our deployed Box instance
        const Box = artifacts.require('Box');
        const fs = require('fs');
        const input = fs.readFileSync('scripts/add_log_file.txt', 'utf8');
        const bn = fs.readFileSync('scripts/bn_log_file.txt', 'utf8');
        const box = await Box.at(input);
		// Call the retrieve() function of the deployed Box contract
        const value = await box.retrieve();
        var months_arr = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
        const blockha = await web3.eth.getBlock(bn);
        let unix_timestamp = blockha.timestamp
        let box_tx = blockha.transactions
        const info = await web3.eth.getTransaction(box_tx.toString(16));
        let box_data = info.input
        let base = 0x6057361d0000000000000000000000000000000000000000000000000000000000000000
        console.log('','======================================','\n');
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

        console.log('Block timestamp: ', convdataTime);
        console.log('Box value for this address: ', value.toString(16));
        fs.writeFileSync('scripts/value_in_add.txt', value.toString(16));
        console.log('Box tx: ', box_tx.toString(16));
        let current = box_data.toString(16)
        console.log('Box value for this block number: ', current.split("0x6057361d").pop());
        fs.writeFileSync('scripts/value_in_bn.txt', current.split("0x6057361d").pop());
        console.log('','======================================','\n');

    callback(0);
  } catch (error) {
    console.error(error);
    callback(1);
  }
};

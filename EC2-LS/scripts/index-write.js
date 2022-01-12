// scripts/index-write.js
var startTime, endTime;
startTime = new Date();
module.exports = async function main (callback) {
  try {
        const Box = artifacts.require('Box');
        const box = await Box.new();
        const fs = require('fs');
        const input = fs.readFileSync('scripts/hash_data_file.txt', 'utf8');
        const inf = await box.store(input);
        let scdata = inf.logs
        fs.writeFileSync('scripts/metadata.json', JSON.stringify(scdata), (err) => {
                 //check if there is error
              if (err) throw err;
        });
//////////////////////////////////////////////////////
    callback(0);
  } catch (error) {
    console.error(error);
    callback(1);
  }
endTime = new Date();
var timeDiff = endTime - startTime; //in ms
console.log('time2 to write:', timeDiff, 'ms', '\n');
};

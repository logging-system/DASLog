const Web3=require('web3');
const Box = require('./build/contracts/Box.json');
const HDWalletProvider = require('@truffle/hdwallet-provider');

const web3 = new Web3('http://Anonymous:8545');
const deployedNetwork = Box.networks[1994];
const contract = new web3.eth.Contract(
        Box.abi,
        deployedNetwork.address
);

const readAddress = async (counterIndex) => {
    let blockNumber = await web3.eth.getBlockNumber();
    let blockLength=8000;
    let result=blockNumber-blockLength;
    const receipt= await contract.getPastEvents(
                    'ValueChanged',
                    { filter: {
                                counter: counterIndex
                               },
                       fromBlock:result
                    }
    );
    let transactionHash;
    if (receipt.length==0) {
        throw "error";
    } else {
        transactionHash = receipt[0].transactionHash;
    };
    console.log(transactionHash);
        fs.writeFileSync('metadata.txt', transactionHash, (err) => {
                if (err) throw err;
                });
};
const fs = require('fs');
const input3 = fs.readFileSync('croot.txt', 'utf8');
let counter = input3;
console.log(input3);
console.log(typeof input3);
readAddress(counter);


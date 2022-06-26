const Web3=require('web3');
const Box = require('./build/contracts/Box.json');
const HDWalletProvider = require('@truffle/hdwallet-provider');
const address = '0xfe3b557e8fb62b89f4916b721be55ceb828dbd73';
const privatekey = "0x8f2a55949038a9610f50fb23b5883af3b4ecb3c3bb792cbcefbd1542c692be63";
const provider = new HDWalletProvider(privatekey,'http://18.133.191.37:8545');
const web3 = new Web3(provider);
const deployedNetwork = Box.networks[1994];
const contract = new web3.eth.Contract(
        Box.abi,
        deployedNetwork.address
);

function write (proof,counter) {
      contract.methods.store(proof,counter).send({from: address, gasPrice: 0});
};

function proofGeneration() {
        const fs = require('fs');
        const input1 = fs.readFileSync('root.txt', 'utf8');
        console.log(input1);
    let proof = input1;
        const input2 = fs.readFileSync('pointer2.txt', 'utf8');
    let counter = input2;
    console.log(proof, 'and', counter);
    console.log('writing to BC ...', '\n');
    write(proof,counter);

}

proofGeneration();

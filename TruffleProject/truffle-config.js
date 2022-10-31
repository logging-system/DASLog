const PrivateKeyProvider = require("@truffle/hdwallet-provider");
const privateKey = "0x8f2a55949038a9610f50fb23b5883af3b4ecb3c3bb792cbcefbd1542c692be63";
const privateKeyProvider = new PrivateKeyProvider(privateKey, "http://18.133.191.37:8545");

module.exports = {
  // See <http://truffleframework.com/docs/advanced/configuration>
  // for more about customizing your Truffle configuration!
  networks: {
    besuWallet: {
      gasPrice:0,
      gas: "0x1ffffffffffffe",
      provider: privateKeyProvider,
      network_id: "*"
    },
  }
};

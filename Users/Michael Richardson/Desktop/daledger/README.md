# daledger
DA Ledger Blockchain MarketPlace for Architects in Romania

To run the code (windows):

1. Go to the github rep

`https://github.com/euroledger/daledger`

Change branch to "test"

2. clone the code

`git clone https://github.com/euroledger/daledger.git`

`cd daledger\server`

3. Install server node modules

`npm install`

4. Install client node modules (on dev there are two processes running concurrently: expressjs and react client)

`cd client`
`npm install` 

5. Create the file dev.js in server\config and paste in the dev keys (ask Mike).
These are our private keys for various APIs such as Google and MongoDB which are not committed to github for security reasons.

6. Run the app

`npm run dev`

This concurrently runs the server and client (see package.json)







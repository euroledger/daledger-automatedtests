const crypto = require('crypto');

const hash = crypto.createHash('sha256') // enables digest
                   .update('I love cupcakes') // create the hash
                   .digest('hex'); // convert to string


console.log(" hash of 'I love cupcakes' = \t\t\t" + hash);

const hash2 = crypto.createHash('sha256')
                   .update('I love cupcakes?')
                   .digest('hex');


console.log(" hash of 'I love cupcakes?' = \t\t\t" + hash2);

const akey="key123456"

const hash3 = crypto.createHmac('sha256', akey)
                   .update('I love cupcakes')
                   .digest('hex');


console.log(" hash (with key) of 'I love cupcakes' = \t" + hash3);


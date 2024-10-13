https://snippet-generator.app/

const { response } = require("express");
const express = require("express");
const app = express();


app.get("/", function (req, res) {
    // both req and res is an object
    // console.log(req);
    // console.log("\n");
    // console.log("\n");
    // console.log("\n");
    // console.log(res);
    // res.send("<h1>hello</h1>"); // if we want to sent string
    res.sendFile(__dirname + "/index.html");
});




app.listen(process.env.PORT || 3000, function () {
    console.log("server is listening on port 3000.");
});







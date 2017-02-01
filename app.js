fs = require('fs');
fs.readFile("./Test.csv", 'utf8', function(err, str) {
    if (err) {
        console.log(err);
    } else {
        var inQuotes = false;
        for (var i = 0; i < str.length; i++) {
            if (str[i] === '"' && str[i-1] !== "\\") {
                inQuotes = !inQuotes;
            }

            if (str[i] === '"' && str[i-1] === "\\") {
                str = str.substr(0, i-1) + "'" + str.substr(i + 1); // Just make it a single quote
            }

            if (str[i] === "\n" && inQuotes) {
                str = str.substr(0, i) + ' ' + str.substr(i + 1); // Just make it a space
            }

            if (str[i] === "\r" && inQuotes) {
                str = str.substr(0, i) + ' ' + str.substr(i + 1); // Just make it a space
            }

            if (str[i] === "\t" && inQuotes) {                
                str = str.substr(0, i) + ' ' + str.substr(i + 1);  // Just make it a space
            }
        }

        //console.log(str);
        fs.writeFile('fixed.csv', str, 'utf8' ,function (err) {
            if (err) {
                console.log(err);
            }
        });
    }
});

// usage

// node copy.js <source> <destination>

var path = require('path');
var args = process.argv.slice(2); // Skips 'node' and script path

var sourceDir = args[0];
var destDir = args[1];

console.log('Arguments:', args);
var fs = require('fs');

fs.readdir(sourceDir, (err, files) => {
    if (err) {
        console.error('Error reading source directory:', err);
        return;
    }

    files.forEach(file => {
        var srcFile = path.join(sourceDir, file);
        var destFile = path.join(destDir, file);

        console.log('Copying:', srcFile, 'to', destFile);

        /*

        fs.copyFile(srcFile, destFile, err => {
            if (err) {
                console.error('Error copying file:', err);
            } else {
                console.log('Copied:', srcFile, 'to', destFile);
            }
        });
        */
    });
});

// usage

// node copy.js <source> <destination>

var path = require('path');
var args = process.argv.slice(2); // Skips 'node' and script path

var folderPath = "./images"

// get all folders in folderPath
var fs = require('fs');

var files = fs.readdirSync(folderPath);

async function processFiles() {
    for (const file of files) {
        const source = path.join(folderPath, file);
        const destination = path.join(folderPath, file, "output.glb");

        // if file is not directory
        if (!fs.lstatSync(source).isDirectory()) {
            continue;
        }
        if (fs.existsSync(destination)) {
            continue;
        }

        const { exec } = require('child_process');
        const { promisify } = require('util');
        const execAsync = promisify(exec);

        try {
            // Wait for git commands to complete
            await execAsync(`python trellis-run.py ${folderPath}/${file}`);
            console.log(`File ${destination} created.`);
        } catch (err) {
            console.error(`Error processing ${file}: ${err}`);
        }
    }
}

processFiles();

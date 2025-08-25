// usage

// node copy.js <source> <destination>

var path = require('path');
var args = process.argv.slice(2); // Skips 'node' and script path

var folderPath = "../assets/";

// get all folders in folderPath
var fs = require('fs');

var files = fs.readdirSync(folderPath);

async function processFiles() {
    for (const file of files) {
        const source = path.join(folderPath, file);
        const destination = path.join("./data/scripts/images", file);
        
        // if file is not directory
        if (!fs.lstatSync(source).isDirectory()) {
            continue;
        }
        if (!fs.existsSync(destination)) {
            continue;
        }

        const { exec } = require('child_process');
        const { promisify } = require('util');
        const execAsync = promisify(exec);

        try {
            // Wait for copy to complete
            await execAsync(`cp -r ${source} ${destination}`);
            console.log(`File ${file} copied to ${destination}`);
            
            // Wait for git commands to complete
            await execAsync(`git add ${destination}; git commit -m "Add ${file}";git push`);
            console.log(`File ${destination} added to git.`);
        } catch (err) {
            console.error(`Error processing ${file}: ${err}`);
        }
    }
}

processFiles();

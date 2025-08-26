
var path = require('path');
var args = process.argv.slice(2); 

async function processFiles() {

        const { exec } = require('child_process');
        const { promisify } = require('util');
        const execAsync = promisify(exec);

        try {
            // Wait for git commands to complete
            await execAsync(`git add *; git commit -m "Auto commit";git push`);
            console.log(`File ${destination} created.`);
        } catch (err) {
            console.error(`Error processing ${file}: ${err}`);
        }
    
}

processFiles();
setInterval(processFiles, 10*60*1000);

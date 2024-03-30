// server.js

const express = require('express');
const fs = require('fs');
const bodyParser = require('body-parser');
const app = express();
const port = 3001;
const hostname = "169.254.70.105"

app.use(express.static('public'));
app.use(bodyParser.json()); // Parse JSON bodies

app.get('/config', (req, res) => {
    fs.readFile('PLC_Config.json', 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading JSON file:', err);
            res.status(500).send('Internal Server Error');
            return;
        }
        res.json(JSON.parse(data));
    });
});

// Endpoint to handle POST request for updating config
app.post('/update-config', (req, res) => {
    const newData = req.body;
    console.log('start ',newData);
    // Read existing data from PLC_Config.json
    fs.readFile('public/PLC_Config.json', 'utf8', (err, existingData) => {
        
        if (err) {
            console.error('Error reading JSON file:', err);
            res.status(500).send('Internal Server Error');
            return;
        }

        let configData = {};

        try {
            // Parse existing JSON data
            configData = JSON.parse(existingData);
        } catch (parseError) {
            console.error('Error parsing JSON file:', parseError);
            res.status(500).send('Internal Server Error');
            return;
        }

        // Merge existing data with new data
        const updatedData = { ...configData, ...newData };
        console.log(newData)
        // Write updatedData back to PLC_Config.json
        fs.writeFile('public/PLC_Config.json', JSON.stringify(updatedData, null, 2), 'utf8', (writeErr) => {
            if (writeErr) {
                console.error('Error writing JSON file:', writeErr);
                res.status(500).send('Internal Server Error');
                return;
            }
            res.status(200).send('Config updated successfully');
        });
    });
});
app.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
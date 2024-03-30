function saveConfig() {
    // Get the values from the input fields
    const IN1Enable = document.getElementById('IN1').checked;
    const IN1TagName = document.getElementById('IN1_tag').value;
    const IN2Enable = document.getElementById('IN2').checked;
    const IN2TagName = document.getElementById('IN2_tag').value;
    const OUT1Enable = document.getElementById('OUT1').checked;
    const OUT1TagName = document.getElementById('OUT1_tag').value;
    const OUT2Enable = document.getElementById('OUT2').checked;
    const OUT2TagName = document.getElementById('OUT2_tag').value;
    const Port = document.getElementById('Port').value;
    const IPV4 = document.getElementById('IPV4').value;

    // Construct the payload object
    const configData = {
        IN1: {
            Enable: IN1Enable,
            TagName: IN1TagName
        },
        IN2: {
            Enable: IN2Enable,
            TagName: IN2TagName
        },
        OUT1: {
            Enable: OUT1Enable,
            TagName: OUT1TagName
        },
        OUT2: {
            Enable: OUT2Enable,
            TagName: OUT2TagName
        },
        Port: Port,
        IPV4: IPV4
    };

    // Send the data to the server
    fetch('PLC_Config.json', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(configData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to update config');
        }
        console.log('Config updated successfully');
    })
    .catch(error => console.error('Error updating config:', error));
}
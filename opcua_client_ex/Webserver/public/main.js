fetch('PLC_Config.json')
    .then(response => response.json())
    .then(data => {
        //document.getElementById('PLCName').value = data.PLC_Name;
        //document.getElementById('IPAddr').value = data.IPV4_ADDRS;

        //tag names
        document.getElementById('IN1_tag').value = data.IN1_Conf[1].TagName;
        document.getElementById('IN2_tag').value = data.IN2_Conf[1].TagName;
        document.getElementById('OUT1_tag').value = data.OUT1_Conf[1].TagName;
        document.getElementById('OUT2_tag').value = data.OUT2_Conf[1].TagName;

        //IP address
        document.getElementById('IPV4').value = data.IPV4_ADDRS
        //port nmumber
        document.getElementById('Port').value = data.port_Conf
    
    
        // Populate other fields as needed
    })
    .catch(error => console.error('Error fetching data:', error));




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


        console.log(IN1TagName)
        console.log(IN2TagName)
        console.log(OUT1TagName)
        console.log(OUT2TagName)
        console.log(Port)
        console.log(IPV4)
    
        const configData = {
            "IN1_Conf": [
                { "Enable": "False" },
                { "TagName": IN1TagName }
            ],
            "IN2_Conf": [
                { "Enable": "False" },
                { "TagName": IN2TagName }
            ],
            "OUT1_Conf": [
                { "Enable": "False" },
                { "TagName": OUT1TagName }
            ],
            "OUT2_Conf": [
                { "Enable": "False" },
                { "TagName": OUT2TagName }
            ],
            "port_Conf": Port,
            "IPV4_ADDRS": IPV4
        };
    
        console.log('Sending config data:', configData);
    
        fetch('/update-config', {
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
            console.log(configData)
        })
        .catch(error => console.error('Error updating config:', error));
    }
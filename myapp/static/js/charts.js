fetch('/api/data/')
    .then(response => response.json())
    .then(data => {
        let jsonData = JSON.parse(data.data);
        let labels = jsonData.map(item => item.fields.country);
        let values = jsonData.map(item => item.fields.likelihood);
        
        var ctx = document.getElementById('visualChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Likelihood',
                    data: values,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true
            }
        });
    });

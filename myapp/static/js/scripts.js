function fetchData() {
    let params = new URLSearchParams();
    ['end_year', 'topic', 'sector', 'region', 'pestle', 'source', 'country', 'city'].forEach(filter => {
        let value = document.getElementById(filter).value;
        if (value) {
            params.append(filter, value);
        }
    });

    fetch('/api/data/?' + params.toString())
        .then(response => response.json())
        .then(data => {
            let jsonData = JSON.parse(data.data);
            let labels = jsonData.map(item => item.fields.topic);
            let values = jsonData.map(item => item.fields.intensity);
            
            var ctx = document.getElementById('chart').getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Intensity',
                        data: values,
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        });
}

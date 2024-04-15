document.addEventListener('DOMContentLoaded', function () {
    const cities = ["Mumbai", "Pune", "Delhi", "Bangalore", "Chennai"];
    const backgroundImageUrls = {
      "Mumbai": "https://th.bing.com/th?id=OIP.MbHkqfu4VUpzxoIIhlct4wHaEo&w=316&h=197&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2",
      "Pune": "https://th.bing.com/th?id=OIP.FZ7O9sqeSAHLBmbQH0DjMAHaEK&w=333&h=187&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2",
      "Delhi": "https://th.bing.com/th?id=OIP._dpxdJcbfJnyecpAR4h9agHaE9&w=305&h=204&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2",
      "Bangalore": "https://th.bing.com/th?id=OIP.37sLYy1TbGBPi-pXmvKmBgHaEK&w=333&h=187&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2",
      "Chennai": "https://th.bing.com/th?id=OIP.cpiUOaZj0McSo8ClXIIeswHaE8&w=306&h=204&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2"
    };
  
    const backgroundDiv = document.getElementById('background');
  
    function changeBackground(city) {
      const imageUrl = backgroundImageUrls[city];
      if (imageUrl) {
        backgroundDiv.style.backgroundImage = `url('${imageUrl}')`;
      }
    }
  
    // Example of how to trigger background change when city changes
    const currentCity = "Mumbai"; // You would replace this with your actual city detection logic
    changeBackground(currentCity);
  });
  
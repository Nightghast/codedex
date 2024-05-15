async function fetchWeather() {
    let searchInput = document.getElementById('search').value;
    const weatherDataSection = document.getElementById("weather-data");
    const weatherDetails = document.getElementsByClassName("city");
    weatherDataSection.style.display = "block";
  
    const apiKey = "ef2a0262b0c3ebadd675f71c87d997f5"
  
    if (searchInput == "") {
      weatherDataSection.innerHTML = `
      <div>
        <h2>Empty Input!</h2>
        <p>Please try again with a valid <u>city name</u>.</p>
      </div>
      `;
      return;
    }

    async function getLonAndLat() {
      const countryCode = 44;
      const geocodeURL = `https://api.openweathermap.org/geo/1.0/direct?q=${searchInput.replace(" ", "%20")},${countryCode}&limit=1&appid=${apiKey}`
  
      const response = await fetch(geocodeURL);
      if (!response.ok) {
        console.log("Bad response! ", response.status);
        return;
      }
  
      const data = await response.json();
      if (data.length == 0) {
        console.log("Something went wrong here.");
        weatherDataSection.innerHTML = `
        
        <img src="https://cdn-icons-png.flaticon.com/512/755/755014.png" width="224" height="224"/>
        <div id="weather-data">
        <p class="temperature">0°C</p>
        <h2 class="city">Invalid City: "${searchInput}"</h2>
        <p>Please try again with a valid <u>city name</u>.</p>
        <div class="details">
            <div class="cols">
                <img src="images/humidity.png">
                <div>
                    <p class="humidity">0%</p>
                    <p>Humidity</p>
                </div>
            </div>
            <div class="cols">
                <img src="images/wind.png">
                <div>
                    <p class="wind">0 km/h</p>
                    <p>Wind Speed</p>
                </div>
            </div>
        </div>
    </div>
        `;
        return;
      } else {
        return data[0];
      }
    }
  
    async function getWeatherData(lon, lat) {
      const weatherURL = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}`
      const response = await fetch(weatherURL);
      const data = await response.json();

    let imageSrc;
    let temperature = Math.round(data.main.temp - 273.15);

    if (temperature >= 28) {
        imageSrc = 'images/clear.png';
        document.getElementById("weather-wrapper").style.backgroundImage = 'url("https://mir-s3-cdn-cf.behance.net/project_modules/disp/3ad89154827733.596dc6164dbd1.gif")';
    } else if (temperature > 22 && temperature <= 27) {
        imageSrc = 'images/mist.png';
        document.getElementById("weather-wrapper").style.backgroundImage = 'url("https://mir-s3-cdn-cf.behance.net/project_modules/disp/e47a3354827733.596dc61650daa.gif")';
    } else if (temperature > 17 && temperature <= 22) {
        imageSrc = 'images/clouds.png';
        document.getElementById("weather-wrapper").style.backgroundImage = 'url("https://mir-s3-cdn-cf.behance.net/project_modules/disp/5b500254827733.596dc6164ee44.gif")';
    } else if (temperature > 12 && temperature <= 17) {
        imageSrc = 'images/drizzle.png';
        document.getElementById("weather-wrapper").style.backgroundImage = 'url("https://mir-s3-cdn-cf.behance.net/project_modules/disp/14842d54827733.596dc6164f832.gif")';
    } else if (temperature > 10 && temperature <= 20) {
        imageSrc = 'images/rain.png';
        document.getElementById("weather-wrapper").style.backgroundImage = 'url("https://mir-s3-cdn-cf.behance.net/project_modules/disp/d8b05154827733.596dc77a0361f.gif")';
    } else {
        imageSrc = 'images/snow.png';
        document.getElementById("weather-wrapper").style.backgroundImage = 'url("https://mir-s3-cdn-cf.behance.net/project_modules/disp/52f06c54827733.596dc6165122d.gif")';
    }


    weatherDataSection.innerHTML = `
    <img src="${imageSrc}" width="224" height="224"/>
    <div id="weather-data">
        <p class="temperature">${Math.round(data.main.temp - 273.15)}°C</p>
        <h2 class="city">${data.name}</h2>
        <p>${data.weather[0].description}</p>
        <div class="details">
            <div class="cols">
                <img src="images/humidity.png">
                <div>
                    <p class="humidity">${data.main.humidity}</p>
                    <p>Humidity</p>
                </div>
            </div>
            <div class="cols">
                <img src="images/wind.png">
                <div>
                    <p class="wind">${data.wind.speed} km/h</p>
                    <p>Wind Speed</p>
                </div>
            </div>
        </div>
    </div>
    `
    }
  
    document.getElementById("search").value = "";
    const geocodeData = await getLonAndLat();
    getWeatherData(geocodeData.lon, geocodeData.lat);
  }
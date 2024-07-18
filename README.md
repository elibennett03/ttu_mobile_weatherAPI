I know this seem meaningless or wasteful but the reason im taking this route in creating a python script that captures the json data is becasue the weather widget being on the homescreen would mean that 
everytime someone opens the app they are making that api request which could lead to users making to many requests and me end up getting charged for it 
im deciding to automate this python script and for it to run every 2 hours so that the weather data is updated to an extent and doesnt charge me for many API GET's

temperatureApparent
Cloud Cover:

cloudCover: This value indicates the percentage of cloud cover. Higher values suggest more cloudiness.
Precipitation (Rain, Snow, Sleet):

rainIntensity: Measures the intensity of rain. A value greater than 0 indicates that it is raining.
snowIntensity: Measures the intensity of snow. A value greater than 0 indicates that it is snowing.
sleetIntensity: Measures the intensity of sleet. A value greater than 0 indicates that it is sleeting.
precipitationProbability: Represents the probability of any form of precipitation. Higher values indicate a greater likelihood of precipitation.
Accumulation (Rain, Snow, Ice):

rainAccumulation: Indicates the accumulation of rain. A value greater than 0 suggests rain accumulation.
snowAccumulation: Indicates the accumulation of snow. A value greater than 0 suggests snow accumulation.
sleetAccumulation: Indicates the accumulation of sleet. A value greater than 0 suggests sleet accumulation.
iceAccumulation: Indicates the accumulation of ice. A value greater than 0 suggests ice accumulation.
Weather Codes:

weatherCode: This code typically corresponds to specific weather conditions. For example, 1000 might represent clear skies, whereas other codes might represent various types of precipitation or cloudiness. Refer to the API documentation for exact weather codes and their meanings.
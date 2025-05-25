Feature: Weather API Testing

Scenario: Get weather for a specific city
Given I provide the city name as "Melbourne"
When I call the weather API
Then the response status code should be 200
And I should get the current temperature

Scenario: Invalid city name - no weather displayed
Given I provide the city name as "ABC123"
When I call the weather API
Then the response status code should be 404
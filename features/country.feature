Feature: Country API Testing

  Scenario: Get details for a specific country
    Given the country name is "Australia"
    When I fetch data from the REST Countries API
    Then the API response status code should be 200
    And the country capital should be "Canberra"
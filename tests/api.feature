Feature: API testing

  Scenario: Retrieve data from API
    Given realizo la operacion "GET" con el endpoint "https://postman-echo.com/get"
    Then Obtengo el status code "200"
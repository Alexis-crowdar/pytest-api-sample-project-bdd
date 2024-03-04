Feature: API testing

  Scenario Outline: Api
    Given realizo la operacion "GET" con el endpoint "https://postman-echo.com/get"
    Then Obtengo el status code "<status_code>"

    Examples:
      | status_code |
      | 400         |
      | 200         |
      | 400         |

  Scenario Outline: Api sample
    Given realizo la operacion "GET" con el endpoint "https://postman-echo.com/get"
    Then Obtengo el status code "<status_code>"

    Examples:
      | status_code |
      | 200         |

  Scenario: RickAndMorty
    Given realizo la operacion "GET" con el endpoint "https://rickandmortyapi.com/api/character/1"
    Then Obtengo el status code "200"
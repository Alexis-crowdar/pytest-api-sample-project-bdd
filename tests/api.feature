Feature: API testing

  Scenario Outline: Api
    Given realizo la operacion "GET" con el endpoint "https://postman-echo.com/get"
    Then Obtengo el status code "<status_code>"

    Examples:
      | status_code |
      | 400         |
      | 200         |
      | 400         |
      | 200         |

    Scenario Outline: Api2
    Given realizo la operacion "GET" con el endpoint "https://postman-echo.com/get"
    Then Obtengo el status code "<status_code>"

    Examples:
      | status_code |
      | 400         |


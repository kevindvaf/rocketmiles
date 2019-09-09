Feature: searching on rocketmiles.com



Scenario: Location is missing
    Given a web browser is at the rocketmiles home page
      And the location is blank
    When a search is initiated
    Then the missing location error is shown


Scenario: Reward program is missing
    Given a web browser is at the rocketmiles home page
      And the reward program is blank
      And the location is not blank
    When a search is intitiated`
    Then the missing reward program error is shown



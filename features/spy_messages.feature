Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I add "Strength and honor!" to the inputfield "#letters"
    When I select the 2 option for element "#shift-amount"
    When I click on the button "#submit"
    When I pause for 100ms
    Then I expect that element "#decoded_message" contains the text "Uvtgpivj cpf jqpqt!"

Scenario: I can successfully decode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I add "Uvtgpivj cpf jqpqt!" to the inputfield "#letters"
    When I select the 1 option for element "#decoder-setting"
    When I click on the element "p"
    When I select the 2 option for element "#shift-amount"
    When I click on the button "#submit"
    When I pause for 100ms
    Then I expect that element "#decoded_message" contains the text "Strength and honor!"

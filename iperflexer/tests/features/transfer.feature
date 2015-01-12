Feature: Transfer Data
 Scenario Outline: The IperfParser  generates transfers
   Given an <parser> with <data> data loaded and set to bits
   When the transfers are traversed
   Then the values from the data column have the <output>
   

 Examples:
 | parser      | data    | output       |
 | IperfParser | all     | sums         |
 | IperfParser | missing | sums         |
 | SumParser   | all     | sums         |
 | SumParser   | missing | fewer points |


 Scenario: Last Transfer
   Given a SumParser loaded with data that has a last line
   When the transfers are traversed
   Then the transfer from the last line is saved as last_line_transfer

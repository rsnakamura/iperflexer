Feature: A DecimalUnitConverter
  In order to convert the Network Transfers
  A converter is needed
  That handles decimal data prefixes

Scenario Outline: User converts decimal units
  Given a DecimalUnitConverter
  When the user converts from <source> to <target> and back
  Then the outcome is the correct conversion

  Examples: bytes to bits
  | source    | target     |
  | bytes     | bits       |
  | kilobytes | bits       |
  | bits      | bits       |
  | bits      | megabits   |
  | bits      | gigabits   |
  | bits      | megabytes  |
  | bits      | gigabytes  |
  | bits      | terabytes  |
  | bits      | petabits   |
  | bits      | petabytes  |
  | bits      | exabits    |
  | bits      | exabytes   |
  | bits      | zettabits  |
  | bits      | zettabytes |
  | bits      | yottabits  |
  | bits      | yottabytes |


  


Feature: A BinaryUnitConverter
  In order to convert the Data Transfers
  A converter is needed
  That handles binary data prefixes

Scenario Outline: User converts binary units
  Given a BinaryUnitConverter
  When the user converts from <source> to <target> and back
  Then the outcome is the correct conversion

  Examples: bytes to bits
  | source    | target    |
  | bytes     | bits      |
  | kibibytes | bits      |
  | bits      | bits      |
  | bits      | mebibits  |
  | bits      | gibibits  |
  | bits      | mebibytes |
  | bits      | gibibytes |
  | bits      | tebibytes |

  


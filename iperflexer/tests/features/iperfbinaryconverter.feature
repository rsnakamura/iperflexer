Feature: An IperfbinaryConverter
  In order to convert the Data Transfers
  A converter is needed
  That handles binary data conversion with iperf's unit names

Scenario Outline: User converts iperf binary units
  Given an IperfbinaryConverter
  When the user converts from <source> to <target> and back using iperf-units
  Then the outcome is the correct conversion

  Examples: Iperf bytes to bits
  | source    | target    |
  | kibibytes | bits      |
  | bits      | mebibytes |
  | bits      | gibibytes |
  | bits      | tebibytes |
  | bits      | pebibytes |
  | bits      | exbibytes |
  | bits      | zebibytes |
  | bits      | yobibytes |
  | bytes     | bits      |


Scenario Outline: User converts normal binary units
  Given an IperfbinaryConverter
  When the user converts from <source> to <target> and back
  Then the outcome is the correct conversion

  Examples: bits to bits
  | source | target   |
  | bits   | bits     |
  | bits   | mebibits |
  | bits   | gibibits |
  | bits   | pebibits |
  | bits   | exbibits |
  | bits   | zebibits |
  | bits   | yobibits |


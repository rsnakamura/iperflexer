Feature: Last Line Bandwidth
 Scenario Outline: Last Line Bandwidth
   Given a data set of <data format> iperf output
   When the user gets the last-line bandwidth
   Then the last-line bandwidth is the iperf summary

 Examples: last-line bandwidth
 | data format    |
 | human-readable |
 | csv-formatted  |


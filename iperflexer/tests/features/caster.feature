Feature: Flexible casting of values from strings to ints or floats
 Scenario Outline: The IperfParser is passed a line
   Given an IperfParser set to bits and a thread of 1
   When the IperfParser is called with a line with <numtype> <datatype>
   Then the returned <datatype> is of type <numtype>

 Examples: number types
 | numtype | datatype  |
 | integer | bandwidth |
 | float   | bandwidth |
 | integer | transfer  |
 | float   | transfer  |
   
   

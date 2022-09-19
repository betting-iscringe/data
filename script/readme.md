# Betting board script

Python 3 script that calls nasfaq bettingpools api

## Usage

Requires [python 3](https://www.python.org/downloads/) to run script.

Create a file named `instructions.txt` located in the same folder of the script

In the file, write the name of event category in the first line and all the betting pool ids (in order) in the next lines
```
VTL Example
9c22fc01-588b-479e-be31-74c769f32407
bae15cd3-fd77-4951-a0d2-95fda562f61c
ca0fa2ea-f39d-43e1-8b22-1f6552a80189
02889a1c-2631-47aa-b34f-b4530fc9c5f6
c3d03628-471f-4d0f-8897-ca20c91f8e01
2a66e17c-543c-43c2-bc2a-0abe29ac9651
9b66497c-7ce9-438d-92ec-7942eaa43bf7
7697ae51-1e25-44f7-89cd-e95a5037df0d
```
Run the python file to generate the betting data and it should make a file named `<event_category>.json`

In the example above, the file would be named `VTL Example.json`

Then open the corresponding betting type folder `divegrass`, `hfz` and `etc` and place the generated json in it.

Next, edit `index.json` in the same folder and add the event category to the array of names.
```json
{
  "names": [
    "VTL2 Day 1",
    "VTL2 Day 2 (only winnings)",
    "VTL2 Day 3",
    "VTL2 Day 4",
    "VTL2 Day 5",
    "VTL2 Day 6",
    "4cc Spring Babby",
    "4cc Spring Babby days 2, 5 and 11 (only winnings)",
    "4cc Summer Cup",
    "VTL3 Day 1",
    "VTL3 Day 2",
    "VTL3 Day 3",
    "VTL3 Day 4",
    "VTL3 Day 5",
    "VTL3 Day 6",
    "VTL Example"
  ]
}
```

Finally, commit changes and push and board should auto update in a minute or two

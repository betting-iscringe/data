# Betting board script

Python 3 script that calls nasfaq bettingpools api

## Usage

Requires [python 3](https://www.python.org/downloads/) to run script.

1. Create a file named `instructions.txt` in the same folder of the script

2. In `instructions.txt`, write the name of event category on the first line and all the betting pool IDs (in order) on the next lines
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
3. Run the python file to generate the betting data. This will create a file named `<event_category>.json`. For example, if your event category is "VTL Example" the file would be named `VTL Example.json`

4. Open the corresponding betting type folder (`divegrass`, `hfz`, `etc`) and move the generated JSON file into it.

5. Commit your changes and push them to update the board automatically within a minute or two.

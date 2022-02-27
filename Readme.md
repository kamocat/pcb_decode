This project is a PCB "decoder" using OpenCV.
The goal is to take a picture of the front and back of a PCB, and use
computer vision to generate a netlist. Converting a netlist to a schematic
is somewhat outside the scope of this project - I'm hoping there are
existing tools to do that.

## Process outline

Preparation:
-    Find corners of board
-    Crop
-    Map front to back

Feature identification:
-    Identify traces
-    Identify pins
-    Identify components

Association:
-    Associate pins with components, establish pin order
-    Create netlist from traces
-    Connect nets through vias and pins

Cleanup:
-    Guess hidden connections
-    Generate schematic from netlist

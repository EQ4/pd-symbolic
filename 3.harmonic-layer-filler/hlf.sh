#!/bin/bash

# declare and print STRING variable
STRING="Harmonic Layer Filler"
echo $STRING

pd-extended --nogui open "./harmonic-layer-filler.pd" &
sleep 0.5
wish hlf.tk
killall pd-extended
killall pd
exit

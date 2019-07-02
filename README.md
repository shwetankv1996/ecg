# ecg
In order to find the heartbeat from the raw input data sampled at a frequency of 200Hz we nned to first filter the data in order to remove the 50Hz power noise. For this porpuse a notch filter with frequency 45-55Hz has been designed and the data was saved in the extracted file.

Now to get the heartbeat of the data we will check the simultaneous peaks in the signal and find the index difference between the two consecutive peaks.

1. Filter the 50Hz noise
2. Detect two consecutive peaks
3. save the consecutive peak indexes
4. Find the index difference 
5. Divide the idex difference with sample frequency
6. This gives the time between each peak i.e. the time of one heartbeat
7. Inverse the time and multiply with 60 to find beats per minute.


https://github.com/berndporr/iir_fixed_point/blob/master/Makefile
https://www.earlevel.com/main/2012/11/26/biquad-c-source-code/
https://www.youtube.com/watch?v=dJCZc8mJrRo

g++ (Ubuntu 7.4.0-1ubuntu1~18.04.1) 7.4.0
Copyright (C) 2017 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.



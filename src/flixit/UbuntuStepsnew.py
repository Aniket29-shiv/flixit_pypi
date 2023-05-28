sudo apt install python3-pip 
sudo apt update
sudo apt upgrade


Linux System: Run in Terminal 
1.	Check the GCC version: gcc –version

2.	Installation : sudo apt install gcc

3.	Configuring OpenMP: sudo apt install libomp-dev

4.	Setting the number of threads: export OMP_NUM_THREADS=8

5.   	sudo nano filename.cpp 

6.	ctrl+O & ctrl+X

7.	Compile:  g++ -fopenmp filename.cpp -o demo

8.	Execute:  ./filename






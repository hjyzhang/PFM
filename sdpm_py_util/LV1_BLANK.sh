module purge
module load gcc11/11.3.0
module load openmpi4/gcc/4.1.5
module load hdf5/1.14.3
module load netcdf/mpicc/4.8.1
# module load netcdf/gcc/64/gcc/64/4.8.1

#export OMP_NUM_THREADS=$np$ 
# nohup mpirun -v -np #$np$ $np$ $lv1_executable$  $lv1_infile_local$ > $lv1_logfile_local$ 
mpirun -v -np $np$ $lv1_executable$  $lv1_infile_local$  >& $lv1_logfile_local$ 

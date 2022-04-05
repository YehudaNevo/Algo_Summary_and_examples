# Major Functionalities of Operating System:
#
# Resource Management: When parallel accessing happens in the OS means when multiple users are accessing the system
# the OS works as Resource Manager, Its responsibility is to provide hardware to the user. It decreases the load in
# the system.
# Process Management: It includes various tasks like scheduling, termination of the process. OS manages various
# tasks at a time. Here CPU Scheduling happens means all the tasks would be done by the many algorithms that use
# for scheduling.
# Storage Management: The file system mechanism used for the management of the storage. NIFS, CFS, CIFS, NFS, etc.
# are some file systems. All the data stores in various tracks of Hard disks that all managed by the storage
# manager. It included Hard Disk.
# Memory Management: Refers to the management of primary memory. The operating system has to keep track, how much
# memory has been used and by whom. It has to decide which process needs memory space and how much. OS also has to
# allocate and deallocate the memory space.
# Security/Privacy Management: Privacy is also provided by the Operating system by means of passwords
# so that unauthorized applications can’t access programs or data. For example, Windows uses Kerberos
# authentication to prevent unauthorized access to data.
#
# -------------------------------------------------------------------------------------------------------------------
#
# Types of Operating Systems
# 1. Batch Operating System –
# This type of operating system does not interact with the computer directly.
# There is an operator which takes similar jobs having the same requirement and group them into batches.
# It is the responsibility of the operator to sort jobs with similar needs.
# Examples of Batch based Operating System: Payroll System, Bank Statements, etc.
#
# 2. Time-Sharing Operating Systems –
# Each task is given some time to execute so that all the tasks work smoothly.
# Each user gets the time of CPU as they use a single system.
# These systems are also known as Multitasking Systems. The task can be from a single user or
# different users also. The time that each task gets to execute is called quantum.
# After this time interval is over OS switches over to the next task.
# Examples of Time-Sharing OSs are: Multics, Unix, etc.
#
# 3. Distributed Operating System –
# These types of the operating system is a recent advancement in the world of computer technology
# and are being widely accepted all over the world and, that too, with a great pace. Various autonomous
# interconnected computers communicate with each other using a shared communication network. Independent
# systems possess their own memory unit and CPU. These are referred to as loosely coupled systems or distributed
# systems. These system’s processors differ in size and function. The major benefit of working
# with these types of the operating system is that it is always possible that one user can access the files or
# software which are not actually present on his system but some other system connected within
# this network i.e., remote access is enabled within the devices connected in that network.
#
# 4. Network Operating System,
# 5. Real-Time Operating System –
# ----------------------------------------------------------------------------------------


# process might be in 5 states: 1. new   2. ready   3. run  4. wait  5. terminated or completed
# Types of schedulers:
# Long term – performance – Makes a decision about how many processes should be made to stay  in the ready state,
# this decides the degree of multiprogramming. Once a decision is taken it lasts for
# a long time hence called long term scheduler.
# Short term – Context switching time – Short term scheduler will decide which process to be executed next and
# then it will call dispatcher. A dispatcher is a software that moves process from ready to run and vice versa.
# In other words, it is context switching.
# Medium term – Swapping time – Suspension decision is taken by medium term scheduler. Medium term scheduler
# is used for swapping that is moving the process from main memory to secondary and vice versa.


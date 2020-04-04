linux-sgio
===========
access /dev/sg* devices using ioctl(SG_IO). 

This Extention was part of the [python-scsi](https://github.com/python-scsi/python-scsi) project and got replaced by 
[cython-sgio](https://github.com/python-scsi/cython-sgio).
  
*  Only available for Linux

License
=======
Python-scsi is distributed under LGPLv2.1
Please see the LICENSE file for the full license text.


Getting the sources
===================
The module is hosted at https://github.com/rosjat/linux_sgio

You can use git to checkout the latest version of the source code using:

    $ git clone git@github.com:rosjat/linux_sgio.git

It is also available as a downloadable zip archive from:

    https://github.com/rosjat/linux_sgio/archive/master.zip 


Building and installing
=======================
Building the module:

    $ python setup.py build
    
Installing the module:

    $ python setup.py install


Unit testing
============
The tests directory contain unit tests for python-scsi.
To run the tests:

   $ cd tests
   $ make


Tools (examples)
================
The tools directory contains example programs written against the python-scsi
API. 

inquiry.py
----------
An example tool to send INQUIRY commands to a device.

mtx.py
------
An example tool to operate a SCSI media changer. Similar to, but not as
advanced as, the 'mtx' utility.


Mailinglist
===========
A mailinglist for python-scsi is available at:
https://groups.google.com/forum/#!forum/python-scsi
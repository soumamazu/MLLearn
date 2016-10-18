# Learning ML from Scratch
Self Learning Machine Learning

Most of the code is written in Python my Windows Docker using TensorFlow and Microsoft CNTK.

### To install and run Docker and TensorFlow on Windows --

1. Install Docker Toolbox from https://www.docker.com/products/docker-toolbox. Do not enable Hyper-V or anything like that. Install the VirtualBox that comes with it, and that should be the best. For more details check here - http://www.netinstructions.com/how-to-install-and-run-tensorflow-on-a-windows-pc/.
2. Once the installation is done, open the quickstart terminal and let Docker create a VM. By default, it creates the default VM, you can add machines according to the tutorial above.
3. Open up a CMD prompt, and check if the machine exists using `docker-machine ls`. If it's active and running, type in the following --
  * `FOR /f "tokens=*" %i IN ('docker-machine env --shell cmd default') DO %i`
  * `docker exec -it MyTensorFlow bash`
4. And you're done. Make sure you type in those two every time you start up.

In the dependency downloading part, you might have issues with the Python versions, make sure you have pip for all your versions --

  * `curl -O https://bootstrap.pypa.io/get-pip.py`
  * `sudo python3.2 get-pip.py`

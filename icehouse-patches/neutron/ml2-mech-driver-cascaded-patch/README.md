Neutron ml2-mech-driver-cascaded-patch
===============================

 Cascaded Neutron Server acts as the same role of Neutron Server in Cascaded OpenStack Layer.
 Cascaded Neutron-Server inherits from Neutron Server, we modifed only one module l2pop. Because we introduce concept of remote port in Cascaded Neutron-Server, and add some code to process the remote port in mechanism driver.

Key modules
-----------

* Cascaded Neutron-Server inherits from Neutron Server, we modifed only one module plugins/ml2/drivers/l2pop. Because we introduce concept of remote port in Cascaded Neutron-Server, and add some code to process the remote port in mechanism driver��

    neutron/plugins/ml2/drivers/l2pop/db.py
    neutron/plugins/ml2/drivers/l2pop/mech_driver.py
    neutron/plugins/ml2/drivers/l2pop/config.py

Requirements
------------
* openstack-neutron-2014.1-1.1 has been installed and DVR patch has been made.

Installation
------------

We provide two ways to install the Cascaded neutron-server code. In this section, we will guide you through installing the Cascaded neutron-server with the minimum configuration.

* **Note:**

    - Make sure you have an existing installation of **Openstack Icehouse**.
    - We recommend that you Do backup at least the following files before installation, because they are to be overwritten or modified:
        $NEUTRON_PARENT_DIR/neutron
        (replace the $... with actual directory names.)

* **Manual Installation**

    - Navigate to the local repository and copy the contents in 'neutron' sub-directory to the corresponding places in existing neutron, e.g.
      ```cp -r $LOCAL_REPOSITORY_DIR/neutron $NEUTRON_PARENT_DIR```
      (replace the $... with actual directory name.)
      ```

    - Restart the neutron server.
      ```service openstack-neutron restart```

    - Done. The cascaded neutron server should be working with a ml2 plugin.

* **Automatic Installation**

    - Navigate to the installation directory and run installation script.
      ```
      cd $LOCAL_REPOSITORY_DIR/installation
      sudo bash ./install.sh
      ```
      (replace the $... with actual directory name.)

    - Done. The installation code should modify the neutron code without modifying the configuration.

* **Troubleshooting**

    In case the automatic installation process is not complete, please check the followings:

    - Make sure your OpenStack version is Icehouse and DVR patch has been made.

    - Check the variables in the beginning of the install.sh scripts. Your installation directories may be different from the default values we provide.

    - The installation code will automatically modify the related codes to $NEUTRON_PARENT_DIR/neutron and not modify the related configuration.

    - In case the automatic installation does not work, try to install manually.
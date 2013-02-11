Introduction
=========================
A simple [skype4py](https://github.com/awahlig/skype4py) script that allows speed dialing with pauses and extensions.

Installation
=========================

* Ensure that you have [Skype](http://www.skype.com/) installed. On Ubuntu this can be done using the following command:

        sudo apt-get install skype

* Ensure that you have [skype4py](https://github.com/awahlig/skype4py) installed. On Ubuntu this can be done by performing the following commands

        sudo apt-get install python python-pip
        sudo pip install --upgrade Skype4Py

* Copy [speeddial.py](./speeddial.py) to a known location and ensure that it is executable (i.e. chmod +x speeddial.py). In the future, we will refer to this location as $SPEEDDIAL_HOME

Usage
=========================

After following the Installation instructions, you can use speeddial.py as soon as you have started Skype by executing the script with the number you wish to dial. For example, I create a script named conference.sh that looks like this:

    $SPEEDDIAL_HOME/speeddial.py 18001234567

Now to run it all you need to do is execute the script. This isn't all that useful since you can create a contact within Skype that has a number. However, the script also supports pausing and extensions. For example, if you enter the following:

    $SPEEDDIAL_HOME/speeddial.py 18001234567,,890#

* The number 18001234567 is dialed
* It waits 2 seconds (1 second for each ,). You can add as few or as many , as you like
* It dials 890#

Now you can create a shortcut (i.e. bash script, alias, etc) for each phone number you call frequently!

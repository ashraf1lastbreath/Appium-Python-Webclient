# Appium-Python-Webclient

Appium is an open-source test-automation framework for mobile apps – native, hybrid and web apps are supported. 



  - cross platform, works both on ioS and Android
  - Free
  - automates native, web and hybrid apps

# About

  - This is a Python Webclient for Appium 1.6 or Above. 
  - The target test case is to open www.google.com on a Simulator, and then enter a random search string for Google to do a search on.


You can also:
  - with a few minor changes, use the same example for a Real Ios Device
  - use any other url to automate tests on.
  

[Appium](www.appium.io) was designed to meet mobile automation needs according to a philosophy outlined by the following four tenets: 
> 1.  You shouldn’t have to recompile your app or modify it in any way in order to automate it
> 2.  You shouldn’t be locked into a specific language or framework to write and run your tests.
> 3.  A mobile automation framework shouldn’t reinvent the wheel when it comes to automation APIs.
> 4.  A mobile automation framework should be open source, in spirit and practice as well as in name!


### Dependecies / System Requirements 

Appium uses a number of open source projects to work properly:


* [Appium1.6](www.appium.io) - Apple's new [XCUITest](https://forums.developer.apple.com/thread/6503) framework, needs Appium ver 1.6 or higher. Presently no GUI version on Appium 1.6 is available. Only a commandline version is available as a Beta release. 
* OS-X 10.7 or higher 
* [Xcode 8](https://itunes.apple.com/in/app/xcode/id497799835?mt=12)  or higher
* [Python 2.7](https://www.python.org/download/releases/2.7/) 
* [Sublime Text](https://www.sublimetext.com/) - An awesome test editor which supports Python bindings
* [node.js] - evented I/O for the backend
* [Safari Launcher](https://github.com/budhash/SafariLauncher) -  simple IOS application that automatically launches Mobile Safari after a certain delay 


### Installation

Appium installation requires [Node.js](https://nodejs.org/) v4+ to run.

Install the dependencies and devDependencies and start the server.

Install Appium 1.6 
```sh
$ sudo npm install -g appium@1.6
```

Check node version (node -v). Appium1.6 requires atleast Node 4.

#Setting up dependencies for Appium1.6 :

For ioS 9 : 

```sh
$ brew install ideviceinstaller
```

For ioS 10 : 

```sh
$ npm install -g ios-deploy
```

### Plugins

Appium is currently extended with the following plugins. Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| carthage | [Carthage/Carthage/blob/master/README.md] [PlDb] |
| deviceconsole | [rpetrich/deviceconsole] [PlGh] |
| Xcpretty | [supermarin/xcpretty/blob/master/README.md] [PlGd] |
| Libimobiledevice | [libimobiledevice/libimobiledevice/blob/master/README] [PlOd] |
| Appiumdoctor | [/appium/appium-doctor/blob/master/README.md] [PlMe] |

**carthage :**
```sh
$ brew install carthage
```

**deviceconsole :**
```sh
$ npm install -g deviceconsole
```

**Xcpretty :**
```sh
$ gem install Xcpretty
```

**libimobiledevice :**
ios 9 :
```sh
$ brew install libimobiledevice
```

ios 10 :
```sh
$ brew install libimobiledevice --HEAD
```

**Appium Doctor :**
```sh
$ sudo npm install -g appium-doctor
```

### Inspecting Elements :
Appium1.6 doesnot support Appium Inspector. So have to use an alternative Inspector to inspect elements.

**Xcode > Open Developer Tool > Accessibility Inspector**

Click   '*No Target*' > *Show to Simulator*

License
----

Ashraf


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
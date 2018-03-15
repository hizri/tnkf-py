 ##### framework was written with python3 #####

 - install allure
```
brew install allure
```

````
➜  ~ allure --version
2.3.4
````

 - clone repository
```
git clone https://github.com/hizri/tnkf-py.git
```
 - move to project directory
 - create virtualenv "env" (e.g)
```
virtualenv -p python3 env  # if python3 is not set by default

# or for pyenv
pyenv virtualenv env
```
 - activate virtualenv
```
source env/bin/activate

# or for pyenv
pyenv activate env
```

 - install requirements
 ```
 pip install -r requirements.txt
```

 #### Run tests ####
 - via commandline
```
py.test tests/ -s -v --alluredir=output  # output/ was added to .gitignore

# or for pytest
PYTHONPATH . py.test tests/ -s -v --alluredir=output
```

 - or using IDE runner
 
 #### Allure report ####
 
 After test run is finished `output/` directory should be created
 
 To generate allure report execute commands

```
# first way
allure generate -c output
allure open

# another way
allure serve output 
```
 
 #### Logging ####
 
Each case in allure report has steps

Some steps (request steps in this case) have inner attachments that can be checked by expanding step<br>
and clicking on attachmment<br>

 ##### Full case log is attached to case report #####
Check `teardown` case report section<br>
(*Tear down > attach_full_log::attach_and_clear_buffer > Full log*)


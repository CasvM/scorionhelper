import time;
import sys;
import os;

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)

def getGroups(course_id, fileName, seperator, write):
    password = "Geheim123!";


    f = open(fileName, "r");

    lines = f.readlines();

    f.close();

    result = [];
    for line in lines:
        if not line.startswith("Username"):
            editedLine = line.split(seperator);
            editedLine[-1] = editedLine[-1].split("\n")[0];
            result.append(editedLine);
    
    groupList = [];
    oldGroupName = "";
    fileLength = len(result);
    
    if write:
        f = open(fileName.split(".")[0] + "_result" + ".txt", "w");

        #first line
        f.write("firstname;lastname;grouphand;role;status;username;password;email;syncstatus\n");
        
        if "-" in course_id:
            course_id_firstPart = course_id.split("-")[0];
        else:
            course_id_firstPart = course_id;
            
        for i in range(fileLength):
            line = result[i]
            if not line[2]=="Instructor":
                groupName = course_id_firstPart + "-" + line[1];

                if not (groupName == oldGroupName):
                    groupList.append(groupName);
                
                f.write(line[3] + ";" + line[4] + ";" + course_id.split("-")[0] +
                                "-" + line[1] + ";" + "group_student,overall_filemanager" +
                                ";" + "active" + ";" + "tudelft_" + line[0] + "@tudelft.nl" +
                                ";" + password + ";" + line[5] + ";" + "notsynced")
                if not (i == (fileLength - 1)):
                    f.write("\n")

                oldGroupName = groupName;

        f.close();
    
    else:
        for i in range(1,fileLength):
            line = result[i]
            groupName = line[2];

            if not (groupName == oldGroupName):
                groupList.append(groupName);
            oldGroupName = groupName;

    return groupList[0:len(groupList)];

def createScorionGroups(subGroupNames, courseId):
    from selenium import webdriver;
    chrome_path = 'chromedriver.exe';
    chromedriver = resource_path(chrome_path);
    driver = webdriver.Chrome(executable_path = chromedriver);
    driver.implicitly_wait(10);

    driver.get("https://scorion3.parantion.nl");
    
    def __del__():
        driver.quit();
    
    def waitForGroupsLoaded():
        while len(driver.find_elements_by_xpath(
        "//*[@class='jstree-icon glyphicon glyphicon-group']")) <= 1:
            if not checkTree():
                openTree();
            time.sleep(0.1);
        return;

    def waitForOptionsLoaded(n_options):
        while len(driver.find_elements_by_tag_name("option")) <= n_options:
            time.sleep(0.1);
        return;

    def waitForSubGroupOk(startOpts):
        while len(driver.find_elements_by_tag_name("option")) > startOpts:
            time.sleep(0.1);
        return;

    def selectOptionFromString(text):
        options = driver.find_elements_by_tag_name("option");
        for i in range(len(options)):
            if text in options[i].get_attribute("outerText"):
                options[i].click();
                break;
        return;

    def goToGroups():
        selected = driver.find_elements_by_class_name("selected ")[0]
        
        correctLink = driver.find_elements_by_xpath(
        "//*[@class='glyphicon glyphicon-user_group_1']")[-1].find_element_by_xpath(
            '..');

        if not (selected == correctLink):
            correctLink.click();
        return;

    def inCourseId():
        if len(driver.find_elements_by_class_name("jstree-clicked")) == 0:
              return False;          
        return (courseId + " ") in driver.find_elements_by_class_name("jstree-clicked")[0].get_attribute("innerText");

    def openTree():
        elem = driver.find_elements_by_tag_name("ins")[0];

        if not checkTree():
            elem.click();
    
    def checkTree():
        elem = driver.find_elements_by_tag_name("ins")[0];
        checkstr = elem.find_element_by_xpath("..").get_attribute("outerHTML");
        return "jstree-open" in checkstr or "jstree-loading" in checkstr;
    
    def selectCourseId():
        if inCourseId():
            return;
        
        groups = driver.find_elements_by_xpath(
        "//*[@class='jstree-icon glyphicon glyphicon-group']")

        
        courseIdExists = False;
        for i in range(len(groups)):
            if (courseId + " ") in groups[i].find_element_by_xpath('..').get_attribute(
                "outerText"):
                groups[i].find_element_by_xpath('..').click();
                courseIdExists = True;
                break;
        
        if not courseIdExists:
            createCourse();
            waitForGroupsLoaded();
            selectCourseId();
            return;
        
    def waitForInCourseId():
        while not inCourseId():
            time.sleep(0.1);
        return;

    def createSubGroup(subGroupName):
        startOpts = len(driver.find_elements_by_tag_name("option"));
        driver.find_elements_by_xpath(
        "//*[@class='glyphicon glyphicon-add_user_group_1']")[-1].find_element_by_xpath(
            '..').click();
        
        waitForOptionsLoaded(startOpts);
        driver.find_element_by_id("name").send_keys(subGroupName);
        selectOptionFromString("Groep (Handmatig)");

        waitForOptionsLoaded(12 + startOpts);
        selectOptionFromString(courseId);

        driver.find_element_by_id("PopupAjaxOkButton1").click();
        waitForSubGroupOk(startOpts);

    def createCourse():
        startOpts = len(driver.find_elements_by_tag_name("option"));
        driver.find_elements_by_xpath(
        "//*[@class='glyphicon glyphicon-add_user_group_1']")[-1].find_element_by_xpath(
            '..').click();

        waitForOptionsLoaded(startOpts);
        driver.find_element_by_id("name").send_keys(courseId);
        selectOptionFromString("Cursus (handmatig)");
        time.sleep(1);
        driver.find_element_by_id("PopupAjaxOkButton1").click();
        waitForSubGroupOk(startOpts);


    #username
    driver.find_element_by_id("username").send_keys("tudpeeadmin");

    #password
    driver.find_element_by_id("password").send_keys("rtgeh678");

    #click to login
    driver.find_element_by_id("loginsubmit").click();

    ########################## go to correct group ################################
    goToGroups();

    waitForGroupsLoaded();

    selectCourseId();

    waitForInCourseId();
    
    time.sleep(1);    
    
    waitForGroupsLoaded();
    ############################## create subgroups ################################

    for i in range(len(subGroupNames)):
        createSubGroup(subGroupNames[i]);
        waitForGroupsLoaded();
    
    return driver;

    

    
    

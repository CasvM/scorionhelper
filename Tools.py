"""
Created on Wed Jun 21 09:50:15 2017

@author: cwvanmierlo
"""

import time;
import sys;
import os;

def resource_path(relative_path):
    #This function is needed for PyInstaller, without this function the 
    #incorrect path will be pulled while compiling the .EXE
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)

def splitGroups(fileName, errorFile):
    f = open(fileName, "r");
    lines = f.readlines();
    f.close();

    f = open(errorFile, "r");
    errors = f.readlines();
    f.close();

    newUsers = [];
    existingUsers = [];
    for i in range(1, len(lines)):
        addToExisting = False;
        for j in range(len(errors)):
            seperator = " ";            
            if "\t" in errors[j]:
                seperator = "\t";
            if (i + 1)==int(errors[j].split(seperator)[0]):
                addToExisting = True;
                break;
        if addToExisting:
            existingUsers.append(lines[i]);
        else:
            newUsers.append(lines[i]);


    newFile = fileName[0:fileName.rfind(".")].split("_formatresult")[0];
    
    
    fNew = open(newFile + "_new" + ".txt", "w");
    fNew.write(lines[0]);
    
    
    for newUser in newUsers:
        fNew.write(newUser);
    fNew.close();
    
    sortOrder = lines[0];    
    
    exVarIndex1 = sortOrder.split(";").index("username");
    exVarIndex2 = sortOrder.split(";").index("grouphand");
    
    
    fExisting = open(newFile + "_existing" + ".txt", "w");
    fExisting.write(lines[0].split(";")[exVarIndex1] + ";" + lines[0].split(";")[exVarIndex2] + "\n");
    
    for existingUser in existingUsers:
        split = existingUser.split(";");
        fExisting.write(split[exVarIndex1] + ";" + split[exVarIndex2] + "\n");
        #TODO: (minor) delete last \n from file
    fExisting.close();
    
def getGroups(course_id, fileName, seperator, write):
    password = "Geheim12345!";
    
    
    f = open(fileName, "r");

    lines = f.readlines();
    f.close();


    cleanFileName = fileName[0:fileName.rfind(".")];

    sortOrder = [item.lower() for item in lines.pop(0).split("\n")[0].split(seperator)];

    result = [];
    
    #TODO: fix formatting errors once and for all
    import unicodedata;

    
    for line in lines:
        editedLine = u"".join([c for c in unicodedata.normalize('NFKD', line) if not unicodedata.combining(c)]).replace("ł", "l").replace("Ł", "L");
        editedLine = editedLine.split("\n")[0];
        result.append(editedLine);
        
    
    if "-" in course_id:
        course_id_firstPart = course_id.split("-")[0];
    else:
        course_id_firstPart = course_id;    
    
    groupList = [];
    fileLength = len(result);
    
    if write:
        f = open(cleanFileName + "_formatresult" + ".txt", "w");

        #first line
        f.write("firstname;lastname;grouphand;role;status;username;password;email;syncstatus\n");
            
        for i in range(fileLength):
            line = result[i].split(seperator);
            if True: #TODO add exclusion lists
                groupName = course_id_firstPart + "-" + line[sortOrder.index("groupname")];
                groupName = groupName.replace(" ", "-");
                if not any(groupName in s for s in groupList):
                    groupList.append(groupName);
                
                currentUsername = "tudelft_" + line[sortOrder.index("username")];
                if not "@" in currentUsername:
                     currentUsername += "@tudelft.nl";
                     
                currentFirstname = line[sortOrder.index("firstname")]
                currentLastname = line[sortOrder.index("lastname")]
                
                f.write(currentFirstname + ";" + currentLastname + ";" + groupName + ";" + "group_student,overall_filemanager" +
                                ";" + "active" + ";" + currentUsername +
                                ";" + password + ";" + line[sortOrder.index("email")] + ";" + "notsynced")
                if not (i == (fileLength - 1)):
                    f.write("\n")

        f.close();
    
    else:
        for i in range(fileLength):
            line = result[i].split(seperator);
            groupName = line[sortOrder.index("grouphand")];
            groupName = groupName.replace(" ", "-");
            
            if not any(groupName in s for s in groupList):
                groupList.append(groupName);

    return groupList[0:len(groupList)];

def errorChecker(fileName):
    class possibleError(object):
        ordNumber = 0;
        ordCharacter = "";
        lineOccurence = 0;
        colOccurence = 0;
        sourceLine = "";
         
        def __init__(self, ordNumber, ordCharacter, lineOccurence, colOccurence, sourceLine):
            self.ordNumber = ordNumber;
            self.ordCharacter = ordCharacter;
            self.lineOccurence = lineOccurence;
            self.colOccurence = colOccurence;
            self.sourceLine = sourceLine;
        
        def getOrdNumber(self):
            return self.ordNumber;
        
        def getOrdCharacter(self):
            return self.ordCharacter;
        
        def getLineOccurence(self):
            return self.lineOccurence;
        
        def getColOccurence(self):
            return self.colOccurence;
        
        def getSourceLine(self):
            return self.sourceLine;
        
        def __repr__(self):
            return "ord:%d\t|\tchr:%s\t|\tline:%d\t|\tcolumn:%d\t\n" % (self.ordNumber, self.ordCharacter, self.lineOccurence, self.colOccurence);

    
    f = open(fileName, "r");

    lines = f.readlines();
    f.close();
    
    
    errorArray = []
    for i in range(len(lines)):
        
        numberedLine = []
        for j in range(len(lines[i])):
            numberedLine.append(ord(lines[i][j]));

        if (max(numberedLine) > 255):
            errorArray.append(possibleError(max(numberedLine), chr(max(numberedLine)), i, numberedLine.index(max(numberedLine)), lines[i]));
        
    errorArray = errorArray[0:];
    
    return errorArray;
    


def createScorionGroups(subGroupNames, courseId):
    from selenium import webdriver;
    chrome_path = "chromedriver.exe";
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
            '..').send_keys(webdriver.common.keys.Keys.RETURN);
        
        waitForOptionsLoaded(startOpts);
        driver.find_element_by_id("label").send_keys(subGroupName);
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
        driver.find_element_by_id("label").send_keys(courseId);
        selectOptionFromString("Cursus (handmatig)");
        time.sleep(1);
        driver.find_element_by_id("PopupAjaxOkButton1").click();
        waitForSubGroupOk(startOpts);


    driver.find_element_by_id("username").send_keys("tudpeeadmin");

    driver.find_element_by_id("password").send_keys("rtgeh678");

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
    
    

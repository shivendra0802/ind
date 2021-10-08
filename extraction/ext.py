import pandas as pd
from tika import parser
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
import string
from nltk.tokenize import word_tokenize 
import os
nltk.download('stopwords')
nltk.download('punkt')

t = os.getcwd()
print(t)



def LoadSkillDataset():
    skillDataset = pd.read_csv('/home/cheems/Desktop/indee/extraction/ResumeSkill.csv')
    frontEnd = list(skillDataset['Front_End'])
    backEnd = list(skillDataset['Back_End'])
    machineLearning = list(skillDataset['Machine_Learning'])
    androidDeveloper = list(skillDataset['Android_Developer'])
    educationLevel = list(skillDataset['Education'])
    cleanedFrontEndList = [x for x in frontEnd if str(x) != 'nan']
    cleanedBackEndList = [x for x in backEnd if str(x) != 'nan']
    cleanedMachineLearningList = [x for x in machineLearning if str(x) != 'nan']
    cleanedAndroidDeveloperList = [x for x in androidDeveloper if str(x) != 'nan']
    cleanedEducationLevel = [x for x in educationLevel if str(x) != 'nan']
    return cleanedFrontEndList , cleanedBackEndList , cleanedMachineLearningList , cleanedAndroidDeveloperList, cleanedEducationLevel

frontEndList , backEndList , machineLearningList , androidDevelopmentList, educationLevelList = LoadSkillDataset()

print(LoadSkillDataset)
def fileTextExtractor():
    newResumeTxtFile = open('/home/cheems/Desktop/indee/extraction/sample.txt', 'w')
    resumeFile = '/home/cheems/Desktop/indee/extraction/SampleResume.pdf'
    # resumeFile = '/home/cheems/Desktop/indee/extraction/Grace-ResumeViking-20.pdf'
    resumeFileData = parser.from_file(resumeFile)
    fileContent = resumeFileData['content']
    newResumeTxtFile.write(fileContent)
    return fileContent
obtainedResumeText = fileTextExtractor()


def personalDetailExtractor():
    finalExtractedEmail = []
    resumeFinalPhone = []
    oneFourthOfResume = obtainedResumeText[0:len(obtainedResumeText)//4] 
    emailResume = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", oneFourthOfResume)
    phoneResume = re.findall(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})",oneFourthOfResume)
    
    if len(emailResume) > 1:
        finalExtractedEmail = emailResume[0]
    else:
        finalExtractedEmail = emailResume
        
    for i in range(len(phoneResume)):
        if len(phoneResume[i])>=10:
            finalExtractedPhone = phoneResume[i]
    return finalExtractedEmail,finalExtractedPhone

finalExtractedEmail , finalExtractedPhone = personalDetailExtractor()


firstLetterCapitalizedObtainedResumeText = []
def CapitalizeFirstLetter(obtainedResumeText):
    capitalizingString = " "
    obtainedResumeTextLowerCase = obtainedResumeText.lower()
    obtainedResumeTextUpperCase = obtainedResumeText.upper()
    splitListOfObtainedResumeText = obtainedResumeText.split()
    for i in splitListOfObtainedResumeText:
        firstLetterCapitalizedObtainedResumeText.append(i.capitalize())        
    return (capitalizingString.join(firstLetterCapitalizedObtainedResumeText),obtainedResumeTextLowerCase,obtainedResumeTextUpperCase)
firstLetterCapitalizedText,obtainedResumeTextLowerCase,obtainedResumeTextUpperCase = CapitalizeFirstLetter(obtainedResumeText)


firstLetterCapitalizedObtainedResumeText = []
def CapitalizeFirstLetter(obtainedResumeText):
    capitalizingString = " "
    obtainedResumeTextLowerCase = obtainedResumeText.lower()
    obtainedResumeTextUpperCase = obtainedResumeText.upper()
    splitListOfObtainedResumeText = obtainedResumeText.split()
    for i in splitListOfObtainedResumeText:
        firstLetterCapitalizedObtainedResumeText.append(i.capitalize())        
    return (capitalizingString.join(firstLetterCapitalizedObtainedResumeText),obtainedResumeTextLowerCase,obtainedResumeTextUpperCase)
firstLetterCapitalizedText,obtainedResumeTextLowerCase,obtainedResumeTextUpperCase = CapitalizeFirstLetter(obtainedResumeText)

#Resume educational Details Extracting Module
def EducationDetailsExtractor(obtainedResumeText):
    obtainedResumeText.strip('/n')
    newLineRemovedResumeText = obtainedResumeText    
    resumeEducationSpecificationList = {'Education':educationLevelList}

    # Create an empty list where the scores will be stored
    educationExtracted = []
    for area in resumeEducationSpecificationList.keys():
        if area == 'Education':
            educationWord = []
            for word in resumeEducationSpecificationList[area]:
                if word in obtainedResumeText:
                    educationWord.append(word)
            educationExtracted.append(educationWord)
    return educationExtracted

extractedEducatioDetails = EducationDetailsExtractor(obtainedResumeText)



def stopWordRemoval(obtainedResumeText):
    stop_words = set(stopwords.words('english')) 
    word_tokens = word_tokenize(obtainedResumeText) 
    filtered_sentence = [w for w in word_tokens if not w in stop_words] 

    filtered_sentence = [] 
    joinEmptyString = " "
    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w)
    return(joinEmptyString.join(filtered_sentence))
    
filteredTextForSkillExtraction = stopWordRemoval(obtainedResumeText)

#Resume Skill Specification Listing and Extracting Module
resumeTechnicalSkillSpecificationList = {'Front End':frontEndList,

            'Back End':backEndList, 'Machine Learning':machineLearningList,'Android Developer':androidDevelopmentList}


def ResumeSkillExtractor(resumeTechnicalSkillSpecificationList,filteredTextForSkillExtraction):
    frontend = 0
    backend = 0
    machinelearning = 0
    androiddeveloper = 0

    # Create an empty list where the scores will be stored
    skillScores = []
    skillExtracted = []


    # Obtain the scores for each area
    for area in resumeTechnicalSkillSpecificationList.keys():

        if area == 'Front End':
            frontEndWord = []
            for word in resumeTechnicalSkillSpecificationList[area]:
                if word in filteredTextForSkillExtraction:
                    frontend += 1
                    frontEndWord.append(word)
            skillExtracted.append(frontEndWord)
            skillScores.append(frontend)

        elif area == 'Back End':
            backEndWord = []
            for word in resumeTechnicalSkillSpecificationList[area]:
                if word in filteredTextForSkillExtraction:
                    backend += 1
                    backEndWord.append(word)
            skillExtracted.append(backEndWord)
            skillScores.append(backend)

        elif area == 'Machine Learning':
            machineLearningWord = []
            for word in resumeTechnicalSkillSpecificationList[area]:
                if word in filteredTextForSkillExtraction:
                    machinelearning += 1
                    machineLearningWord.append(word)
            skillExtracted.append(machineLearningWord)
            skillScores.append(machinelearning)

        elif area == 'Android Developer':
            androidDeveloperWord = []
            for word in resumeTechnicalSkillSpecificationList[area]:
                if word in filteredTextForSkillExtraction:
                    androiddeveloper += 1
                    androidDeveloperWord.append(word)
            skillExtracted.append(androidDeveloperWord)
            skillScores.append(androiddeveloper)
    return skillScores,skillExtracted
technicalSkillScore , technicalSkillExtracted = ResumeSkillExtractor(resumeTechnicalSkillSpecificationList,filteredTextForSkillExtraction)


'''Personal Details, Skills and Academic Qualification Output Display'''

dataList = {'Scores':technicalSkillScore,"Skills":technicalSkillExtracted}
softwareDevelopemtTechnicalSkills = pd.DataFrame(dataList,index=resumeTechnicalSkillSpecificationList.keys())
print("Email Address:",finalExtractedEmail)
print("Phone Number:",finalExtractedPhone)
print("Academic Qualifications:",extractedEducatioDetails)
print(softwareDevelopemtTechnicalSkills)
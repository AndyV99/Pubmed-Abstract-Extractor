from xml.etree import cElementTree as ET

# Input and Output file names
inputFileName = 'pubmed_result.xml'
outputFileName = 'output.txt'

# Initialize xml tree
tree = ET.parse(inputFileName)
root = tree.getroot()

#Array to hold abstracts as strings
texts = []

outputFile = open(outputFileName, 'w')

# Various Counters
articles = 0
noMedline = 0
noText = 0


# For each pubmed article in the file
for PubmedArticle in list(root):
    
    articles += 1
    
    # Get the medline citation for that article
    medline = PubmedArticle.find('MedlineCitation')

    #Ensure the article has a MedlineCitation
    if(type(medline) != type(None)):
        
        article = medline.find('Article')
        
        abstract = article.find('Abstract')
        
        text = abstract.find('AbstractText')
        
        if(text.text != None):
            texts.append(text.text.encode('utf-8'))
        else:
            noText +=1
    else:
        noMedline += 1

for text in texts:
    outputFile.write("%s\n" % text)

print("{0} articles in input file".format(articles))
print("{0} articles missing MedlineCitation attribute".format(noMedline))
print("{0} articles missing abstract text attribute".format(noText))

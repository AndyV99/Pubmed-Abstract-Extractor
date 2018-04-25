from xml.etree import cElementTree as ET

# Input and Output file names
inputFileName = 'pubmed_result{0}.xml'
inputFileNames = [ inputFileName.format(i) for i in range(1, 36) ]
outputFileName = 'output.txt'

#Array to hold abstracts as strings
texts = []

outputFile = open(outputFileName, 'w')

# Various Counters
articles = 0
noMedline = 0
noAbstract = 0
noText = 0

for filename in inputFileNames:
    # Initialize xml tree
    tree = ET.parse(filename)
    root = tree.getroot()

    # For each pubmed article in the file
    for PubmedArticle in list(root):
    
        articles += 1
    
        # Get the medline citation for that article
        medline = PubmedArticle.find('MedlineCitation')

        #Ensure the article has a MedlineCitation
        if(medline != None):
        
            article = medline.find('Article')
            
            abstract = article.find('Abstract')
            if(abstract != None):
                text = abstract.find('AbstractText')
        
                if(text.text != None):
                    texts.append(text.text.encode('utf-8'))
                else:
                    noText += 1
            else:
                noAbstract += 1
        else:
            noMedline += 1

    for text in texts:
        outputFile.write("%s\n" % text)
    texts.clear()

print("{0} articles in input file".format(articles))
print("{0} articles missing MedlineCitation attribute".format(noMedline))
print("{0} articles missing Abstract attribute".format(noAbstract))
print("{0} articles missing AbtractText attribute".format(noText))

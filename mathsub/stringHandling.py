#math string handling


def cleanAst(inputObject):
    output = str(inputObject)
    output = output.replace('**','^')
    output = output.replace('*','')
    #input is an object
    #output is a string
    return output

def removeBrackets(inputObject):
    output = str(inputObject)
    output = output.replace('{','')
    output = output.replace('}','')
    #input is an object
    #output is a string
    return output
    
    
def appendAsterisk(i,k):
    output = ''
    if i == k:
        output = '*'
        return output
    else:
        output = ''
        return output

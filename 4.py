import sys

if __name__ == '__main__':
    if len(sys.argv)>1:
        inData = sys.argv[1].replace(",","")
        inData = inData.replace (";","")
        inData = inData.replace (".","")
        inData = inData.replace ("(","")
        inData = inData.replace (")","")
        inData = inData.replace ("\n","")
        inData = inData.replace ("\r","")
        print("\n\n",inData)
        data = list(inData.split())
        d = {}
        for v1 in data:
            if v1 not in d:
                d[v1] = 1
            else:
                d[v1] += 1
        for v2 in d:
            print(v2,"=>",d[v2])
'''
Integrating and innovating information and communication technologystrengthen and nurture high quality IT professionals. In the coming era,
the College of Information and Electrical Engineering emphasizes on thefusion of management of computer science and technology, and reinforcementof 
innovative knowledge systems as our educational goal. Our college aimsto achieve an integration of science and technology with a fusion ofvarious 
hw/sw resources. Here, we will nurture the future leaders of thise-century to master the developing trends of Internet, informationcommunication, 
digital media communication, and medical informationprocessing.
'''

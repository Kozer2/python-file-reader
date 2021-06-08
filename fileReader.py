import os

# Take in directory and create a dictionary of documents represented by word frequencies.
def create_document_dictionary(text_dir):
    all_docs = {}

    # retrieve all text files from specified directory
    files = os.listdir(text_dir)

    # walk through files and add each to our dictionary
    for cur_file in files:
        cur_path = text_dir + cur_file

        doc_dictionary = {}
        cur_doc = open(cur_path)
        cur_text = cur_doc.read()

        # walk through word by word and add frequency to dictionary
        for word in cur_text.split():
            # clean up word
            word = word.strip().lower()
            punctuation = ',.?!;:"\'()_'
            for punct in punctuation:
                word = word.replace(punct, '')

            # update word frequency in dictionary
            if(word not in doc_dictionary):
                doc_dictionary[word] = 1
            else:
                doc_dictionary[word] += 1

        cur_doc.close()

        all_docs[cur_file] = doc_dictionary


    return all_docs
        

# Compares query_doc to all documents in all_docs and returns most similar document
def find_best_doc(query_doc, all_docs):
    stoppedWordsFile = open("querywords2.txt")
    query_doc = stoppedWordsFile.read()
    query_doc = query_doc.lower().strip().split('\n') 
    print(all_docs)
   

    # walk through candidate documents and calculate similarity to query document
    for cur_doc in all_docs:
        cur_doc_dictionary = all_docs[cur_doc]
       

        # step through query document word by word
        for cur_word in query_doc:
            # check if in current candidate document, if so add frequency to our score
            if(cur_word in cur_doc_dictionary):
                print("The word " + str(cur_word) + " was found in " + str(cur_doc))
                
                
test_doc = create_document_dictionary('texts/')
find_best_doc('querywords2.txt', test_doc)               



















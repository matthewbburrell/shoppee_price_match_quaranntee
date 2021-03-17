# Shopee - Price Match Guarantee: Kaggle Completion  
## Determine if two products are the same by their images

### Main Directory/

- README.md Project Summary Document (this file)
- code/
    - 01_eda.ipynb: Notebook containing EDA
- malay_stop_words/ 
    - geonetwork-malay.txt: file containing Malay stopwords
- refence_code/
    - image_veiwer_test.py
    - rapids-cuml-tfdfvectorizer-and-knn.ipynb


### Problem Statement
Shopee is an e-commerce platform who wants to make users experience better while shopping on their site. To help shoppers on shopee, they want to use machine learning to help by automate product comparisons to insure shoppers the lowest price is guaranteed. Other potential use cases for the application are more accurate product categorization and uncover marketplace spam. 

### Executive Summary

### Data
[train/test].csv - the training set metadata. Each row contains the data for a single posting. Multiple postings might have the exact same image ID, but with different titles or vice versa.

- posting_id - the ID code for the posting.
- image - the image id/md5sum.
- image_phash - a percaptual has of the image
- title - the product description for the posting
- label_group - ID code for all postings that map to the same product. Not provided for the test set. 

[train/test]images - the images assocaited with the posting.

- posting_id - the ID code for the posting
- matches - Space delimited list of all posting IDs that match this posting. 
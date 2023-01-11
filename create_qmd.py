
import os
import yaml

content = {
'title': "Beta calibration: a well-founded and easily implemented improvement on logistic calibration for binary classifiers",
'description': 'For optimal decision making under variable class distributions and misclassification costs a classifier needs to produce well-calibrated estimates of the posterior probability. Isotonic calibration is a powerful non-parametric method that is however prone to overfitting on smaller datasets; hence a parametric method based on the logistic curve is commonly used. While logistic calibration is designed to correct for a specific kind of distortion where classifiers tend to score on too narrow a scale, we demonstrate experimentally that many classifiers including naive Bayes and Adaboost suffer from the opposite distortion where scores tend too much to the extremes.',
'image': 'https://upload.wikimedia.org/wikipedia/commons/5/59/Empty.png',
'categories': ["Calibration"] ,
'format': {
  'html':{
    'df-print': 'paged',
    'toc': True
  }
},

'params':{
  'author_1':{
    'name': 'Meelis Kull',
    'url': 'https://scholar.google.com/citations?user=yJwctG4AAAAJ&hl=en'},

  'author_2':{
    'name': 'Telmo M. Silva Filho',
    'url': 'https://scholar.google.com/citations?user=-EGO0o8AAAAJ&hl=en'},

  'author_3':{
    'name': 'Peter A. Flach',
    'url': 'https://scholar.google.com/citations?user=o9ggd4sAAAAJ&hl=en'},
  
  'author_4':{
    'name': '',
    'url': ''},
},
  'scholar_url': 'https://scholar.google.com/citations?user=o9ggd4sAAAAJ&hl=en#d=gs_md_cita-d&u=%2Fcitations%3Fview_op%3Dview_citation%26hl%3Den%26user%3Do9ggd4sAAAAJ%26cstart%3D20%26pagesize%3D80%26citation_for_view%3Do9ggd4sAAAAJ%3ARc-B-9qnGaUC%26tzom%3D-60',
  
  'pdf_url': 'http://proceedings.mlr.press/v54/kull17a.html',
  
  'poster_url': 'https://github.com/betacal/aistats2017/blob/master/aistats2017_beta_calibration_poster.pdf',

  'code_url': 'https://github.com/meeliskull/prg',

  'supplement_url': 'http://proceedings.mlr.press/v54/kull17a/kull17a-supp.pdf',

  'slides_url': 'https://github.com/betacal/aistats2017/blob/master/aistats2017_beta_calibration_slides.pdf',
}

if not os.path.exists('content/test'):
  os.makedirs('content/test/')

  with open('/home/ck22122/Documents/icr-quarto/icr/content/test/index.qmd', 'w+') as fp:
      fp.write('---\n')
      yaml.dump(content, fp)
      fp.write('\n---')

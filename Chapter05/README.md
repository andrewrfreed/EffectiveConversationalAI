# Chapter 5 companion output

Each of the subfolders in this folder contain data used in the iterative improvement cycles done in Chapter 5.

The content was generated using an open source tool called [WA Testing Tool](https://github.com/cognitive-catalyst/WA-Testing-Tool) which was developed for testing conversational AI built with Watson Assistant.

The tool process includes:
1) Create a ground truth of two columns (utterance and expected intent)
2) Test your assistant against that ground truth, creating an output file of three columns (utterance, predicted intent, expected intent)
3) Score the output file across multiple dimensions

If you do not use Watson Assistant you can still use the scripts for step 3 (you will have to build your own step 2).
There are standalone scripts for [generating intent metrics](https://github.com/cognitive-catalyst/WA-Testing-Tool/blob/master/examples/intent-metrics.md) (as score and heatmap) plus [building a confusion matrix](https://github.com/cognitive-catalyst/WA-Testing-Tool/blob/master/examples/confusion-matrix.md)

Note the progression through the subfolders as the iterations improve the accuracy of the assistant!

# PaddleOCR VietOCR for Vietnamese Texts
Ongoing Project

This is a project about Optical Character Recognition (OCR) in Vietnamese texts by using PaddleOCR and VietOCR.

# Outline
1. Text Detection
2. Text Recognition
3. OCR Error Correction

# Text Dectection
In the Text Dectection task, I used [DB algorithm](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/doc/doc_en/algorithm_det_db_en.md) in the [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) framework to localization texts in the input image. To improve the accuracy of Text Recognition, I padded images croped by DB algorithm.
# Text Recognition
For Text Recognitionm part, I used [VietOCR](https://github.com/pbcquoc/vietocr)-a popular framework for Vietnamese OCR task, baseded on Transformer OCR architecture.

# OCR Error Correction
In the OCR Error Correction, I used [VietnameseOcrCorrection](https://github.com/buiquangmanhhp1999/VietnameseOcrCorrection) framework to correct texts in the output of Text Recognition task.

# References
* [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
* [VietOCR](https://github.com/pbcquoc/vietocr])
* [VietnameseOcrCorrection](https://github.com/buiquangmanhhp1999/VietnameseOcrCorrection)

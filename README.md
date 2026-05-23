# House of Cards video/photo to ASCII generator

[Radiohead - House of Cards](https://youtu.be/8nTFjVm9sTQ?si=FyQgqJ9K2NxlGfbK)

![House of Cards image 1](https://rfmfuyylmr.ufs.sh/f/gqVzWdKR2bsiqcge0jJvObPDLd6rVhc8psGR7za5QwTEyHNU)

![House of Cards image 2](https://rfmfuyylmr.ufs.sh/f/gqVzWdKR2bsii0IE5UqZTCI2JrkXG8pb3AmRvLxDjaVWwyHl)

![House of Cards image 3](https://rfmfuyylmr.ufs.sh/f/gqVzWdKR2bsi74KFISUsdvqDJXbFKLRNZf13QrknOhelA76m)


This project was inspired by [Radiohead - House of Cards](https://youtu.be/8nTFjVm9sTQ?si=FyQgqJ9K2NxlGfbK). I had seen quite a few similar projects, of using python to convert videos and photos to ASCII art but I decided to write my own because i thought it would be fun. 

I usde the [algorithm for converting the pixels to strings based on their luminosity](https://stevendkay.wordpress.com/2009/09/08/generating-ascii-art-from-photographs-in-python/) by stevendkay, opencv2 and pillow library to create the first version of the project. I understood that the first version posed quite a few performance issues.  

Usign AI, specifically chat gippidy 5 mini, I prompted it to suggest any improvements to the code. As much as I dislike AI and the hype around it, it suggested quite a few things that greatly improved performance. 

One of the major improvements was using numpy LUTs to convert the pixel values to ASCII characters. This proved to be much faster, less expensive and more readable than the previous version.

---

# Step-by-Step instructions (recommended)


1. Install all requirements
```bash
    pip install -r requirements.txt

```

2. Run the converter:
```bash
    py main.py
```

Enjoy!

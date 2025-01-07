# audio features extractor

Simple audio features extractor made for [CVPR 2022 - Workshop on Media Forensics](https://sites.google.com/view/mediaforensics2022/).

## Requirements

Install Python3.9.12+ and the related dependencies using:

```
pip3 install -r requirements.txt
```

## Usage

Run the `main.py` file giving as input the path of the audio that you want to extract the features.

Example:

```bash
python3 main.py "data/sample.wav"
```

The result will be a list of specific audio features saved in the file `output_features.csv`.

Feel free to re-use the feature extraction script, if you have any issues or questions about this script [open an issue](https://github.com/UNICT-Fake-Audio/fake-audio-detector/issues/new).

### Explore features via web application

These features can be explored in the main synthetic audio datasets using this [web application](https://unict-fake-audio.github.io/audio-datasets-overview/#/datasets?feature=bit_rate&system_id=A07_A19&speaker=LA_0012&feature_per_speaker=1&dataType=0&dataset=ASVSPOOF_2019_LA&algorithm=false).

## Reference

[Is synthetic voice detection research going into the right direction?](https://paperswithcode.com/paper/is-synthetic-voice-detection-research-going)

If this paper helped you in the research, please cite:

```BibTex
@inproceedings{borzi2022synthetic,
  title={Is Synthetic Voice Detection Research Going Into the Right Direction?},
  author={Borz{\`\i}, Stefano and Giudice, Oliver and Stanco, Filippo and Allegra, Dario},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={71--80},
  year={2022}
}
```

## Credits

- Stefano Borzì
- Oliver Giudice
- Dario Allegra
- Filippo Stanco

# fake-audio-detector

Simple fake audio detector made for [CVPR 2022 - Workshop on Media Forensics](https://sites.google.com/view/mediaforensics2022/).

⚠️ TODO: I have to update the models, the current ones could not work properly ⚠️, but the based logic and the feature extraction is the one described in the paper.

## Requirements

Install Python3.9.12+ and the related dependencies using:

```
pip3 install -r requirements.txt
```

## Usage

Run the `main.py` file giving as input the path of the audio that you want to check through the trained model ADC.

Example:

```bash
python3 main.py "data/sample.wav"
```

The result will be `The sample audio is fake` or `The sample audio is real`.
Feel free to re-use the feature extraction script, if you have any issues or questions about this script [open an issue](https://github.com/UNICT-Fake-Audio/fake-audio-detector/issues/new).

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

ASV_SPOOF_DATA = "data/ASVspoof_all_data.csv"

SP_FEATS_NAMES = [
    'duration', 'spectrum', 'mean_frequency', 'peak_frequency', 'frequencies_std', 'amplitudes_cum_sum', 'mode_frequency', 'median_frequency', 'frequencies_q25', 'frequencies_q75',
    'iqr', 'freqs_skewness', 'freqs_kurtosis', 'spectral_entropy', 'spectral_flatness', 'spectral_centroid', 'spectral_bandwidth', 'spectral_spread', 'spectral_rolloff', 'energy',
    'rms', 'zcr', 'spectral_mean', 'spectral_rms', 'spectral_std', 'meanfun', 'minfun', 'maxfun', 'meandom', 'mindom', 'maxdom', 'dfrange', 'modindex'
]

MEDIA_INFO_FEATURES = ['bit_rate']

SPECTRUM_FEATURES = ['mfcc', 'imfcc', 'bfcc', 'lfcc', 'lpc', 'lpcc', 'msrcc', 'ngcc', 'psrcc', 'plp', 'rplp', 'gfcc']

DROP_FEATURES = ["label", "duration", "size", "spectral_bandwidth"]

SPECTRAL_COMPLEX_VALUES = ['spectral_flatness', 'spectral_centroid', 'spectral_spread']

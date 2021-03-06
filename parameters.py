__author__ = 'jyl111'

import numpy as np

import utils


class Parameters:
    def __init__(self,
                 n=2**10,
                 k=10,
                 snr=np.inf,
                 repeat=1,
                 B_k_location=2,
                 B_k_estimation=0.2,
                 location_loops=4,
                 estimation_loops=16,
                 loop_threshold=2,
                 tolerance_location=1e-6,
                 tolerance_estimation=1e-8
                 ):
        """

        :param n: Signal size
        :param k: Signal sparsity
        :param snr: SNR ratio
        :param repeat: Number of times to repeat the experiment and the result averaged
        :param B_k_location
        :param B_k_estimation
        :param location_loops: Number of iterations to find the locations of large frequency bins
        :param estimation_loops: Number of iterations to find the values of large frequency bins
        :param loop_threshold
        :param tolerance_location
        :param tolerance_estimation
        """
        self.n = utils.floor_to_pow2(n)
        self.k = k
        self.snr = snr
        self.repeat = repeat
        self.B_k_location = B_k_location
        self.B_k_estimation = B_k_estimation
        self.location_loops = location_loops
        self.estimation_loops = estimation_loops
        self.loop_threshold = loop_threshold
        self.tolerance_location = tolerance_location
        self.tolerance_estimation = tolerance_estimation

    @property
    def total_loops(self):
        return self.location_loops + self.estimation_loops

    @property
    def BB_location(self):
        return np.floor(self.B_k_location * np.sqrt((self.n*self.k)/np.log2(self.n)))

    @property
    def BB_estimation(self):
        return np.floor(self.B_k_estimation * np.sqrt((self.n*self.k)/np.log2(self.n)))

    @property
    def lobe_fraction_location(self):
        return 0.5 / self.BB_location

    @property
    def lobe_fraction_estimation(self):
        return 0.5 / self.BB_estimation

    @property
    def b_location(self):
        return int(1.2*1.1*(self.n/self.BB_location))

    @property
    def b_estimation(self):
        return int(1.4*1.1*(self.n/self.BB_estimation))

    @property
    def B_location(self):
        return utils.floor_to_pow2(self.BB_location)

    @property
    def B_estimation(self):
        return utils.floor_to_pow2(self.BB_estimation)

    @property
    def B_threshold(self):
        return 2 * self.k

from dataclasses import dataclass


@dataclass(frozen=True)
class FreqIdx:
    freq: int
    first_idx: int


class Solution:
    def firstUniqueFreq(self, nums: list[int]) -> int:
        # O(N) - time, space
        freqs = {}  # O(N) - space
        for i, e in enumerate(nums):  # O(N) - time
            if e not in freqs:
                freqs[e] = FreqIdx(1, i)
            freqs[e] = FreqIdx(freqs[e].freq + 1, freqs[e].first_idx)

        freqs_to_int = defaultdict(list)
        for e, freqidx in freqs.items():
            freqs_to_int[freqidx.freq].append(e)

        min_idx = len(nums)
        for freq_key in freqs_to_int.keys():
            if len(freqs_to_int[freq_key]) == 1:  # unique frequency
                value = freqs_to_int[freq_key][0]
                min_idx = min(min_idx, freqs[value].first_idx)
        return -1 if min_idx == len(nums) else nums[min_idx]

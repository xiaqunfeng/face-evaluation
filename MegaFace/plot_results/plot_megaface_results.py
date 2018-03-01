# -*- coding: utf-8 -*-
"""
Created on Sat Feb 03 06:44:14 2018

@author: zhaoy
"""
import _init_paths
from plot_megaface_result import plot_megaface_result


if __name__ == '__main__':
    your_method_dirs = [
        r'../Challenge1External/facenet',
        r'../Challenge1External/SIAT_MMLAB',
    ]
    your_method_labels = [
        'facenet',
        'SIAT_MMLAB'
    ]

    probesets = ['facescrub', 'fgnet']
    # feat_ending = '_feat'

    # other_methods_dir = None
    other_methods_dir = r'../Challenge1External'
    # save_tpr_and_rank1_for_others = False
    save_tpr_and_rank1_for_others = True

    for probe_name in probesets:
        save_dir = './rlt_megaface_%s_results' % probe_name
        plot_megaface_result(your_method_dirs, your_method_labels,
                             probe_name,
                             save_dir,
                             other_methods_dir,
                             save_tpr_and_rank1_for_others
                             )

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 03 06:44:14 2018

@author: zhaoy
"""
import _init_paths
from plot_megaface_result import plot_megaface_result


if __name__ == '__main__':
    my_method_dirs = [
        r'../eval-results-idcard1M',
    ]

    my_method_labels = [
        'sphereface-1220',
    ]

    probe = 'idProbe'
    # feat_ending = '_feat'

    other_methods_dir = None
    # other_methods_dir = r'C:\zyf\dataset\megaface\Challenge1External'
    save_tpr_and_rank1_for_others = False
    # save_tpr_and_rank1_for_others = True

    save_dir = './rlt_idcard1M_%s_facex_sphere64' % probe
    plot_megaface_result(my_method_dirs, my_method_labels,
                            probe,
                            save_dir,
                            other_methods_dir,
                            save_tpr_and_rank1_for_others
                            )

import os
import argparse
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser(description="Fix Timestamp")
    parser.add_argument(
        "--input", help="",
        required=True)
    parser.add_argument(
        "--inputts", help="",
        required=True)
    return parser.parse_args()


if __name__ == "__main__":

    args = parse_args()

    print("Loading results_in")
    results_in = np.loadtxt(args.input, delimiter=',')
    num_rows, num_cols = results_in.shape
    print("Loading ts_in")
    ts_in = np.loadtxt(args.inputts, delimiter=',')
    line_idx_ts = 0

    for line_idx in range(num_rows):
        line = results_in[line_idx, :]
        line_afterfix = line
        frame_idx = line_afterfix[0]
                
        while ts_in[line_idx_ts, 0] < frame_idx:
            line_idx_ts+=1
        line_afterfix[7] = ts_in[line_idx_ts, 8]
        
        if line_idx == 0:
            results_out = line_afterfix
        else:
            results_out = np.vstack([results_out, line_afterfix])
        print("Frame %05d/%05d" % (line_idx, num_rows))

        # if line_idx == 100:
        #     break

    output_filename = os.path.splitext(args.input)[0]+"_tsfixed.txt"
    f = open(output_filename, 'w')
    for row in results_out:
        print('%d,%d,%.2f,%.2f,%.2f,%.2f,%d,%.6f,-1,-1' % (
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]), file=f)

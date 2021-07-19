import os
import argparse
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser(description="Fix Timestamp")
    parser.add_argument(
        "--input_dir", help="Path to directory",
        required=True)
    return parser.parse_args()


if __name__ == "__main__":

    args = parse_args()

    for sequence in os.listdir(args.input_dir):
        sequence_dir = os.path.join(args.input_dir, sequence)
        det_dir = os.path.join(sequence_dir, "det")
        input_file = os.path.join(det_dir, sequence)

        print("Loading results_in")
        results_in = np.loadtxt(input_file+".txt", delimiter=',')
        num_rows, num_cols = results_in.shape
        print("Loading ts_in")
        ts_in = np.loadtxt(os.path.join(det_dir, "det.txt"), delimiter=',')
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
            print("Processing %s - Frame %05d/%05d" % (sequence, line_idx, num_rows))

        output_filename = os.path.splitext(input_file)[0]+"_tsfixed.txt"
        f = open(output_filename, 'w')
        for row in results_out:
            print('%d,%d,%.2f,%.2f,%.2f,%.2f,%d,%.6f,-1,-1' % (
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]), file=f)

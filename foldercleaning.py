import os
import argparse
import shutil


def parse_args():
    parser = argparse.ArgumentParser(description="Clean folder")
    parser.add_argument(
        "--input_dir", help="Path to directory",
        required=True)
    return parser.parse_args()


if __name__ == "__main__":

    args = parse_args()

    for sequence in os.listdir(args.input_dir):
        sequence_dir = os.path.join(args.input_dir, sequence)
        det_dir = os.path.join(sequence_dir, "det")
        img_dir = os.path.join(sequence_dir, "img1")

        print("Deleting %s - img1" % sequence)
        try:
            shutil.rmtree(img_dir)
        except OSError as e:
            print("Error: %s : %s" % (img_dir, e.strerror))

        print("Deleting %s - det files" % sequence)
        try:
            os.remove(os.path.join(det_dir, "det.txt"))
            os.remove(os.path.join(det_dir, sequence + ".txt"))
            os.remove(os.path.join(det_dir, sequence + ".npy"))
        except OSError as e:
            print("Error: %s" % e.strerror)
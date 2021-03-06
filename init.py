import argparse, os
from train import train
from test import test

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--dir-path',
                        type=str,
                        default=os.getcwd() + '/DIV2K_train_HR/',
                        help='The path for DIV2K data set')

    parser.add_argument('--lr-height',
                        type=int,
                        default=64,
                        help='Height of low resolution image')

    parser.add_argument('--lr-width',
                        type=int,
                        default=64,
                        help='Width of low resolution image')

    parser.add_argument('-nc', '--number_channels',
                        choices=[1, 3],
                        default=3,
                        help='number of channels each image contains')

    parser.add_argument('-up', '--upscale-factor',
                        type=int,
                        default=4,
                        help='Upscaling factor - ratio between high and low resolution images must be product of 2')

    parser.add_argument('-glr', '--generator-lr',
                        type=float,
                        default=1e-4,
                        help='Generator learning rate')

    parser.add_argument('-dlr', '--discriminator-lr',
                        type=float,
                        default=1e-4,
                        help='Discriminator learning rate')

    parser.add_argument('-galr', '--gan-lr',
                        type=float,
                        default=1e-4,
                        help='GAN learning rate')

    parser.add_argument('-ni', '--n-images',
                        type=int,
                        default=4,
                        help='Number of presented images when testing the model')

    parser.add_argument('-epo', '--epochs',
                        type=int,
                        default=500,
                        help='Number of epochs')

    parser.add_argument('-bs', '--batch_size',
                        type=int,
                        default=16,
                        help='Batchsize value')

    parser.add_argument('-se', '--save-interval',
                        type=int,
                        default=20,
                        help='per how many epochs save the model')

    parser.add_argument('-lw', '--load-weights-path',
                        type=str,
                        default=os.getcwd(),
                        help='path to weights file which you want to load')

    parser.add_argument('--mode',
                        choices=['train', 'test'],
                        default='train',
                        help='Upscaling factor - ratio between high and low resolution images')

    FLAGS, unparsed = parser.parse_known_args()


    if FLAGS.mode.lower() == 'train':
        train(FLAGS)

    elif FLAGS.mode.lower() == 'test':
        test(FLAGS)

    else:
        raise RuntimeError('Unknown mode passed. \n mode passed should be either "train" or "test"')

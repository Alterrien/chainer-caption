#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Sample code to generate caption using beam search
'''
# comment out the below if you want to do type check. Remeber this have to be done BEFORE import chainer
# os.environ["CHAINER_TYPE_CHECK"] = "0"

import argparse

from code.CaptionGenerator import CaptionGenerator

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-g", "--gpu", default=-1, type=int, help=u"GPU ID.CPU is -1")
parser.add_argument('--vocab', default='./data/MSCOCO/mscoco_caption_train2014_processed_dic.json', type=str, help='path to the vocaburary json')
parser.add_argument('--img', default='./sample_imgs/dog.jpg', type=str, help='path to the image')
parser.add_argument('--cnn-model', type=str, default='./data/ResNet50.model', help='place of the ResNet model')
parser.add_argument('--rnn-model', type=str, default='./data/caption_model.model', help='place of the caption model')
parser.add_argument('--beam', default=3, type=int, help='beam size in beam search')
parser.add_argument('--depth', default=50, type=int, help='depth limit in beam search')
parser.add_argument('--lang', default="<sos>", type=str, help='special word to indicate the langauge or just <sos>')
parser.add_argument('--hidden', default=512, type=int, help='Hidden units in LSTM')
args = parser.parse_args()

caption_generator = CaptionGenerator(
    rnn_model_place=args.rnn_model,
    cnn_model_place=args.cnn_model,
    dictonary_place=args.vocab,
    beamsize=args.beam,
    depth_limit=args.depth,
    gpu_id=args.gpu,
    first_word=args.lang,
    hidden_dim=args.hidden
    )

captions = caption_generator.generate(args.img)
for caption in captions:
    print(" ".join(caption["sentence"]))
    print(caption["log_likelihood"])

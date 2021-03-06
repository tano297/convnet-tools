#!/usr/bin/python2.7

"""
Quick script to show an image using opencv and matplotlib because I never
remember how it is and I am too lazy to google.
"""
import argparse
import matplotlib.pyplot as plt
import cv2

def im_plt(img):
  """
    Open image and print it on screen
  """
  plt.ion()
  plt.figure()
  plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

def im_block():
  """
  Blocks thread until windows are closed
  """
  plt.show(block=True)

if __name__ == "__main__":
  parser = argparse.ArgumentParser("Takes input image and plots it")
  parser.add_argument(
    'img',
    type=str,
    help='Path for image. No default'
  )
  FLAGS, unparsed = parser.parse_known_args()

  #plot the image
  print("Opening image \'%s\'"%FLAGS.img)
  img = cv2.imread(FLAGS.img)
  im_plt(img)
  # im_plt(img) #Shows that we can open different figures and wait 4 all
  im_block()


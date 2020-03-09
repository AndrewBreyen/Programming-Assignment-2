#!/bin/bash

awk -v n=$1 '
BEGIN{
  srand();
  print n;
  for (i=0; i<n; i++) {
    x[i] = rand();
    y[i] = rand();
  }

  for (i=0; i<n; i++)
    printf "%8f %8f\n", x[i], y[i]
}' > $1.pts

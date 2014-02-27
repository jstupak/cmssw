#include "RecoJets/JetAlgorithms/interface/Bins.h"
#include <iostream>
#include <vector>
#include <cmath>

bool Bins::getBin(std::vector<int>& bins, double value, int& low, int& up){
  if(value <= bins.front() || value >= bins.back()) return false;
  std::vector<int>::iterator binUp = bins.begin() + 1;
  while(value > *binUp) ++binUp;
  low = *(binUp-1);
  up = *(binUp);
  return true;
}

int Bins::getBinNumber(std::vector<int>& bins, double value){
  if(value <= bins.front() || value >= bins.back()) return -1;
  std::vector<int>::iterator binUp = bins.begin() + 1;
  while(value > *binUp) ++binUp;
  return binUp - bins.begin() - 1;
}

void Bins::getBins_int(std::vector<int>& bins, int nBins, double xmin, double xmax, bool log){
  const double dx = (log ? std::pow((xmax/xmin), (1./(double)nBins)) : ((xmax - xmin)/(double)nBins));
  bins.push_back((int)xmin);
  double binEdge = xmin;
  for(int i = 1; i < nBins; ++i){
    if(log) binEdge *= dx;
    else binEdge += (int)dx;
    bins.push_back((int)(binEdge + 1));
  }
  bins.push_back((int)xmax);
}

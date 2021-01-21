#include <iostream>
#include <fstream>
#include <string>
#include "PhysicsTools/NanoAOD/interface/WCPoint.h"
#include "PhysicsTools/NanoAOD/interface/WCFit.h"

void test(){

  std::vector<WCPoint> vwc;
  WCFit wcfit;

  std::string line;
  std::ifstream f("test.txt");
  if(f.is_open()){
    while(std::getline(f, line)){
      TString t = TString(line);
      TString s = t(0,t.First(" "));
      TString w = t(t.First(" ")+1, t.Sizeof());
      std::cout << line << std::endl;
      WCPoint wc = WCPoint(s.Data(), w.Atof());
      vwc.push_back(wc);
    }
  }

  wcfit = WCFit(vwc, "wcfit");
  std::vector<double> coefs = wcfit.getCoefficients();
  int nCoef = coefs.size();

  f.close();
  return;
}


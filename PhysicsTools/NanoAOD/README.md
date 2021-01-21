# Start a new nanoAOD env:

    cmsrel CMSSW_10_6_8
    cd CMSSW_10_6_8/src/
    export SCRAM_ARCH=slc7_amd64_gcc700
    cmsenv
    git cms-addpkg PhysicsTools/NanoAOD
    git remote add eftfit https://github.com/GonzalezFJR/cmssw.git
    git fetch eftfit
    git checkout eftfit/fitWC_oldMiniAOD

### Or just clone the full repo:

    git clone --branch fitWC_oldMiniAOD https://github.com/GonzalezFJR/cmssw.git

### Or install nanoAOD-tools only

    cmsrel CMSSW_9_4_6_patch1
    cd CMSSW_9_4_6_patch1/src
    cmsenv
    git cms-init 
    git clone https://github.com/GonzalezFJR/nanoAOD-tools.git


# How to run the code

- Count number of evets with `countEvents.py`

- Produce nanoAOD with `NANO_ttHEFT.py` (You might need to run from `CMSSW_10_6_8/src/`)

- Run on miniAOD with `ReadMiniAODweights.py`

- Prepare env with `start.sh` or just jun
    export SCRAM_ARCH=slc7_amd64_gcc700
    cmsenv

Most of the modifications to the original code are in `PhysicsTools/NanoAOD/plugins/GenWeightsTableProducer.cc`


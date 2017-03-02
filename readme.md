

#installing Miniconda

wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

bash miniconda.sh -p miniconda

##Creating a new conda environment
conda create --name rapidsdg pandas numpy nltk

##Activating it
source activate rapidsdg

##Git cloning from a branch:
git clone https://github.com/jmmnn/Rapid_Assessment_Tools.git

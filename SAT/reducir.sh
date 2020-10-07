-x() {
    pip install python-sat[pblib,aiger]
    pip install python-sat
    pip install -U python-sat
    cd Reductor
    python reductor.py $*
}

$1 $2
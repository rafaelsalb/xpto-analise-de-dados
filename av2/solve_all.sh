SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
python $SCRIPT_DIR 1 -w -v &
python $SCRIPT_DIR 2 -w -v &
python $SCRIPT_DIR 3 -w -v &
python $SCRIPT_DIR 4 -w -v &
python $SCRIPT_DIR 5 -w -v &
python $SCRIPT_DIR 6 -w -v &
python $SCRIPT_DIR 7 -w -v &
python $SCRIPT_DIR 8 -w -v &
python $SCRIPT_DIR 9 -w -v &
python $SCRIPT_DIR 10 -w -v
wait
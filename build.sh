SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
echo "Creating virtual environment"
python3 -m venv .
echo "Activating virtual environment"
source bin/activate
echo "Installing dependencies"
pip install -r requirements.txt
echo "Ready! 'python av2' to run"
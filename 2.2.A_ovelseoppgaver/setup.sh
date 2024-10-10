#!/bin/bash
python -m venv miljo

sorurce miljo/bin/activate
pip install pyjokes

deactivate

scriptS="script.sh"

touch "$scriptS"
chmod +x "$scriptS"

echo -e "#!/bin/bash \n\nsource miljo/bin/activate \npython main.py \ndeactivate" > "$scriptS"
echo -e "\n\n\n"
./script.sh

rm setup.sh

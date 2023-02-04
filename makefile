install:
	@echo "installing Python dependencies..."
	@pip3 install -r requirements.txt --quiet
	@echo "Python dependencies installed successfully"

recomendador_precios:
	python3 -m set_prices -brand=$(brand) -model=$(model) -year=$(year) -km=$(km)
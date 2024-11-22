{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "18b8bc88-f6ab-47fd-811d-2403410aeedb",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask\n",
    "app = Flask(\"Google PlayStore Data Analysis.ipynb\")\n",
    "\n",
    "@app.route('/')\n",
    "def hello_world():\n",
    "    return 'Hello, World!'\n",
    "\n",
    "if \"Google PlayStore Data Analysis.ipynb\" =='_main_':\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "278908a9-5ba3-44a9-a047-4245f85a1ff9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

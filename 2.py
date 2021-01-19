{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "enormous-crystal",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "import time\n",
    "from pymongo import MongoClient\n",
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "aboriginal-rental",
   "metadata": {},
   "outputs": [],
   "source": [
    "db = MongoClient('mongodb://localhost:27017').usedcars"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "going-glenn",
   "metadata": {},
   "outputs": [],
   "source": [
    "Model=[]\n",
    "Year=[]\n",
    "Negociable=[]\n",
    "Price=[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "cognitive-tattoo",
   "metadata": {},
   "outputs": [],
   "source": [
    "def find_2nd(string, substring):\n",
    "    return string.find(substring, substring.find(substring)+1)\n",
    "\n",
    "def find_1st(string, substring):\n",
    "    return string.find(substring, substring.find(substring))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "handled-acrobat",
   "metadata": {},
   "outputs": [],
   "source": [
    "response = requests.get('https://ecuador.patiotuerca.com/usados/pichincha-quito/autos?type_autos_moderated=moderated')\n",
    "soup = BeautifulSoup(response.content,\"lxml\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "hungry-memphis",
   "metadata": {},
   "outputs": [],
   "source": [
    "post_model=soup.find_all(\"h4\", class_=\"bold size-h6 left\")\n",
    "for element in post_model:\n",
    "    element=str(element)\n",
    "    limpio=str(element[find_1st(element,'>')+1:find_2nd(element,'<')])\n",
    "    Model.append(limpio.strip())\n",
    "    #print(limpio.strip())\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "innocent-photography",
   "metadata": {},
   "outputs": [],
   "source": [
    "post_year=soup.find_all(\"span\", class_=\"year\")\n",
    "for element in post_year:\n",
    "    element=str(element)\n",
    "    limpio=str(element[find_1st(element,'>')+1:find_2nd(element,'<')])\n",
    "    Year.append(str(limpio.strip()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "absent-greeting",
   "metadata": {},
   "outputs": [],
   "source": [
    "post_negociable=soup.find_all(\"span\", class_=\"latam-secondary-text text-lighten-2 negotiable-txt left\")\n",
    "for element in post_year:\n",
    "    element=str(element)\n",
    "    limpio=str(element[find_1st(element,'>')+1:find_2nd(element,'<')])\n",
    "    Negociable.append(str(limpio.strip()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "marked-verification",
   "metadata": {},
   "outputs": [],
   "source": [
    "post_price=soup.find_all(\"span\", class_=\"left share-value\")\n",
    "for element in post_price:\n",
    "    element=str(element)\n",
    "    limpio=str(element[find_1st(element,'>')+1:find_2nd(element,'<')])\n",
    "    Price.append(str(limpio.strip()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "higher-ensemble",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n",
      "guardado exitosamente\n"
     ]
    }
   ],
   "source": [
    "i=0\n",
    "for j in post_model:\n",
    "    doc={}\n",
    "    id=i\n",
    "    try:\n",
    "        doc = {'model':Model[i],'year': Year[i],'negociable': Negociable[i],'price':Price[i]}\n",
    "        db.autos.insert_one(doc)\n",
    "        print(\"guardado exitosamente\")\n",
    "    except Exception as e:    \n",
    "        print(\"no se pudo grabar:\" + str(e))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dominican-makeup",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "political-message",
   "metadata": {},
   "outputs": [],
   "source": [
    "from argparse import ArgumentParser\n",
    "import requests\n",
    "import pymongo \n",
    "from pymongo.errors import ConnectionFailure\n",
    "from bson import json_util, ObjectId\n",
    "import couchdb\n",
    "import dns\n",
    "import json\n",
    "\n",
    "CLIENT = couchdb.Server('http://admin:2910@localhost:5984/')\n",
    "\n",
    "try:\n",
    "    print('cocuh connection: Success')\n",
    "except ConnectionFailure as e:\n",
    "    print('Couch connection: failed', e)\n",
    "    \n",
    "HEADERS = {\n",
    "    'Accept': 'application/json',\n",
    "    'Content-Type': 'application/json'\n",
    "}\n",
    "\n",
    "client = pymongo.MongoClient(\"mongodb+srv://esfot:esfot@cluster0.845nq.mongodb.net/xiaomi3?retryWrites=true&w=majority\")\n",
    "DBm = client.get_database('elecciones_2021')\n",
    "DBma =DBm.eleccionesgenerales20\n",
    "\n",
    "try:\n",
    "    client.admin.command('ismaster')\n",
    "    print('MongoDB Atlas connection: Success')\n",
    "except ConnectionFailure as e:\n",
    "    print('MongoDB Atlas connection: failed', e)\n",
    "    \n",
    "DBc=CLIENT['xiaomi3']\n",
    "\n",
    "for db in DBc:\n",
    "    try:\n",
    "        DBma.insert_one(DBc[db])\n",
    "        print('Data saved mongoDB Atlas')\n",
    "    except TypeError as et:\n",
    "        print('current document raised error: {}'.format(et))\n",
    "        SKIPPED.append(db)  # creating list of skipped documents for later analysis\n",
    "        continue    # continue to next document\n",
    "    except Exception as e:\n",
    "        raise e"
   ]
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

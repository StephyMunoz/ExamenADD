{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "educational-rough",
   "metadata": {},
   "outputs": [],
   "source": [
    "from facebook_scraper import get_posts\n",
    "import json\n",
    "import time\n",
    "from pymongo import MongoClient"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "breathing-mediterranean",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\program files\\python37\\lib\\site-packages\\ipykernel_launcher.py:24: DeprecationWarning: insert is deprecated. Use insert_one or insert_many instead.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "guardado exitosamente\n",
      "2\n",
      "guardado exitosamente\n",
      "3\n",
      "guardado exitosamente\n",
      "4\n",
      "guardado exitosamente\n",
      "5\n",
      "guardado exitosamente\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-426eb2237e3a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mi\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[1;32mfor\u001b[0m \u001b[0mpost\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mget_posts\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'elecciones2021'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpages\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m1000\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m     \u001b[0mi\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\facebook_scraper\\facebook_scraper.py\u001b[0m in \u001b[0;36m_generic_get_posts\u001b[1;34m(self, extract_post_fn, iter_pages_fn, page_limit, options, remove_source)\u001b[0m\n\u001b[0;32m    104\u001b[0m             \u001b[0mlogger\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Extracting posts from page %s\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mi\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    105\u001b[0m             \u001b[1;32mfor\u001b[0m \u001b[0mpost_element\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mpage\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 106\u001b[1;33m                 \u001b[0mpost\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mextract_post_fn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpost_element\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrequest_fn\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    107\u001b[0m                 \u001b[1;32mif\u001b[0m \u001b[0mremove_source\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    108\u001b[0m                     \u001b[0mpost\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'source'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\facebook_scraper\\extractors.py\u001b[0m in \u001b[0;36mextract_post\u001b[1;34m(raw_post, options, request_fn)\u001b[0m\n\u001b[0;32m     26\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     27\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mextract_post\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mraw_post\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mRawPost\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mOptions\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrequest_fn\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mRequestFunction\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m->\u001b[0m \u001b[0mPost\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 28\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0mPostExtractor\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mraw_post\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrequest_fn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mextract_post\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     29\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     30\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\facebook_scraper\\extractors.py\u001b[0m in \u001b[0;36mextract_post\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    118\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mmethod\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mmethods\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    119\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 120\u001b[1;33m                 \u001b[0mpartial_post\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmethod\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    121\u001b[0m                 \u001b[1;32mif\u001b[0m \u001b[0mpartial_post\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    122\u001b[0m                     \u001b[0mlogger\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Extract method %s didn't return anything\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmethod\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__name__\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\facebook_scraper\\extractors.py\u001b[0m in \u001b[0;36mextract_time\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    214\u001b[0m         \u001b[0mdate_element\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0melement\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'abbr'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfirst\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    215\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mdate_element\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 216\u001b[1;33m             \u001b[0mdate\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mutils\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mparse_datetime\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdate_element\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msearch\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mFalse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    217\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mdate\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    218\u001b[0m                 \u001b[1;32mreturn\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;34m'time'\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mdate\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\facebook_scraper\\utils.py\u001b[0m in \u001b[0;36mparse_datetime\u001b[1;34m(text, search)\u001b[0m\n\u001b[0;32m     98\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     99\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 100\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0mdateparser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mparse\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    101\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    102\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\dateparser\\conf.py\u001b[0m in \u001b[0;36mwrapper\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m     87\u001b[0m             \u001b[1;32mraise\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"settings can only be either dict or instance of Settings class\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     88\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 89\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     90\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mwrapper\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     91\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\dateparser\\__init__.py\u001b[0m in \u001b[0;36mparse\u001b[1;34m(date_string, date_formats, languages, locales, region, settings)\u001b[0m\n\u001b[0;32m     52\u001b[0m                                 region=region, settings=settings)\n\u001b[0;32m     53\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 54\u001b[1;33m     \u001b[0mdata\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mparser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_date_data\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdate_string\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdate_formats\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     55\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     56\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\dateparser\\date.py\u001b[0m in \u001b[0;36mget_date_data\u001b[1;34m(self, date_string, date_formats)\u001b[0m\n\u001b[0;32m    420\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mlocale\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_get_applicable_locales\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdate_string\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    421\u001b[0m             parsed_date = _DateLocaleParser.parse(\n\u001b[1;32m--> 422\u001b[1;33m                 locale, date_string, date_formats, settings=self._settings)\n\u001b[0m\u001b[0;32m    423\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mparsed_date\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    424\u001b[0m                 \u001b[0mparsed_date\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'locale'\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlocale\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mshortname\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\dateparser\\date.py\u001b[0m in \u001b[0;36mparse\u001b[1;34m(cls, locale, date_string, date_formats, settings)\u001b[0m\n\u001b[0;32m    176\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mparse\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcls\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlocale\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdate_string\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdate_formats\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msettings\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    177\u001b[0m         \u001b[0minstance\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcls\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlocale\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdate_string\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdate_formats\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msettings\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 178\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0minstance\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parse\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    179\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    180\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_parse\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\dateparser\\date.py\u001b[0m in \u001b[0;36m_parse\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    180\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_parse\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    181\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mparser_name\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_settings\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mPARSERS\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 182\u001b[1;33m             \u001b[0mdate_data\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parsers\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mparser_name\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    183\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_is_valid_date_data\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdate_data\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    184\u001b[0m                 \u001b[1;32mreturn\u001b[0m \u001b[0mdate_data\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\dateparser\\date.py\u001b[0m in \u001b[0;36m_try_freshness_parser\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    194\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_try_freshness_parser\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    195\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 196\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mfreshness_date_parser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_date_data\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_get_translated_date\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_settings\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    197\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mOverflowError\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mValueError\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    198\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\dateparser\\freshness_date_parser.py\u001b[0m in \u001b[0;36mget_date_data\u001b[1;34m(self, date_string, settings)\u001b[0m\n\u001b[0;32m    157\u001b[0m         \u001b[1;32mfrom\u001b[0m \u001b[0mdateparser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdate\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mDateData\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    158\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 159\u001b[1;33m         \u001b[0mdate\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mperiod\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mparse\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdate_string\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msettings\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    160\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mDateData\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdate_obj\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mdate\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mperiod\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mperiod\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    161\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\dateparser\\freshness_date_parser.py\u001b[0m in \u001b[0;36mparse\u001b[1;34m(self, date_string, settings)\u001b[0m\n\u001b[0;32m     93\u001b[0m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnow\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mapply_timezone\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mutc_dt\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msettings\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mTIMEZONE\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     94\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 95\u001b[1;33m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnow\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdatetime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnow\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_local_tz\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     96\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     97\u001b[0m         \u001b[0mdate\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mperiod\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parse_date\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdate_string\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msettings\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mPREFER_DATES_FROM\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\dateparser\\freshness_date_parser.py\u001b[0m in \u001b[0;36mget_local_tz\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m     41\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     42\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mget_local_tz\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 43\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mget_localzone\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     44\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     45\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mparse\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdate_string\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msettings\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\tzlocal\\win32.py\u001b[0m in \u001b[0;36mget_localzone\u001b[1;34m()\u001b[0m\n\u001b[0;32m     91\u001b[0m     \u001b[1;32mglobal\u001b[0m \u001b[0m_cache_tz\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     92\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0m_cache_tz\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 93\u001b[1;33m         \u001b[0m_cache_tz\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpytz\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtimezone\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mget_localzone_name\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     94\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     95\u001b[0m     \u001b[0mutils\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0massert_tz_offset\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0m_cache_tz\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\pytz\\__init__.py\u001b[0m in \u001b[0;36mtimezone\u001b[1;34m(zone)\u001b[0m\n\u001b[0;32m    177\u001b[0m         \u001b[1;32mraise\u001b[0m \u001b[0mUnknownTimeZoneError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mzone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    178\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 179\u001b[1;33m     \u001b[0mzone\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_case_insensitive_zone_lookup\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0m_unmunge_zone\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mzone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    180\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mzone\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32min\u001b[0m \u001b[0m_tzinfo_cache\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    181\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mzone\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mall_timezones_set\u001b[0m\u001b[1;33m:\u001b[0m  \u001b[1;31m# noqa\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\pytz\\__init__.py\u001b[0m in \u001b[0;36m_case_insensitive_zone_lookup\u001b[1;34m(zone)\u001b[0m\n\u001b[0;32m    203\u001b[0m     \u001b[1;32mglobal\u001b[0m \u001b[0m_all_timezones_lower_to_standard\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    204\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0m_all_timezones_lower_to_standard\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 205\u001b[1;33m         \u001b[0m_all_timezones_lower_to_standard\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdict\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtz\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlower\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtz\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mtz\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mall_timezones\u001b[0m\u001b[1;33m)\u001b[0m  \u001b[1;31m# noqa\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    206\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0m_all_timezones_lower_to_standard\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mzone\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlower\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mor\u001b[0m \u001b[0mzone\u001b[0m  \u001b[1;31m# noqa\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    207\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\pytz\\lazy.py\u001b[0m in \u001b[0;36m_lazy\u001b[1;34m(self, *args, **kw)\u001b[0m\n\u001b[0;32m     99\u001b[0m                 \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    100\u001b[0m                     \u001b[1;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfill_iter\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m>\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 101\u001b[1;33m                         \u001b[0mlist\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mextend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfill_iter\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    102\u001b[0m                         \u001b[1;32mfor\u001b[0m \u001b[0mmethod_name\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mcls\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_props\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    103\u001b[0m                             \u001b[0mdelattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mLazyList\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmethod_name\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\pytz\\__init__.py\u001b[0m in \u001b[0;36m<genexpr>\u001b[1;34m(.0)\u001b[0m\n\u001b[0;32m   1110\u001b[0m  'Zulu']\n\u001b[0;32m   1111\u001b[0m all_timezones = LazyList(\n\u001b[1;32m-> 1112\u001b[1;33m         tz for tz in all_timezones if resource_exists(tz))\n\u001b[0m\u001b[0;32m   1113\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1114\u001b[0m \u001b[0mall_timezones_set\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mLazySet\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mall_timezones\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\pytz\\__init__.py\u001b[0m in \u001b[0;36mresource_exists\u001b[1;34m(name)\u001b[0m\n\u001b[0;32m    119\u001b[0m             \u001b[1;31m# for the presence of the resource file on disk.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    120\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 121\u001b[1;33m         \u001b[0mopen_resource\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclose\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    122\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    123\u001b[0m     \u001b[1;32mexcept\u001b[0m \u001b[0mIOError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\program files\\python37\\lib\\site-packages\\pytz\\__init__.py\u001b[0m in \u001b[0;36mopen_resource\u001b[1;34m(name)\u001b[0m\n\u001b[0;32m    106\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mresource_stream\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    107\u001b[0m                 \u001b[1;32mreturn\u001b[0m \u001b[0mresource_stream\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0m__name__\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'zoneinfo/'\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 108\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilename\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'rb'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    109\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    110\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "db = MongoClient('mongodb://localhost:27017').elecciones2021\n",
    "\n",
    "i=1\n",
    "for post in get_posts('elecciones2021', pages=1000):\n",
    "    print(i)\n",
    "    i=i+1\n",
    "    time.sleep(5)\n",
    "    \n",
    "    id=post['post_id']\n",
    "    doc={}\n",
    "     \n",
    "    doc['id']=id\n",
    "    \n",
    "    mydate=post['time']\n",
    "    \n",
    "    try:\n",
    "        doc['texto']=post['text']\n",
    "        doc['date']=mydate.timestamp()\n",
    "        doc['likes']=post['likes']\n",
    "        doc['comments']=post['comments']\n",
    "        doc['shares']=post['shares']\n",
    "\n",
    "        doc['post_url']=post['post_url']\n",
    "        db.eleccionesgenerales.insert(doc)\n",
    "\n",
    "    \n",
    "        print(\"guardado exitosamente\")\n",
    "\n",
    "    except Exception as e:    \n",
    "        print(\"no se pudo grabar:\" + str(e))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "divided-rouge",
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

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "835c02f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import pandas_datareader.data as web\n",
    "import datetime\n",
    "\n",
    "def gather_data(data_codes, start, end = datetime.datetime.today(), freq = \"A\"):\n",
    "    i = 0\n",
    "    # dct.items() calls key and value that key points to\n",
    "    for key, val in data_codes.items():\n",
    "        if i == 0:\n",
    "            # Create dataframe for first variable, then rename column\n",
    "            df = web.DataReader(val, \"fred\", start, end).resample(freq).mean()\n",
    "            df.rename(columns = {val:key}, inplace = True) \n",
    "            i = None\n",
    "        else:\n",
    "            # If dataframe already exists, add new column\n",
    "            df[key] = web.DataReader(val, \"fred\", start, end).resample(freq).mean()\n",
    "\n",
    "    return df\n",
    "\n",
    "def bil_to_mil(series):\n",
    "    return series.mul(10**3)"
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

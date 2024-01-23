{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "initial_id",
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "outputs": [],
   "source": [
    "# prompt: financial stock repot for last 10 years from yahoo finance\n",
    "!pip install yfinance\n",
    "\n",
    "start = datetime(2023, 12, 1)\n",
    "end = datetime.now()\n",
    "stock = yf.Ticker('2370.SR')\n",
    "hist = stock.history(start=start, end=end)\n",
    "hist.to_csv('stock.csv')"
   ],
   "metadata": {
    "collapsed": false,
    "is_executing": true
   },
   "id": "565035a0fc1e488c"
  },
  {
   "cell_type": "code",
   "outputs": [],
   "source": [],
   "metadata": {
    "collapsed": false
   },
   "id": "20fecfce989955db"
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
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

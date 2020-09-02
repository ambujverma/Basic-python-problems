{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter number to how many terms generate :10\n",
      "0\n",
      "1\n",
      "1\n",
      "2\n",
      "3\n",
      "5\n",
      "8\n",
      "13\n",
      "21\n",
      "34\n"
     ]
    }
   ],
   "source": [
    "def fibonacci():\n",
    "    n = int(input(\"enter number to how many terms generate :\"))\n",
    "    if n==0:\n",
    "        print(0)\n",
    "    else:\n",
    "        x=0\n",
    "        y=1\n",
    "        print(x)\n",
    "        print(y)\n",
    "        for i in range(2,n):\n",
    "            z=(x+y)\n",
    "            x=y\n",
    "            y=z\n",
    "            print(y) \n",
    "fibonacci()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter how many terms you want to print10\n",
      "0\n",
      "1\n",
      "1\n",
      "2\n",
      "3\n",
      "5\n",
      "8\n",
      "13\n",
      "21\n",
      "34\n"
     ]
    }
   ],
   "source": [
    "def fib():\n",
    "    n = int(input('enter how many terms you want to print'))\n",
    "    \n",
    "    if n==0:\n",
    "        print(0)\n",
    "    else:\n",
    "        x=0\n",
    "        y=1\n",
    "        print(x)\n",
    "        print(y)\n",
    "        for i in range(2,n):\n",
    "            z=(x+y)\n",
    "            x=y\n",
    "            y=z\n",
    "            print(y)\n",
    "    \n",
    "fib() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 1, 8, 27]\n"
     ]
    }
   ],
   "source": [
    "# Map lambda function cube of fibonacci series\n",
    "\n",
    "cube = lambda x:x*x*x\n",
    "def fibonacci(n):\n",
    "\n",
    "    i = 1\n",
    "    if n==0:\n",
    "        fib = []\n",
    "    elif n==1:\n",
    "        fib = [0]\n",
    "    elif n==2:\n",
    "        fib = [0,1]\n",
    "    elif n>2:\n",
    "        fib = [0,1]\n",
    "        while i<(n-1):\n",
    "            fib.append(fib[i] + fib[i-1])\n",
    "            i += 1\n",
    "       \n",
    "        \n",
    "    return(fib)\n",
    "print(list(map(cube, fibonacci(5))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}


#PNG to ZWALL converter

## What is it?

A Python function that takes a PNG and x/y coordinates and outputs the string for the PutPixel method of the ZilWall contract.

## Which contract?

The ZilWall contract provides a transition PutPixels that allows you to draw on a 256x256 pixel canvas stored directly on the Zilliqa blockchain.

    transition PutPixels (pixels: List Uint64)

Contract Address (bech32):

    zil1rrnp26y7948tq26hpqncj8yvtnkuqv3vvt00au

Contract Address (base16):

    0x18e615689e2d4eb02b570827891c8c5cedc0322c


Viewblock: [https://viewblock.io/zilliqa/address/zil1rrnp26y7948tq26hpqncj8yvtnkuqv3vvt00au](https://viewblock.io/zilliqa/address/zil1rrnp26y7948tq26hpqncj8yvtnkuqv3vvt00au)


## How to interact with the blockchain?

1. Specify image file and x/y coordinates in the put\_pixel python call:

    pixstr = put_pixels("XCAD.png", 10, 80)

2. Call the python script:

    cd src/
    python3 ./zilwall.py

3. Open the [Zilliqa IDE](https://ide.zilliqa.com)

4. In the bottom left you can import a contract. The contract must be added in the base16 address format.

    0x18e615689e2d4eb02b570827891c8c5cedc0322c

5. Click on the newly imported contract and the ABI (Application Blockchain Interface) will be loaded.

6. Click on the PutPixels Transition.

7. Increase Gas Limit 25000 to 50000.

8. Copy the output of step (2.) in the pixels parameter field.

9. Click "Call transition" button in the IDE.

10. Confirm the transition in your wallet.

11. Once the transaction has been confirmed, you should see your PNG on the [Zilwall](zilwall.com)



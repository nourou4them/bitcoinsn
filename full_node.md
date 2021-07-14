## 1 - What is a full node ?
A full client, or *“full node”* is a client that stores the entire history of bitcoin transactions (every transaction by every user, ever). It’s a ***ledger***.  
It can manage the user’s wallets. It’s a ***bank***.  
It can initiate transactions directly on the bitcoin network. It’s a bank + a ***p2p node***.  
After being validated by miners, blocks are broadcasted to the network, via the full nodes. It’s a ***broadcaster***.  
  
In [John Newbery's presentation](http://diyhpl.us/wiki/transcripts/chaincode-labs/2019-06-17-john-newbery-security-models/), he said that he would call a full node:
> something that is on the block propagation network and is validating the blockchain.  

He made a difference a difference between the **block propagation network** and the **transaction relay network** which is more linked to mining nodes.
After being validated by miners, blocks are broadcasted to the network, via the full nodes.  
  
    
## 2 - What are the incentives to run a full node? 
In [The Onion Model of Blockchain Security](https://insights.deribit.com/market-research/the-onion-model-of-blockchain-security-part-1/) written by _Hasu_, the authors talked about **4 guarantees** given by the bitcoin security model: cryptographic, consensus, economic and social.  
Each one of them is a layer that protect bitcoin viability.  
We can use the same point of vue, but for the incentive.
-	**Social incentive**    
    - ***Being part of a community***  
    - ***Being part of a network*** that you contribute to strengthen  
    - ***Have your word to say (vote)*** in case of disagreement with devs or miners  
  
-	**Economic**  
    - ***Protect your financial sovereignty*** 
    - ***Being your own bank*** 
    - ***Estimate your fees***  
        - By having a mempool, on which you can find unconfirmed transactions  

-	**Consensus**  
    - ***Being an honest node*** for the peers that want to download the blockchain and are open to incoming connections.  
        - To fight *sybil attacks* (Thus, if a Sybil attacker completely surrounded a new node that was syncing from scratch, it could create some short blockchains at low heights at almost no cost, but only up to the various checkpointed blocks.). [Bitcoin Security model](https://www.coindesk.com/bitcoins-security-model-deep-dive) by Jameson Lopp  
    - ***To maintain and validate the blockchain***, with the balance, the old transactions and by adding the new ones.
	    - To fight *Byzantine Fault tolerance*
	    - We talked about it in the [Bitcoin’s Academic Pedigree](https://queue.acm.org/detail.cfm?id=3136559) paper where they said that in every distributed ledger system, there is a risk related to the state replication and the order of the state transition
	    - The solution was to enable a set of nodes to apply the same state transitions in the same order
-	**Cryptographic**
    - ***Hold your private keys***
    - ***Generate multiple addresses***, multiple identities



## 3 - Why accept incoming connections? 
You need to connect to others for the ***IBD (Initial Blockchain Download)***, to retrieve the blockchain.  
Also, it is needed to ***relay blocks*** to other peers.  
Finally, that’s how you ***retrieve unconfirmed transactions***.  
But, you can still ***protect yourself from sybil attacks*** by accepting only the DNS seeds that have been hard coded into the software.    
- Among the peers that run those seeds, you have *Pieter Wuille* and *Luke Dashjr*.  


## 4 - Costs of accepting incoming connections
-	***Memory & Storage Usage***: The blockchain require a lot of available space and some important memory for the consensus checks
-	***Bandwidth***, with the incoming transactions and blocks
-	We can receive ***spamming alerts*** from network nodes, as a DoS attack
	- There is no protection against it.
-	***Sybil attacks*** if fully surrounded by dishonest nodes
-	***Privacy***

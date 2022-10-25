# qbft-genesis-extradata

When using QBFT to start a private Quorum chain, an extraData field is required in the genesis file. 

The following explanation is copied from the [Quorum documentation](https://consensys.net/docs/goquorum/en/22.7.0/configure-and-manage/configure/consensus-protocols/qbft/).

> `extraData` - RLP encoded string with a list of validators.

However, if we simply RLP-encode a list of addresses as extraData, Quorum refuses it.

We can find the following instructions in [Hyperledger Besu documenttation](https://besu.hyperledger.org/en/22.7.0/HowTo/Configure/Consensus-Protocols/QBFT/#extra-data)

> Formally, extraData in the genesis block contains:
> 
> If using block header validator selection: `RLP([32 bytes Vanity, List<Validators>, No Vote, Round=Int(0), 0 Seals])`.
> 
> If using contract validator selection: `RLP([32 bytes Vanity, 0 Validators, No Vote, Round=Int(0), 0 Seals])`.

Combined this with the code from official [Quorum Genesis Tool](https://github.com/ConsenSys/quorum-genesis-tool/blob/master/src/lib/nodeKeys.ts#L121), finally we get a python script that generates valid extraData string.

## Usage

1. Install dependency with `pip install rlp`
2. List initial validators in a file, one line each. Either enode addresses or lowercase addresses or checksum addresses are supported. As an example:

```
enode://8536fd1b707b155e64dabd22b4f76196802c8b7ffdeeed05275705eacf39a8e39a5ed25054a082523edbc23e2bd6e311809467c1123926897404f7262104afc9@127.0.0.1:30303
enode://944bb67295fd21d7f9be9a8ed6d40d89b0fe6472038d25c60f7734280be8aaf638947d8344ac979ff73b47048c5fc2f510ef860df07181cd9e4db17451337a95@172.27.172.1:30303
0x4592c8e45706cc08b8f44b11e43cba0cfc5892cb
c5327f96ee02d7bcbc1bf1236b8c15148971e1de
0xD3CDA913DEB6F67967B99D67ACDFA1712C293601
```

3. Run the script with `python3 extraData.py <filePath>`, where `<filePath>` is the path of the file described in step 2. The extraData string will be printed to stdout.

## Compatibility

This repo is not owned by any blockchain client official, so there is currently no guarantee that the scripts here are compatible with the latest client release.

However, it has been tested to be compatible with the following clients:

```txt
Quorum 22.7.0
Quorum 22.7.2
```
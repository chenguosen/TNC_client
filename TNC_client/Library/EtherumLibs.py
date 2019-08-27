'''
Created on 2019年5月27日

@author: xiecs
'''

from web3 import Web3, HTTPProvider
import json

def queryUser(http_addr, contract_addr, abi_info, userId):
    try:
        web3 = Web3(HTTPProvider(http_addr))

        # 0x335b6192dac4ae14df258f07b8ec46e6eadfb986
        # tst_abi=[{'constant': False, 'inputs': [{'name': 'userId', 'type': 'string'}, {'name': 'userDstId', 'type': 'string'}, {'name': 'credit', 'type': 'uint256'}], 'name': 'transCredit', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'userId', 'type': 'string'}, {'name': 'credit', 'type': 'uint256'}, {'name': 'abstr', 'type': 'string'}], 'name': 'createUser', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [], 'name': 'kill', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'userId', 'type': 'string'}, {'name': 'credit', 'type': 'uint256'}], 'name': 'subtractCredit', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [{'name': 'userId', 'type': 'string'}], 'name': 'queryUser', 'outputs': [{'name': '', 'type': 'string'}, {'name': '', 'type': 'uint256'}, {'name': '', 'type': 'string'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'userId', 'type': 'string'}, {'name': 'credit', 'type': 'uint256'}], 'name': 'addCredit', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'getCount', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'anonymous': False, 'inputs': [{'indexed': False, 'name': 'userId', 'type': 'string'}, {'indexed': False, 'name': 'credit', 'type': 'uint256'}], 'name': 'eventSuccess', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'name': 'code', 'type': 'string'}, {'indexed': False, 'name': 'msg', 'type': 'string'}], 'name': 'eventError', 'type': 'event'}]
        
        # 0x2de48d370e2660e174c3ef7dfd06cce49ddcd460
        tst_abi=[{'constant': False, 'inputs': [{'name': 'userId', 'type': 'string'}, {'name': 'userDstId', 'type': 'string'}, {'name': 'credit', 'type': 'uint256'}], 'name': 'transCredit', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'userId', 'type': 'string'}, {'name': 'credit', 'type': 'uint256'}, {'name': 'abstr', 'type': 'string'}], 'name': 'createUser', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'code', 'type': 'string'}, {'name': 'msg', 'type': 'string'}], 'name': 'returnFail', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [], 'name': 'kill', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'userId', 'type': 'string'}, {'name': 'credit', 'type': 'uint256'}], 'name': 'subtractCredit', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'queryUserCount', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [{'name': 'userId', 'type': 'string'}], 'name': 'queryUser', 'outputs': [{'name': '', 'type': 'string'}, {'name': '', 'type': 'uint256'}, {'name': '', 'type': 'string'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'userId', 'type': 'string'}, {'name': 'credit', 'type': 'uint256'}], 'name': 'addCredit', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [{'name': 'begin', 'type': 'uint256'}, {'name': 'end', 'type': 'uint256'}], 'name': 'queryUserids', 'outputs': [{'name': '', 'type': 'string[]'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'userId', 'type': 'string'}], 'name': 'returnSuccess', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [], 'name': 'getAuthorize', 'outputs': [{'name': '', 'type': 'address'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'wallet', 'type': 'address'}], 'name': 'authorize', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'userId', 'type': 'string'}, {'name': 'status', 'type': 'uint256'}], 'name': 'changeStatus', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'name': '_userData', 'type': 'address'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': False, 'name': 'userId', 'type': 'string'}, {'indexed': False, 'name': 'credit', 'type': 'uint256'}], 'name': 'eventSuccess', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'name': 'code', 'type': 'string'}, {'indexed': False, 'name': 'msg', 'type': 'string'}], 'name': 'eventError', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'name': 'level', 'type': 'uint256'}, {'indexed': False, 'name': 'content', 'type': 'string'}], 'name': 'eventLog', 'type': 'event'}]
        
        # tst_abi=[{'constant': False, 'inputs': [{'name': 'userId', 'type': 'string'}, {'name': 'userDstId', 'type': 'string'}, {'name': 'credit', 'type': 'uint256'}], 'name': 'transCredit', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'userId', 'type': 'string'}, {'name': 'credit', 'type': 'uint256'}, {'name': 'abstr', 'type': 'string'}], 'name': 'createUser', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'code', 'type': 'string'}, {'name': 'msg', 'type': 'string'}], 'name': 'returnFail', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [], 'name': 'kill', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'userId', 'type': 'string'}, {'name': 'credit', 'type': 'uint256'}], 'name': 'subtractCredit', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'queryUserCount', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [{'name': 'userId', 'type': 'string'}], 'name': 'queryUser', 'outputs': [{'name': '', 'type': 'string'}, {'name': '', 'type': 'uint256'}, {'name': '', 'type': 'string'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'userId', 'type': 'string'}, {'name': 'credit', 'type': 'uint256'}], 'name': 'addCredit', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [{'name': 'begin', 'type': 'uint256'}, {'name': 'end', 'type': 'uint256'}], 'name': 'queryUserids', 'outputs': [{'name': '', 'type': 'string[]'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'userId', 'type': 'string'}], 'name': 'returnSuccess', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [], 'name': 'getAuthorize', 'outputs': [{'name': '', 'type': 'address'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'wallet', 'type': 'address'}], 'name': 'authorize', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'userId', 'type': 'string'}, {'name': 'status', 'type': 'uint256'}], 'name': 'changeStatus', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'name': '_userData', 'type': 'address'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': False, 'name': 'userId', 'type': 'string'}, {'indexed': False, 'name': 'credit', 'type': 'uint256'}], 'name': 'eventSuccess', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'name': 'code', 'type': 'string'}, {'indexed': False, 'name': 'msg', 'type': 'string'}], 'name': 'eventError', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'name': 'level', 'type': 'uint256'}, {'indexed': False, 'name': 'content', 'type': 'string'}], 'name': 'eventLog', 'type': 'event'}]

        contract_instance = web3.eth.contract(address= Web3.toChecksumAddress(contract_addr), abi=tst_abi)

        retList = contract_instance.functions.queryUser(userId).call()
        return retList
    except Exception as err:
        print(err)
        return ['', '0', '']

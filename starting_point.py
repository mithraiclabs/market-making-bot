import asyncio
from anchorpy import Program, Provider, Wallet, create_workspace, close_workspace, Idl
from solana.publickey import PublicKey
from solana.rpc.async_api import AsyncClient
import typing
import json

async def derive_option_key_from_params(
    expiration: float, quote_asset_mint: float, program_id: PublicKey, underlying_asset_mint: float, underlying_asset_per_contract: float, quote_asset_per_contract: float):

    instructions = [
        underlying_asset_mint,
        quote_asset_mint,
        underlying_asset_per_contract,
        quote_asset_per_contract,
        expiration
    ]
    authority_and_nonce: typing.Tuple[PublicKey, int] = PublicKey.find_program_address(instructions, program_id)

    return authority_and_nonce

async def find_open_orders_accounts_for_owner(program: Program, dex_program_id: PublicKey, serum_market_address: PublicKey):
    instructions = [
        b"open-orders",
        str.encode(dex_program_id),
        str.encode(serum_market_address),
        str.encode(str(program.provider.wallet.public_key))
    ]
    results: typing.Tuple[PublicKey, int] = PublicKey.find_program_address(instructions, program.program_id)
    open_orders_address_key = results[0]
    open_orders_bump = results[1]
    print(results)

    # program.provider.connection.get_program_accounts(dex_program_id, {})
#   const accounts = await program.provider.connection.getProgramAccounts(
#     dexProgramId,
    return results
#     const [openOrdersAddressKey, openOrdersBump] =
#     await PublicKey.findProgramAddress(
#       [
#         textEncoder.encode("open-orders"),
#         dexProgramId.toBuffer(),
#         serumMarketAddress.toBuffer(),
#         program.provider.wallet.publicKey.toBuffer(),
#       ],
#       program.programId
#     );
#   const filters = [
#     {
#       memcmp: {
#         offset: OpenOrders.getLayout(dexProgramId).offsetOf("market"),
#         bytes: serumMarketAddress.toBase58(),
#       },
#     },
#     {
#       memcmp: {
#         offset: OpenOrders.getLayout(dexProgramId).offsetOf("owner"),
#         bytes: openOrdersAddressKey.toBase58(),
#       },
#     },
#     {
#       dataSize: OpenOrders.getLayout(dexProgramId).span,
#     },
#   ];
#   const accounts = await program.provider.connection.getProgramAccounts(
#     dexProgramId,
#     {
#       filters,
#     }
#   );

#   return accounts.map(({ pubkey, account }) =>
#     OpenOrders.fromAccountInfo(pubkey, account, dexProgramId)
#   );
    # return None

# def initialize_market():

async def main():
    # Read the deployed program from the workspace.

    client = AsyncClient("https://psytrbhymqlkfrhudd.dev.genesysgo.net:8899")
    provider = Provider(client, Wallet.local())
    
    program_id = PublicKey("GDvqQy3FkDB2wyNwgZGp5YkmRMUmWbhNNWDMYKbLSZ5N") # psy
    f = open('idl.json')
    idl_dict = json.load(f)
    idl_obj = Idl.from_json(idl_dict)
    program = Program(idl_obj, program_id, provider)
    
    # print(program.idl)  # swap
    # authority_and_nonce = await derive_option_key_from_params(
    #     expiration=b"1630108799", quote_asset_mint=b"E6Z6zLzk8MWY3TY8E87mr88FhGowEPJTeMWzkqtL6qkF", 
    #     program_id=program_id, underlying_asset_mint=b"C6kYXcaRUMqeBF5fhg165RWU7AnpT9z92fvKNoMqjmz6",
    #     underlying_asset_per_contract=b"3500000", quote_asset_per_contract=b"1000000000")
    # # authority_and_nonce: typing.Tuple[PublicKey, int] = PublicKey.find_program_address(insts, key)
    # print(authority_and_nonce)

    dex_program_id = "DESVgJVGajEgKGXhb6XmqDHGz3VjdgP7rEVESBgxmroY"
    serum_market_address = "2fc2ZLeDDs3RoijbdAMURwCe73J2R6MRLb47VbcbWFqz"
    results = await find_open_orders_accounts_for_owner(program, dex_program_id, serum_market_address)
    print("finished")

    await program.close()

asyncio.run(main())
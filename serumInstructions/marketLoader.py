from anchorpy import Program
from solana.publickey import PublicKey

async def marketLoader(
    program: Program,
    optionMarketKey: PublicKey,
    marketAuthorityBump: int,
    dexProgramId: PublicKey,
    marketKey: PublicKey,
):

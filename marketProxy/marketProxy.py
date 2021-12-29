from solana.rpc.api import Client
from pyserum.market.async_market import Market
from solana.publickey import PublicKey


class marketProxyInstruction:
    def __init__(
        self,
        proxyProgramId: PublicKey,
        dexProgramId: PublicKey,
        market: Market,
    ) -> None:
        self._proxyProgramId = proxyProgramId
        self._dexProgramId = dexProgramId
        self._market = market

        @property
        def proxyProgramId() -> PublicKey:
            return self._proxyProgramId

    _proxyProgramId: PublicKey

    _dexProgramId: PublicKey

    _market: Market


class marketProxy:
    def __init__(self, market: Market, instruction: marketProxyInstruction) -> None:
        self._market = market
        self._instruction = instruction

        @property
        def market(self) -> Market:
            return self._market

        @property
        def instruction(self) -> marketProxyInstruction:
            return self._instruction

        @property
        def dexProgramId(self) -> PublicKey:
            return self._market.state.program_id()

        @property
        def proxyProgramId(self) -> PublicKey:
            return self._instruction.proxyProgramId()

    _market: Market


class marketProxyBuilder:
    def __init__(self) -> None:
        pass

    async def load(
        connection,
        market: PublicKey,
        dexProgramId: PublicKey,
        proxyProgramId: PublicKey,
    ):
        MARKET_CLIENT = await Market.load(connection, market, dexProgramId)
        INSTRUCTION = marketProxyInstruction(
            proxyProgramId, dexProgramId, MARKET_CLIENT
        )
        return marketProxy(MARKET_CLIENT, INSTRUCTION)

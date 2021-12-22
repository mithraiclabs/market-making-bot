from solana.rpc.api import Client
from pyserum.market.market import Market
from solana.publickey import PublicKey


class marketProxy:
    def __init__(self, market: Market) -> None:
        self._market = market

        @property
        def market(self):
            return self._market

    _market: Market


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

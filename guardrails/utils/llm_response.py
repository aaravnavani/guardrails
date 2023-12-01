from typing import Any, Optional

from guardrails.utils.pydantic_utils import ArbitraryModel


class LLMResponse(ArbitraryModel):
    prompt_token_count: Optional[int] = None
    response_token_count: Optional[int] = None
    output: str
    stream_output: Optional[Any] = None

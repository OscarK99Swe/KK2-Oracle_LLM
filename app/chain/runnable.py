from typing import Generic, TypeVar, Any

InputType = TypeVar("InputType")
OutputType = TypeVar("OutputType")

class Runnable(Generic[InputType, OutputType]):
    def invoke(self, input_data: InputType) -> OutputType:
        raise NotImplementedError

    def __or__(self, other: "Runnable[OutputType, Any]") -> "RunnableSequence":
        return RunnableSequence(self, other)

class RunnableSequence(Runnable[Any, Any]):
    def __init__(self, first: Runnable[Any, Any], second: Runnable[Any, Any]):
        self.first = first
        self.second = second

    def invoke(self, input_data: Any) -> Any:
        return self.second.invoke(self.first.invoke(input_data))
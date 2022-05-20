from enum import Enum
from grpc import StatusCode


class Codes(Enum):
    """
    OK: Not an error; returned on success
    CANCELLED: The operation was cancelled (typically by the caller).
    UNKNOWN: Unknown error.
    INVALID_ARGUMENT: Client specified an invalid argument.
    DEADLINE_EXCEEDED: Deadline expired before operation could complete.
    NOT_FOUND: Some requested entity (e.g., file or directory) was not found.
    ALREADY_EXISTS: Some entity that we attempted to create (e.g., file or directory)
    already exists.
    PERMISSION_DENIED: The caller does not have permission to execute the specified
    operation.
    UNAUTHENTICATED: The request does not have valid authentication credentials for the
    operation.
    RESOURCE_EXHAUSTED: Some resource has been exhausted, perhaps a per-user quota, or
    perhaps the entire file system is out of space.
    FAILED_PRECONDITION: Operation was rejected because the system is not in a state
    required for the operation's execution.
    ABORTED: The operation was aborted, typically due to a concurrency issue
    like sequencer check failures, transaction aborts, etc.
    UNIMPLEMENTED: Operation is not implemented or not supported/enabled in this service.
    INTERNAL: Internal errors.  Means some invariants expected by underlying
    system has been broken.
    UNAVAILABLE: The service is currently unavailable.
    DATA_LOSS: Unrecoverable data loss or corruption.
    """
    OK = 0
    CANCELLED = 1
    UNKNOWN = 2
    INVALID_ARGUMENT = 3
    DEADLINE_EXCEEDED = 4
    NOT_FOUND = 5
    ALREADY_EXISTS = 6
    PERMISSION_DENIED = 7
    RESOURCE_EXHAUSTED = 8
    FAILED_PRECONDITION = 9
    ABORTED = 10
    OUT_OF_RANGE = 11
    UNIMPLEMENTED = 12
    INTERNAL = 13
    UNAVAILABLE = 14
    DATA_LOSS = 15
    UNAUTHENTICATED = 16

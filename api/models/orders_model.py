from enum import Enum


class OrderType(str, Enum):
    OPEN = 'open'
    CLOSE = 'close'


class OrderStatus(str, Enum):
    REJECTED = 'rejected'
    CANCELLED = 'cancelled'
    SUBMITTED = 'submitted'
    PARTIALLY_FILLED = 'partially_filled'
    COMPLETED = 'completed'


class OrderSize(str, Enum):
    MEDIUM = 'medium'
    SMALL = 'small'



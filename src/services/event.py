import requests

from sqlalchemy import select
from core.db import session, standalone_session
from models import (
    Event,
    EventType
)
from schemas import (
    CreateEventRequest
)

from typing import List


class EventServices:
    def __init__(self):
        ...

    @standalone_session
    async def create_event(self, event_type: EventType, schema: CreateEventRequest) -> Event:
        params = schema.model_dump()
        event = Event(
            event_type=event_type,
            **params
        )
        session.add(event)
        await session.commit()
        await session.refresh(event)
        return event

    async def get_user_events(self, user_id: int) -> List[Event]:
        return (await session.execute(
            select(Event)
            .where(Event.user_id == user_id)
        )).scalars().all()

import asyncpg
from models import Event
from database import objects

async def get_active_events(*, objects):
    try:
        events = await objects.execute(Event.select().where(Event.active == True))
        return events
    except Exception as e:
        print(f"Error: {e}")
        return None

# Асинхронная функция для обновления события по id
async def update_event(event_id, name=None, description=None, is_active=None, *, objects):
    try:
        event = await objects.get(Event, Event.e_id == event_id)
        if name is not None:
            event.name = name
        if description is not None:
            event.description = description
        if is_active is not None:
            event.active = is_active
        await objects.update(event)
        return event
    except Event.DoesNotExist:
        print(f"Event with id {event_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
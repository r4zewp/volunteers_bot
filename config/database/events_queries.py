import asyncpg
from models.Event import Event
from database import objects

async def get_active_events():
    try:
        events = await objects.execute(Event.select().where(Event.active == True))
        return events
    except Exception as e:
        print(f"Error: {e}")
        return None

# Асинхронная функция для обновления события по id
async def update_event(event_id, name=None, description=None, is_active=None):
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
    
    # Асинхронная функция для создания нового события
async def create_event(event_info: dict):
    try:
        event = await objects.create(
            Event,
            name=event_info['name'],
            description=event_info['description'],
            start_date=event_info['start_date'],
            end_date=event_info['end_date'],
            location=event_info['location'],
            credits_amount=event_info['credits_amount'],
            organization=event_info['organization'],
            hours_amount=event_info['hours_amount'],
            part_format=event_info['part_format'],
            active=event_info.get('active', True)  # по умолчанию активное
        )
        return event
    except Exception as e:
        print(f"Error: {e}")
        return None
import asyncpg
from models.User import User
from models.Volunteer import Volunteer
from models.Volunteer_X_Event import Volunteer_X_Event
from models.Event import Event
from user_queries import get_user_by_id
from database import objects

async def create_volunteer_x_event(volunteer_id, event_id):
    try:
        volunteer = await objects.get(Volunteer, Volunteer.v_id == volunteer_id)
        event = await objects.get(Event, Event.e_id == event_id)
        volunteer_x_event = await objects.create(
            Volunteer_X_Event,
            volunteer=volunteer,
            event=event,
            hours_credited=0
        )
        return volunteer_x_event
    except Volunteer.DoesNotExist:
        print(f"Volunteer with id {volunteer_id} does not exist.")
        return None
    except Event.DoesNotExist:
        print(f"Event with id {event_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
# Асинхронная функция для подтверждения волонтера на событии
async def approve_volunteer_on_event(vxe_id):
    try:
        volunteer_x_event = await objects.get(Volunteer_X_Event, Volunteer_X_Event.vxe_id == vxe_id)
        volunteer_x_event.approved = True
        await objects.update(volunteer_x_event)
        return volunteer_x_event
    except Volunteer_X_Event.DoesNotExist:
        print(f"Volunteer_X_Event with ID {vxe_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
# Асинхронная функция для изменения значения свойства hours_credited
async def update_hours_credited(vxe_id, new_hours_credited):
    try:
        volunteer_x_event = await objects.get(Volunteer_X_Event, Volunteer_X_Event.vxe_id == vxe_id)
        volunteer_x_event.hours_credited = new_hours_credited
        await objects.update(volunteer_x_event)
        return volunteer_x_event
    except Volunteer_X_Event.DoesNotExist:
        print(f"Volunteer_X_Event with ID {vxe_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    
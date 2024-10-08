import asyncpg
from config.models.User import User
from config.models.Volunteer import Volunteer
from config.models.Volunteer_X_Event import Volunteer_X_Event
from config.models.Event import Event
from config.database.user_queries import get_user_by_id

async def create_volunteer_x_event(volunteer_id, event_id, objects):
    try:
        volunteer = await objects.get(Volunteer, Volunteer.v_id == volunteer_id)
        event = await objects.get(Event, Event.e_id == event_id)
        volunteer_x_event = await objects.create(
            Volunteer_X_Event,
            volunteer=volunteer,
            event=event,
            hours_credited=0,
            approved=False,
            appeared=False
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
async def approve_volunteer_on_event(vxe_id, objects):
    try:
        volunteer_x_event = await objects.get(Volunteer_X_Event, Volunteer_X_Event.id == vxe_id)
        volunteer_x_event.approved = True
        await objects.update(volunteer_x_event)
        return volunteer_x_event
    except Volunteer_X_Event.DoesNotExist:
        print(f"Volunteer_X_Event with ID {vxe_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
# Асинхронная функция для отказа волонтеру на событии
async def decline_volunteer_on_event(vxe_id, objects):
    try:
        volunteer_x_event = await objects.get(Volunteer_X_Event, Volunteer_X_Event.id == vxe_id)
        volunteer_x_event.approved = False
        await objects.update(volunteer_x_event)
        return volunteer_x_event
    except Volunteer_X_Event.DoesNotExist:
        print(f"Volunteer_X_Event with ID {vxe_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
# Асинхронная функция для изменения значения свойства hours_credited
async def update_hours_credited(vxe_id, new_hours_credited, objects):
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
    
# Асинхронная функция для подтверждения волонтера на событии
async def confirm_volunteer_appearance(vxe_id, objects):
    try:
        volunteer_x_event = await objects.get(Volunteer_X_Event, Volunteer_X_Event.vxe_id == vxe_id)
        volunteer_x_event.appeared = True
        await objects.update(volunteer_x_event)
        return volunteer_x_event
    except Volunteer_X_Event.DoesNotExist:
        print(f"Volunteer_X_Event with ID {vxe_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


# Асинхронная функция для получения всех записей Volunteer_X_Event по конкретному волонтеру
async def get_volunteer_x_events_by_volunteer(volunteer_id, objects):
    try:
        volunteer = await objects.get(Volunteer, Volunteer.v_id == volunteer_id)
        volunteer_x_events = await objects.execute(Volunteer_X_Event.select().where(Volunteer_X_Event.volunteer == volunteer))
        
        # Выводим все записи для проверки
        for vxe in volunteer_x_events:
            print(f"Volunteer_X_Event ID: {vxe.vxe_id}, Event ID: {vxe.event.e_id}, Hours Credited: {vxe.hours_credited}, Approved: {vxe.approved}, Appeared: {vxe.appeared}")

        return volunteer_x_events
    except Volunteer.DoesNotExist:
        print("Volunteer does not exist.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Асинхронная функция для получения всех записей Volunteer_X_Event, у которых appeared = True
async def get_appeared_volunteer_x_events(objects):
    try:
        volunteer_x_events = await objects.execute(Volunteer_X_Event.select().where(Volunteer_X_Event.appeared == True))
        
        # Выводим все записи для проверки
        for vxe in volunteer_x_events:
            print(f"Volunteer_X_Event ID: {vxe.vxe_id}, Volunteer ID: {vxe.volunteer.v_id}, Event ID: {vxe.event.e_id}, Hours Credited: {vxe.hours_credited}, Approved: {vxe.approved}, Appeared: {vxe.appeared}")

        return volunteer_x_events
    except Exception as e:
        print(f"Error: {e}")
        return None
    
# Асинхронная функция для проверки существования записи Volunteer_X_Event
async def check_volunteer_x_event_exists(volunteer_id, event_id):
    try:
        volunteer_x_event = await objects.get(
            Volunteer_X_Event, 
            (Volunteer_X_Event.volunteer == volunteer_id) & (Volunteer_X_Event.event == event_id)
        )
        return True
    except Volunteer_X_Event.DoesNotExist:
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
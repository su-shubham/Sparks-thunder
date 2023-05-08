from fastapi import BackgroundTasks, APIRouter

router = APIRouter()


def write_log(email, message):
    with open("./background_tasks/logs.txt", mode="w") as email_file:
        content = f"The log is created by {email} with message{message}"
        email_file.write(content)


@router.post("/send_email")
async def send_email(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, email, message="OK")
    return {"message": "Notification is process in background"}

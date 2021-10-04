from pydantic import BaseModel, Field


# -----------------------------------------------------------------------------
# MESSAGE
# -----------------------------------------------------------------------------
class Message(BaseModel):
    subject: str = Field(
        None,
        title="The target topic where the message will be published")
    body: dict = Field(None, title="The content of the message to be sent")

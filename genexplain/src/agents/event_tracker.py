from autogen import ConversableAgent

class EventTrackerAgent(ConversableAgent):
    def __init__(self, name="EventTracker", system_message="I am the Event Tracker Agent. I track and log all events.", **kwargs):
        # Initialize with the name and system message, along with other configurations
        super().__init__(name=name, system_message=system_message, **kwargs)
        self.event_log = []  # This will store the sequence of events

    def log_event(self, event):
        """Log an event with relevant details."""
        self.event_log.append(event)

    def generate_reply(self, msg):
        """Override this method to handle incoming messages and log events."""
        # Example of a basic message structure expected
        if msg.get('role') == 'system' and msg.get('content') == 'log_event':
            event_details = msg.get('event', {})
            self.log_event(event_details)
            return {"role": "system", "content": f"Event logged: {event_details}"}
        
        # If the message is something else, you can add additional conditions here
        return super().generate_reply(msg)  # Default to the base class behavior

    def get_event_log(self):
        """Method to retrieve the full event log."""
        return self.event_log

    def is_termination_msg(self, msg):
        """Override if you want to define specific termination criteria."""
        # For this agent, you might not have a termination message. Leaving this as default.
        return False

if __name__ == "__main__":
    # Example instantiation
    event_tracker = EventTrackerAgent()

    # Simulating logging an event
    event_tracker.log_event({
        "event_type": "AI_Action",
        "timestamp": "2024-08-21T10:00:00Z",
        "details": {"action": "move", "direction": "north"}
    })

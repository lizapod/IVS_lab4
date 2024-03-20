from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData


def process_agent_data(
        agent_data: AgentData,
) -> ProcessedAgentData:
    """
    Process agent data and classify the state of the road surface.
    Parameters:
        agent_data (AgentData): Agent data that containing accelerometer, GPS, and timestamp.
    Returns:
        processed_data_batch (ProcessedAgentData): Processed data containing the classified state of the road surface and agent data.
    """
    road_state = "plain"
    if agent_data.accelerometer.y < -100:
        road_state = "pit"
    elif agent_data.accelerometer.y > 100:
        road_state = "hill"
    return ProcessedAgentData(agent_data=agent_data, road_state=road_state)

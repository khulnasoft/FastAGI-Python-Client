import pytest
from unittest.mock import patch
from fastagi_client.lib.fastagi import Fastagi
from fastagi_client.types import (
    AgentConfig,
    AgentUpdateConfig,
    AgentRun,
    AgentRunFilter,
)


@pytest.fixture
def fastagi():
    return Fastagi(base_url="http://test.com", api_key="test_key")


@patch("requests.post")
def test_create_agent(mock_post, fastagi):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"id": 1}
    agent_config = AgentConfig(
        name="test",
        description="test",
        iteration_interval=1,
        model="test",
        max_iterations=1,
        goal=["goal1", "goal2"],
        instruction=["instruction1", "instruction2"],
        agent_workflow="workflow",
        constraints=["constraint1", "constraint2"],
        tools=[{"name": "tool1"}, {"name": "tool2"}],
    )
    response = fastagi.create_agent(agent_config)
    assert response == {"id": 1}


@patch("requests.put")
def test_update_agent(mock_put, fastagi):
    mock_put.return_value.status_code = 200
    mock_put.return_value.json.return_value = {"id": 1}
    agent_update_config = AgentUpdateConfig(name="test")
    response = fastagi.update_agent(1, agent_update_config)
    assert response == {"id": 1}


@patch("requests.post")
def test_pause_agent(mock_post, fastagi):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"status": "paused"}
    response = fastagi.pause_agent(1)
    assert response == {"status": "paused"}


@patch("requests.post")
def test_resume_agent(mock_post, fastagi):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"status": "resumed"}
    response = fastagi.resume_agent(1)
    assert response == {"status": "resumed"}


@patch("requests.post")
def test_create_agent_run(mock_post, fastagi):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"id": 1}
    agent_run = AgentRun(name="test")
    response = fastagi.create_agent_run(1, agent_run)
    assert response == {"id": 1}


@patch("requests.post")
def test_get_agent_run_status(mock_post, fastagi):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"status": "running"}
    agent_run_filter = AgentRunFilter(run_ids=[1])
    response = fastagi.get_agent_run_status(1, agent_run_filter)
    assert response == {"status": "running"}


@patch("requests.post")
def test_get_agent_run_resources(mock_post, fastagi):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"resources": []}
    response = fastagi.get_agent_run_resources([1])
    assert response == {"resources": []}

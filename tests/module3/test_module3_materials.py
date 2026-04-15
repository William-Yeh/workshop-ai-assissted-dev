from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MATERIALS = REPO_ROOT / "materials" / "module3"


def test_module3_new_materials_exist() -> None:
    for name in [
        "local_convention_inventory_template.md",
        "local_convention_card_template.md",
        "local_convention_trace_eval.md",
        "ai_assisted_convention_extraction_demo.md",
        "local_convention_eval_stack.md",
    ]:
        assert (MATERIALS / name).exists(), name


def test_trace_and_scope_are_documented() -> None:
    trace = (MATERIALS / "local_convention_trace_eval.md").read_text(encoding="utf-8")
    scope = (MATERIALS / "local_convention_card_template.md").read_text(encoding="utf-8")
    assert "Transferable" in trace
    assert "Repeat-backed" in trace
    assert "Signal" in scope
    assert "Proof" in scope



def test_eval_stack_mentions_violation_and_enforcement() -> None:
    stack = (MATERIALS / "local_convention_eval_stack.md").read_text(encoding="utf-8")
    assert "Violation-detection" in stack
    assert "lint / test / CI" in stack

from optuna.samplers import RandomSampler, GridSampler,\
    TPESampler, CmaEsSampler, NSGAIISampler, QMCSampler, \
    MOTPESampler


_hp_optimizers = [
    RandomSampler,
    GridSampler,
    TPESampler,
    CmaEsSampler,
    NSGAIISampler,
    QMCSampler,
    MOTPESampler,
]


def get_hp_optimizers() -> list[str]:
    return [obj.__name__ for obj in _hp_optimizers]

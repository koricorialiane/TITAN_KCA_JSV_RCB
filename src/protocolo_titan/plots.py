from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

from .ui_charts import figure_carrier_distribution, figure_cluster_map, figure_spectrum_from_arfcns


def save_doppler_plot(df: pd.DataFrame, path: Path) -> None:
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(df["speed_kmh"], df["max_doppler_hz"], marker="o")
    ax.set_xlabel("Velocidad (km/h)")
    ax.set_ylabel("Doppler máximo (Hz)")
    ax.set_title("Escenario A: efecto Doppler")
    ax.grid(True)
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


def save_coherence_plot(df: pd.DataFrame, path: Path) -> None:
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(df["speed_kmh"].astype(str), df["coherence_time_ms"])
    ax.axhline(df["gsm_timeslot_ms"].iloc[0], linestyle="--", label="Timeslot GSM")
    ax.set_xlabel("Velocidad (km/h)")
    ax.set_ylabel("Tiempo (ms)")
    ax.set_title("Tiempo de coherencia frente a timeslot GSM")
    ax.legend()
    ax.grid(True, axis="y")
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


def save_fading_plot(df: pd.DataFrame, path: Path) -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df["time_us"], df["envelope_normalized"])
    model = df["model"].iloc[0]
    doppler = df["doppler_hz"].iloc[0]
    duration_us = float(df["time_us"].iloc[-1])
    ax.set_xlabel("Tiempo dentro del timeslot (µs)")
    ax.set_ylabel("Envolvente normalizada")
    ax.set_title(f"Fading {model} durante {duration_us:.0f} µs — fD={doppler:.2f} Hz")
    ax.grid(True)
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


def save_reuse_plot(df: pd.DataFrame, path: Path) -> None:
    fig, ax = plt.subplots(figsize=(6, 4))
    cells = df["cell"]
    distances = df["reuse_distance_km"]
    ax.bar(cells, distances)
    ax.set_xlabel("Celda del clúster")
    ax.set_ylabel("Distancia de reutilización D (km)")
    ax.set_title("Escenario B: distancia de reutilización común")
    ax.grid(True, axis="y")
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


def save_noise_plot(df: pd.DataFrame, path: Path) -> None:
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(df["rbw_khz"], df["noise_floor_dbm"], marker="o")
    ax.set_xscale("log")
    ax.set_xlabel("RBW (kHz)")
    ax.set_ylabel("Suelo de ruido (dBm)")
    ax.set_title("Instrumentación: ruido integrado frente a RBW")
    ax.grid(True)
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


def save_cluster_map_plot(cluster_size: int, cell_radius_km: float, path: Path) -> None:
    fig = figure_cluster_map(cluster_size=cluster_size, cell_radius_km=cell_radius_km)
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


def save_carrier_distribution_plot(
    plan_df: pd.DataFrame,
    logical_df: pd.DataFrame,
    total_carriers: int,
    path: Path,
) -> None:
    fig = figure_carrier_distribution(plan_df, logical_df, total_carriers=total_carriers)
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


def save_spectrum_plot(logical_df: pd.DataFrame, path: Path) -> None:
    fig = figure_spectrum_from_arfcns(logical_df)
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)

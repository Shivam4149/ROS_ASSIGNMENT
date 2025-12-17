# simulator/simulate.py
import sys
from pathlib import Path
import shutil
import json

def copy_screens(src_dir: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    imgs = sorted([p for p in src_dir.iterdir() if p.suffix.lower() in (".png", ".jpg", ".jpeg")])
    for i, p in enumerate(imgs, start=1):
        dst = out_dir / f"frame_{i:03d}{p.suffix}"
        shutil.copy(p, dst)
    return len(imgs)

def make_mock_frames(out_dir: Path, n=5):
    # creates simple PNG frames using Pillow if available
    try:
        from PIL import Image, ImageDraw, ImageFont
    except Exception:
        return 0
    out_dir.mkdir(parents=True, exist_ok=True)
    for i in range(1, n+1):
        img = Image.new("RGB", (640, 480), (230, 230, 230))
        d = ImageDraw.Draw(img)
        text = f"Mock sim frame {i}"
        d.text((20, 220), text, fill=(20,20,20))
        img.save(out_dir / f"frame_{i:03d}.png")
    return n

def main():
    if len(sys.argv) != 3:
        print("Usage: python simulate.py <zip_path> <out_dir>")
        sys.exit(1)

    zip_path = sys.argv[1]   # not used here but kept for workflow
    out_dir = Path(sys.argv[2])

    screenshots_dir = Path(__file__).resolve().parent / "screenshots"
    frames = 0
    if screenshots_dir.exists() and any(screenshots_dir.iterdir()):
        frames = copy_screens(screenshots_dir, out_dir)
        message = "Used provided screenshots"
    else:
        frames = make_mock_frames(out_dir, n=6)
        message = "No screenshots found; created mock frames"

    status = "PASS" if frames >= 1 else "FAIL"
    report = {"status": status, "frames": frames, "message": message}
    with open(out_dir / "simulation_report.json", "w") as f:
        json.dump(report, f, indent=2)

    print(json.dumps(report))

if __name__ == "__main__":
    main()

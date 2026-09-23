#!/usr/bin/env python3
"""Restore Mythmon's committed Aeglet sprite assets exactly.

The polished sprites are authored assets rather than procedural placeholder art.
This script embeds the release-tested PNG bytes so running it cannot regress the
artwork or transparency.
"""
from base64 import b64decode
from pathlib import Path
import struct
import zlib

ROOT = Path(__file__).resolve().parent.parent / "assets"

ASSETS = {
    "aeglet_front.png": (
        (56, 56),
        "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",
    ),
    "aeglet_back.png": (
        (32, 32),
        "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACE0lEQVR4nM1XPUgCYRh+jAYRRwunxnCQhiMcHVoDaWhwcBaHRkGIcigRxEkQEufGBhEaXBpsc7ihSZyiSaw2ibZrkNd77+677+cy6QE5/d7vvvd5n/fHO+C/IhlPONvws6MiEYWIyT2hBJbfXzEAOEtehR4oWjclLFWAQCT8n3Z2FFDJbhWMiCgJDJaNNQk6XIRkPOHMOkXn5vZIx68+gTC0syPP9c9Akc06RaeUajqzTnGdgrvj5/V3svv3qM7XUsCqDQEA9esXAAikgn6T3QQxmZEiEOWeSInsZKNOkmFXh6UIsoLkSMYTjoxIZAK6zvmVwAlF7gIdLCZdVPKZUGKAogb8m3Vk57WxmHQD9v3cBQBXBSMFrNoQskHDbaLIOSgwpQJ8M7CaiIA7Ifm6f40UKJ/M0X9Kr9e5CpGLkIj4YbcK7tyodjG3zz0k6lVvWpQpoOgr+QzsVgGDZSMQKeBVhOTvjae4/7iUqqxdA+XTQwBuIXIig2UDdqugLFJ/9EDEOcAdWbWG1HEp1XQAIG09AFipwvHrOaDTmuScw7gNeX+rwKPkzmmdT0LjNuTwpiJIkM8CTooTMKqBsAPD7L3xFJV8JtS5MQE/+o8zAG6HiCCSfWME6HCRGuRU9XesXYSq2S6CyjmgoYDsuY4fHvVNSjsF9uun0Z7cwR4mb+/Ke5Qp0HmuM9kXGboSb+uldmP4Adv+CyjvgtJTAAAAAElFTkSuQmCC",
    ),
    "aeglet_icon.png": (
        (16, 32),
        "iVBORw0KGgoAAAANSUhEUgAAABAAAAAgCAYAAAAbifjMAAAAz0lEQVR4nGNgGPRgusnh//jkmWAMHg4uvAqRAbJaJnSJGJE2uCTMdmRXIMtjGICsCN1F6IZjGPDlxzdGZIkAnhoG59ipDAwMDAzOsVMZAnhqGBgYGBg2fGlBUcuCbmJd7SVsjmKoq73E0NSshyGOYisPB9f/c51+WA2AAaPyTSguwBoGMIX4+GS7AN0VGC5Atylj6nGcmjFcAHMFAwMDAzaXwAxHjzEMA5DxrYkRKHx09VhNwqYQr634ACl5hDZgNDuPZmdiXDGanYkANM/OAM92qWX2BpQVAAAAAElFTkSuQmCC",
    ),
}


def verify_png(data: bytes, expected_size: tuple[int, int]) -> None:
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("invalid PNG signature")
    pos = 8
    size = None
    while pos < len(data):
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        kind = data[pos + 4:pos + 8]
        payload = data[pos + 8:pos + 8 + length]
        crc = struct.unpack(">I", data[pos + 8 + length:pos + 12 + length])[0]
        actual = zlib.crc32(payload, zlib.crc32(kind)) & 0xffffffff
        if crc != actual:
            raise ValueError(f"CRC mismatch in {kind!r}")
        if kind == b"IHDR":
            size = struct.unpack(">II", payload[:8])
            if payload[9] not in (4, 6):
                raise ValueError("sprite PNG does not contain an alpha channel")
        pos += 12 + length
        if kind == b"IEND":
            break
    if size != expected_size:
        raise ValueError(f"expected {expected_size}, got {size}")


if __name__ == "__main__":
    ROOT.mkdir(parents=True, exist_ok=True)
    for name, (size, encoded) in ASSETS.items():
        data = b64decode(encoded)
        verify_png(data, size)
        (ROOT / name).write_bytes(data)
        print(f"restored {name}")

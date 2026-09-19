import os
import sys
import time
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

base_dir = 'd:/vault/code-square/04-Marketing/creatives/techno-square-case-study'

# 8K UHD Square dimensions
W, H = 7680, 7680
ART_SIZE = 5900
FEATHER_PX = 350

# Brand Palette
NAVY = (0, 31, 63)        # #001F3F
PURPLE = (168, 85, 247)   # #A855F7
GOLD = (213, 177, 130)    # #D5B182
SLATE = (90, 105, 125)    # #5A697D

# Native 8K TrueType Fonts
font_title = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 270)
font_sub = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 142)
font_sub_bold = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 142)

# Feather mask for 5900x5900
mask_feather = np.ones((ART_SIZE, ART_SIZE), dtype=np.float32)
for i in range(FEATHER_PX):
    alpha = float(i) / float(FEATHER_PX)
    mask_feather[i, :] *= alpha
    mask_feather[ART_SIZE - 1 - i, :] *= alpha
    mask_feather[:, i] *= alpha
    mask_feather[:, ART_SIZE - 1 - i] *= alpha
alpha_mask = Image.fromarray((mask_feather * 255).astype(np.uint8), mode='L')

configs = [
    {
        'id': '1a',
        'raw': 'post1_design_1a_roles_light_1789843732505.jpg',
        'out_8k': 'post1_design_1a_roles_8k.jpg',
        'out_final': 'post1_design_1a_roles_titled_final.jpg',
        'title': 'Unified Role Architecture',
        'sub_prefix': 'Techno Square Academy • ',
        'sub_highlight': 'by Code Square',
        'inpaint_rects': [[25, 25, 350, 150]] # [x1, y1, x2, y2]
    },
    {
        'id': '1b',
        'raw': 'post1_design_1b_web_light_1789843754355.jpg',
        'out_8k': 'post1_design_1b_web_8k.jpg',
        'out_final': 'post1_design_1b_web_titled_final.jpg',
        'title': 'Techno Square Web Platform',
        'sub_prefix': 'Corporate & Operations Hub • ',
        'sub_highlight': 'Engineered by Code Square',
        'inpaint_rects': []
    },
    {
        'id': '2a',
        'raw': 'post2_design_2a_access_light_1789843776607.jpg',
        'out_8k': 'post2_design_2a_access_8k.jpg',
        'out_final': 'post2_design_2a_access_titled_final.jpg',
        'title': 'The User Access Barrier',
        'sub_prefix': 'Platform Friction Analysis • ',
        'sub_highlight': 'by Code Square',
        'inpaint_rects': []
    },
    {
        'id': '2b',
        'raw': 'post2_design_2b_missed_light_1789843799067.jpg',
        'out_8k': 'post2_design_2b_missed_8k.jpg',
        'out_final': 'post2_design_2b_question_titled_final.jpg',
        'title': 'Bridging The User Disconnect',
        'sub_prefix': 'Strategic Product Evolution • ',
        'sub_highlight': 'by Code Square',
        'inpaint_rects': []
    },
    {
        'id': '3a',
        'raw': 'post3_design_3a_mobile_light_1789843895868.jpg',
        'out_8k': 'post3_design_3a_mobile_8k.jpg',
        'out_final': 'post3_design_3a_mobile_titled_final.jpg',
        'title': 'Techno Square Academy Mobile App',
        'sub_prefix': 'Instant Access & Push Notifications • ',
        'sub_highlight': 'by Code Square',
        'inpaint_rects': []
    },
    {
        'id': '3b',
        'raw': 'post3_design_3b_solution_light_1789843920241.jpg',
        'out_8k': 'post3_design_3b_solution_8k.jpg',
        'out_final': 'post3_design_3b_solution_titled_final.jpg',
        'is_dual_title': True,
        'title_parts': [
            ('SOFTWARE ', NAVY),
            ('vs. ', GOLD),
            ('SOLUTION', PURPLE)
        ],
        'sub_prefix': 'Continuous Mobile Ecosystem • ',
        'sub_highlight': 'by Code Square',
        'inpaint_rects': []
    }
]

def render_8k_image(cfg):
    t_start = time.time()
    raw_path = os.path.join(base_dir, cfg['raw'])
    print(f"\n=======================================================", flush=True)
    print(f"Processing 8K Master: {cfg['id']} ({cfg['raw']})", flush=True)
    
    cv_raw = cv2.imread(raw_path)
    if cv_raw is None:
        raise ValueError(f"Could not load image: {raw_path}")
        
    # Inpainting if specified
    if cfg.get('inpaint_rects'):
        mask = np.zeros(cv_raw.shape[:2], dtype=np.uint8)
        for r in cfg['inpaint_rects']:
            x1, y1, x2, y2 = r
            mask[y1:y2, x1:x2] = 255
        cv_clean = cv2.inpaint(cv_raw, mask, 7, cv2.INPAINT_TELEA)
    else:
        cv_clean = cv_raw

    # Bilateral edge-preserving filtering (denoise compression without edge blur)
    print("Applying bilateral edge-preserving filter...", flush=True)
    filtered_cv = cv2.bilateralFilter(cv_clean, 9, 75, 75)
    clean_pil = Image.fromarray(cv2.cvtColor(filtered_cv, cv2.COLOR_BGR2RGB))

    # High-precision Lanczos upscaling to 5900x5900
    print("Upscaling artwork to 5900x5900 with high-order Lanczos...", flush=True)
    art_8k = clean_pil.resize((ART_SIZE, ART_SIZE), Image.Resampling.LANCZOS)

    # Multi-frequency micro-contrast enhancement for 8K clarity
    print("Applying dual-frequency micro-contrast enhancement...", flush=True)
    art_8k = art_8k.filter(ImageFilter.UnsharpMask(radius=3, percent=140, threshold=2))
    art_8k = art_8k.filter(ImageFilter.UnsharpMask(radius=8, percent=45, threshold=3))

    # Calculate adaptive background gradient
    arr_art = np.array(art_8k)
    top_c = arr_art[50:150, :, :].mean(axis=(0,1))
    bot_c = arr_art[ART_SIZE-150:ART_SIZE-50, :, :].mean(axis=(0,1))

    print("Generating 8K ambient gradient canvas (7680x7680)...", flush=True)
    canvas_arr = np.zeros((H, W, 3), dtype=np.uint8)
    for y in range(H):
        t = float(y) / float(H)
        c = (1.0 - t) * top_c + t * bot_c
        canvas_arr[y, :, :] = c.astype(np.uint8)

    canvas = Image.fromarray(canvas_arr)
    art_x = int((W - ART_SIZE) / 2)
    art_y = 1520
    canvas.paste(art_8k, (art_x, art_y), mask=alpha_mask)

    # Render Native 8K Typography
    print("Rendering native 8K vector typography and accents...", flush=True)
    draw = ImageDraw.Draw(canvas)

    # Draw Title
    if cfg.get('is_dual_title'):
        total_w = sum(draw.textlength(text, font=font_title) for text, _ in cfg['title_parts'])
        cur_x = int((W - total_w) / 2)
        for text, color in cfg['title_parts']:
            draw.text((cur_x, 430), text, font=font_title, fill=color)
            cur_x += draw.textlength(text, font=font_title)
    else:
        title_text = cfg['title']
        w_title = draw.textlength(title_text, font=font_title)
        draw.text((int(W/2 - w_title/2), 430), title_text, font=font_title, fill=NAVY)

    # Draw Subtitle
    sub_p = cfg['sub_prefix']
    sub_h = cfg['sub_highlight']
    w_sp = draw.textlength(sub_p, font=font_sub)
    w_sh = draw.textlength(sub_h, font=font_sub_bold)
    w_sub = w_sp + w_sh
    start_sx = int(W/2 - w_sub/2)
    draw.text((start_sx, 800), sub_p, font=font_sub, fill=SLATE)
    draw.text((start_sx + w_sp, 800), sub_h, font=font_sub_bold, fill=PURPLE)

    # Draw Elegant Accent Line
    line_w = 640
    line_th = 14
    draw.line([(int(W/2 - line_w/2), 1100), (int(W/2 + line_w/2), 1100)], fill=PURPLE, width=line_th)

    # Save 8K Master
    p_8k = os.path.join(base_dir, cfg['out_8k'])
    p_final = os.path.join(base_dir, cfg['out_final'])
    print(f"Saving 8K master to {cfg['out_8k']} (Quality=98, 4:4:4 subsampling)...", flush=True)
    canvas.save(p_8k, quality=98, subsampling=0)
    print(f"Saving final duplicate to {cfg['out_final']}...", flush=True)
    canvas.save(p_final, quality=98, subsampling=0)

    elapsed = time.time() - t_start
    size_mb = os.path.getsize(p_8k) / (1024 * 1024)
    print(f"DONE {cfg['id']} in {elapsed:.1f}s | Dimensions: 7680x7680 | Size: {size_mb:.2f} MB", flush=True)

if __name__ == '__main__':
    print("STARTING FULL 8K MASTER PRODUCTION PIPELINE", flush=True)
    t_all = time.time()
    for cfg in configs:
        render_8k_image(cfg)
    print(f"\nALL 6 IMAGES COMPLETED IN {time.time() - t_all:.1f} SECONDS!", flush=True)

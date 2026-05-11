import gradio as gr
import yt_dlp
import os
from pathlib import Path

# シンプルなUI（Fish Speech統合は後で）
def download_audio(youtube_url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'downloaded_audio.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        return "ダウンロード完了: downloaded_audio.mp3"
    except Exception as e:
        return f"エラー: {str(e)}"

def clone_and_speak(text):
    return "現在Fish Speechの統合中です。まずは音声ダウンロードをお試しください。"

with gr.Blocks(title="YouTube Voice Clone") as demo:
    gr.Markdown("# 🎤 YouTube Voice Clone App")
    gr.Markdown("YouTubeリンクから声クローンを作ってしゃべらせましょう！")
    
    with gr.Tab("1. 音声ダウンロード"):
        url_input = gr.Textbox(label="YouTube URL", placeholder="https://youtu.be/s86TmYVh-7s")
        download_btn = gr.Button("音声をダウンロード")
        status = gr.Textbox(label="状態")
        download_btn.click(download_audio, inputs=url_input, outputs=status)
    
    with gr.Tab("2. 声でしゃべらせる"):
        text_input = gr.Textbox(label="しゃべらせたいテキスト", lines=3)
        speak_btn = gr.Button("声で再生")
        output_audio = gr.Audio(label="生成音声")
        speak_btn.click(clone_and_speak, inputs=text_input, outputs=output_audio)

if __name__ == "__main__":
    demo.launch()
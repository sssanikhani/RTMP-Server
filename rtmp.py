import subprocess

from hs_infra.utils.utils import Utils


def livestream(input_file):
    host = "0.0.0.0"
    stream_key = Utils.generate_uuid_token()
    rtmp_args = ["rtmp:/", host, "live", stream_key]
    rtmp_url = '/'.join(rtmp_args)
    command_args = [
        "ffmpeg",
        "-re",
        "-i", input_file,
        "-c", "copy",
        "-f", "flv", rtmp_url
    ]
    command = ' '.join(command_args)
    subprocess.Popen(command, shell=True)


livestream('/home/sss/Downloads/1.mp4')

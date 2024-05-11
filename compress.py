                if uploadVideo is not None:

                    input_file_content = uploadVideo.read()
                    bitrate = '800k'
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    original_filename = uploadVideo.name
                    name = f'{timestamp}_{original_filename}'
                    output_filename = f'{name}'
                    thumbnail_filename = f'{name}.jpg'  # Name for the thumbnail image
                    watermark_image = 'clickntokk1.png'  # Path to your watermark image
                    position = '10:10'

                    try:
                        with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as temp_input_file:
                            temp_input_filename = temp_input_file.name

                            temp_input_file.write(input_file_content)

                        ffmpeg_command = ['ffmpeg', '-i', temp_input_filename, '-b', bitrate, output_filename]  # for compress video
                        ffmpeg_command = ['ffmpeg', '-i', temp_input_filename, '-i', watermark_image, '-filter_complex',  # for compress video with watermark
                                          f'[0:v][1:v]overlay={position}',
                                          '-b', bitrate, output_filename
                                          ]

                        # Generate the thumbnail from the compressed video
                        ffmpeg_thumbnail_command = ['ffmpeg', '-i', temp_input_filename, '-ss', '00:00:01', '-vframes',
                                                    '1', thumbnail_filename]
                        subprocess.run(ffmpeg_thumbnail_command, check=True)
                        subprocess.run(ffmpeg_command, check=True)

                        subprocess.run(ffmpeg_command, check=True)

                        os.unlink(temp_input_filename)

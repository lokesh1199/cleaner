audioExt = ['aif', 'cda', 'midi', 'mid',
			'mp3', 'mpa', 'ogg', 'wav',
			 'wma', 'wpl' ]

archiveExt = ['7z', 'arj', 'deb', 'pkg',
			'rar', 'rpm', 'tar.gz', 'z',
			'zip']

discExt = ['bin', 'dmg', 'iso', 'toast',
			'vcd']

imageExt = ['ai' 'bmp', 'gif', 'ico',
			'jpeg', 'jpg', 'png', 'ps',
 			'psd', 'svg', 'tif', 'tiff']

videoExt = ['3g2', '3gp', 'avi', 'flv',
			'h264', 'm4v', 'mkv', 'mov',
			'mp4', 'mpg', 'mpeg', 'rm',
			'swf', 'vob', 'wmv']

documentExt = ['doc', 'odt', 'pdf','rtf',
				'tef', 'txt', 'wpd', 'docx']

appsExt = ['apk', 'xapk',]

torrentsExt = ['torrent']

encExt = ['gpg']

combined = dict(
				Audio=audioExt, Video=videoExt,
				Document=documentExt, Image=imageExt,
				Archive=archiveExt, Discs=discExt,
				Apps=appsExt, Torrents=torrentsExt,
				Encrypted=encExt,
				)

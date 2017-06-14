version=''
commithash='64db13864cb1b377c8a9ab7c08e4688d3d1f94ef'
gittag_short=''
gittag_long='64db138-dirty'
git_lastmod='Mon, 15 May 2017 14:34:53 +0200'
github_url='https://github.com/plasmodic/ecto'

breathe_default_project = 'ecto'
breathe_projects = dict(ecto='/home/arnaud.duhamel/qidata/python-ecto/build/temp.linux-x86_64-2.7/ecto/doc/../api/xml')

# for debug: this is only if you build everything locally
#ecto_module_url_root = '/home/arnaud.duhamel/qidata/python-ecto/build/temp.linux-x86_64-2.7/ecto/doc/../../doc/html/'
# for release
ecto_module_url_root = 'http://plasmodic.github.com/'

intersphinx_mapping = {
                       'ectoimagepipeline': (ecto_module_url_root + 'ecto_image_pipeline', None),
                       'ectoopenni': (ecto_module_url_root + 'ecto_openni', None),
                       'ectoopencv': (ecto_module_url_root + 'ecto_opencv', None),
                       'ectopcl': (ecto_module_url_root + 'ecto_pcl', None),
                       'ectoros': (ecto_module_url_root + 'ecto_ros', None),
                       }

programoutput_path = ''.split(';')

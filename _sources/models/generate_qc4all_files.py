import os
import subprocess

COMPILE = True

STUDIO_PATH = r"C:\Program Files (x86)\Steam\steamapps\common\Source SDK Base 2013 Singleplayer\bin\studiomdl.exe"
GAME_PATH = r"C:\Users\source-engine-slut\Desktop\source-sdk-vs2022\sp\game\mod_hl2"
FLAGS = "-nop4 -verbose -fastbuild"

basic_path = "props_sponza"
basic_material_path = None

basic_model_scale = 64

basic_qc_patt = '''\
$scale {scale}
$modelname	"{path}\{model}.mdl"
$body mybody	"{model}"

$staticprop

$cdmaterials	"models\{materials_path}"

$sequence idle	"{model}"\
'''

for file in os.listdir():
    if file.endswith( '.smd' ):
        print( file )

        model_name = file.split( '.' )[0]
        model_name_qc = model_name + '.qc'

        if not os.path.exists( './' + model_name_qc ):
            with open( './' + model_name_qc, 'w' ) as out:
                try:
                    out.write( basic_qc_patt.format(
                        scale = basic_model_scale,
                        path = basic_path,
                        materials_path = basic_path if not basic_material_path else basic_material_path,
                        model = model_name
                        )
                    )

                    print ( 'Created new QC file ' + model_name )
                except KeyError as error:
                    print( "Пизда корытом " + model_name )
        else:
            print ( 'QC file ' + model_name + ' exists. Compiling...' )

        if ( COMPILE ):

            process = subprocess.run(
                [ STUDIO_PATH,
                 '-game',
                 FLAGS,
                 model_name_qc ], capture_output=True)

            if ( process.returncode == 0 ):
                print( 'Done!' )
            else:
                print( 'Smth wrong?' )


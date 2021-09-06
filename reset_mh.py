from maya import cmds
import pymel.core as pm

cmds.currentTime( 0 )

minTime = 0 #pm.playbackOptions(q = True, minTime = True)
maxTime = pm.playbackOptions(q = True, maxTime = True)

cmds.select('FacialControls', hierarchy=True)

def reset_selected(oColl):
    trList = ['.tx','.ty','.tz','.rx','.ry','.rz']
    sList = ['.sx','.sy','.sz']

    # o is each object, x is each attribute
    for attr in [(o, x) for o in oColl for x in trList]:
        try: pm.Attribute(attr[0] + attr[1]).set(0)
        except: pass
    for attr in [(o, x) for o in oColl for x in sList]:
        try: pm.Attribute(attr[0] + attr[1]).set(1)
        except: pass

runthescipt = pm.Callback(reset_selected, pm.selected() )
runthescipt()
mySel = cmds.ls(sl=1) #my current selection

cmds.cutKey(mySel, s=True)#delete key command
cmds.select( clear=True )

#Bone_reset
cmds.select('neck_01_drv', hierarchy=True)
mySel = cmds.ls(sl=1) #my current selection
cmds.cutKey(mySel, s=True)#delete key command
cmds.select( clear=True )

cmds.confirmDialog( title='Reset Done', message='Proceed now', button=['Yes'], defaultButton='Yes', dismissString='No' )

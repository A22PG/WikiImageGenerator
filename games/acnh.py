import os
import bpy
from math import radians

def configure_lights(basis_collection):
    # Create first sun
    sun1_data = bpy.data.lights.new(name="Sun_1", type='SUN')
    sun1_object = bpy.data.objects.new(name="Sun_1", object_data=sun1_data)
    basis_collection.objects.link(sun1_object)
    sun1_object.location = (5.0, 5.0, 5.0)
    sun1_object.rotation_euler = (radians(-90), radians(15), radians(89))
    sun1_data.color = (1.0, 0.896, 0.8)
    sun1_data.energy = 5.0
    
    # Create second sun
    sun2_data = bpy.data.lights.new(name="Sun_2", type='SUN')
    sun2_object = bpy.data.objects.new(name="Sun_2", object_data=sun2_data)
    basis_collection.objects.link(sun2_object)
    sun2_object.location = (5.0, 5.0, 5.0)
    sun2_object.rotation_euler = (radians(16), radians(14), radians(3))
    sun2_data.color = (1.0, 0.896000, 0.8)
    sun2_data.energy = 2.0
    
def configure_hdri(context, node_tree, tree_nodes, node_background):
    node_environment = tree_nodes.new('ShaderNodeTexEnvironment')
    # Load and assign the image to the node property
    addon_directory = os.path.dirname(__file__)
    hdris_directory = os.path.join(addon_directory, '..', 'HDRIs')
    image_path = os.path.join(hdris_directory, "HDRIHaven_PineAttic.exr")

    node_environment.image = bpy.data.images.load(
        image_path)  # Abs path
    node_environment.location = -300, 0
    
    node_output = tree_nodes.new(type='ShaderNodeOutputWorld')
    node_output.location = 200, 0
    
    # Link nodes
    links = node_tree.links
    link = links.new(
        node_environment.outputs["Color"], node_background.inputs["Color"])
    link = links.new(
        node_background.outputs["Background"], node_output.inputs["Surface"])
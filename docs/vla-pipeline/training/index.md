# Get a model that matches your station

You do not need to train a model to finish platform setup. Use a checkpoint supplied for this arm and a matching sample dataset, then follow [Run a trained model](../inference/index.md).

## Ask for these items together

| Item | Why it matters |
|---|---|
| Checkpoint directory or authorized download location | The trained model files |
| Exact openpi configuration name and source revision | The code must load the checkpoint using the correct architecture and data mapping |
| Task description and example processed episode | A known input for the first prediction test |
| Camera identities, order, orientation, crop, and resolution | The model expects images prepared like its training images |
| Robot state/action layout and units | Joint angles, Cartesian positions/deltas, and gripper values are not interchangeable |
| Control rate and number of actions executed between predictions | These affect motion behavior |
| Normalization assets and gripper convention | Required to interpret the model's values correctly |

The inspected VLA Pipeline setup serves a custom openpi model using `pi05_droid_finetune`. This is not evidence that any checkpoint with “DROID” in its name can safely control this xArm.

## If you need to train a new model

Use [dataset preparation](../teleop/datasets.md), then work with the model owner on the lab openpi training configuration. The source includes general training examples, but the precise reproducible xArm training recipe, dataset release, and acceptance criteria have not been established by this handbook review.

Do not substitute a generic `lerobot-train` command for the lab's custom openpi workflow. Record the chosen training configuration, data revision, normalization procedure, checkpoint, and successful saved-data check as part of the model handoff.

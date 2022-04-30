using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using FMODUnity;

public class ZoneTrigger : MonoBehaviour
{
    [SerializeField]
    int zoneId_;
    [SerializeField]
    StudioEventEmitter eventEmitter_;
 
    private void OnTriggerEnter(Collider other)
    {
        eventEmitter_.EventInstance.setParameterByName("OtherZone", zoneId_);
    }
}

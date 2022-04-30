using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using FMODUnity;

public class SeePlayer : MonoBehaviour
{
    [SerializeField]
    Transform playerTr_;
    [SerializeField]
    StudioEventEmitter eventEmitter_;

    bool seeingPlayer_;
    // Start is called before the first frame update
    void Start()
    {
        seeingPlayer_ = false;
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        // Bit shift the index of the layer (8) to get a bit mask
        int layerMask = 1 << 8;

        // This would cast rays only against colliders in layer 8.
        // But instead we want to collide against everything except layer 8. The ~ operator does this, it inverts a bitmask.
        //layerMask = ~layerMask;

        RaycastHit hit;
        // Does the ray intersect any objects excluding the player layer
        if (Physics.Raycast(transform.position, playerTr_.position - transform.position, out hit, 25, layerMask) && hit.transform.gameObject.tag == "Player")
        {
            if (!seeingPlayer_)
            {
                Debug.Log("Did Hit");
                GameManager.instance.addEnemy();
                eventEmitter_.EventInstance.setParameterByName("Enemies", GameManager.instance.getEnemyNumber());
                seeingPlayer_ = true;
            }

        }
        else if (seeingPlayer_)
        {
            GameManager.instance.subtractEnemy();
            eventEmitter_.EventInstance.setParameterByName("Enemies", GameManager.instance.getEnemyNumber());
            seeingPlayer_ = false;
            Debug.Log("Didn't Hit");
        }

        Debug.DrawRay(transform.position, playerTr_.position - transform.position, Color.yellow);
    }
}

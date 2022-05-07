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
        eventEmitter_.EventInstance.setParameterByName("Health", 100.0f);
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        // Bit shift the index of the layer (8) to get a bit mask
        int layerMask = 1 << 8;

        if (seeingPlayer_)
        {
            float playerHP = playerTr_.gameObject.GetComponent<HealthBar>().subtractHP(0.1f);
            eventEmitter_.EventInstance.setParameterByName("Health", playerHP);
        }


        RaycastHit hit;
        // Does the ray intersect the player layer
        if (Physics.Raycast(transform.position, playerTr_.position - transform.position, out hit, 25, layerMask) && hit.transform.gameObject.tag == "Player")
        {
            if (!seeingPlayer_)
            {
                GameManager.instance.addEnemy();
                eventEmitter_.EventInstance.setParameterByName("Enemies", GameManager.instance.getEnemyNumber());
                seeingPlayer_ = true;
                GameManager.instance.setHeal(false);
            }

        }
        else if (seeingPlayer_)
        {
            GameManager.instance.subtractEnemy();
            eventEmitter_.EventInstance.setParameterByName("Enemies", GameManager.instance.getEnemyNumber());
            seeingPlayer_ = false;
            GameManager.instance.setHeal(true);
        }

        Debug.DrawRay(transform.position, playerTr_.position - transform.position, Color.yellow);
    }
}

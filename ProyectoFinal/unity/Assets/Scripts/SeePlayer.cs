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
    [SerializeField]
    string shotAudioPath_;

    [SerializeField]
    Material spottedMaterial_, attackMaterial_;
    Material IdleMaterial_;

    bool seeingPlayer_, matTimerRunning_;

    float shootTimer_, matTimer_, maxMatTime_ = 0.25f,
        maxDamage_ = 12.0f, minDamage_ = 6.0f;

    void Start()
    {
        seeingPlayer_ = false;
        matTimerRunning_ = false;
        eventEmitter_.EventInstance.setParameterByName("Health", 100.0f);
        IdleMaterial_ = GetComponent<Renderer>().material;
    }

    void FixedUpdate()
    {
        // Cogemos la mascara de capa del jugador
        int layerMask = 1 << 8;

        if (seeingPlayer_)
        {
            shootTimer_ -= Time.deltaTime;

            if (shootTimer_ <= 0.0f)
            {
                //Quitamos vida
                float playerHP = playerTr_.gameObject.GetComponent<HealthBar>().subtractHP(Random.Range(minDamage_, maxDamage_));
                eventEmitter_.EventInstance.setParameterByName("Health", playerHP);

                if (playerHP <= 0.0f)
                    this.enabled = false;

                shootTimer_ = Random.Range(2.0f, 5.0f);

                //Feedback auditivo
                RuntimeManager.PlayOneShot(shotAudioPath_, transform.position);

                //Feedback visual
                GetComponent<Renderer>().material = attackMaterial_;
                matTimerRunning_ = true;
                matTimer_ = maxMatTime_;
            }
        }
        if (matTimerRunning_)
        {
            matTimer_ -= Time.deltaTime;

            if (matTimer_ < 0.0f)
            {
                matTimerRunning_ = false;
                GetComponent<Renderer>().material = spottedMaterial_;
            }
        }

        RaycastHit hit;
        // Si impacta en el jugador..
        if (Physics.Raycast(transform.position, playerTr_.position - transform.position, out hit, 25, layerMask) && hit.transform.gameObject.tag == "Player")
        {
            if (!seeingPlayer_)
            {
                GameManager.instance.addEnemy();

                //Cambio de parámetro en FMOD
                eventEmitter_.EventInstance.setParameterByName("Enemies", GameManager.instance.getEnemyNumber());
                seeingPlayer_ = true;

                //Jugador no se cura automáticamente
                GameManager.instance.setHeal(false);

                //Feedback visual
                GetComponent<Renderer>().material = spottedMaterial_;

                shootTimer_ = Random.Range(2.0f, 5.0f);
            }

        }
        else if (seeingPlayer_)
        {
            //Se quita un enemigo y se actualiza variable de FMOD
            GameManager.instance.subtractEnemy();
            eventEmitter_.EventInstance.setParameterByName("Enemies", GameManager.instance.getEnemyNumber());
            seeingPlayer_ = false;

            //Jugador posiblemente se cura automáticamente
            GameManager.instance.setHeal(true);

            //Feedback visual
            GetComponent<Renderer>().material = IdleMaterial_;
            matTimerRunning_ = false;
        }
    }
}

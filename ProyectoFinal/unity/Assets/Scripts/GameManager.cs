using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameManager : MonoBehaviour
{
    public static GameManager instance;

    int enemyNumber_;
    bool canHeal_, healEnabled_;

    float maxHealTime_ = 4.0f, healTimer_;


    void Awake()
    {
        if (instance == null)
        {
            instance = this;
            DontDestroyOnLoad(this.gameObject);
        }
        else
        {
            Destroy(this.gameObject);
        }
    }
    // Start is called before the first frame update
    void Start()
    {
        enemyNumber_ = 0;
        canHeal_ = true;
        healTimer_ = maxHealTime_;
    }

    // Update is called once per frame
    void Update()
    {
        if (healEnabled_)
        {
            healTimer_ -= Time.deltaTime;

            if (healTimer_ <= 0.0f)
            {
                canHeal_ = true;
                healEnabled_ = false;
                healTimer_ = maxHealTime_;
            }
        }
        Debug.Log(healTimer_);
    }

    public void addEnemy()
    {
        enemyNumber_++;
    }
    public void subtractEnemy()
    {
        enemyNumber_--;
    }
    public int getEnemyNumber()
    {
        return enemyNumber_;
    }
    public bool canHeal()
    {
        return canHeal_;
    }
    public void setHeal(bool val)
    {
        if (val)
        {
            healTimer_ = maxHealTime_;
            healEnabled_ = true;
        }
        else
        {
            healEnabled_ = false;
            canHeal_ = false;
        }
    }   
}

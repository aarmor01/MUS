using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameManager : MonoBehaviour
{
    public static GameManager instance;

    int enemyNumber_;
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
    }

    // Update is called once per frame
    void Update()
    {
        Debug.Log(enemyNumber_);
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
}

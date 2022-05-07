using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;

public class HealthBar : MonoBehaviour
{
    public float currentHP;
    public Image HP;
    float maxHP = 100.0f;
    float healAmount_ = .125f;

    void Start()
    {
        currentHP = maxHP;
    }

    private void Update()
    {
        if (GameManager.instance.canHeal() && currentHP < maxHP)
        {
            currentHP += healAmount_;
            HP.fillAmount = currentHP / maxHP;
        }
    }

    public float subtractHP(float amount)
    {
        currentHP -= amount;
        HP.fillAmount = currentHP / maxHP;

        if (currentHP <= 0)
            GetComponent<FirstPersonAIO>().enabled = false;
        return currentHP;
        
    }
}

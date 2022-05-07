using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Rendering.PostProcessing;

public class HealthBar : MonoBehaviour
{
    public float currentHP_;
    public PostProcessProfile ppp_;
    public Image HP_;
    float maxHP_ = 100.0f;
    float healAmount_ = .125f;
    public Button resstartButt_;

    void Start()
    {
        currentHP_ = maxHP_;
        ppp_.GetSetting<Vignette>().intensity.value = 0;
    }

    private void Update()
    {
        if (GameManager.instance.canHeal() && currentHP_ < maxHP_)
        {
            currentHP_ += healAmount_;
            HP_.fillAmount = currentHP_ / maxHP_;
        }

        //Post procesado
        ppp_.GetSetting<ColorGrading>().tint.value = 100 - currentHP_;
        ppp_.GetSetting<ColorGrading>().temperature.value = 100 - currentHP_;

        if (currentHP_ < 40)
            ppp_.GetSetting<Vignette>().intensity.value = 1 - currentHP_ / 40;

        if (currentHP_ <= 0)
        {
            resstartButt_.gameObject.SetActive(true);
        }
    }

    public float subtractHP(float amount)
    {
        currentHP_ -= amount;
        HP_.fillAmount = currentHP_ / maxHP_;

        if (currentHP_ <= 0)
            GetComponent<FirstPersonAIO>().enabled = false;
        return currentHP_;

    }
}

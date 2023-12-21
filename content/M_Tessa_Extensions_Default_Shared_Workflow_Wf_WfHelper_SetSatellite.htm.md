# WfHelper.SetSatellite - метод
Сохраняет карточку-сателлит в пакете основной карточки.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetSatellite(
    	Card mainCard,
    	Card satellite
    )
VB __Копировать
     Public Shared Sub SetSatellite ( 
    	mainCard As Card,
    	satellite As Card
    )
C++ __Копировать
     public:
    static void SetSatellite(
    	Card^ mainCard, 
    	Card^ satellite
    )
F# __Копировать
     static member SetSatellite : 
            mainCard : Card * 
            satellite : Card -> unit 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Пакет основной карточки.
satellite [Card](T_Tessa_Cards_Card.htm)
    Карточка-сателлит или null, если карточка-сателлит ещё не создана.
##  __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)

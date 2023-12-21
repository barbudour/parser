# WfHelper.TryGetSatellite - метод
Возвращает карточку-сателлит, которая была установлена в пакете основной
карточки, или null, если карточка-сателлит не была установлена или была
установлена как отсутствующая.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Card TryGetSatellite(
    	Card mainCard
    )
VB __Копировать
     Public Shared Function TryGetSatellite ( 
    	mainCard As Card
    ) As Card
C++ __Копировать
     public:
    static Card^ TryGetSatellite(
    	Card^ mainCard
    )
F# __Копировать
     static member TryGetSatellite : 
            mainCard : Card -> Card 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Пакет основной карточки, в которой может быть установлена карточка-сателлит.
#### Возвращаемое значение
[Card](T_Tessa_Cards_Card.htm)  
Карточку-сателлит, которая была установлена в пакете основной карточки, или
null, если карточка-сателлит не была установлена или была установлена как
отсутствующая.
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)

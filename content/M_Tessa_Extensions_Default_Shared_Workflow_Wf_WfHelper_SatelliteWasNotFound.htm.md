# WfHelper.SatelliteWasNotFound - метод
Возвращает признак того, что карточка-сателлит была установлена как
отсутствующая в пакете основной карточки.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool SatelliteWasNotFound(
    	Card mainCard
    )
VB __Копировать
     Public Shared Function SatelliteWasNotFound ( 
    	mainCard As Card
    ) As Boolean
C++ __Копировать
     public:
    static bool SatelliteWasNotFound(
    	Card^ mainCard
    )
F# __Копировать
     static member SatelliteWasNotFound : 
            mainCard : Card -> bool 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Пакет основной карточки, в которой может быть установлена карточка-сателлит.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если карточка-сателлит была установлена как отсутствующая в пакете
основной карточки; false в противном случае.
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)

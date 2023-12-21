# WfHelper.CanModifyTaskCard - метод
Возвращает признак того, что пользователь может изменять карточку-сателлит
задания.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool CanModifyTaskCard(
    	Card taskCard
    )
VB __Копировать
     Public Shared Function CanModifyTaskCard ( 
    	taskCard As Card
    ) As Boolean
C++ __Копировать
     public:
    static bool CanModifyTaskCard(
    	Card^ taskCard
    )
F# __Копировать
     static member CanModifyTaskCard : 
            taskCard : Card -> bool 
#### Параметры
taskCard [Card](T_Tessa_Cards_Card.htm)
    Карточка-сателлит задания или основная карточка. Должна содержать загруженные задания.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если пользователь может изменять карточку-сателлит задания; false в
противном случае.
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)

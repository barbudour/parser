# WfHelper.TryGetData - метод
Возвращает неструктурированную информацию по бизнес-процессам, содержащуюся в
карточке-сателлите Workflow, или null, если такая информация отсутствует в
карточке.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static WfData TryGetData(
    	Card satellite
    )
VB __Копировать
     Public Shared Function TryGetData ( 
    	satellite As Card
    ) As WfData
C++ __Копировать
     public:
    static WfData^ TryGetData(
    	Card^ satellite
    )
F# __Копировать
     static member TryGetData : 
            satellite : Card -> WfData 
#### Параметры
satellite [Card](T_Tessa_Cards_Card.htm)
    Карточка-сателлит Workflow.
#### Возвращаемое значение
[WfData](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfData.htm)  
Неструктурированная информация по бизнес-процессам, содержащаяся в карточке-
сателлите Workflow, или null, если такая информация отсутствует в карточке.
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)

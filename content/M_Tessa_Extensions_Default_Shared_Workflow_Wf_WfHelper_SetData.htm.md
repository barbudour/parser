# WfHelper.SetData - метод
Устанавливает неструктурированную информацию по бизнес-процессам для карточки-
сателлита Workflow.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetData(
    	Card satellite,
    	WfData data,
    	bool notifyFieldChanged = true
    )
VB __Копировать
     Public Shared Sub SetData ( 
    	satellite As Card,
    	data As WfData,
    	Optional notifyFieldChanged As Boolean = true
    )
C++ __Копировать
     public:
    static void SetData(
    	Card^ satellite, 
    	WfData^ data, 
    	bool notifyFieldChanged = true
    )
F# __Копировать
     static member SetData : 
            satellite : Card * 
            data : WfData * 
            ?notifyFieldChanged : bool 
    (* Defaults:
            let _notifyFieldChanged = defaultArg notifyFieldChanged true
    *)
    -> unit 
#### Параметры
satellite [Card](T_Tessa_Cards_Card.htm)
    Карточка-сателлит Workflow.
data [WfData](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfData.htm)
     Неструктурированная информация по бизнес-процессам или null, если любую такую информацию следует удалить. 
notifyFieldChanged
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
Признак того, что информация устанавливается с уведомлением об изменении поля.
Значение true рекомендуется указывать перед сохранением карточки-сателлита, а
значение false \- если потребовалось подменить информацию после создания или
загрузки карточки-сателлита.
##  __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)

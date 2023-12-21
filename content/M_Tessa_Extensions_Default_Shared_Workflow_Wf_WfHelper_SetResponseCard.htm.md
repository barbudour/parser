# WfHelper.SetResponseCard - метод
Устанавливает заданную карточку в ответе на запрос. При этом выполняется
компрессия карточки.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetResponseCard(
    	CardResponseBase response,
    	Card card
    )
VB __Копировать
     Public Shared Sub SetResponseCard ( 
    	response As CardResponseBase,
    	card As Card
    )
C++ __Копировать
     public:
    static void SetResponseCard(
    	CardResponseBase^ response, 
    	Card^ card
    )
F# __Копировать
     static member SetResponseCard : 
            response : CardResponseBase * 
            card : Card -> unit 
#### Параметры
response [CardResponseBase](T_Tessa_Cards_CardResponseBase.htm)
    Ответ на запрос, в котором устанавливается карточки.
card [Card](T_Tessa_Cards_Card.htm)
     Устанавливаемая карточки или null, если карточка удаляется из ответа на запрос. 
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)

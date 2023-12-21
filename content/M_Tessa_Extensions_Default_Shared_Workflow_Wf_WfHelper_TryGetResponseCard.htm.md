# WfHelper.TryGetResponseCard - метод
Возвращает карточку из ответа на запрос, установленную посредством метода
[SetResponseCard(CardResponseBase,
Card)](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SetResponseCard.htm),
или null, если карточка не была установлена.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Card TryGetResponseCard(
    	CardResponseBase response
    )
VB __Копировать
     Public Shared Function TryGetResponseCard ( 
    	response As CardResponseBase
    ) As Card
C++ __Копировать
     public:
    static Card^ TryGetResponseCard(
    	CardResponseBase^ response
    )
F# __Копировать
     static member TryGetResponseCard : 
            response : CardResponseBase -> Card 
#### Параметры
response [CardResponseBase](T_Tessa_Cards_CardResponseBase.htm)
    Ответ на запрос, из которого требуется получить карточку.
#### Возвращаемое значение
[Card](T_Tessa_Cards_Card.htm)  
Карточка, полученная из ответа на запрос, или null, если карточка не была
установлена.
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)

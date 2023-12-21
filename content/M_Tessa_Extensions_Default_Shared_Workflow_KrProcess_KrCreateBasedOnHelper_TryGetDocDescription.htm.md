# KrCreateBasedOnHelper.TryGetDocDescription - метод
Возвращает поле DocDescription для описания ссылки на документ, которая обычно
возвращается типовым представлением RefDocumentsLookup, или null, если в
заданной карточке отсутствуют соответствующие секции.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static string TryGetDocDescription(
    	Card card
    )
VB __Копировать
     Public Shared Function TryGetDocDescription ( 
    	card As Card
    ) As String
C++ __Копировать
     public:
    static String^ TryGetDocDescription(
    	Card^ card
    )
F# __Копировать
     static member TryGetDocDescription : 
            card : Card -> string 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой требуется получить текстовое описание для ссылки на эту карточку.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Поле DocDescription для описания ссылки на документ, которая обычно
возвращается типовым представлением RefDocumentsLookup, или null, если в
заданной карточке отсутствуют соответствующие секции.
## __См. также
#### Ссылки
[KrCreateBasedOnHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCreateBasedOnHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

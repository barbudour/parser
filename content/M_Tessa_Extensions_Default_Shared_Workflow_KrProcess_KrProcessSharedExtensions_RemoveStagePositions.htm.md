# KrProcessSharedExtensions.RemoveStagePositions - метод
Удаляет из
[Card](T_Tessa_Cards_Card.htm).[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)
информацию о позиции этапов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void RemoveStagePositions(
    	this Card card
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub RemoveStagePositions ( 
    	card As Card
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void RemoveStagePositions(
    	Card^ card
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RemoveStagePositions : 
            card : Card -> unit 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка в [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm) которой удаляется информация о позиции этапов.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [Card](T_Tessa_Cards_Card.htm). При вызове метода для экземпляра
следует опускать первый параметр. Дополнительные сведения см. в разделе
[Методы расширения (Visual Basic)](https://docs.microsoft.com/dotnet/visual-
basic/programming-guide/language-features/procedures/extension-methods) или
[Методы расширения (Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[KrProcessSharedExtensions -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

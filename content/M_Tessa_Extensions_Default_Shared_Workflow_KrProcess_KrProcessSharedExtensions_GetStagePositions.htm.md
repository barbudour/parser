# KrProcessSharedExtensions.GetStagePositions - метод
Возвращает информацию о позиции этапов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<KrStagePositionInfo> GetStagePositions(
    	this Card card
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetStagePositions ( 
    	card As Card
    ) As List(Of KrStagePositionInfo)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static List<KrStagePositionInfo^>^ GetStagePositions(
    	Card^ card
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetStagePositions : 
            card : Card -> List<KrStagePositionInfo> 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка из [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm) которой возвращается информация о позиции этапов.
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[KrStagePositionInfo](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStagePositionInfo.htm)>  
Список содержащий информацию о позиции этапов или значение по умолчанию для
типа, если её нет.
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

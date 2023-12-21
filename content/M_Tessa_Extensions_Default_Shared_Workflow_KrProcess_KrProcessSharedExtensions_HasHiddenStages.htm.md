# KrProcessSharedExtensions.HasHiddenStages - метод
Возвращает значение, показывающее, что в информации о позиции этапов
содержится информация о скрытых этапах.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool HasHiddenStages(
    	this Card card
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function HasHiddenStages ( 
    	card As Card
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool HasHiddenStages(
    	Card^ card
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member HasHiddenStages : 
            card : Card -> bool 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка в [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm) которой содержится информация о позиции этапов.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Значение, показывающее, что в информации о позиции этапов содержится
информация о скрытых этапах.
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

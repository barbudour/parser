# KrProcessSharedExtensions.GetKrProcessClientCommands(CardInfoStorageObject)
- метод
Возвращает из указанного хранилища список клиентских команд или значение по
умолчанию для типа, если оно их не содержало.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<KrProcessClientCommand> GetKrProcessClientCommands(
    	this CardInfoStorageObject storage
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetKrProcessClientCommands ( 
    	storage As CardInfoStorageObject
    ) As List(Of KrProcessClientCommand)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static List<KrProcessClientCommand^>^ GetKrProcessClientCommands(
    	CardInfoStorageObject^ storage
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetKrProcessClientCommands : 
            storage : CardInfoStorageObject -> List<KrProcessClientCommand> 
#### Параметры
storage [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Хранилище содержащее получаемое значение.
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[KrProcessClientCommand](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientCommand.htm)>  
Список клиентских команд или значение по умолчанию для типа, если оно их не
содержало.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[KrProcessSharedExtensions -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm)
[GetKrProcessClientCommands -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetKrProcessClientCommands.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

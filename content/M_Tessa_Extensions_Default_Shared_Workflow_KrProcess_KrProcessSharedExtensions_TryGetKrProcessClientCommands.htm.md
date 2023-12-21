# KrProcessSharedExtensions.TryGetKrProcessClientCommands - метод
Возвращает из указанного хранилища список клиентских команд или значение по
умолчанию для типа, если оно их не содержало.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryGetKrProcessClientCommands(
    	this CardInfoStorageObject storage,
    	out List<KrProcessClientCommand> clientCommands
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetKrProcessClientCommands ( 
    	storage As CardInfoStorageObject,
    	<OutAttribute> ByRef clientCommands As List(Of KrProcessClientCommand)
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool TryGetKrProcessClientCommands(
    	CardInfoStorageObject^ storage, 
    	[OutAttribute] List<KrProcessClientCommand^>^% clientCommands
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetKrProcessClientCommands : 
            storage : CardInfoStorageObject * 
            clientCommands : List<KrProcessClientCommand> byref -> bool 
#### Параметры
storage [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Хранилище содержащее получаемое значение.
clientCommands
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[KrProcessClientCommand](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientCommand.htm)>
    Возвращаемое значение. Список клиентских команд или значение по умолчанию для типа, если коллекция их не содержит.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Значение true, если хранилище содержит клиентские команды, иначе - false.
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
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

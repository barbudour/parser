# KrProcessSharedExtensions.TryGetLocalTiles - метод
Получает из указанного объекта коллекцию объектов содержащих информацию о
локальных тайлах маршрутов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryGetLocalTiles(
    	this CardInfoStorageObject storage,
    	out List<KrTileInfo> localTiles
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetLocalTiles ( 
    	storage As CardInfoStorageObject,
    	<OutAttribute> ByRef localTiles As List(Of KrTileInfo)
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool TryGetLocalTiles(
    	CardInfoStorageObject^ storage, 
    	[OutAttribute] List<KrTileInfo^>^% localTiles
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetLocalTiles : 
            storage : CardInfoStorageObject * 
            localTiles : List<KrTileInfo> byref -> bool 
#### Параметры
storage [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Хранилище из которого запрашивается значение.
localTiles
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[KrTileInfo](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTileInfo.htm)>
    Возвращаемое значение. Коллекция объектов содержащих информацию о локальных тайлах маршрутов.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Значение true, если объект содержал коллекцию объектов содержащих информацию о
локальных тайлах маршрутов, иначе - false.
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

# KrProcessSharedExtensions.GetGlobalTiles - метод
Получает из указанного объекта коллекцию объектов содержащих информацию о
глобальных тайлах маршрутов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<KrTileInfo> GetGlobalTiles(
    	this InitializationResponse response
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetGlobalTiles ( 
    	response As InitializationResponse
    ) As List(Of KrTileInfo)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static List<KrTileInfo^>^ GetGlobalTiles(
    	InitializationResponse^ response
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetGlobalTiles : 
            response : InitializationResponse -> List<KrTileInfo> 
#### Параметры
response
[InitializationResponse](T_Tessa_Platform_Initialization_InitializationResponse.htm)
    Ответ на запрос на инициализацию приложения.
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[KrTileInfo](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTileInfo.htm)>  
Коллекция объектов содержащих информацию о глобальных тайлах маршрутов.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[InitializationResponse](T_Tessa_Platform_Initialization_InitializationResponse.htm).
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

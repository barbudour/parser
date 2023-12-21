# KrProcessSharedExtensions.GetRecalcChanges - метод
Возвращает информацию о различиях в маршруте до и после пересчёта.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<RouteDiff> GetRecalcChanges(
    	this CardInfoStorageObject obj
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetRecalcChanges ( 
    	obj As CardInfoStorageObject
    ) As List(Of RouteDiff)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static List<RouteDiff^>^ GetRecalcChanges(
    	CardInfoStorageObject^ obj
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetRecalcChanges : 
            obj : CardInfoStorageObject -> List<RouteDiff> 
#### Параметры
obj [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Хранилище из которого должно быть получено значение.
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[RouteDiff](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_RouteDiff.htm)>  
Список содержащий различия до и после пересчёта маршрута.
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

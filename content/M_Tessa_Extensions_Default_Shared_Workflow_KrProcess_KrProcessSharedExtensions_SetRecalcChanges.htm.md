# KrProcessSharedExtensions.SetRecalcChanges - метод
Сохраняет в заданном хранилище информацию о различиях в маршруте до и после
пересчёта.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetRecalcChanges(
    	this CardInfoStorageObject obj,
    	IEnumerable<RouteDiff> diffs
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetRecalcChanges ( 
    	obj As CardInfoStorageObject,
    	diffs As IEnumerable(Of RouteDiff)
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetRecalcChanges(
    	CardInfoStorageObject^ obj, 
    	IEnumerable<RouteDiff^>^ diffs
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetRecalcChanges : 
            obj : CardInfoStorageObject * 
            diffs : IEnumerable<RouteDiff> -> unit 
#### Параметры
obj [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Хранилище в котором должно быть сохранено значение.
diffs
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[RouteDiff](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_RouteDiff.htm)>
    Перечисление содержащее различия до и после пересчёта маршрута.
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

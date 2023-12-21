# KrProcessSharedExtensions.SetRecalcFlag(IDictionary<String, Object>) - метод
Задаёт значение, показывающее, что должен быть выполнен пересчёт маршрута.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetRecalcFlag(
    	this IDictionary<string, Object> info
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetRecalcFlag ( 
    	info As IDictionary(Of String, Object)
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetRecalcFlag(
    	IDictionary<String^, Object^>^ info
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetRecalcFlag : 
            info : IDictionary<string, Object> -> unit 
#### Параметры
info
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище в котором должно быть сохранено значение.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>. При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[KrProcessSharedExtensions -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm)
[SetRecalcFlag -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetRecalcFlag.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

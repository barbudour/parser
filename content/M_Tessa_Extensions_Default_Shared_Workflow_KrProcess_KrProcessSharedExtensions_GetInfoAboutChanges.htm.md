# KrProcessSharedExtensions.GetInfoAboutChanges(IDictionary<String, Object>) -
метод
Возвращает режим вывода информации об изменениях в маршруте после пересчёта
или значение по умолчанию для типа, если хранилище его не содержало.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static InfoAboutChanges? GetInfoAboutChanges(
    	this IDictionary<string, Object> info
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetInfoAboutChanges ( 
    	info As IDictionary(Of String, Object)
    ) As InfoAboutChanges?
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Nullable<InfoAboutChanges> GetInfoAboutChanges(
    	IDictionary<String^, Object^>^ info
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetInfoAboutChanges : 
            info : IDictionary<string, Object> -> Nullable<InfoAboutChanges> 
#### Параметры
info
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище из которого должно быть получено значение.
#### Возвращаемое значение
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[InfoAboutChanges](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_InfoAboutChanges.htm)>  
Режим вывода информации об изменениях в маршруте после пересчёта или значение
по умолчанию для типа, если хранилище его не содержало.
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
[GetInfoAboutChanges -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetInfoAboutChanges.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

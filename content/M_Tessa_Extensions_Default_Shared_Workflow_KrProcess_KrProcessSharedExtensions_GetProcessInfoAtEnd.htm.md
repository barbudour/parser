# KrProcessSharedExtensions.GetProcessInfoAtEnd - метод
Возвращает дополнительную информацию завершившегося асинхронного процесса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static IDictionary<string, Object> GetProcessInfoAtEnd(
    	this IDictionary<string, Object> info
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetProcessInfoAtEnd ( 
    	info As IDictionary(Of String, Object)
    ) As IDictionary(Of String, Object)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IDictionary<String^, Object^>^ GetProcessInfoAtEnd(
    	IDictionary<String^, Object^>^ info
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetProcessInfoAtEnd : 
            info : IDictionary<string, Object> -> IDictionary<string, Object> 
#### Параметры
info
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище из которого должно быть получено значение.
#### Возвращаемое значение
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>  
Дополнительная информация завершившегося асинхронного процесса.
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
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

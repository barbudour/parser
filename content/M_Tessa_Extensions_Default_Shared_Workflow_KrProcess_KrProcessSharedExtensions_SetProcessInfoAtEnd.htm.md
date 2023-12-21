# KrProcessSharedExtensions.SetProcessInfoAtEnd - метод
Задаёт дополнительную информацию завершившегося асинхронного процесса в
указанном хранилище.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetProcessInfoAtEnd(
    	this IDictionary<string, Object> info,
    	IDictionary<string, Object> processInfo
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetProcessInfoAtEnd ( 
    	info As IDictionary(Of String, Object),
    	processInfo As IDictionary(Of String, Object)
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetProcessInfoAtEnd(
    	IDictionary<String^, Object^>^ info, 
    	IDictionary<String^, Object^>^ processInfo
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetProcessInfoAtEnd : 
            info : IDictionary<string, Object> * 
            processInfo : IDictionary<string, Object> -> unit 
#### Параметры
info
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище в котором должно быть сохранено значение.
processInfo
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Дополнительную информация завершившегося асинхронного процесса.
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

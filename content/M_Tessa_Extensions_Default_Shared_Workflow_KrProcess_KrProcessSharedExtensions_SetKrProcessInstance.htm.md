# KrProcessSharedExtensions.SetKrProcessInstance(Dictionary<String, Object>,
KrProcessInstance) - метод
Сохраняет в указанном объекте информация об экземпляре процесса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetKrProcessInstance(
    	this Dictionary<string, Object> storage,
    	KrProcessInstance krProcess
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetKrProcessInstance ( 
    	storage As Dictionary(Of String, Object),
    	krProcess As KrProcessInstance
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetKrProcessInstance(
    	Dictionary<String^, Object^>^ storage, 
    	KrProcessInstance^ krProcess
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetKrProcessInstance : 
            storage : Dictionary<string, Object> * 
            krProcess : KrProcessInstance -> unit 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище в котором должно быть сохранено значение.
krProcess
[KrProcessInstance](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessInstance.htm)
    Информация об экземпляре процесса.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
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
[SetKrProcessInstance -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetKrProcessInstance.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

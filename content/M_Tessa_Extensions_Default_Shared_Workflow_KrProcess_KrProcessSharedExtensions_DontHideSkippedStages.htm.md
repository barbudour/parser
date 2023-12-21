# KrProcessSharedExtensions.DontHideSkippedStages - метод
Устанавливает значение в заданном хранилище, показывающее, требуется ли
отображать пропущенные этапы.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void DontHideSkippedStages(
    	this Dictionary<string, Object> storage,
    	bool value = true
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub DontHideSkippedStages ( 
    	storage As Dictionary(Of String, Object),
    	Optional value As Boolean = true
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void DontHideSkippedStages(
    	Dictionary<String^, Object^>^ storage, 
    	bool value = true
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member DontHideSkippedStages : 
            storage : Dictionary<string, Object> * 
            ?value : bool 
    (* Defaults:
            let _value = defaultArg value true
    *)
    -> unit 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище в котором должно быть сохранено значение.
value [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Значение true, если необходимо отображать пропущенные этапа, иначе - false.
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
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

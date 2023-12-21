# KrProcessSharedExtensions.DontHideStages(IDictionary<String, Object>,
Boolean) - метод
Добавляет в указанный словарь значение, показывающее, необходимо ли загружать
в карточку скрытые этапы маршрута или нет.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void DontHideStages(
    	this IDictionary<string, Object> storage,
    	bool value = true
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub DontHideStages ( 
    	storage As IDictionary(Of String, Object),
    	Optional value As Boolean = true
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void DontHideStages(
    	IDictionary<String^, Object^>^ storage, 
    	bool value = true
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member DontHideStages : 
            storage : IDictionary<string, Object> * 
            ?value : bool 
    (* Defaults:
            let _value = defaultArg value true
    *)
    -> unit 
#### Параметры
storage
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Словарь, в который должно быть добавлено значение управляющее загрузкой скрытых этапов маршрута.
value [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Значение true, если в карточку должны быть загружены скрытые этапы маршрута, иначе - false.
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
[DontHideStages -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_DontHideStages.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

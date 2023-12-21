#
KrProcessSharedExtensions.SetStartingKrProcessParameters(CardInfoStorageObject,
Dictionary<String, Object>) - метод
Устанавливает параметры запускаемого процесса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetStartingKrProcessParameters(
    	this CardInfoStorageObject storage,
    	Dictionary<string, Object> info
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetStartingKrProcessParameters ( 
    	storage As CardInfoStorageObject,
    	info As Dictionary(Of String, Object)
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetStartingKrProcessParameters(
    	CardInfoStorageObject^ storage, 
    	Dictionary<String^, Object^>^ info
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetStartingKrProcessParameters : 
            storage : CardInfoStorageObject * 
            info : Dictionary<string, Object> -> unit 
#### Параметры
storage [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Хранилище в котором задаётся значение.
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Параметры запускаемого процесса. Могут иметь значение по умолчанию для типа.
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
[SetStartingKrProcessParameters -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetStartingKrProcessParameters.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

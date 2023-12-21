# KrProcessSharedExtensions.SetHasRecalcChanges - метод
Задаёт значение, показывающее, что после пересчёта были изменения в маршруте
или нет. Информация добавляется только при выставленном флаге
[HasChangesToInfo](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_InfoAboutChanges.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetHasRecalcChanges(
    	this CardInfoStorageObject storage,
    	bool hasChanges
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetHasRecalcChanges ( 
    	storage As CardInfoStorageObject,
    	hasChanges As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetHasRecalcChanges(
    	CardInfoStorageObject^ storage, 
    	bool hasChanges
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetHasRecalcChanges : 
            storage : CardInfoStorageObject * 
            hasChanges : bool -> unit 
#### Параметры
storage [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Хранилище в котором должно быть сохранено значение.
hasChanges [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Значение true, если после пересчёта были изменения в маршруте, иначе false.
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

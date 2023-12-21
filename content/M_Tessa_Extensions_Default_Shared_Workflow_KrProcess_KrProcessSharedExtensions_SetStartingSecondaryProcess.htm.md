# KrProcessSharedExtensions.SetStartingSecondaryProcess - метод
Устанавливает информацию о процессе, запускаемого посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetStartingSecondaryProcess(
    	this CardInfoStorageObject request,
    	StartingSecondaryProcessInfo info
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetStartingSecondaryProcess ( 
    	request As CardInfoStorageObject,
    	info As StartingSecondaryProcessInfo
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetStartingSecondaryProcess(
    	CardInfoStorageObject^ request, 
    	StartingSecondaryProcessInfo^ info
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetStartingSecondaryProcess : 
            request : CardInfoStorageObject * 
            info : StartingSecondaryProcessInfo -> unit 
#### Параметры
request [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Запрос к сервису карточек на сохранение карточки.
info
[StartingSecondaryProcessInfo](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StartingSecondaryProcessInfo.htm)
    Информация о запускаемом процессе.
#### Возвращаемое значение
Текущий объект request для цепочки действий.
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

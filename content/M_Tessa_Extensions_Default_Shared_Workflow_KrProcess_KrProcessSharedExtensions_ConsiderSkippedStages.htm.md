# KrProcessSharedExtensions.ConsiderSkippedStages - метод
Возвращает значение из заданного хранилища, показывающее, требуется ли
отображать пропущенные этапы.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool ConsiderSkippedStages(
    	this CardInfoStorageObject storage
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ConsiderSkippedStages ( 
    	storage As CardInfoStorageObject
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool ConsiderSkippedStages(
    	CardInfoStorageObject^ storage
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ConsiderSkippedStages : 
            storage : CardInfoStorageObject -> bool 
#### Параметры
storage [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Хранилище из которого должно быть получено значение.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Значение true, если необходимо отображать пропущенные этапа, иначе - false.
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

# KrProcessSharedExtensions.RemoveSecondaryProcess - метод
Удаляет из объекта содержащего дополнительную информацию, информацию
необходимую для запуска процесса добавленную
[SetStartingSecondaryProcess(CardInfoStorageObject,
StartingSecondaryProcessInfo)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetStartingSecondaryProcess.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void RemoveSecondaryProcess(
    	this CardInfoStorageObject cardInfoStorageObject
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub RemoveSecondaryProcess ( 
    	cardInfoStorageObject As CardInfoStorageObject
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void RemoveSecondaryProcess(
    	CardInfoStorageObject^ cardInfoStorageObject
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RemoveSecondaryProcess : 
            cardInfoStorageObject : CardInfoStorageObject -> unit 
#### Параметры
cardInfoStorageObject
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Объект содержащий информацию.
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

# KrProcessSharedExtensions.GetStartingSecondaryProcess - метод
Возвращает из объекта содержащего дополнительную информацию, информацию
необходимую для запуска процесса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static StartingSecondaryProcessInfo GetStartingSecondaryProcess(
    	this CardInfoStorageObject cardInfoStorageObject
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetStartingSecondaryProcess ( 
    	cardInfoStorageObject As CardInfoStorageObject
    ) As StartingSecondaryProcessInfo
C++ __Копировать
     public:
    [ExtensionAttribute]
    static StartingSecondaryProcessInfo^ GetStartingSecondaryProcess(
    	CardInfoStorageObject^ cardInfoStorageObject
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetStartingSecondaryProcess : 
            cardInfoStorageObject : CardInfoStorageObject -> StartingSecondaryProcessInfo 
#### Параметры
cardInfoStorageObject
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Объект содержащий информацию.
#### Возвращаемое значение
[StartingSecondaryProcessInfo](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StartingSecondaryProcessInfo.htm)  
Информацию необходимая для запуска процесса или значение по умолчанию для
типа, если её не удалось получить.
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

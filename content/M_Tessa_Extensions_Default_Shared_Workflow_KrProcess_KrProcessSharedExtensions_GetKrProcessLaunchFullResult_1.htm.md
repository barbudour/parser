# KrProcessSharedExtensions.GetKrProcessLaunchFullResult(CardStoreResponse) -
метод
Возвращает объект, содержащий результат запуска процесса, с заполненными
свойствами содержащими информацию по объекту его содержащему.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static KrProcessLaunchResult GetKrProcessLaunchFullResult(
    	this CardStoreResponse cardStoreResponse
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetKrProcessLaunchFullResult ( 
    	cardStoreResponse As CardStoreResponse
    ) As KrProcessLaunchResult
C++ __Копировать
     public:
    [ExtensionAttribute]
    static KrProcessLaunchResult^ GetKrProcessLaunchFullResult(
    	CardStoreResponse^ cardStoreResponse
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetKrProcessLaunchFullResult : 
            cardStoreResponse : CardStoreResponse -> KrProcessLaunchResult 
#### Параметры
cardStoreResponse [CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm)
    Ответ на запрос содержащий результаты запуска процесса. Может иметь значение по умолчанию для типа.
#### Возвращаемое значение
[KrProcessLaunchResult](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessLaunchResult.htm)  
Объект содержащий результат запуска процесса.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
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
[GetKrProcessLaunchFullResult -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetKrProcessLaunchFullResult.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

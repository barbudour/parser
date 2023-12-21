# KrProcessSharedExtensions.TryGetKrProcessInstance - метод
Возвращает информацию об экземпляре процесса из указанного хранилища.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryGetKrProcessInstance(
    	this CardInfoStorageObject storage,
    	out KrProcessInstance krProcessInstance
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetKrProcessInstance ( 
    	storage As CardInfoStorageObject,
    	<OutAttribute> ByRef krProcessInstance As KrProcessInstance
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool TryGetKrProcessInstance(
    	CardInfoStorageObject^ storage, 
    	[OutAttribute] KrProcessInstance^% krProcessInstance
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetKrProcessInstance : 
            storage : CardInfoStorageObject * 
            krProcessInstance : KrProcessInstance byref -> bool 
#### Параметры
storage [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Хранилище из которого должно быть получено значение.
krProcessInstance
[KrProcessInstance](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessInstance.htm)
    Возвращаемое значение. Информация об экземпляре процесса.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Значение true, если объект содержал искомую информацию, иначе - false.
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

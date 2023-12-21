# KrProcessSharedExtensions.SetInfoAboutChanges(CardInfoStorageObject,
InfoAboutChanges) - метод
Устанавливает в хранилище информацию о режиме информирования об изменениях в
маршруте после пересчёта.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetInfoAboutChanges(
    	this CardInfoStorageObject storage,
    	InfoAboutChanges infoAboutChanges
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetInfoAboutChanges ( 
    	storage As CardInfoStorageObject,
    	infoAboutChanges As InfoAboutChanges
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetInfoAboutChanges(
    	CardInfoStorageObject^ storage, 
    	InfoAboutChanges infoAboutChanges
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetInfoAboutChanges : 
            storage : CardInfoStorageObject * 
            infoAboutChanges : InfoAboutChanges -> unit 
#### Параметры
storage [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Хранилище в котором должно быть сохранено значение.
infoAboutChanges
[InfoAboutChanges](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_InfoAboutChanges.htm)
    Перечисление режимов вывода информации об изменениях в маршруте после пересчёта.
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
[SetInfoAboutChanges -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetInfoAboutChanges.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

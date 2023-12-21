# KrProcessSharedExtensions.TryGetKrApprovalHistorySection - метод
Возвращает секцию карточки содержащую сопоставление истории заданий с историей
согласования (с учетом циклов согласования).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryGetKrApprovalHistorySection(
    	this Card card,
    	out CardSection section
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetKrApprovalHistorySection ( 
    	card As Card,
    	<OutAttribute> ByRef section As CardSection
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool TryGetKrApprovalHistorySection(
    	Card^ card, 
    	[OutAttribute] CardSection^% section
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetKrApprovalHistorySection : 
            card : Card * 
            section : CardSection byref -> bool 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка содержащая получаемую секцию.
section [CardSection](T_Tessa_Cards_CardSection.htm)
     Возвращаемое значение. Секция карточки.
Идентификатор типа карточки| Имя возвращаемой секции карточки  
---|---  
[KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm)|
[Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrApprovalHistory_Name.htm)  
Любой другой тип| [!:KrApprovalHistory.Synthetic]  
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Значение true, если секцию содержащую информацию по этапам процесса удалось
получить, иначе - false.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [Card](T_Tessa_Cards_Card.htm). При вызове метода для экземпляра
следует опускать первый параметр. Дополнительные сведения см. в разделе
[Методы расширения (Visual Basic)](https://docs.microsoft.com/dotnet/visual-
basic/programming-guide/language-features/procedures/extension-methods) или
[Методы расширения (Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[KrProcessSharedExtensions -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

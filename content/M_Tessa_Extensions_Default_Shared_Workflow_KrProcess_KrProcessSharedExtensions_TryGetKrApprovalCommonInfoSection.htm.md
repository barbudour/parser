# KrProcessSharedExtensions.TryGetKrApprovalCommonInfoSection - метод
Возвращает секцию заданной карточки содержащую информацию по процессу.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryGetKrApprovalCommonInfoSection(
    	this Card card,
    	out CardSection section
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetKrApprovalCommonInfoSection ( 
    	card As Card,
    	<OutAttribute> ByRef section As CardSection
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool TryGetKrApprovalCommonInfoSection(
    	Card^ card, 
    	[OutAttribute] CardSection^% section
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetKrApprovalCommonInfoSection : 
            card : Card * 
            section : CardSection byref -> bool 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой требуется получить секцию.
section [CardSection](T_Tessa_Cards_CardSection.htm)
     Возвращаемое значение. Секция карточки или значение по умолчанию для типа, если секцию карточки получить не удалось.
Идентификатор типа карточки| Имя возвращаемой секции карточки  
---|---  
[KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm)|
[Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrApprovalCommonInfo_Name.htm)  
[KrSecondarySatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSecondarySatelliteTypeID.htm)|
[Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrSecondaryProcessCommonInfo_Name.htm)  
Любой другой тип|
[Virtual](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrApprovalCommonInfo_Virtual.htm)  
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Значение true, если секцию содержащую информацию по процессу удалось получить,
иначе - false.
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

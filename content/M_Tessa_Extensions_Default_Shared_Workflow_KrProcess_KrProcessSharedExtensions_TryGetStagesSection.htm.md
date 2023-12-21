# KrProcessSharedExtensions.TryGetStagesSection - метод
Возвращает секцию заданной карточки содержащую информацию по этапам процесса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryGetStagesSection(
    	this Card card,
    	out CardSection section,
    	bool preferVirtual = false
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetStagesSection ( 
    	card As Card,
    	<OutAttribute> ByRef section As CardSection,
    	Optional preferVirtual As Boolean = false
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool TryGetStagesSection(
    	Card^ card, 
    	[OutAttribute] CardSection^% section, 
    	bool preferVirtual = false
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetStagesSection : 
            card : Card * 
            section : CardSection byref * 
            ?preferVirtual : bool 
    (* Defaults:
            let _preferVirtual = defaultArg preferVirtual false
    *)
    -> bool 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой требуется получить секцию.
section [CardSection](T_Tessa_Cards_CardSection.htm)
     Возвращаемое значение. Секция карточки или значение по умолчанию для типа, если секцию карточки получить не удалось.
Идентификатор типа карточки| Значение параметра preferVirtual| Имя
возвращаемой секции карточки  
---|---|---  
[KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm)|
Любое значение|
[Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_Name.htm)  
[KrSecondarySatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSecondarySatelliteTypeID.htm)|
Любое значение|
[Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_Name.htm)  
[KrStageTemplateTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrStageTemplateTypeID.htm)|
false|
[Virtual](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_Virtual.htm)  
[KrStageTemplateTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrStageTemplateTypeID.htm)|
true|
[Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_Name.htm)  
[KrSecondaryProcessTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSecondaryProcessTypeID.htm)|
false|
[Virtual](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_Virtual.htm)  
[KrSecondaryProcessTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSecondaryProcessTypeID.htm)|
true|
[Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_Name.htm)  
Любой другой тип| Любое значение|
[Virtual](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_Virtual.htm)  
preferVirtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Значение true, если для типов карточек с идентификатором [KrStageTemplateTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrStageTemplateTypeID.htm) или [KrSecondaryProcessTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSecondaryProcessTypeID.htm) необходимо возвратить секцию [Virtual](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_Virtual.htm), иначе - false \- будет возвращена секция [Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_Name.htm).
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

# IKrPermissionExtendedCardSettings.SetCardAccess - метод
Метод для установки доступа
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     void SetCardAccess(
    	bool isAllowed,
    	Guid sectionID,
    	ICollection<Guid> fields
    )
VB __Копировать
     Sub SetCardAccess ( 
    	isAllowed As Boolean,
    	sectionID As Guid,
    	fields As ICollection(Of Guid)
    )
C++ __Копировать
     void SetCardAccess(
    	bool isAllowed, 
    	Guid sectionID, 
    	ICollection<Guid>^ fields
    )
F# __Копировать
     abstract SetCardAccess : 
            isAllowed : bool * 
            sectionID : Guid * 
            fields : ICollection<Guid> -> unit 
#### Параметры
isAllowed [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Определяет, должен ли данный флаг быть доступным или нет
sectionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор секции, для которой устанавливаются права
fields
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор полей, для которых устанавливаются права. Если не заданы, то доступ устанаваливается для всей секции
##  __См. также
#### Ссылки
[IKrPermissionExtendedCardSettings -
](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_IKrPermissionExtendedCardSettings.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)

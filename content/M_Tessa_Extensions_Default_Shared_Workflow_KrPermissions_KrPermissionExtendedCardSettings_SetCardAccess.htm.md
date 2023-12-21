# KrPermissionExtendedCardSettings.SetCardAccess - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public void SetCardAccess(
    	bool isAllowed,
    	Guid sectionID,
    	ICollection<Guid> fields
    )
VB __Копировать
     Public Sub SetCardAccess ( 
    	isAllowed As Boolean,
    	sectionID As Guid,
    	fields As ICollection(Of Guid)
    )
C++ __Копировать
     public:
    virtual void SetCardAccess(
    	bool isAllowed, 
    	Guid sectionID, 
    	ICollection<Guid>^ fields
    ) sealed
F# __Копировать
     abstract SetCardAccess : 
            isAllowed : bool * 
            sectionID : Guid * 
            fields : ICollection<Guid> -> unit 
    override SetCardAccess : 
            isAllowed : bool * 
            sectionID : Guid * 
            fields : ICollection<Guid> -> unit 
#### Параметры
isAllowed [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
sectionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
fields
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
#### Реализации
[IKrPermissionExtendedCardSettings.SetCardAccess(Boolean, Guid,
ICollection<Guid>)](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_IKrPermissionExtendedCardSettings_SetCardAccess.htm)  
##  __См. также
#### Ссылки
[KrPermissionExtendedCardSettings -
](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionExtendedCardSettings.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)

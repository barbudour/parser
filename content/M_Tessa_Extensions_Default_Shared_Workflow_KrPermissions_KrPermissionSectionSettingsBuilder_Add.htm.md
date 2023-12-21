# KrPermissionSectionSettingsBuilder.Add - метод
Метод для добавления настроек секции с указанием приоритета.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public IKrPermissionSectionSettingsBuilder Add(
    	IKrPermissionSectionSettings sectionSettings,
    	int priority = 0
    )
VB __Копировать
     Public Function Add ( 
    	sectionSettings As IKrPermissionSectionSettings,
    	Optional priority As Integer = 0
    ) As IKrPermissionSectionSettingsBuilder
C++ __Копировать
     public:
    virtual IKrPermissionSectionSettingsBuilder^ Add(
    	IKrPermissionSectionSettings^ sectionSettings, 
    	int priority = 0
    ) sealed
F# __Копировать
     abstract Add : 
            sectionSettings : IKrPermissionSectionSettings * 
            ?priority : int 
    (* Defaults:
            let _priority = defaultArg priority 0
    *)
    -> IKrPermissionSectionSettingsBuilder 
    override Add : 
            sectionSettings : IKrPermissionSectionSettings * 
            ?priority : int 
    (* Defaults:
            let _priority = defaultArg priority 0
    *)
    -> IKrPermissionSectionSettingsBuilder 
#### Параметры
sectionSettings
[IKrPermissionSectionSettings](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_IKrPermissionSectionSettings.htm)
priority [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
(Optional)
#### Возвращаемое значение
[IKrPermissionSectionSettingsBuilder](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_IKrPermissionSectionSettingsBuilder.htm)  
Текущий билдер.
#### Реализации
[IKrPermissionSectionSettingsBuilder.Add(IKrPermissionSectionSettings,
Int32)](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_IKrPermissionSectionSettingsBuilder_Add.htm)  
##  __См. также
#### Ссылки
[KrPermissionSectionSettingsBuilder -
](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionSectionSettingsBuilder.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)

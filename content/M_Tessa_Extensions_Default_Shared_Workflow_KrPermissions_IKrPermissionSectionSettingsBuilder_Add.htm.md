# IKrPermissionSectionSettingsBuilder.Add - метод
Метод для добавления настроек секции с указанием приоритета.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     IKrPermissionSectionSettingsBuilder Add(
    	IKrPermissionSectionSettings settings,
    	int prioroty = 0
    )
VB __Копировать
     Function Add ( 
    	settings As IKrPermissionSectionSettings,
    	Optional prioroty As Integer = 0
    ) As IKrPermissionSectionSettingsBuilder
C++ __Копировать
    IKrPermissionSectionSettingsBuilder^ Add(
    	IKrPermissionSectionSettings^ settings, 
    	int prioroty = 0
    )
F# __Копировать
     abstract Add : 
            settings : IKrPermissionSectionSettings * 
            ?prioroty : int 
    (* Defaults:
            let _prioroty = defaultArg prioroty 0
    *)
    -> IKrPermissionSectionSettingsBuilder 
#### Параметры
settings
[IKrPermissionSectionSettings](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_IKrPermissionSectionSettings.htm)
    Настройки секции.
prioroty [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
(Optional)
    Приоритет добавляемых настроек.
#### Возвращаемое значение
[IKrPermissionSectionSettingsBuilder](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_IKrPermissionSectionSettingsBuilder.htm)  
Текущий билдер.
##  __См. также
#### Ссылки
[IKrPermissionSectionSettingsBuilder -
](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_IKrPermissionSectionSettingsBuilder.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)

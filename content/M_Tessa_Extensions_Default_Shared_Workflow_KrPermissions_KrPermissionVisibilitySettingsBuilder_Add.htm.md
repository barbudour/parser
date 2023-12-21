# KrPermissionVisibilitySettingsBuilder.Add - метод
Метод для добавления правила видимости с приоритетом.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public KrPermissionVisibilitySettingsBuilder Add(
    	IEnumerable<KrPermissionVisibilitySettings> settings,
    	int priority = 0
    )
VB __Копировать
     Public Function Add ( 
    	settings As IEnumerable(Of KrPermissionVisibilitySettings),
    	Optional priority As Integer = 0
    ) As KrPermissionVisibilitySettingsBuilder
C++ __Копировать
     public:
    KrPermissionVisibilitySettingsBuilder^ Add(
    	IEnumerable<KrPermissionVisibilitySettings>^ settings, 
    	int priority = 0
    )
F# __Копировать
     member Add : 
            settings : IEnumerable<KrPermissionVisibilitySettings> * 
            ?priority : int 
    (* Defaults:
            let _priority = defaultArg priority 0
    *)
    -> KrPermissionVisibilitySettingsBuilder 
#### Параметры
settings
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[KrPermissionVisibilitySettings](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionVisibilitySettings.htm)>
    Настройки правил видимости.
priority [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
(Optional)
    Приоритет правила.
#### Возвращаемое значение
[KrPermissionVisibilitySettingsBuilder](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionVisibilitySettingsBuilder.htm)  
Текущий билдер.
##  __См. также
#### Ссылки
[KrPermissionVisibilitySettingsBuilder -
](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionVisibilitySettingsBuilder.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)

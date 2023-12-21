# KrToken.HasPermission - метод
Метод для проверки наличия заданного доступа к токене
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public bool HasPermission(
    	KrPermissionFlagDescriptor krPermission
    )
VB __Копировать
     Public Function HasPermission ( 
    	krPermission As KrPermissionFlagDescriptor
    ) As Boolean
C++ __Копировать
     public:
    bool HasPermission(
    	KrPermissionFlagDescriptor^ krPermission
    )
F# __Копировать
     member HasPermission : 
            krPermission : KrPermissionFlagDescriptor -> bool 
#### Параметры
krPermission
[KrPermissionFlagDescriptor](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor.htm)
    Проверяемая настройка доступа
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Возвращает true, если в токене есть данная настройка доступа, иначе false
##  __См. также
#### Ссылки
[KrToken - ](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

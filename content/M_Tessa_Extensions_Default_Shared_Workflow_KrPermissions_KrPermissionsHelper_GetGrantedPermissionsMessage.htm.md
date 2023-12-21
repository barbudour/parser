# KrPermissionsHelper.GetGrantedPermissionsMessage - метод
Формирует сообщение о выданных правах.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetGrantedPermissionsMessage(
    	params KrPermissionFlagDescriptor[] granted
    )
VB __Копировать
     Public Shared Function GetGrantedPermissionsMessage ( 
    	ParamArray granted As KrPermissionFlagDescriptor()
    ) As String
C++ __Копировать
     public:
    static String^ GetGrantedPermissionsMessage(
    	... array<KrPermissionFlagDescriptor^>^ granted
    )
F# __Копировать
     static member GetGrantedPermissionsMessage : 
            granted : KrPermissionFlagDescriptor[] -> string 
#### Параметры
granted
[KrPermissionFlagDescriptor](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor.htm)[]
    Список выданных прав
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Сообщение о выданных правах
##  __См. также
#### Ссылки
[KrPermissionsHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)

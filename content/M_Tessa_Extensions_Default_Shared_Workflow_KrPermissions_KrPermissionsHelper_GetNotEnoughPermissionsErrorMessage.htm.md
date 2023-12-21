# KrPermissionsHelper.GetNotEnoughPermissionsErrorMessage - метод
Формирует сообщение об ошибке недостаточности прав.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetNotEnoughPermissionsErrorMessage(
    	params KrPermissionFlagDescriptor[] stillRequired
    )
VB __Копировать
     Public Shared Function GetNotEnoughPermissionsErrorMessage ( 
    	ParamArray stillRequired As KrPermissionFlagDescriptor()
    ) As String
C++ __Копировать
     public:
    static String^ GetNotEnoughPermissionsErrorMessage(
    	... array<KrPermissionFlagDescriptor^>^ stillRequired
    )
F# __Копировать
     static member GetNotEnoughPermissionsErrorMessage : 
            stillRequired : KrPermissionFlagDescriptor[] -> string 
#### Параметры
stillRequired
[KrPermissionFlagDescriptor](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor.htm)[]
    Список прав, которых не хватает
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Сообщение об ошибке
##  __См. также
#### Ссылки
[KrPermissionsHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)

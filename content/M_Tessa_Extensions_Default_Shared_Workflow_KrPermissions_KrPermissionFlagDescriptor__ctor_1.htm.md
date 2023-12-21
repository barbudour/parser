# KrPermissionFlagDescriptor(Guid, String, KrPermissionFlagDescriptor[]) -
конструктор
Объект, содержащий информацию о текущем флаге настроек прав доступа, не
харящийся в базе данных и не имеющий контрола в карточке прав доступа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public KrPermissionFlagDescriptor(
    	Guid id,
    	string name,
    	params KrPermissionFlagDescriptor[] includedPermissions
    )
VB __Копировать
     Public Sub New ( 
    	id As Guid,
    	name As String,
    	ParamArray includedPermissions As KrPermissionFlagDescriptor()
    )
C++ __Копировать
     public:
    KrPermissionFlagDescriptor(
    	Guid id, 
    	String^ name, 
    	... array<KrPermissionFlagDescriptor^>^ includedPermissions
    )
F# __Копировать
     new : 
            id : Guid * 
            name : string * 
            includedPermissions : KrPermissionFlagDescriptor[] -> KrPermissionFlagDescriptor
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор флага
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя флага
includedPermissions
[KrPermissionFlagDescriptor](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor.htm)[]
    Список флагов, которые включены в данный флаг
##  __См. также
#### Ссылки
[KrPermissionFlagDescriptor -
](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor.htm)
[KrPermissionFlagDescriptor -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor__ctor.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)

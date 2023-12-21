# KrPermissionFlagDescriptor(Guid, String, Int32, String, String, String,
String, KrPermissionFlagDescriptor[]) - конструктор
Объект, содержащий информацию о текущем флаге настроек прав доступа
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public KrPermissionFlagDescriptor(
    	Guid id,
    	string name,
    	int order,
    	string description,
    	string controlCaption,
    	string controlTooltip,
    	string sqlName,
    	params KrPermissionFlagDescriptor[] includedPermissions
    )
VB __Копировать
     Public Sub New ( 
    	id As Guid,
    	name As String,
    	order As Integer,
    	description As String,
    	controlCaption As String,
    	controlTooltip As String,
    	sqlName As String,
    	ParamArray includedPermissions As KrPermissionFlagDescriptor()
    )
C++ __Копировать
     public:
    KrPermissionFlagDescriptor(
    	Guid id, 
    	String^ name, 
    	int order, 
    	String^ description, 
    	String^ controlCaption, 
    	String^ controlTooltip, 
    	String^ sqlName, 
    	... array<KrPermissionFlagDescriptor^>^ includedPermissions
    )
F# __Копировать
     new : 
            id : Guid * 
            name : string * 
            order : int * 
            description : string * 
            controlCaption : string * 
            controlTooltip : string * 
            sqlName : string * 
            includedPermissions : KrPermissionFlagDescriptor[] -> KrPermissionFlagDescriptor
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор флага
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя флага
order [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Определяет порядок флагов в карточке правил доступа и в сообщениях
description [String](https://learn.microsoft.com/dotnet/api/system.string)
    Заголовок флага. Выводится в ообщениях о правах на карточку или когда недостаточно прав
controlCaption [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя контрола флага в карточке правил доступа. Имеет смысл заполнять только совместно с sqlName
controlTooltip [String](https://learn.microsoft.com/dotnet/api/system.string)
    Подсказка к флагу в карточке правил доступа.
sqlName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя поля в SQL в таблице KrPermissions. Если не задано, то флаг не хранится в базе
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

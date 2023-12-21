# OperationAdTypes - перечисление
Операции синхронизации с Active Directory / LDAP.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Operations](N_Tessa_Platform_Operations.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum OperationAdTypes
VB __Копировать
    <FlagsAttribute>
    Public Enumeration OperationAdTypes
C++ __Копировать
    [FlagsAttribute]
    public enum class OperationAdTypes
F# __Копировать
     [<FlagsAttribute>]
    type OperationAdTypes
##  __Члены
None| 0|  Операции не указаны.  
---|---|---  
Employees| 1|  Синхронизация сотрудников.  
Departments| 2|  Синхронизация подразделений.  
StaticRoles| 4|  Синхронизация групп (статических ролей).  
ManualEmployee| 8|  Синхронизация сотрудников, запущенная вручную из карточки
сотрудника.  
ManualDepartment| 16|  Синхронизация подразделений, запущенная вручную из
карточки подразделения.  
ManualStaticRole| 32|  Синхронизация групп (статических ролей), запущенная
вручную из карточки статической роли.  
## __См. также
#### Ссылки
[Tessa.Platform.Operations - пространство
имён](N_Tessa_Platform_Operations.htm)

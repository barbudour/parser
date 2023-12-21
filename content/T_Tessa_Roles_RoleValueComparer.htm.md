# RoleValueComparer - класс
Сравнивает роли по всем свойствам с учётом возможных наследников
[Role](T_Tessa_Roles_Role.htm).
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class RoleValueComparer : IEqualityComparer<Role>, 
    	IEqualityComparer<StaticRole>, IEqualityComparer<PersonalRole>, IEqualityComparer<DepartmentRole>, 
    	IEqualityComparer<DynamicRole>, IEqualityComparer<ContextRole>, IEqualityComparer<MetaRole>, 
    	IEqualityComparer<TaskRole>
VB __Копировать
     Public NotInheritable Class RoleValueComparer
    	Implements IEqualityComparer(Of Role), IEqualityComparer(Of StaticRole), 
    	IEqualityComparer(Of PersonalRole), IEqualityComparer(Of DepartmentRole), IEqualityComparer(Of DynamicRole), 
    	IEqualityComparer(Of ContextRole), IEqualityComparer(Of MetaRole), IEqualityComparer(Of TaskRole)
C++ __Копировать
     public ref class RoleValueComparer sealed : IEqualityComparer<Role^>, 
    	IEqualityComparer<StaticRole^>, IEqualityComparer<PersonalRole^>, IEqualityComparer<DepartmentRole^>, 
    	IEqualityComparer<DynamicRole^>, IEqualityComparer<ContextRole^>, IEqualityComparer<MetaRole^>, 
    	IEqualityComparer<TaskRole^>
F# __Копировать
     [<SealedAttribute>]
    type RoleValueComparer = 
        class
            interface IEqualityComparer<Role>
            interface IEqualityComparer<StaticRole>
            interface IEqualityComparer<PersonalRole>
            interface IEqualityComparer<DepartmentRole>
            interface IEqualityComparer<DynamicRole>
            interface IEqualityComparer<ContextRole>
            interface IEqualityComparer<MetaRole>
            interface IEqualityComparer<TaskRole>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RoleValueComparer
Implements
    [IEqualityComparer](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1)<[Role](T_Tessa_Roles_Role.htm)>, [IEqualityComparer](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1)<[StaticRole](T_Tessa_Roles_StaticRole.htm)>, [IEqualityComparer](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1)<[PersonalRole](T_Tessa_Roles_PersonalRole.htm)>, [IEqualityComparer](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1)<[DepartmentRole](T_Tessa_Roles_DepartmentRole.htm)>, [IEqualityComparer](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1)<[DynamicRole](T_Tessa_Roles_DynamicRole.htm)>, [IEqualityComparer](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1)<[ContextRole](T_Tessa_Roles_ContextRole.htm)>, [IEqualityComparer](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1)<[MetaRole](T_Tessa_Roles_MetaRole.htm)>, [IEqualityComparer](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1)<[TaskRole](T_Tessa_Roles_TaskRole.htm)>
##  __Заметки
Возможно сравнение классов [Role](T_Tessa_Roles_Role.htm),
[StaticRole](T_Tessa_Roles_StaticRole.htm),
[PersonalRole](T_Tessa_Roles_PersonalRole.htm),
[DepartmentRole](T_Tessa_Roles_DepartmentRole.htm),
[DynamicRole](T_Tessa_Roles_DynamicRole.htm),
[ContextRole](T_Tessa_Roles_ContextRole.htm),
[MetaRole](T_Tessa_Roles_MetaRole.htm).
## __Конструкторы
[RoleValueComparer](M_Tessa_Roles_RoleValueComparer__ctor.htm)| Инициализирует
новый экземпляр класса RoleValueComparer  
---|---  
##  __Свойства
[Instance](P_Tessa_Roles_RoleValueComparer_Instance.htm)| Экземпляр класса.  
---|---  
##  __Методы
[Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Equals(ContextRole,
ContextRole)](M_Tessa_Roles_RoleValueComparer_Equals.htm)|  Сравнивает
контекстные роли по всем свойствам.  
[Equals(DepartmentRole,
DepartmentRole)](M_Tessa_Roles_RoleValueComparer_Equals_1.htm)|  Сравнивает
роли департаментов по всем свойствам.  
[Equals(DynamicRole,
DynamicRole)](M_Tessa_Roles_RoleValueComparer_Equals_2.htm)|  Сравнивает
динамические роли по всем свойствам.  
[Equals(MetaRole, MetaRole)](M_Tessa_Roles_RoleValueComparer_Equals_3.htm)|
Сравнивает метароли по всем свойствам.  
[Equals(PersonalRole,
PersonalRole)](M_Tessa_Roles_RoleValueComparer_Equals_4.htm)|  Сравнивает
персональные роли по всем свойствам.  
[Equals(Role, Role)](M_Tessa_Roles_RoleValueComparer_Equals_5.htm)|
Сравнивает роли по всем свойствам с учётом возможных наследников
[Role](T_Tessa_Roles_Role.htm).  
[Equals(StaticRole,
StaticRole)](M_Tessa_Roles_RoleValueComparer_Equals_6.htm)|  Сравнивает
статические роли по всем свойствам.  
[Equals(TaskRole, TaskRole)](M_Tessa_Roles_RoleValueComparer_Equals_7.htm)|
Сравнивает роли задания по всем свойствам.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode(ContextRole)](M_Tessa_Roles_RoleValueComparer_GetHashCode.htm)|
Возвращает хеш-код роли.  
[GetHashCode(DepartmentRole)](M_Tessa_Roles_RoleValueComparer_GetHashCode_1.htm)|
Возвращает хеш-код роли.  
[GetHashCode(DynamicRole)](M_Tessa_Roles_RoleValueComparer_GetHashCode_2.htm)|
Возвращает хеш-код роли.  
[GetHashCode(MetaRole)](M_Tessa_Roles_RoleValueComparer_GetHashCode_3.htm)|
Возвращает хеш-код метароли.  
[GetHashCode(PersonalRole)](M_Tessa_Roles_RoleValueComparer_GetHashCode_4.htm)|
Возвращает хеш-код роли.  
[GetHashCode(Role)](M_Tessa_Roles_RoleValueComparer_GetHashCode_5.htm)|
Возвращает хеш-код роли.  
[GetHashCode(StaticRole)](M_Tessa_Roles_RoleValueComparer_GetHashCode_6.htm)|
Возвращает хеш-код роли.  
[GetHashCode(TaskRole)](M_Tessa_Roles_RoleValueComparer_GetHashCode_7.htm)|
Возвращает хеш-код роли.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Roles - пространство имён](N_Tessa_Roles.htm)

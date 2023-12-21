# RoleUser - структура
Информация о пользователе, используемая в ролевой модели. Представлена в виде
неизменяемого типа значения.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public readonly struct RoleUser : IRoleUser, 
    	IEquatable<RoleUser>, IEquatable<IUser>
VB __Копировать
    <SerializableAttribute>
    Public Structure RoleUser
    	Implements IRoleUser, IEquatable(Of RoleUser), 
    	IEquatable(Of IUser)
C++ __Копировать
    [SerializableAttribute]
    public value class RoleUser : IRoleUser, 
    	IEquatable<RoleUser>, IEquatable<IUser^>
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type RoleUser = 
        struct
            inherit ValueType
            interface IRoleUser
            interface IEquatable<RoleUser>
            interface IEquatable<IUser>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype) __ RoleUser
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<RoleUser>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IUser](T_Tessa_Platform_Runtime_IUser.htm)>, [IRoleUser](T_Tessa_Roles_IRoleUser.htm)
##  __Заметки
По умолчанию структуры сравниваются только по идентификатору.
## __Конструкторы
[RoleUser(IUser)](M_Tessa_Roles_RoleUser__ctor_1.htm)|  Создаёт экземпляр типа
значения по системной информации о пользователе.  
---|---  
[RoleUser(Guid, String)](M_Tessa_Roles_RoleUser__ctor.htm)|  Создаёт экземпляр
типа значения с указанием идентификатора и имени пользователя.  
## __Свойства
[ID](P_Tessa_Roles_RoleUser_ID.htm)| Идентификатор пользователя.  
---|---  
[Name](P_Tessa_Roles_RoleUser_Name.htm)| Имя пользователя.  
##  __Методы
[Equals(IUser)](M_Tessa_Roles_RoleUser_Equals_1.htm)| Сравнивает текущий
объект с заданным.  
---|---  
[Equals(Object)](M_Tessa_Roles_RoleUser_Equals.htm)| Сравнивает текущий объект
с заданным.  
(Переопределяет
[ValueType.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)))  
[Equals(RoleUser)](M_Tessa_Roles_RoleUser_Equals_2.htm)| Сравнивает текущий
объект с заданным.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Roles_RoleUser_GetHashCode.htm)| Возвращает хеш-код
объекта.  
(Переопределяет
[ValueType.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode))  
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
[ToString](M_Tessa_Roles_RoleUser_ToString.htm)| Возвращает строковое
представление объекта.  
(Переопределяет
[ValueType.ToString()](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring))  
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

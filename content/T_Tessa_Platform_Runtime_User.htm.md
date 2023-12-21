# User - класс
Пользователь системы.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class User : IUser, IEquatable<IUser>
VB __Копировать
     Public NotInheritable Class User
    	Implements IUser, IEquatable(Of IUser)
C++ __Копировать
     public ref class User sealed : IUser, 
    	IEquatable<IUser^>
F# __Копировать
     [<SealedAttribute>]
    type User = 
        class
            interface IUser
            interface IEquatable<IUser>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ User
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IUser](T_Tessa_Platform_Runtime_IUser.htm)>, [IUser](T_Tessa_Platform_Runtime_IUser.htm)
##  __Конструкторы
[User](M_Tessa_Platform_Runtime_User__ctor.htm)|  Создаёт экземпляр класса с
указанием значений его свойств.  
---|---  
## __Свойства
[AccessLevel](P_Tessa_Platform_Runtime_User_AccessLevel.htm)| Уровень доступа
для пользователя.  
---|---  
[ID](P_Tessa_Platform_Runtime_User_ID.htm)| Идентификатор пользователя.  
[Name](P_Tessa_Platform_Runtime_User_Name.htm)| Имя пользователя.  
##  __Методы
[Equals(IUser)](M_Tessa_Platform_Runtime_User_Equals_1.htm)| Сравнивает
текущий объект с заданным.  
---|---  
[Equals(Object)](M_Tessa_Platform_Runtime_User_Equals.htm)| Сравнивает текущий
объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Platform_Runtime_User_GetHashCode.htm)| Возвращает хеш-
код объекта.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
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
[ToString](M_Tessa_Platform_Runtime_User_ToString.htm)| Возвращает строковое
представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
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
[IsAdministrator](M_Tessa_Platform_Runtime_RuntimeExtensions_IsAdministrator.htm)|
Возвращает признак того, что пользователь является администратором системы.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[IsRegular](M_Tessa_Platform_Runtime_RuntimeExtensions_IsRegular.htm)|
Возвращает признак того, что пользователь является обычным пользователем.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)

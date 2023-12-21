# IUser - интерфейс
Пользователь системы.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IUser : IEquatable<IUser>
VB __Копировать
     Public Interface IUser
    	Inherits IEquatable(Of IUser)
C++ __Копировать
     public interface class IUser : IEquatable<IUser^>
F# __Копировать
     type IUser = 
        interface
            interface IEquatable<IUser>
        end
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IUser>
##  __Свойства
[AccessLevel](P_Tessa_Platform_Runtime_IUser_AccessLevel.htm)| Уровень доступа
для пользователя.  
---|---  
[ID](P_Tessa_Platform_Runtime_IUser_ID.htm)| Идентификатор пользователя.  
[Name](P_Tessa_Platform_Runtime_IUser_Name.htm)| Имя пользователя.  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))| Indicates whether the current object is equal to
another object of the same type.  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IUser>)  
---|---  
##  __Методы расширения
[IsAdministrator](M_Tessa_Platform_Runtime_RuntimeExtensions_IsAdministrator.htm)|
Возвращает признак того, что пользователь является администратором системы.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
---|---  
[IsRegular](M_Tessa_Platform_Runtime_RuntimeExtensions_IsRegular.htm)|
Возвращает признак того, что пользователь является обычным пользователем.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)

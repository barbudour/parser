# UserSecurityProvider - класс
Объект, управляющий хранением объекта с настройками безопасности сотрудника
[UserSecurityObject](T_Tessa_Platform_Runtime_UserSecurityObject.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class UserSecurityProvider : IUserSecurityProvider
VB __Копировать
     Public NotInheritable Class UserSecurityProvider
    	Implements IUserSecurityProvider
C++ __Копировать
     public ref class UserSecurityProvider sealed : IUserSecurityProvider
F# __Копировать
     [<SealedAttribute>]
    type UserSecurityProvider = 
        class
            interface IUserSecurityProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ UserSecurityProvider
Implements
    [IUserSecurityProvider](T_Tessa_Platform_Runtime_IUserSecurityProvider.htm)
##  __Конструкторы
[UserSecurityProvider](M_Tessa_Platform_Runtime_UserSecurityProvider__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetSecurityObjectAsync](M_Tessa_Platform_Runtime_UserSecurityProvider_GetSecurityObjectAsync.htm)|
Возвращает объект с настройками безопасности для сотрудника с заданным
идентификатором. Если сотрудник отсутствует или для него ещё не указаны
настройки безопасности, то возвращает объект с параметрами по умолчанию. Не
возвращает null. В реализации по умолчанию метод не обеспечивает
транзакционности и блокировки на настройки безопасности для сотрудника, об
этом должен заботиться вышележащий код.  
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
[StoreSecurityObjectAsync](M_Tessa_Platform_Runtime_UserSecurityProvider_StoreSecurityObjectAsync.htm)|
Сохраняет объект с настройками безопасности для сотрудника с заданным
идентификатором. Если сотрудник отсутствует, то метод не выполняет действий. В
реализации по умолчанию метод не обеспечивает транзакционности и блокировки на
настройки безопасности для сотрудника, об этом должен заботиться вышележащий
код.  
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)

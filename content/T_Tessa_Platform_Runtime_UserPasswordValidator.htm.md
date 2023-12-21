# UserPasswordValidator - класс
Объект, выполняющий проверку пароля сотрудника на соответствие настройкам
безопасности.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class UserPasswordValidator : IUserPasswordValidator
VB __Копировать
     Public Class UserPasswordValidator
    	Implements IUserPasswordValidator
C++ __Копировать
     public ref class UserPasswordValidator : IUserPasswordValidator
F# __Копировать
     type UserPasswordValidator = 
        class
            interface IUserPasswordValidator
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ UserPasswordValidator
Implements
    [IUserPasswordValidator](T_Tessa_Platform_Runtime_IUserPasswordValidator.htm)
##  __Конструкторы
[UserPasswordValidator](M_Tessa_Platform_Runtime_UserPasswordValidator__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[SignatureProviderFactory](P_Tessa_Platform_Runtime_UserPasswordValidator_SignatureProviderFactory.htm)|
Фабрика объектов
[ISignatureProvider](T_Tessa_Platform_ISignatureProvider.htm), используемых
для проверки подписи на паролях пользователей.  
---|---  
## __Методы
[CheckIfPasswordIsUniqueAsync](M_Tessa_Platform_Runtime_UserPasswordValidator_CheckIfPasswordIsUniqueAsync.htm)|
Проверяет является ли заданный пароль уникальным, и возвращает результат
проверки или null, если результат является успешным без дополнительных
сообщений.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[PasswordIsStrongAsync](M_Tessa_Platform_Runtime_UserPasswordValidator_PasswordIsStrongAsync.htm)|
Возвращает признак того, что заданный пароль является сильным. Метод
вызывается, когда по настройкам безопасности пароль пользователя должен быть
сильным.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ValidateAsync](M_Tessa_Platform_Runtime_UserPasswordValidator_ValidateAsync.htm)|
Выполняет проверку пароля сотрудника на соответствие настройкам безопасности и
возвращает объект с результатом проверки. Возвращаемый объект не может быть
равен null.  
## __Методы расширения
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
